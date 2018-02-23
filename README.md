# dst-viz

Visualise dst data. Source: http://wdc.kugi.kyoto-u.ac.jp/dstdir/index.html

Current plan of plots:
 - Accross years
 - Across months
 - Across hours


## Usage
```py
$ python

> from api import query

> query(12, 'Jan', 2013)
# returns data for specific date

> query(month='January', year=2014)
# returns data for a particular month

> query(year=1980)
# returns data for a particular year
```



## Code

* [`download.py`](download.py) downloads all data so far.
* [`api.py`](api.py) handles querying.