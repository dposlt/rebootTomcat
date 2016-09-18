# rebootTomcat

Reboot tomcat is simply scrip for kill runnig Tomcat Java process

Program is better copy to user, witch has access to tomcat folders


Run 
    ./rtomcat.py -su {change to tomcat or another user, witch has access to tomcat folders}

    ./rtomcat.py -k {kill process}

    ./rtomcat.py -c {copy logs to /tmp "for transfer"}

    ./rtomcat.py -d {delete logs from /tmp}

    ./rtomcat.py -s {start tomcat}
 
    ./rtomcat.py -l {show catalina.out "for start tomcat"}
    
    ./rtomcat.py -h {create heapDump to /aplikace/liferay/ "must by run first"} 
    
    ./rtomcat.py -a {all process - kill, copy, start, show}


