'''
Code for all api-related functions
'''
import json

m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
mon = ['January','February','March','April','May','June','July',
		'August','September','October','November','December']

with open('data.json') as f:
	data = json.load(f)

def query(date=0, month='x', year='x'):
	if month in m:
		month = m.index(month) + 1
	elif month in mon:
		month = mon.index(month) + 1

	date, month, year = int(date) - 1, str(month), str(year)

	out = {}
	if date == -1:
		out = data[year][month]
	elif month == 'x':
		out = data[year]
	elif year == 'x':
		out = '-_-'
	else:
		out = data[year][month][date]

	return out
