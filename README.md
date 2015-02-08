# spreadBuilder
visual tool for pairs trading
used as a front-end to a [Trading With Python](https://code.google.com/p/trading-with-python/) set of algorithms

The tool should decrease the amount of work needed to find a tradeable spread, consisting of multiple legs (2 and up). 
Planned features
* easily get data from yahoo
* load and save portfolio combinations
* automatically generate portfolios using PCA
* browse through combinations
* tweak weights
* follow current positions


The general workflow should be:

1. based on a list of symbols, use PCA to determine initial weights. Transform to a set of spreads based on principal components.
2. chose a spread (portfolio) that looks interesting
3. tweak the spread by adjusting weights manually and or adding and removing symbols, until it looks tradeable
4. save the spread to a file for developing a trading strategy in a separate notebook.

# Current status
At this moment the code is very much in early development phase. Don't expect anything to work, but you're welcome to fork :)
