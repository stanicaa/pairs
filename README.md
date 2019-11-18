# pairs
Finding pairs in the market that are about or just mean reversed

Current file assumes that you use an excel file as input with stock prices. If different, just change the processing within function proc().

The structure is very basic: pandas uses the timeframe as index, and then each stock is a column with its last_price.

I am also getting rid of the Sat/Sun dates, but ignored the public holidays, as I believe not material enough.
