#!/usr/bin/python
__author__ = 'David Poslt'


import os,shutil,sys,commands


def wrapper(*args):
	if sys.argv[1] == '-c':
		copyLogs()
	elif sys.argv[1] == '-su':
		sudo()
	elif sys.argv[1] == '-d':
		deleteLog()
	elif sys.argv[1] == '-l':
		showCatalinaLog()
	elif sys.argv[1] == '-p':
		PID()
	elif sys.argv[1] == '-s':
		startTomcat()
	elif sys.argv[1] == '-a':
		sudo()
		PID()
		copyLogs()
		startTomcat()
		showCatalinaLog()
	else:
		print('neplatny argument')


def sudo():
	os.system('sudo -su tomcat')
	

def copyLogs():
	'''
	backup logs file
	'''
	target = '/tmp'
	source = '/aplikace/liferay/logs/'
	catalina = '/aplikace/liferay/tomcat-7.0.42/logs/catalina.out'

	shutil.copy2(source+'genmapa.log',target)
	shutil.copy2(source+'eagle.log',target)
	shutil.copy2(source+'spilka.log',target)
	shutil.copy2(catalina, target)

	if os.path.isfile('/tmp/genmapa.log'):
		print('genamapa done')
	else:
		print('ERROR genmapa log')

	if os.path.isfile('/tmp/eagle.log'):
		print ('eagle done')
	else:
		print('ERROR eagle LOG')

	if os.path.isfile('/tmp/spilka.log'):
		print('spilka done')
	else:
		print('ERROR spilka log')

	if os.path.isfile('/tmp/catalina.out'):
		print('catalina done')
	else:
		print('ERROR catalina log') 


def deleteLog():
	'''
	smazani logu z adresare tmp
	aby se nemuseli mazat rucne
	'''
	target = '/tmp/'
	logs = ['spilka.log','genmapa.log','eagle.log','catalina.out']
	for log in logs:
		os.remove(target+log)
		if os.path.isfile(target+log) == False:
			print('Successful delete log: ' + log)
		else:
			print('ERROR delete log: ' + log)


def PID():
	pid = commands.getoutput("ps aux | egrep '^tomcat' | grep java | egrep -v grep | awk '{print $2}'")

	os.system('kill -9 '+pid)
	print('Process java was killed')
		

def showCatalinaLog():
	os.system('tail -f /aplikace/liferay/tomcat-7.0.42/logs/catalina.out')


def startTomcat():
	target = ('/aplikace/liferay/tomcat-7.0.42/bin/')
	os.system(target + './startup.sh')

try:	
    wrapper()
except:
   print(''' python rtomcat.py -c pro zkopirovani logu do /tmp
 python rtomcat.py -d pro smazani logu z /tmp
 python rtomcat.py -l pro zobrazeni logu catalina.out
 python rtomcat.py -p pro zabiti procesu java
 python rtomcat.py -s pro nastartovani sluzby tomcat
 python rtomcat.py -a pro spusteni vsech procesu(kill java, copy log, start tomcat)
	''')

