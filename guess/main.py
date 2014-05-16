import urllib2
import urllib
from pyquery import PyQuery as pq
import MySQLdb

def main():
	res = urllib2.urlopen('https://sports.bwin.com/en/sports/6/betting/formula-1').read()
	d = pq(res)
	for i in range(0,22):
		conn = MySQLdb.connect(host='192.168.230.29',port=3306,user='inuser',passwd='in@sohu&ct',db='mysql')
		cursor = conn.cursor()
		conn.select_db('f1');
		cursor.execute("update guess_driver set rate=%s where ename = %s",[float(d('.odds').eq(i).html()),d('.option-name').eq(i).html()])
		cursor.close()

if __name__ == '__main__':
    main()
