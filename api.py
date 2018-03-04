'''
Code for all api-related functions
'''
import json
import matplotlib.pyplot as plt

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


def meanplot():
	da = []
	for y in range(1957,2018):
		t = []
		for m in range(12):
			s = 0
			for d in range(len(data[str(y)][str(m)])):
				print d, h
				s += sum(data[str(y)][str(m)][d])
			t.append(s/24)
		da.append(t)

	ma = []
	for m in range(1, 13):
		t = []
		for y in range(1957, 2018):
			t.append(da[y-1957][m])
		ma.append(t)

	# 3*4 matrix of plots - 1 per month
	plt.subplot(3,4,1)
	plt.plot(ma[0])

	plt.subplot(3,4,2)
	plt.plot(ma[1])

	plt.subplot(3,4,3)
	plt.plot(ma[2])

	plt.subplot(3,4,4)
	plt.plot(ma[3])

	plt.subplot(3,4,5)
	plt.plot(ma[4])

	plt.subplot(3,4,6)
	plt.plot(ma[5])

	plt.subplot(3,4,7)
	plt.plot(ma[6])

	plt.subplot(3,4,8)
	plt.plot(ma[7])

	plt.subplot(3,4,9)
	plt.plot(ma[8])

	plt.subplot(3,4,10)
	plt.plot(ma[9])

	plt.subplot(3,4,11)
	plt.plot(ma[10])

	plt.subplot(3,4,12)
	plt.plot(ma[11])

	plt.show()