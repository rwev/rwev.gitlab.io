Title: Trading and Volatility
Author: rwev
Category: finance

When uncertainty is low and little new information is entering the market, market participants don't trade aggressively and prices don't move. With market volatility low for long periods of time, like the current streak we are witnessing in this post-Trump era, market makers and other proprietary trading parties don't have anybody to trade with (or against) and employ their trading strategies. Thus trading profits suffer.
Let's take a look at a shallow theoretical basis of _why_ traders prefer higher volatility over lower.

### Positive Effects of Increased Volatility (Θ ↑)

| Factor | Description |
| -------| ----------- |
| Liquidity ↓ | markets widen with uncertainty (bid-ask spreads theoretically sized to compensate for adverse selection costs) |
| T ↑ _(time)_ | given that locals have edge, Θ ↑ means they can apply that edge to more trades over a shorter period of time and invoke the _Central Limit Theorem_ |
| Kurtosis ↑ | Θ ↑ stretches the distribution of price outcomes, while trading costs remain constant; μ<sub>payoff</sub>_(expected value)_ ↑ = profit per trade ↑, _given that locals have edge (μ<sub>payoff</sub> &gt; 0)_ |
| ϵ_(noise)_↑ | noise generates predictable edge for traders in general (more frequently and with greater magnitude); all arbitrage-based trading systems trade in the opposite direction of noise (bet on mean reversion of price Δ driven by noise) |

In mathematical finance, changes in variance and changes in length of time are _inseparable_.

Θ √T (volatility over arbitrary time period T)

    - Θ = volatility = standard deviations of yearly logarithmic price returns
	- T = time in years

_Inseparable _means that changes in Θ √T can not be attributed to specifically to changes in _Θ_ or_T_ given that they are unknown. Increasing _Θ_has the same effect as increasing _T_ by an unequal and non-linear amount. If the trading period remains constant, this essentially _speeds up time_.

Notice that it's impossible to exclusively separate each of the factors; there is overlap between the conceptual ground of the concepts described here.

There are negative aspects of each of the factors that need to be considered also.

### Negative Effects of Increased Volatility (Θ² ↑)

| Factor | Description |
| -------| ----------- |
| Liquidity ↓ | fewer resting orders to take profit / stop loss against; algorithmic maker making vanishes |
| Kurtosis ↑ | larger (possibly bankrupting) losses possible if trader on wrong side of large move |

