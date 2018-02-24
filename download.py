###
## Download files from website
## and populate db for viz
##
import requests
import json
import csv

NUM_MONTHS = 12
NUM_HOURS = 24
table_start_str = '\nDAY\n'
table_end_str = '\n<!-- vvvvv S yyyymm_part3.html'
website = 'http://wdc.kugi.kyoto-u.ac.jp/'
MIN = -999
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


'''
3 types of files:

2016 - . : http://wdc.kugi.kyoto-u.ac.jp/dst_realtime/201601/index.html
2014 - 15: http://wdc.kugi.kyoto-u.ac.jp/dst_provisional/201401/index.html
1957 - 13: http://wdc.kugi.kyoto-u.ac.jp/dst_final/195701/index.html
'''

def year_url(year):
	if year > 1956 and year < 2014:
		return 'dst_final'
	elif year < 2016:
		return 'dst_provisional'
	else:
		return 'dst_realtime'


def download():
	'''
		Populate database by downloading everything
	'''
	dst = {}
	for y in range(1957, 2018):
		print '+--- Year', y
		dst[y] = {}
		for  m in range(1, NUM_MONTHS+1):
			print m,
			month = "{0:0=2d}".format(m)
			month_url = website + year_url(y)+ '/' + str(y) + month + '/index.html'

			r = requests.get(month_url)
			table_start = r.content.find(table_start_str) + len(table_start_str)
			table_end = r.content.find(table_end_str)
			table = r.content[table_start: table_end]
			table = table.split('\n')
			table = filter(None, table)
			# table corresponds to one month of data
			# no. of days * no. of hours
			# list of strings with data
			for day in range(len(table)):
				p = table[day]
				r = p.replace('-',' -').split(' ')
				r = filter(None, r)
				r.pop(0) # remove date
				table[day] = [int(x) for x in r]
		
			dst[y][m] = table
		print ''

		if (y-1958) % 10 == 0:
			print 'Saving', y-1956,'years data'
			with open('data'+str(y-1957)+'.json', 'w') as file:
				file.write(json.dumps(dst))

	# Final version
	print 'Saving', y-1956,'years data'
	with open('data.json', 'w') as file:
		file.write(json.dumps(dst))


def json2csv_():
	
	with open('data.json') as f:
		data = json.load(f)


	l = []
	for m in range(1, NUM_MONTHS+1):
		month = "{0:0=2d}".format(m)
		print m
		for d in range(0, days[m-1]):
			day = "{0:0=2d}".format(d+1)
			for h in range(1, NUM_HOURS+1):
				hour = "{0:0=2d}".format(h)
				#
				date = month + '-' + day + ' ' + hour + ':00'
				t = [date]
				for y in range(1957, 2018):
					print y, m, d, h-1, data[str(y)][str(m)][d][h-1]
					t.append( data[str(y)][str(m)][d][h-1] )
				l.append(t)

	with open('data.csv', 'wb') as f:
		wr = csv.writer(f, quoting=csv.QUOTE_ALL)
		# a = 'Date'
		# for i in range(1957,2018):
		# 	a += ',' + str(i)
		# wr.writerow(a)
		wr.writerows(l)


def json2csv():
	
	with open('data.json') as f:
		data = json.load(f)


	l = []
	for m in range(1, NUM_MONTHS+1):
		month = "{0:0=2d}".format(m)
		print m
		for d in range(0, days[m-1]):
			day = "{0:0=2d}".format(d+1)
			date = '2018-' + month + '-' + day
			t = [date]
			#
			for y in range(1957, 2018):
				s = sum(data[str(y)][str(m)][d][h] for h in range(0, NUM_HOURS) )
				s /= 24
				t.append( s )
			l.append(t)

	# Date,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017
	with open('data.csv', 'wb') as f:
		wr = csv.writer(f, quoting=csv.QUOTE_ALL)
		# a = 'Date'
		# for i in range(1957,2018):
		# 	a += ',' + str(i)
		# wr.writerow(a)
		wr.writerows(l)

if __name__ == '__main__':
	download()
	# json2csv()