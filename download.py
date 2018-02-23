###
## Download files from website
## and populate db for viz
##
import requests
import json

NUM_MONTHS = 12
NUM_HOURS = 24
table_start_str = '\nDAY\n'
table_end_str = '\n<!-- vvvvv S yyyymm_part3.html'
website = 'http://wdc.kugi.kyoto-u.ac.jp/'
MIN = -999

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



if __name__ == '__main__':
    download()