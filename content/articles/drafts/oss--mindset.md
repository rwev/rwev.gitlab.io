Title: The Open Source Mindset
Philosophy: oss
Tags: rules,principle

A lot of young aspiring professionals, including myself, have experienced intellectual development through curiosity. Curiosity to understand. If one doesn't understand something works -- an algorithm, a piece of software, a 2-stroke engine, a firearm -- they are driven to explore until they find a satisfactory balance between known and unknown. This trait in and of itself, I would say, is a major character strength: _always asking why and how_.

However, it can be a slippery slope: what point of understanding is useful in my life, given that I may never again utilize such knowledge in a personal or professional manner?

### Dodging the Rabbit Holes

A former boss of mine, while appreciating my yearning to always know _why _and _how_, and generally seeing it as a very advantageous trait to have as a professional, once gave me a serious talk -- a talk only given to the young, naive, inexperienced, and perhaps overconfident recent graduates. Not about birds, not about bees: about rabbits. Specifically rabbit holes.

<blockquote>"Down the rabbit hole" -- a metaphor for an entry into the unknown, the disorienting or the mentally deranging, from its use in <i>Alice's Adventures in Wonderland </i>(Wikipedia)

While appreciating my desire to always know the why and how, we were in business, and had a specific task at hand. My knowledge and understanding of related topics in the system design or auxiliary blocks of code were often (not always) inconsequential -- my curiosities, while building on my "education" on the entire code base, was not economically practical or rewarding.

It tempting to excuse such distraction by shirking it off as a "practical overview" to ensure that I understand the relationship between the feature we are tasked to implement and another section of the code base. This is fine: but never forget the rabbit hole and the temptation it presents to all those curious.

### Reinventing the Wheel
When I think about how a often-encountered problem should be solved (the form the solution should take), I am tempted to work that solution out myself whether out of pride or desire for a challenge. But the result is often bug-ridden code that requires time and effort to beat into shape, and provides little or no marginal improvement over open-source solutions.

Because problems that we frequently encounter are also the ones that others also frequently encounter (on average), it is often hard to step back and recognize how mundane and monotonous such problems are at their core. Perhaps it is another sign of nativity that this has recently been an obstacle for me.

Nonetheless, here is a thought process I've development to make sure I'm not working without real results:

- Is the problem one that everyone has?
- Chances are many have solved: view open source.
- Robust open source libraries already exist, and have been worked on by a multiple of people more experienced and specialized in that area than me. If my solution is similar in function and form to theirs, theirs is better.
- If my solution offers a materially better form and function, whether in speed, simplicity, or ease of use, consider implementing, but remain realistic in the time it will take to develop a stable, functioning solution.
- No one has solved it? Good luck.
- Is the problem more seldom?
- Good solutions remain unclear and unimplemented?
- Ask why: why hasn't someone (a business, or the open source community) offered a clear solution to this problem? There are two possible explanation:
- If no open source solutions available, solving the problem isn't interesting enough to do for free
- Solving the problem isn't economically consequential _(and_ monetizable) enough to invest company time into.

Problems related to point #2 are the ones the bottom 99% of companies are built on. Find the sweet spot between non-commercialized and not already solved by hobbyist in the open source network.

This gap can be penetrated by recognizing monetization potential that technology companies haven't, and solving the problem is a way that goes against the grain (or non-metaphorically, the "industry best practice").

### Move Fast and Fail Fast
Priding oneself on individual solutions to common problems isn't just futile and without reward (other than the intellectual stimulation one may gain), it is also poor business strategy.

A large portion of any formulated technology product already exists: data storage, manipulation, and access; displaying user interfaces; logging and error handling; graphing and visualization, etc..

Custom solutions are a large time commitment. Implementing a closed-source solution to common problems takes a lot of time, a lot of thinking, and a lot of debugging to iron into a business-ready solution. The speed at which the technology sector moves makes this approach impractical. There are multiple ways in which devoting potentially an order of magnitude more development time into a closed-source solution doesn't make sense:

- If solution to problem is interesting and is in high enough demand, the open source community will solve it faster than a single developer (or small team) can. Specialized experts in the subject area will offer their expertise.
- If solution to problem is economically rewarding enough, another business, whose development time is vastly accelerated by the utilization of open-source solution to solve routine problems, will offer a solution faster than you can.

Thus, if one wastes time developing proprietary solutions to commonly-faced and already-hashed-out challenges, one loses the ability to quickly implement the business idea and fail fast: a solution baked from scratch that is likely unable to capture any return on innovation when rolled out.

### Stay on Top of the Pyramid

Or in other works, stand on the shoulders of giants. Don't seek self-sufficiency for its own sake: use the work of others and extend it, build upon it, contribute back to the pyramid that is the base. 

Nothing would get done if everyone wanted to "own it" and built everything from scratch. \

As mentioned before, businesses are built on special solutions to special problems. Most

> You want to concentrate on code that either solves an uncommon problem or solves a common problem in an uncommon way. That’s what makes your application valuable: the code that implements the business rules that are unique to your app alone — the “secret sauce.” ... Third-party code  in the form of libraries — allows you to quickly implement those commoditized features of your app, so you can stay focused on your “secret sauce.”


### A Personal Example
I recently was working on a financial analysis desktop application. Not one I planned to start a business on, but more like a programming experiment and a potentially useful tool for later in my career in quantitative finance.

A desired feature was the saving and loading of configurations use in pricing and modelling formulas. I decided that I liked the YAML serialization format for this, because it seems like the natural complement to Python (the development language): both embrace human readability and the usage of white space.

Although YAML configuration managers (with load / dump functionality) already exist in Python, I decided on a custom solution. So I began writing my own custom class.

A few hours later, I was beginning to feel stupid. I wasn't even done implementing the load process. I was trying to implement a simple solution to (what I thought was) a simple problem: using flags variables and conditions to step through the text according to YAML specification. What can be so hard about populating a Python object with values extracted from text in a specific format?

Turns out, I was in over my heard, having fallen down the rabbit hole of parsing. Experts rule this <a href="http://tratt.net/laurie/blog/entries/parsing_the_solved_problem_that_isnt.html">surprisingly complicated </a>section of the programming lair. Bright professionals have devoted large portions to working on the topic. Research papers are written about how quickly and accurately perform it.
<blockquote>Figure on 10 man-years to do a correct C++ parser, and that's if you're an experienced compiler guy.

