

After seeing praise for the Cython language in a few places on the internet, and given the minimal translation overhead (basically just adding C-like types into Python code). I was curious what performance leaps could be realized in a practical environment in my industry: financial trading software.

Thus I applied Cython to the most computationally expensive functions in financial industry: the pricing of _derivatives_ and their related _greeks_.
### What is Cython?
Cython is a _superset _of Python, meaning that (almost) all Python code is valid Cython code, while the converse usually isn't true.

[caption id="attachment_3937" align="aligncenter" width="318"]<img class="  wp-image-3937 aligncenter" src="https://tawusa.files.wordpress.com/2017/11/cython-python-superset.png" alt="cython-python-superset" width="318" height="306" /> Cython, Python superset[/caption]

Cython is both:

	- a programming language that adds the static type system
of C and C++ to Python
	- a compiler that translates Cython source code into efficient C or C++
source code

But why would would want to blur the line between Python and C? Python is high-level, flexible (dynamic typing), and slow, while C is low-level, inflexible (static typing), and fast. Cython offers the ability to blend of the two smoothly and with minimal re-translation overhead.
<blockquote>Cython’s beauty is this: it combines Python’s expressiveness and dynamism with C’s bare-metal performance while still feeling like Python. [1]</blockquote>
But before we get to the guts of a practical example, I tested one of the flagship examples in the Cython marketing strategy against the performance on my own machine. The example claims that translating a Fibonacci function written in Python to Cython (by only adding static typing):

[caption id="attachment_3938" align="aligncenter" width="666"]<img class="  wp-image-3938 aligncenter" src="https://tawusa.files.wordpress.com/2017/11/fib-py-c-cy.png" alt="fib-py-c-cy.png" width="666" height="224" /> Syntactical differences between Python / C / Cython for Trivial Fibonacci example [1][/caption]results in a <strong>73 times net speedup:</strong>

[caption id="attachment_3939" align="aligncenter" width="557"]<img class="  wp-image-3939 aligncenter" src="https://tawusa.files.wordpress.com/2017/11/py-c-cy-fib-results.jpg" alt="py-c-cy-fib-results" width="557" height="194" /> Speedup results for aforementioned implementations of _fib(n) _[1][/caption]That's a big claim. I wrote the following Python script in attempt to independently verify:

[code language="python"]
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pyximport; pyximport.install()
import fib

from time import time

def timems (itern, func, argtup):
    t = time()
    for i in range(itern):
        func(*argtup)
    ms = 1000 * (time() - t)
    return ms

FIBN = 90
ITERATIONS = 100000

def fibpy(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a

pure_py_ms = timems (ITERATIONS, fibpy, (FIBN,))
print &quot;\nPYTHON FIB(%d) = %0.0f ms&quot; % (FIBN, pure_py_ms)

cython_ms = timems (ITERATIONS, fib.fibcy, (FIBN,))
print &quot;\nCYTHON FIB(%d) = %0.0f ms&quot; % (FIBN, cython_ms)

print &quot;\nSPEEDUP = %0.0f\n&quot; % (pure_py_ms / cython_ms)
[/code]

_Before running, a C++ compiler must be installed; Visual Studio is recommended on Windows. A minimal Visual C++ compiler for compiling extensions for Python 2.7 is provided <a href="https://www.microsoft.com/en-us/download/details.aspx?id=44266">here</a>._

_<a href="https://github.com/cython/cython/wiki/CythonExtensionsOnWindows">Note</a> behind the import statements: it's a hacky "<a href="https://en.wikipedia.org/wiki/Monkey_patch">monkey-patch</a>" to make Python find compiler executable.  _

And implemented fib in Cython, in fib.pyx:

[code language="python"]
cpdef fibcy(int n):
    cdef int i
    cdef double a=0.0, b=1.0
    for i in range(n):
        a, b = a + b, a
    return a
[/code]

Which results in a <strong>33 times speedup</strong> when ran locally.

[caption id="attachment_3940" align="aligncenter" width="622"]<img class="alignnone  wp-image-3940" src="https://tawusa.files.wordpress.com/2017/11/fib-test-results.jpg" alt="fib-test-results" width="622" height="126" /> Results of local test.[/caption]

This is clearly not the full bang for our buck. Nevertheless, the 33 x speedup for a minimal time investment seems worth it, even in today's development environment, when programmer time is becoming ever more expensive as machine time ever cheaper.
### Experiment in Financial Mathematics
After verifying independently that Cython presents at least some of the tangible benefit it advertises, let's apply it to industry, the pricing of American options using the <a href="http://www.math.ku.dk/~rolf/teaching/thesis/B-AWhaley.pdf">Barone-Adesi And Whaley (BAW) model</a>.

Here is a Cython implementation and interface for the model (_cy__baw.pyx). _I've included the original Python _(baw.py) _in the <a title="python-cython-options-pricing-code" href="https://tawusa.files.wordpress.com/2017/11/python-cython-options-pricing-code.zip">source code</a> for this post:

[code language="python"]
from math import log, exp 

cpdef double pdf_ND(double x):
    cdef double val
    val = (1 / (2 * 3.14159265)**0.5) * exp(-1 * (x**2) / 2)
    return val

cdef double cdf_ND(double x): 

    cdef double y, exp_fact
    cdef double sum_a, sum_b
    cdef double val

    y = abs(x)

    if y &amp;amp;gt; 37:
        return 0
    else:
        exp_fact = exp(-1 * (y**2) / 2)

    if y &amp;amp;lt; 7.07106781186547:         sum_a = 0.0352624965998911 * y + 0.700383064443688         sum_a = sum_a * y + 6.37396220353165         sum_a = sum_a * y + 33.912866078383         sum_a = sum_a * y + 112.079291497871         sum_a = sum_a * y + 221.213596169931         sum_a = sum_a * y + 220.206867912376         sum_b = 0.0883883476483184 * y + 1.75566716318264         sum_b = sum_b * y + 16.064177579207         sum_b = sum_b * y + 86.7807322029461         sum_b = sum_b * y + 296.564248779674         sum_b = sum_b * y + 637.333633378831         sum_b = sum_b * y + 793.826512519948         sum_b = sum_b * y + 440.413735824752         val = exp_fact * sum_a / sum_b     else:         sum_a = y + 0.65         sum_a = y + 4 / sum_a         sum_a = y + 3 / sum_a         sum_a = y + 2 / sum_a         sum_a = y + 1 / sum_a         val = exp_fact / (sum_a * 2.506628274631)          if x &amp;amp;gt; 0:
         return 1 - val
    else:
         return val

cdef double price_BlackScholes(str call_put_flag, double S, double X, double T, double r, double b, double v):

    cdef double d1, d2, bsp

    # strings
    if (call_put_flag not in ['c', 'p']):
        raise ValueError

    # mins
    if (S &amp;amp;lt;= 0) or (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):
        raise ValueError

    d1 = (log(S / X) + (b + v**2 / 2) * T) / (v * (T)**0.5)
    d2 = d1 - v * (T)**0.5

    if call_put_flag == 'c':
        bsp = S * exp((b - r) * T) * cdf_ND(d1) - X * exp(-r * T) * cdf_ND(d2)
    else:
        bsp = X * exp(-r * T) * cdf_ND(-d2) - S * exp((b - r) * T) * cdf_ND(-d1)

    return bsp

cdef double price_WhaleyApproximation(str call_put_flag, double S, double X, double T, double r, double b, double v):

    cdef double american_approx

    # strings
    if (call_put_flag not in ['c', 'p']):
        raise ValueError

    # mins
    if (S &amp;amp;lt;= 0) or (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):
        raise ValueError

    if call_put_flag == 'c':
        american_approx = price_call_WhaleyApproximation(S, X, T, r, b, v)
    else:
        american_approx = price_put_WhaleyApproximation(S, X, T, r, b, v)

    return american_approx

cdef double price_call_WhaleyApproximation(double S, double X, double T, double r, double b, double v):

    cdef double Sk, N, k, d1, Q2, a2
    cdef double american_call_approx

    # mins
    if (S &amp;amp;lt;= 0) or (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):         raise ValueError     if b &amp;amp;gt;= r:
        american_call_approx = price_BlackScholes('c', S, X, T, r, b, v)
    else:
        Sk = Kc(X, T, r, b, v)
        N = 2 * b / v**2
        k = 2 * r / (v**2 * (1 - exp(-1 * r * T)))
        d1 = (log(Sk / X) + (b + (v**2) / 2) * T) / (v * (T**0.5))
        Q2 = (-1 * (N - 1) + ((N - 1)**2 + 4 * k))**0.5 / 2
        a2 = (Sk / Q2) * (1 - exp((b - r) * T) * cdf_ND(d1))
        if S &amp;amp;lt; Sk:
            american_call_approx = price_BlackScholes('c', S, X, T, r, b, v) + a2 * (S / Sk)**Q2
        else:
            american_call_approx = S - X

    return american_call_approx

cdef double price_put_WhaleyApproximation(double S, double X, double T, double r, double b, double v):

    cdef double Sk, N, k, d1, Q1, a1
    cdef double american_put_approx

    # mins
    if (S &amp;amp;lt;= 0) or (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):         raise ValueError     Sk = Kp(X, T, r, b, v)     N = 2 * b / v**2     k = 2 * r / (v**2 * (1 - exp(-1 * r * T)))     d1 = (log(Sk / X) + (b + (v**2) / 2) * T) / (v * (T)**0.5)     Q1 = (-1 * (N - 1) - (((N - 1)**2 + 4 * k))**0.5) / 2     a1 = -1 * (Sk / Q1) * (1 - exp((b - r) * T) * cdf_ND(-1 * d1))     if S &amp;amp;gt; Sk:
        american_put_approx = price_BlackScholes('p', S, X, T, r, b, v) + a1 * (S / Sk)**Q1
    else:
        american_put_approx = X - S

    return american_put_approx

cdef double Kc(double X, double T, double r, double b, double v):

    cdef double N, m, q2u, su, h2, Si
    cdef double k, d1, Q2
    cdef double LHS, RHS
    cdef double bi, E

    # mins
    if (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):         raise ValueError     N = 2 * b / v**2     m = 2 * r / v**2     q2u = (-1 * (N - 1) + ((N - 1)**2 + 4 * m)**0.5) / 2     su = X / (1 - 1 / q2u)     h2 = -1 * (b * T + 2 * v * (T)**0.5) * X / (su - X)     Si = X + (su - X) * (1 - exp(h2))     k = 2 * r / (v**2 * (1 - exp(-1 * r * T)))     d1 = (log(Si / X) + (b + v**2 / 2) * T) / (v * (T)**0.5)     Q2 = (-1 * (N - 1) + ((N - 1)**2 + 4 * k)**0.5) / 2     LHS = Si - X     RHS = price_BlackScholes('c', Si, X, T, r, b, v) + (1 - exp((b - r) * T) * cdf_ND(d1)) * Si / Q2     bi = exp((b - r) * T) * cdf_ND(d1) * (1 - 1 / Q2) + (1 - exp((b - r) * T) * pdf_ND(d1) / (v * (T)**0.5)) / Q2     E = 0.001      while abs(LHS - RHS) / X &amp;amp;gt; E:
        Si = (X + RHS - bi * Si) / (1 - bi)
        d1 = (log(Si / X) + (b + v**2 / 2) * T) / (v * (T)**0.5)
        LHS = Si - X
        RHS = price_BlackScholes('c', Si, X, T, r, b, v) + (1 - exp((b - r) * T) * cdf_ND(d1)) * Si / Q2
        bi = exp((b - r) * T) * cdf_ND(d1) * (1 - 1 / Q2) + (1 - exp((b - r) * T) * cdf_ND(d1) / (v * (T)**0.5)) / Q2

    return Si

cdef double Kp(double X, double T, double r, double b, double v):

    cdef double N, m, q1u, su, h1, Si
    cdef double k, d1, Q1
    cdef double LHS, RHS
    cdef double bi, E

    # mins
    if (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):         raise ValueError     N = 2 * b / v**2     m = 2 * r / v**2     q1u = (-1 * (N - 1) - ((N - 1)**2 + 4 * m)**0.5) / 2     su = X / (1 - 1 / q1u)     h1 = (b * T - 2 * v * (T)**0.5) * X / (X - su)     Si = su + (X - su) * exp(h1)          k = 2 * r / (v**2 * (1 - exp(-1 * r * T)))     d1 = (log(Si / X) + (b + v**2 / 2) * T) / (v * (T)**0.5)     Q1 = (-1 * (N - 1) - ((N - 1)**2 + 4 * k)**0.5) / 2     LHS = X - Si     RHS = price_BlackScholes('p', Si, X, T, r, b, v) - (1 - exp((b - r) * T) * cdf_ND(-1 * d1)) * Si / Q1     bi = -1 * exp((b - r) * T) * cdf_ND(-1 * d1) * (1 - 1 / Q1) - (1 + exp((b - r) * T) * pdf_ND(-d1) / (v * (T)**0.5)) / Q1          E = 0.001           while abs(LHS - RHS) / X &amp;amp;gt; E:
        Si = (X - RHS + bi * Si) / (1 + bi)
        d1 = (log(Si / X) + (b + v**2 / 2) * T) / (v * (T)**0.5)
        LHS = X - Si
        RHS = price_BlackScholes('p', Si, X, T, r, b, v) - (1 - exp((b - r) * T) * cdf_ND(-1 * d1)) * Si / Q1
        bi = -exp((b - r) * T) * cdf_ND(-1 * d1) * (1 - 1 / Q1) - (1 + exp((b - r) * T) * cdf_ND(-1 * d1) / (v * (T)**0.5)) / Q1

    return Si

cpdef double greeks_WhaleyApproximation(str greek_flag, str call_put_flag, double S, double X, double T, double r, double b, double v):

    cdef double dS, dV, T0
    cdef double greeks_WhaleyApproximation
    # strings
    if (greek_flag not in ['p', 'd', 'g', 'v', 't']):
        raise ValueError
    if (call_put_flag not in ['c', 'p']):
        raise ValueError

    # mins
    if (S &amp;amp;lt;= 0) or (X &amp;amp;lt;= 0) or (T &amp;amp;lt;= 0):
        raise ValueError
    if (r &amp;amp;lt; 0) or (b &amp;amp;lt; 0) or (v &amp;amp;lt; 0):
        raise ValueError

    dS = 0.001
    dV = 0.00001
    T0 = 0.00001

    # price
    if greek_flag == 'p':
        greeks_WhaleyApproximation = price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v)
    # delta
    elif greek_flag == 'd':
        greeks_WhaleyApproximation = (price_WhaleyApproximation(call_put_flag, S + dS, X, T, r, b, v) - price_WhaleyApproximation(call_put_flag, S - dS, X, T, r, b, v)) / (2 * dS)
    # gamma
    elif greek_flag == 'g':
        greeks_WhaleyApproximation = (price_WhaleyApproximation(call_put_flag, S + dS, X, T, r, b, v) - 2 * price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v) + price_WhaleyApproximation(call_put_flag, S - dS, X, T, r, b, v)) / dS**2
    # vega
    elif greek_flag == 'v':
        greeks_WhaleyApproximation = (price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v + dV) - price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v - dV)) / 2
    # theta
    elif greek_flag == 't':
        if T &amp;amp;lt;span 				data-mce-type=&quot;bookmark&quot; 				id=&quot;mce_SELREST_start&quot; 				data-mce-style=&quot;overflow:hidden;line-height:0&quot; 				style=&quot;overflow:hidden;line-height:0&quot; 			&amp;amp;gt;&amp;amp;amp;#65279;&amp;amp;lt;/span&amp;amp;gt;&amp;amp;lt;= 1.0 / 365.0:
            greeks_WhaleyApproximation = price_WhaleyApproximation(call_put_flag, S, X, T0, r, b, v) - price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v)
        else:
            greeks_WhaleyApproximation = price_WhaleyApproximation(call_put_flag, S, X, T - 1 / 365, r, b, v) - price_WhaleyApproximation(call_put_flag, S, X, T, r, b, v)

    return greeks_WhaleyApproximation
[/code]

Now for the test. Each model will price the same 10,000 options, which randomly generated inputs and pricing goals (e.g. the greeks, or the theoretical value of the option itself.)

[code language="python"]
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pyximport; pyximport.install()
import baw, cybaw

from time import time
from collections import namedtuple
from random import choice, uniform
from pprint import pprint

def test():

    bounds =            namedtuple('bounds', ['min', 'max'])
    pricing_inputs =    namedtuple('pricing_inputs', ['greek', 'type','spot', 'strike', 'years', 'interest', 'carry', 'volatility'])

    OPTIONS_TO_PRICE =  10000
    greek_choice =      ('p', 'd', 'g', 'v', 't')
    type_choice =       ('c', 'p')
    spot_bounds =       bounds(min = 95,        max = 105)
    strike_bounds =     bounds(min = 90,        max = 110)
    year_bounds =       bounds(min = 1 / 12.0,  max = 4.0)
    interest_bounds =   bounds(min = 0.000,     max = 0.025)
    carry_bounds =      bounds(min = 0.000,     max = 0.000)
    volatility_bounds = bounds(min = 0.025,     max = 0.075)

    to_price = []
    for i in range(OPTIONS_TO_PRICE):

        t_greek =       choice(greek_choice)
        t_type =        choice(type_choice)
        t_spot =        uniform(spot_bounds.min,        spot_bounds.max)
        t_strike =      uniform(strike_bounds.min,      strike_bounds.max)
        t_years =       uniform(year_bounds.min,        year_bounds.max)
        t_interest =    uniform(interest_bounds.min,    interest_bounds.max)
        t_carry =       uniform(carry_bounds.min,       carry_bounds.max)
        t_volatility =  uniform(volatility_bounds.min,  volatility_bounds.max)

        t_inputs = pricing_inputs(
                                    greek = t_greek,
                                    type = t_type,
                                    spot = t_spot,
                                    strike = t_strike,
                                    years = t_years,
                                    interest = t_interest,
                                    carry = t_carry,
                                    volatility = t_volatility
                                )
        to_price.append(t_inputs)

    t = time()
    for pinp in to_price:
        # pprint(dict(pinp._asdict()))
        baw.greeks_WhaleyApproximation(
                                    pinp.greek,
                                    pinp.type,
                                    pinp.spot,
                                    pinp.strike,
                                    pinp.years,
                                    pinp.interest,
                                    pinp.carry,
                                    pinp.volatility
                                    )
    pure_py_ms = 1000* (time() - t)
    print &quot;\nPYTHON BAW = %0.0f ms&quot; % (pure_py_ms,)
t = time()
    for pinp in to_price:
        cybaw.greeks_WhaleyApproximation(
                                    pinp.greek,
                                    pinp.type,
                                    pinp.spot,
                                    pinp.strike,
                                    pinp.years,
                                    pinp.interest,
                                    pinp.carry,
                                    pinp.volatility
                                    )
    cython_ms = 1000* (time() - t)
    print &quot;\nCYTHON CYBAW = %0.0f ms&quot; % (cython_ms,)

    print &quot;\nSPEEDUP = %0.0f\n&quot; % (pure_py_ms / cython_ms)

if __name__ == '__main__':
    test()
    # import cProfile
    # cProfile.run('test()', sort='time')
[/code]

Running the test,

[caption id="attachment_3941" align="aligncenter" width="595"]<img class="alignnone  wp-image-3941" src="https://tawusa.files.wordpress.com/2017/11/cybaw-test-results.jpg" alt="cybaw-test-results" width="595" height="130" /> Option pricing test results.[/caption]

Unfortunately, these results are rather disappointing, as they demonstrated less than a single magnitude of improvement, as compared to given examples.

There very well could be something that I'm doing wrong in my Cython translation _cybaw.pyx_ that could be holding back the gains, such an a variable accidentally left dynamically typed.

My hunch is that for this particular application, the lack of major iteration restrains the impressive leaps in performance. The minor gains in a single order of magnitude range (or less as as seen here) are a result of

	- reduced function call overhead

<blockquote>Cython generates code that is nearly an order of magnitude faster than calling a Python function... Cython accomplishes this by generating highly optimized C code that bypasses some of the slower Python/C API calls. [1]</blockquote>

	- reduced function call overhead math operation as a consequence of static typing

<blockquote>Python never makes the assumption [that a and b are only ever going to be floating-point numbers]...at runtime, Python has to look up the types of both a and b.... then find the type’s underlying __add__ method (or the equivalent), and call  __add__ with a and b as arguments. Inside this __add__ method, the Python floats a and b have to be unboxed to extract the underlying C doubles, and only then can the actual addition occur!

[Meanwhile] the C and Cython versions already know that a and b are doubles and can never be anything else, so adding a and b compiles to just one machine code instruction. [1]</blockquote>
The more minor performance improvements to non-iterative code aspects can be seen in the results table above for the _fib(n)_ test.

Source:
