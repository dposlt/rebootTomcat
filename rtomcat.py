#!/usr/bin/python
__author__ = 'David Poslt'


import os,shutil,sys,commands


def wrapper(*args):
	if sys.argv[1] == '-c':
		copyLogs()
	elif sys.argv[1] == '-hd':
		heapdump(killPID().pid)
	elif sys.argv[1] == '-su':
		sudo()
	elif sys.argv[1] == '-d':
		deleteLog()
	elif sys.argv[1] == '-l':
		showCatalinaLog()
	elif sys.argv[1] == '-k':
		killPID()
	elif sys.argv[1] == '-s':
		startTomcat()
	elif sys.argv[1] == '-a':
		sudo()
		killPID()
		copyLogs()
		startTomcat()
		showCatalinaLog()
	else:
		print('invalid argument')


def sudo():
	os.system('sudo -su adminUser')
	

def copyLogs():
	'''
	backup logs file
	'''
	target = '/tmp'
	source = '/app/liferay/logs/'
	catalina = '/app/liferay/tomcat-7.0.42/logs/catalina.out'

    logsArray = ['genmapa.log','spilka.log','eagle.log','catalina.out']
    
    for log in logsArray:
        if os.path.isfile('source + log'):
            shutil.copy2(source + log, target)
        elif os.path.isfile('catalina + log'):
            shutil.copy2(catalina + log, target)
        else:
            print('ERROR path')
    
    for Islog in logsArray:
          if os.path.isfile('target + Islog'):
            print(Islog + ' done')
          else:
            print('LOG ' + Islog + ' doesn\'t exists')
   
def deleteLog():
	'''
        delete logs from tmp directory
	
	'''
	target = '/tmp/'
	logs = ['log1.log','log2.log','log3.log','catalina.out']
	for log in logs:
		os.remove(target+log)
		if os.path.isfile(target+log) == False:
			print('Successful delete log: ' + log)
		else:
			print('ERROR delete log: ' + log)


def killPID():
	pid = commands.getoutput("ps aux | egrep '^tomcat' | grep java | egrep -v grep | awk '{print $2}'")

	os.system('kill -9 '+pid)
	print('Process java was killed')
		

def showCatalinaLog():
	os.system('tail -f /app/liferay/tomcat/logs/catalina.out')


def startTomcat():
	target = ('/app/liferay/tomcat/bin/')
	os.system(target + './startup.sh')


def heapdump(pid):
	os.system('jmap -dump:format=b,file=/tmp.hprof'+killPID().pid)

try:	
    wrapper()
except:
   print(''' python rtomcat.py -c for copy logs to /tmp
 python rtomcat.py -d for delete log from /tmp
 python rtomcat.py -l for show log catalina.out
 python rtomcat.py -k for kill java process
 python rtomcat.py -s for start tomcat
 python rtomcat.py -hd for create heapdump "must by run first"
 python rtomcat.py -a for all (kill java, copy log, start tomcat)
	''')

