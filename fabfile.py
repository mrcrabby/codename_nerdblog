'''
Created on Jun 6, 2010

@author: dro
'''
from fabric.operations import local 

def start_apache2():
    local("sudo apache2ctl start", capture = False)
    
def stop_apache2():
    local("sudo apache2ctl stop", capture = False)
    
def edit_apache2_conf():
    local("sudo vim /etc/apache2/apache2.conf", capture = False)
    
def start_lighttpd():
    local("sudo lighttpd start -f /etc/lighttpd/lighttpd.conf", capture = False)
    
def edit_lighttpd_conf():
    local("sudo vim /etc/lighttpd/lighttpd.conf",capture = False)
    
def start_redis():
    local("./~/redis/redis-server")
    
def rootfolder():
    local("cd ~")
    
   


def initial_setup():
    
    #Loading of Initial Tools
    local("sudo apt-get install vim", capture = False)
    local("sudo update-alternatives --config editor", capture = False)
    local("sudo apt-get install subversion", capture = False)
    local("sudo apt-get install curl", capture = False)
    local("sudo apt-get install openssh-server openssh-client", capture = False)
    
    local("curl -O http://peak.telecommunity.com/dist/ez_setup.py", capture = False)
    local("sudo python ez_setup.py", capture = False)
    local("rm ez_setup.py", capture = False)
    
    #Install Couch
    local("sudo aptitude install couchdb", capture = False)
    
    #Install Tornado
    local("sudo apt-get install python-pycurl python-simplejson", capture = False)
    local("wget http://www.tornadoweb.org/static/tornado-0.2.tar.gz", capture = False)
    local("tar xvzf tornado-0.2.tar.gz", capture = False)
    local("cd tornado-0.2")
    local("sudo python setup.py build", capture = False)
    local("sudo python setup.py install", capture = False)
    rootfolder()
    local("sudo rm -rf tor*")
    
    #Install CouchDB for Python
    local("sudo easy_install -U httplib2", capture = False)
    local("sudo easy_install simplejson", capture = False)
    local("wget  http://pypi.python.org/packages/source/C/CouchDB/CouchDB-0.7.tar.gz", capture = False)
    local("tar -xvf CouchDB-0.7.tar.gz", capture = False)
    local("cd CouchDB-0.7")
    local("sudo python setup.py install", capture = False)
    rootfolder()
    local("sudo rm -rf Cou*")
    
    #install Redis
    local("git clone git://github.com/antirez/redis.git", capture = False)
    local("cd redis")
    local("make", capture = False)
    rootfolder()
    
    #install Redis for Python
    local("git clone git://github.com/andymccurdy/redis-py.git", capture = False)
    local("cd redis-py", capture = False)
    local("python setup.py build", capture = False)
    local("sudo python setup.py install", capture = False)
    rootfolder()
    local("sudo rm -rf redis-py")
    
    #Install Apache2
    local("sudo apt-get install apache2.2-common", capture = False)
    local("sudo apt-get install apache2", capture = False)
    local("sudo apt-get install apache2-threaded-dev", capture = False)
    local("sudo apt-get install python-dev", capture = False)
    stop_apache()
    
    #Get Mod_WSGI
    
    local("wget http://modwsgi.googlecode.com/files/mod_wsgi-3.2.tar.gz", capture = False)
    local("tar xvf mod_wsgi-3.2.tar.gz", capture = False)
    local("cd mod_wsgi-3.2")
    local("./configure", capture = False)
    local("sudo make", capture = False)
    local("sudo make install", capture = False)
    rootfolder()
    local("sudo rm -rf mod_wsgi*");
    
    #Install Lighttpd
    local("sudo apt-get install lighttpd", capture = False)
    
    #copy fabfile to root
    local("sudo cp fabfile.py ~/fabfile.py")