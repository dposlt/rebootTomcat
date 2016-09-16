#!/usr/bin/env python
__author__ = 'David Poslt'


import os,shutil,sys


def wrapper(*args):
	if sys.argv[1] == '-c':
		copyLogs()
	elif sys.argv[1] == '-h':
		heapdump(getpid())
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
	os.system('sudo -su tomcat')
	

def copyLogs():
    '''
        backup logs file
    '''

    target = '/tmp/'
    source = '/aplikace/liferay/logs/'
    catalina = '/aplikace/liferay/tomcat-7.0.42/logs/'
    
    logsArray = ['genmapa.log','spilka.log','eagle.log','catalina.out']

    for log in logsArray:
        if os.path.isfile(source + log):
            shutil.copy2(source + log, target)
        elif os.path.isfile(catalina + log):
            shutil.copy2(catalina + log, target)

                        
    for Islog in logsArray:
        if os.path.isfile(target + Islog):
            print(Islog + ' done')
        else:
            print('LOG ' + Islog + ' doesn\'t exists')

            
def deleteLog():
	'''
        delete logs from tmp directory
	
	'''
	target = '/tmp/'
	logs = ['genmapa.log','spilka.log','eagle.log','catalina.out']
	for log in logs:
                if os.path.isfile(target+log):
                    os.remove(target+log)
                    print('Successful delete log: ' + log)
		else:
		    print('ERROR delete log: ' + log)

def getpid():
    pid = os.system("ps aux | egrep '^tomcat' | grep java | egrep -v grep | awk '{print $2}'")

def killPID():
	os.system('kill -9 '+getpid())
	print('Process java was killed')
    
		

def showCatalinaLog():
	os.system('tail -f /aplikace/liferay/tomcat-7.0.42/logs/catalina.out')


def startTomcat():
	target = ('/aplikace/liferay/tomcat-7.0.42/bin/')
	os.system(target + './startup.sh')
    
def heapdump(pid):
	os.system('jmap -dump:format=b,file=/tmp.hprof' + pid)


try:	
    wrapper()
except:
   print(''' python rtomcat.py -c for copy logs to /tmp
 python rtomcat.py -d for delete log from /tmp
 python rtomcat.py -l for show log catalina.out
 python rtomcat.py -k for kill java process
 python rtomcat.py -s for start tomcat
 python rtomcat.py -h for create heapdump "must by run first"
 python rtomcat.py -a for all (kill java, copy log, start tomcat)
	''')


