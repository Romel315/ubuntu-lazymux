## lazymux.py - Lazymux v4.0 - Modified/Ported by lemonek for ubuntu
##
import os, sys
import readline
from time import sleep as timeout
## lzmcore.py - useful module of Lazymux, slightly modified

import time
import urllib.request
from subprocess import check_output as inputstream

current_dir = os.getcwd()
lazymux_banner = """
 _
( )
| |       _ _  ____  _   _   ___ ___   _   _
| |  _  /'_` )(_  ,)( ) ( )/' _ ` _ `\( ) ( )(`\/')
| |_( )( (_| | /'/_ | (_) || ( ) ( ) || (_) | >  <
(____/'`\__,_)(____)`\__, |(_) (_) (_)`\___/'(_/\_)
                    ( )_| |
                    `\___/'
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazymux
"""

configBase = "./"
configFile = "./lazymux.conf"
cache_1 = "/cache/"

def repo_check(sources_list):
	if os.path.isfile(os.getenv("PREFIX")+"/etc/apt/sources.list.d/"+sources_list):
		return True
	return False

def writeStatus(statusId):
	print(str(statusId) + "[StatusID]")

def readStatus():
	try:
		statusId = open(cache_1,"r").read()
		if statusId == "1":
			return True
		return False
	except IOError:
		return False

def checkConfigFile():
	if os.path.exists(configFile):
		if os.path.isdir(configFile):
			os.system(f"rm -rf {configFile}")
			open(configFile,"w").write(configBase)
	else:
		open(configFile,"w").write(configBase)

def loadConfigFile():
	checkConfigFile()
	lfile = ""
	try:
		lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
	except Exception as e:
		lfile = "~"
	return lfile

homeDir = loadConfigFile()

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	if not readStatus():
		print(backtomenu_banner)
		backtomenu = input("lzmx > ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "0" or backtomenu == "00":
			sys.exit()
		else:
			print("\nERROR: Wrong Input")
			time.sleep(2)
			restart_program()

def banner():
	print(lazymux_banner)

### Repo Installer
def pointless_repo():
	urllib.request.urlretrieve('https://its-pointless.github.io/setup-pointless-repo.sh','setup-pointless-repo.sh')
	os.system('bash setup-pointless-repo.sh')
	os.remove('setup-pointless-repo.sh')
	os.system('apt update -y && apt upgrade -y')
###

def nmap():
	print('\n###### Installing Nmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap')
	print('###### Done')
	print("###### Type 'nmap' to start.")
	backtomenu_option()

def red_hawk():
	print('\n###### Installing RED HAWK')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	print('This mf tried to move RED_HAWK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dtect():
	print('\n###### Installing D-TECT')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	print('This mf tried to move D-Tech {}/D-TECT'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmap():
	print('\n###### Installing sqlmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	print('This mf tried to move sqlmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def infoga():
	print('\n###### Installing Infoga')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	print('This mf tried to move Infoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def reconDog():
	print('\n###### Installing ReconDog')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	print('This mf tried to move ReconDog {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androZenmap():
	print('\n###### Installing AndroZenmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir {}/AndroZenmap'.format(homeDir))
	print('This mf tried to move androzenmap.sh {}/AndroZenmap'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmate():
	print('\n###### Installing sqlmate')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/s0md3v/sqlmate')
	print('This mf tried to move sqlmate {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def astraNmap():
	print('\n###### Installing AstraNmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	print('This mf tried to move AstraNmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def weeman():
	print('\n###### Installing weeman')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang git python2')
	os.system('python2 -m pip bs4 html5lib lxml')
	os.system('git clone https://github.com/evait-security/weeman')
	print('This mf tried to move weeman {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def easyMap():
	print('\n###### Installing Easymap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	print('This mf tried to move Easymap {}'.format(homeDir))
	os.system('cd {}/Easymap && sh install.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xd3v():
	print('\n###### Installing XD3v')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	print('This mf tried to move xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(homeDir))
	print('###### Done')
	print("###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	print('\n###### Installing Crips')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sir():
	print('\n###### Installing SIR')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def xshell():
	print('\n###### Installing Xshell')
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilURL():
	print('\n###### Installing EvilURL')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def striker():
	print('\n###### Installing Striker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	print('This mf tried to move Striker {}'.format(homeDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dsss():
	print('\n###### Installing DSSS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	print('This mf tried to move DSSS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqliv():
	print('\n###### Installing SQLiv')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/the-robot/sqliv')
	print('This mf tried to move sqliv {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlscan():
	print('\n###### Installing sqlscan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	print('This mf tried to move sqlscan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wordpreSScan():
	print('\n###### Installing Wordpresscan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	print('This mf tried to move Wordpresscan {}'.format(homeDir))
	os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wpscan():
	print('\n###### Installing WPScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	print('This mf tried to move wpscan {0} && cd {0}/wpscan'.format(homeDir))
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print('###### Done')
	backtomenu_option()

def wordpresscan():
	print('\n###### Installing wordpresscan(2)')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	print('This mf tried to move termux-wordpresscan {}'.format(homeDir))
	print('###### Done')
	print("###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	print('\n###### Installing Routersploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/threat9/routersploit')
	print('This mf tried to move routersploit {0};cd {0}/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def torshammer():
	print('\n###### Installing Torshammer')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	print('This mf tried to move torshammer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def slowloris():
	print('\n###### Installing Slowloris')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	print('This mf tried to move slowloris {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fl00d12():
	print('\n###### Installing Fl00d & Fl00d2')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 curl')
	os.system('mkdir {}/fl00d'.format(homeDir))
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	print('This mf tried to move fl00d.py {0}/fl00d && mv fl00d2.py {0}/fl00d'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goldeneye():
	print('\n###### Installing GoldenEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	print('This mf tried to move GoldenEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xerxes():
	print('\n###### Installing Xerxes')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/baraalmasri/xerxes')
	print('This mf tried to move xerxes {}'.format(homeDir))
	os.system('cd {}/xerxes && clang xerxes.c -o xerxes'.format(homeDir))
	os.system('chmod 755 {0}/xerxes/xerxes && cp {0}/xerxes/xerxes $PREFIX/bin'.format(homeDir))
	print('###### Done')
	print('###### Usage: xerxes ​www.fakesite.com​ 80')
	backtomenu_option()

def planetwork_ddos():
	print('\n###### Installing Planetwork-DDOS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	print('This mf tried to move Planetwork-DDOS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hydra():
	print('\n###### Installing Hydra')
	os.system('apt update -y && apt upgrade -y')
	os.system('')
	os.system('git clone https://github.com/vanhauser-thc/thc-hydra')
	print('###### Done')
	backtomenu_option()

def black_hydra():
	print('\n###### Installing Black Hydra')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	print('This mf tried to move Black-Hydra {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cupp():
	print('\n###### Installing Cupp')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	print('This mf tried to move cupp {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def asu():
	print('\n###### Installing ASU')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	print('This mf tried to move ASU {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hash_buster():
	print('\n###### Installing Hash-Buster')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/Hash-Buster')
	print('This mf tried to move Hash-Buster {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def instaHack():
	print('\n###### Installing InstaHack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Slayeri4/instahack')
	print('This mf tried to move instahack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def indonesian_wordlist():
	print('\n###### Installing indonesian-wordlist')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	print('This mf tried to move indonesian-wordlist {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbBrute():
	print('\n###### Installing Facebook Brute Force 3')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir {}/facebook-brute-3'.format(homeDir))
	print('This mf tried to move facebook3.py {0}/facebook-brute-3 && mv password.txt {0}/facebook-brute-3'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webdav():
	print('\n###### Installing WebDAV')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir {}/webdav'.format(homeDir))
	os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR {}/webdav/webdav.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webmassploit():
	print('\n###### Installing Webdav Mass Exploiter')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir {0}/webdav-mass-exploit && mv webdav.py {0}/webdav-mass-exploit".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqldump():
	print('\n###### Installing sqldump')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir {0}/sqldump && chmod +x sqldump.py && mv sqldump.py {0}/sqldump'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def websploit():
	print('\n###### Installing Websploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	print('This mf tried to move websploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def metasploit():
	print('\n###### Installing Metasploit')
	os.system("apt update && apt upgrade")
	os.system("apt install unstable-repo")
	os.system("cd {} && apt install metasploit".format(homeDir))
	print('###### Done')
	print("###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	print('\n###### Installing Commix')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	print('This mf tried to move commix {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutal():
	print('\n###### Installing Brutal')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	print('This mf tried to move Brutal {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def knockmail():
	print('\n###### Installing KnockMail')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	print('This mf tried to move KnockMail {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hac():
	print('\n###### Installing Hac')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	print('This mf tried to move Hac {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rang3r():
	print('\n###### Installing Rang3r')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sh33ll():
	print('\n###### Installing SH33LL')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def social():
	print('\n###### Installing Social-Engineering')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def spiderbot():
	print('\n###### Installing SpiderBot')
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def ngrok():
	print('\n###### Installing Ngrok')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	print('This mf tried to move ngrok {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sudo():
	print('\n###### Installing sudo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	print('This mf tried to move termux-sudo {0} && cd {0}/termux-sudo && chmod 777 *'.format(homeDir))
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print('###### Done')
	backtomenu_option()

def ubuntu():
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	print('This mf tried to move termux-ubuntu {0} && cd {0}/termux-ubuntu && bash ubuntu.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install ubuntu')
	print('###### Done')
	backtomenu_option()

def fedora():
	"""
	print('\n###### Installing Fedora')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	print('This mf tried to move termux-fedora.sh {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install fedora')
	print('###### Done')
	backtomenu_option()

def nethunter():
	print('\n###### Installing Kali NetHunter')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	print('This mf tried to move Nethunter-In-Termux {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def blackbox():
	print('\n###### Installing BlackBox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	print('This mf tried to move blackbox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xattacker():
	print('\n###### Installing XAttacker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	print('This mf tried to move XAttacker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vcrt():
	print('\n###### Installing VCRT')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	print('This mf tried to move Evil-create-framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def socfish():
	print('\n###### Installing SocialFish')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	print('This mf tried to move SocialFish {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ecode():
	print('\n###### Installing ECode')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	print('This mf tried to move Ecode {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xsstrike():
	print('\n###### Installing XSStrike')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/s0md3v/XSStrike')
	print('This mf tried to move XSStrike {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def breacher():
	print('\n###### Installing Breacher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/s0md3v/Breacher')
	print('This mf tried to move Breacher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def stylemux():
	print('\n###### Installing Termux-Styling')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	print('This mf tried to move Termux-Styling-Shell-Script {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def txtool():
	print('\n###### Installing TXTool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	print('This mf tried to move txtool {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def passgencvar():
	print('\n###### Installing PassGen')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	print('This mf tried to move PassGen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def owscan():
	print('\n###### Installing OWScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	print('This mf tried to move OWScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sanlen():
	print('\n###### Installing santet-online')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	print('This mf tried to move santet-online {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def spazsms():
	print('\n###### Installing SpazSMS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	print('This mf tried to move SpazSMS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasher():
	print('\n###### Installing Hasher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/CiKu370/hasher')
	print('This mf tried to move hasher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashgenerator():
	print('\n###### Installing Hash-Generator')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/CiKu370/hash-generator')
	print('This mf tried to move hash-generator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kodork():
	print('\n###### Installing ko-dork')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/CiKu370/ko-dork')
	print('This mf tried to move ko-dork {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def snitch():
	print('\n###### Installing snitch')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	print('This mf tried to move snitch {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def osif():
	print('\n###### Installing OSIF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	print('This mf tried to move OSIF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nk26():
	print('\n###### Installing nk26')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/milio48/nk26')
	print('This mf tried to move nk26 {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def devploit():
	print('\n###### Installing Devploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	print('This mf tried to move Devploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasherdotid():
	print('\n###### Installing Hasherdotid')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	print('This mf tried to move hasherdotid {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def namechk():
	print('\n###### Installing Namechk')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	print('This mf tried to move Namechk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xlPy():
	print('\n###### Installing xl-py')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	print('This mf tried to move xl-py {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def beanshell():
	print('\n###### Installing Beanshell')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print('###### Done')
	print("###### Type 'bsh' to start.")
	backtomenu_option()

def crunch():
	print('\n###### Installing Crunch')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	print("###### Done")
	print("###### Type 'crunch' to start.")
	backtomenu_option()

def binploit():
	print('\n###### Installing Binary Exploitation')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	print("###### Done")
	print("###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	print('\n###### Installing Textr')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print('###### Done')
	print("###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	print('\n###### Installing ApSca')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print('###### Done')
	print("###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	print('\n###### Installing amox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print('###### Done')
	print("###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	print('\n###### Installing FaDe')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	print('This mf tried to move FaDe {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ginf():
	print('\n###### Installing GINF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	print('This mf tried to move GINF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def auxile():
	print('\n###### Installing AUXILE')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	print('This mf tried to move AUXILE {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inther():
	print('\n###### Installing inther')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	print('This mf tried to move inther {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hpb():
	print('\n###### Installing HPB')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print('###### Done')
	print("###### Type 'hpb' to start.")
	backtomenu_option()

def fmbrute():
	print('\n###### Installing FMBrute')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FMBrute')
	print('This mf tried to move FMBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashid():
	print('\n###### Installing HashID')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 && python2 -m pip install hashid')
	print("###### Done")
	print("###### Type 'hashid -h' to show usage of hashid")
	backtomenu_option()

def gpstr():
	print('\n###### Installing GPS Tracking')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	print('This mf tried to move gps_tracking {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def pret():
	print('\n###### Installing PRET')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	print('This mf tried to move PRET {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def atlas():
	print('\n###### Installing Atlas')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	print('This mf tried to move Atlas {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def hashcat():
	print('\n###### Installing Hashcat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	print("###### Done")
	print("###### Type 'hashcat' to start.")
	backtomenu_option()

def liteotp():
	print('\n###### Installing LiteOTP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	print("###### Done")
	print("###### Type 'lite' to start.")
	backtomenu_option()

def fbbrutex():
	print('\n###### Installing FBBrute')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	print('This mf tried to move FBBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fim():
	print('\n###### Installing fim')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	print('This mf tried to move fim {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rshell():
	print('\n###### Installing RShell')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	print('This mf tried to move RShell {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def termpyter():
	print('\n###### Installing TermPyter')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	print('This mf tried to move TermPyter {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maxsubdofinder():
	print('\n###### Installing MaxSubdoFinder')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	print('This mf tried to move MaxSubdoFinder {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def jadx():
	print('\n###### Installing jadx')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print('###### Done')
	print("###### Type 'jadx' to start.")
	backtomenu_option()

def pwnedOrNot():
	print('\n###### Installing pwnedOrNot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	print('This mf tried to move pwnedOrNot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maclook():
	print('\n###### Installing Mac-Lookup')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	print('This mf tried to move Mac-Lookup {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def f4k3():
	print('\n###### Installing F4K3')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	print('###### Done')
	print("###### Type 'f4k3' to start.")
	backtomenu_option()

def katak():
	print('\n###### Installing Katak')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	print('This mf tried to move Katak {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def heroku():
	print('\n###### Installing heroku')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nodejs')
	os.system('npm install heroku -g')
	print('###### Done')
	print("###### Type 'heroku' to start.")
	backtomenu_option()

def google():
	print('\n###### Installing google')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python')
	os.system('python -m pip install google')
	print('###### Done')
	print("###### Type 'google' to start.")
	backtomenu_option()

def billcypher():
	print('\n###### Installing BillCypher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	print('This mf tried to move BillCypher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vbug():
	print('\n###### Installing vbug')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/vbug')
	print('This mf tried to move vbug {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kojawafft():
	print('\n###### Installing kojawafft')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nodejs')
	os.system('git clone https://github.com/sandalpenyok/kojawafft')
	print('This mf tried to move kojawafft {}'.format(homeDir))
	os.system('cd $HOME/kojawafft && unzip node_modules.zip && cd -')
	print('###### Done')
	backtomenu_option()

def aircrackng():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing aircrack-ng')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo aircrack-ng')
		print('###### Done')
		print("###### Type 'aircrack-ng' to start.")
	backtomenu_option()

def ettercap():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing ettercap')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo ettercap')
		print('###### Done')
		print("###### Type 'ettercap' to start.")
	backtomenu_option()

def ccgen():
	print('\n###### Installing ccgen')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ccgen')
	print('This mf tried to move ccgen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ddcrypt():
	print('\n###### Installing ddcrypt')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ddcrypt')
	print('This mf tried to move ddcrypt {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dnsrecon():
	print('\n###### Installing dnsrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	print('This mf tried to move dnsrecon {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zphisher():
	print('\n###### Installing zphisher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	print('This mf tried to move zphisher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def apktool():
	print('\n###### Installing apktool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git dpkg')
	os.system('git clone https://github.com/Lexiie/Termux-Apktool')
	print('This mf tried to move Termux-Apktool {}'.format(homeDir))
	os.system('cd {}/Termux-Apktool && dpkg -i *.deb'.format(homeDir))
	print('###### Done')
	print("###### Type 'apktool' to start.")
	backtomenu_option()

def uncompyle():
	print('\n###### Installing uncompyle6')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python python2')
	os.system('python2 -m pip install uncompyle6')
	print('This mf tried to move $PREFIX/bin/uncompyle6 $PREFIX/bin/uncompyle')
	os.system('python -m pip install uncompyle6')
	print('###### Done')
	print('###### (py2) Usage: uncompyle')
	print('###### (py3) Usage: uncompyle6')
	backtomenu_option()

def wifite():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing Wifite')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install git python2')
		os.system('git clone https://github.com/derv82/wifite')
		print('This mf tried to move wifite {}'.format(homeDir))
		print('###### Done')
	backtomenu_option()

def parrot():
	print('\n###### Installing Parrot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget openssl-tool proot -y && hash -r && cd {} && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh && bash parrot.sh'.format(homeDir))
	os.system('cd {} && bash start-parrot.sh'.format(homeDir))
	print('###### Done')
	print('###### Make sure visit: https://techriz.com/how-to-install-parrot-linux-on-android-without-root/')
	os.system('am start -a android.intent.action.VIEW -d "https://techriz.com/how-to-install-parrot-linux-on-android-without-root/"')
	backtomenu_option()

def archlinux():
	"""
	print('\n###### Installing Arch Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('cd $HOME && git clone https://github.com/sdrausty/TermuxArch')
	os.system('cd $HOME && bash TermuxArch/setupTermuxArch.sh')
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Arch Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install archlinux')
	print('###### Done')
	print("###### Type 'proot-distro login archlinux' to start.")
	backtomenu_option()

def tshark():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tshark')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo tshark')
		print('###### Done')
		print("###### Type 'tshark' to start.")
	backtomenu_option()

def dos2unix():
	print('\n###### Installing dos2unix')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dos2unix')
	print('###### Done')
	print("###### Type 'dos2unix' to start.")
	backtomenu_option()

def exiftool():
	print('\n###### Installing exiftool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install exiftool')
	print('###### Done')
	print("###### Type 'exiftool' to start.")
	backtomenu_option()

def iconv():
	print('\n###### Installing iconv')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install iconv')
	print('###### Done')
	print("###### Type 'iconv' to start.")
	backtomenu_option()

def mediainfo():
	print('\n###### Installing mediainfo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install mediainfo')
	print('###### Done')
	print('###### Usage: mediainfo filename.pdf')
	backtomenu_option()

def pdfinfo():
	print('\n###### Installing pdfinfo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install poppler')
	print('###### Done')
	print('###### Usage: pdfinfo filename.pdf')
	backtomenu_option()

def tcpdump():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tcpdump')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo tcpdump')
		print('###### Done')
		print("###### Type 'tcpdump' to start.")
	backtomenu_option()

def hping3():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing hping3')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo hping3')
		print('###### Done')
		print("###### Type 'hping3' to start.")
	backtomenu_option()

def dbdat():
	print('\n###### Installing DbDat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install MySQL-python psycopg2 cx_Oracle pymssql ibm_db pymongo pyyaml couchdb')
	os.system('git clone https://github.com/foospidy/DbDat')
	print('This mf tried to move DbDat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nosqlmap():
	print('\n###### Installing NoSQLMap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 unstable-repo metasploit')
	os.system('python2 -m pip install pymongo httplib2')
	os.system('git clone https://github.com/codingo/NoSQLMap')
	print('This mf tried to move NoSQLMap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def audit_couchdb():
	print('\n###### Installing audit_couchdb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nodejs')
	os.system('npm install -g npm@next audit_couchdb')
	os.system('git clone https://github.com/iriscouch/audit_couchdb')
	print('This mf tried to move audit_couchdb {}'.format(homeDir))
	print('###### Done')
	print('###### Usage: audit_couchdb https://admin:secret@localhost:5984')
	backtomenu_option()

def mongoaudit():
	print('\n###### Installing mongoaudit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install pymongo mongoaudit')
	print('###### Done')
	print("###### Type 'mongoaudit' to start.")
	backtomenu_option()

def wifiphisher():
	print('\n###### Installing Wifiphisher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install setuptools scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher')
	print('This mf tried to move wifiphisher {0} && cd {0}/wifiphisher && python setup.py install'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sherlock():
	print('\n###### Installing sherlock')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/sherlock-project/sherlock')
	print('This mf tried to move sherlock {0} && cd {0}/sherlock && python -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install shc -y')
	print('###### Done')
	print("###### Type 'shc' to start.")
	backtomenu_option()

def steghide():
	print('\n###### Installing steghide')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install steghide -y')
	print('###### Done')
	print("###### Type 'steghide' to start.")
	backtomenu_option()

def tesseract():
	print('\n###### Installing tesseract')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tesseract -y')
	print('###### Done')
	print("###### Type 'tesseract' to start.")
	backtomenu_option()

def sleuthkit():
	print('\n###### Installing sleuthkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install sleuthkit -y')
	print('###### Done')
	print("###### Type 'pkg files sleuthkit | grep usr/bin' to check executable file related to sleuthkit package.")
	backtomenu_option()

def octave():
	print('\n###### Installing Octave')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install octave -y')
	print('###### Done')
	print("###### Type 'octave' to start.")
	backtomenu_option()

def fpcompiler():
	print('\n###### Installing fp-compiler')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install fp-compiler -y')
	print('###### Done')
	print("###### Type 'fpc' to start.")
	backtomenu_option()

def numpy():
	print('\n###### Installing numpy')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install numpy -y')
	print('###### Done')
	print("###### Type 'pkg files numpy | grep usr/bin' to check executable file related to numpy package.")
	backtomenu_option()

def userrecon():
	print('\n###### Installing userrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	print('###### Done')
	print("###### Type 'userrecon' to start.")
	backtomenu_option()

def mrsip():
	print('\n###### Installing Mr.SIP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	print('This mf tried to move Mr.SIP {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tmscanner():
	print('\n###### Installing TM-scanner')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python python2 nmap git -y')
	os.system('python -m pip install colorama requests')
	os.system('python2 -m pip install colorama requests')
	os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	print('This mf tried to move TM-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xss_payload_list():
	print('\n###### Installing xss-payload-list')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/payloadbox/xss-payload-list')
	print('This mf tried to move xss-payload-list {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickbot():
	print('\n###### Installing ClickBot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ziziwho/clickbot')
	os.system("python -m pip install asyncio colorama telethon rsa pyaes asyncio async_generator colorama bs4 requests")
	print('This mf tried to move clickbot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def phoneinfoga():
	print('\n###### Installing PhoneInfoga')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	os.chdir("PhoneInfoga")
	os.system("python -m pip install -r requirements.txt")
	os.chdir("..")
	print('This mf tried to move PhoneInfoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def btc2idr():
	print('\n###### Installing BTC-to-IDR-checker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/guruku/BTC-to-IDR-checker')
	print('This mf tried to move BTC-to-IDR-checker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sitebroker():
	print('\n###### Installing SiteBroker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python php git -y')
	os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	os.chdir("SiteBroker")
	os.system('python -m pip install -r requirements.txt')
	os.system('python -m pip install html5lib')
	os.chdir("..")
	print('This mf tried to move SiteBroker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dostattack():
	print('\n###### Installing dost-attack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/verluchie/dost-attack')
	print('This mf tried to move dost-attack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cfr():
	print('\n###### Installing CFR')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dx wget -y')
	os.system('mkdir $PREFIX/bin/lib')
	os.system('wget https://www.benf.org/other/cfr/cfr-0.151.jar -O $PREFIX/bin/lib/cfr-0.151.jar')
	os.chdir(prefix+"/bin/lib")
	os.system('dx --dex --output=cfr-0.151.dex cfr-0.151.jar')
	with open(prefix+"/bin/cfr","w") as f:
		f.write("#!/usr/bin/bash\n")
		f.write("dalvikvm -cp $PREFIX/bin/lib/cfr-0.151.dex org/benf/cfr/reader/Main \"$@\"")
	os.system('chmod 755 $PREFIX/bin/cfr')
	os.system('chmod 755 $PREFIX/bin/lib/cfr-0.151.dex')
	os.chdir(current_dir)
	print('###### Done')
	print("###### Type 'cfr' to start.")
	backtomenu_option()

def upx():
	print('\n###### Installing UPX')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget tar -y')
	os.system('wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-arm64_linux.tar.xz')
	os.system('tar xf upx-3.96-arm64_linux.tar.xz')
	print('This mf tried to move upx-3.96-arm64_linux/upx $PREFIX/bin/upx')
	os.system('rm -rf upx-3.96-arm64_linux upx-3.96-arm64_linux.tar.xz')
	os.system('chmod 755 $PREFIX/bin/upx')
	print('###### Done')
	print("###### Type 'upx' to start.")
	backtomenu_option()

def pyinstxtractor():
	print('\n###### Installing pyinstxtractor')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/extremecoders-re/pyinstxtractor')
	print('This mf tried to move pyinstxtractor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def innoextract():
	print('\n###### Installing innoextract')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git clang -y')
	os.system('git clone https://github.com/dscharrer/innoextract')
	os.chdir("innoextract")
	os.system('mkdir -p build')
	os.chdir("build")
	os.system('cmake .. && make')
	print('This mf tried to move innoextract $PREFIX/bin && chmod 755 $PREFIX/bin/innoextract')
	os.chdir(current_dir)
	os.system('rm -rf innoextract')
	print('###### Done')
	print("###### Type 'innoextract' to start.")
	backtomenu_option()

def lynis():
	print('\n###### Installing Lynis')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/CISOfy/lynis')
	print('This mf tried to move lynis {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def chkrootkit():
	print('\n###### Installing Chkrootkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang git -y')
	os.system('git clone https://github.com/Magentron/chkrootkit')
	print('This mf tried to move chkrootkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clamav():
	print('\n###### Installing ClamAV')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clamav -y')
	os.system('freshclam')
	print('###### Done')
	print("###### Type 'clamscan' to start.")
	backtomenu_option()

def yara():
	print('\n###### Installing Yara')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install yara -y')
	print('###### Done')
	print("###### Type 'yara' to start.")
	backtomenu_option()

def virustotal():
	print('\n###### Installing VirusTotal-CLI')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install virustotal-cli -y')
	print('###### Done')
	print("###### Type 'vt' to start.")
	backtomenu_option()

def maigret():
	print('\n###### Installing maigret')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	print('###### Done')
	print("###### Usage: maigret <username>")
	print("###### Usage: maigret -h")
	backtomenu_option()

def xplsearch():
	print('\n###### Installing XPL-SEARCH')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php -y')
	os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	print('This mf tried to move XPL-SEARCH {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xadmin():
	print('\n###### Installing Xadmin')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git perl -y')
	os.system('git clone https://github.com/Manisso/Xadmin')
	print('This mf tried to move Xadmin {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def credmap():
	print('\n###### Installing Credmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/lightos/credmap')
	print('This mf tried to move credmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def mapeye():
	print('\n###### Installing MapEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	print('This mf tried to move MapEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gathetool():
	print('\n###### Installing GatheTOOL')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	print('This mf tried to move GatheTOOL {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def avpass():
	print('\n###### Installing avpass')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 python -y')
	os.system('git clone https://github.com/sslab-gatech/avpass')
	print('This mf tried to move avpass {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def binwalk():
	print('\n###### Installing binwalk')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install gzip bzip2 tar arj lhasa p7zip cabextract sleuthkit lzop mtd-utils cmake build-essential make numpy scipy python git -y')
	os.system('git clone https://github.com/ReFirmLabs/binwalk')
	os.chdir("binwalk")
	os.system('python setup.py install')
	os.chdir("..")
	print('This mf tried to move binwalk {}'.format(homeDir))
	print('###### Done')
	print("###### Type 'binwalk' to start.")
	backtomenu_option()

def arat():
	print('\n###### Installing A-Rat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/RexTheGod/A-Rat')
	print('This mf tried to move A-Rat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def adbtk():
	print('\n###### Installing ADB-Toolkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	print('This mf tried to move ADB-Toolkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androbugs():
	print('\n###### Installing AndroBugs_Framework')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install pymongo')
	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	print('This mf tried to move AndroBugs_Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tekdefense():
	print('\n###### Installing TekDefense-Automater')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	print('This mf tried to move TekDefense-Automater {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def baf():
	print('\n###### Installing BAF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests bs4 selenium colored termcolor')
	os.system('git clone https://github.com/engMaher/BAF')
	print('This mf tried to move BAF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutex():
	print('\n###### Installing BruteX')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git hydra -y')
	os.system('git clone https://github.com/1N3/BruteX')
	print('This mf tried to move BruteX {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmseek():
	print('\n###### Installing CMSeeK')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
	print('This mf tried to move CMSeeK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmsmap():
	print('\n###### Installing CMSmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/Dionach/CMSmap')
	print('This mf tried to move CMSmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickjacking():
	print('\n###### Installing Clickjacking-Tester')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
	print('This mf tried to move Clickjacking-Tester {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cookiestealer():
	print('\n###### Installing Cookie-stealer')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php -y')
	os.system('git clone https://github.com/Xyl2k/Cookie-stealer')
	print('This mf tried to move Cookie-stealer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dhcpig():
	print('\n###### Installing DHCPig')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/kamorin/DHCPig')
	print('This mf tried to move DHCPig {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cyberscan():
	print('\n###### Installing CyberScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/medbenali/CyberScan')
	print('This mf tried to move CyberScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dkmc():
	print('\n###### Installing DKMC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/Mr-Un1k0d3r/DKMC')
	os.mkdir("DKMC/output")
	print('This mf tried to move DKMC {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def crawlbox():
	print('\n###### Installing CrawlBox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install tldextract requests requests_ntlm fake_useragent')
	os.system('git clone https://github.com/abaykan/CrawlBox')
	print('This mf tried to move CrawlBox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def eagleeye():
	print('\n###### Installing EagleEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install termcolor opencv-python selenium face_recognition WeasyPrint requests-html')
	os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
	print('This mf tried to move EagleEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gemailhack():
	print('\n###### Installing Gemail-Hack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/Ha3MrX/Gemail-Hack')
	print('This mf tried to move Gemail-Hack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def eyewitness():
	print('\n###### Installing EyeWitness')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
	print('This mf tried to move EyeWitness {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goblinwordgenerator():
	print('\n###### Installing GoblinWordGenerator')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/UndeadSec/GoblinWordGenerator')
	print('This mf tried to move GoblinWordGenerator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inspy():
	print('\n###### Installing InSpy')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
	os.system('git clone https://github.com/leapsecurity/InSpy')
	print('This mf tried to move InSpy {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def leaked():
	print('\n###### Installing Leaked')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/GitHackTools/Leaked')
	print('This mf tried to move Leaked {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gloomframework():
	print('\n###### Installing Gloom-Framework')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nmap python -y')
	os.system('python -m pip install mechanize pythonwhois')
	os.system('git clone https://github.com/StreetSec/Gloom-Framework')
	print('This mf tried to move Gloom-Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def lfisuite():
	print('\n###### Installing LFISuite')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/D35m0nd142/LFISuite')
	print('This mf tried to move LFISuite {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def parsero():
	print('\n###### Installing Parsero')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/behindthefirewalls/Parsero')
	print('This mf tried to move Parsero {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pwnstar():
	print('\n###### Installing PwnSTAR')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/SilverFoxx/PwnSTAR')
	print('This mf tried to move PwnSTAR {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pybozocrack():
	print('\n###### Installing PyBozoCrack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install wheel==0.22.0')
	os.system('git clone https://github.com/ikkebr/PyBozoCrack')
	print('This mf tried to move PyBozoCrack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pyrit():
	print('\n###### Installing Pyrit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install httplib2==0.10.3 colorlog==2.10.0 beautifulsoup4==4.5.3 protobuf==3.2.0rc2 requests==2.11.1 google==1.9.3')
	os.system('git clone https://github.com/JPaulMora/Pyrit')
	print('This mf tried to move Pyrit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sn1per():
	print('\n###### Installing Sn1per')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/1N3/Sn1per')
	os.chdir("Sn1per")
	os.system("bash install.sh")
	os.chdir("..")
	print('This mf tried to move Sn1per {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sublist3r():
	print('\n###### Installing Sublist3r')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install argparse dnspython requests')
	os.system('git clone https://github.com/aboul3la/Sublist3r')
	print('This mf tried to move Sublist3r {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wppluginscanner():
	print('\n###### Installing WP-plugin-scanner')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/mintobit/WP-plugin-scanner')
	print('This mf tried to move WP-plugin-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def whatweb():
	print('\n###### Installing WhatWeb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/urbanadventurer/WhatWeb')
	print('This mf tried to move WhatWeb {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zerodoor():
	print('\n###### Installing Zerodoor')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git gcc nmap-ncat python2 -y')
	os.system('git clone https://github.com/Souhardya/Zerodoor')
	print('This mf tried to move Zerodoor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutespray():
	print('\n###### Installing brutespray')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install argcomplete==1.10.0')
	os.system('git clone https://github.com/x90skysn3k/brutespray')
	print('This mf tried to move brutespray {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()


def pycdc():
	print('\n###### Installing pycdc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python clang cmake make -y')
	os.system('git clone https://github.com/zrax/pycdc')
	print('This mf tried to move pycdc {}'.format(homeDir))
	os.chdir(homeDir)
	os.chdir("pycdc")
	os.system('cmake .')
	os.system('make')
	os.system('make check')
	os.chdir(current_dir)
	print('###### Done')
	backtomenu_option()

def apkid():
	print('\n###### Installing APKiD')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python yara yara-static -y')
	os.system('python -m pip install apkid')
	print('###### Done')
	print("###### Type 'apkid' to start.")
	backtomenu_option()

def dtlx():
	print('\n###### Installing DTL-X')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git apktool apksigner openjdk-17 -y')
	os.system('python -m pip install loguru')
	os.system('git clone https://github.com/Gameye98/DTL-X')
	print('This mf tried to move DTL-X {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def crowbar():
	print('\n###### Installing crowbar')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install paramiko==2.7.1')
	os.system('git clone https://github.com/galkan/crowbar')
	print('This mf tried to move crowbar {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def voidLinux():
	print('\n###### Installing Void Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install void')
	print("###### Type 'proot-distro login void' to start.")
	print('###### Done')
	backtomenu_option()

def apkleaks():
	print('\n###### Installing APKLeaks')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	if not os.path.isfile(os.getenv("PREFIX")+"/bin/jadx"):
		os.system('apt install dpkg wget -y')
		os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
		os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
		os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	os.system('python -m pip install apkleaks')
	print('###### Done')
	print("###### Type 'apkleaks' to start.")
	print("###### Usage: apkleaks -f /path/file.apk")
	backtomenu_option()

def apkmitm():
	print('\n###### Installing apk-mitm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nodejs apktool -y')
	os.system('npm i -g apk-mitm')
	open(os.getenv("HOME")+"/.bashrc","a").write("\nalias apk-mitm=\"apk-mitm --apktool $PREFIX/share/java/apktool.jar\"\n")
	print('###### Done')
	print("###### Type 'apk-mitm' to start.")
	print("###### Usage: apk-mitm /path/file.apk")
	backtomenu_option()

def ssl_pinning_remover():
	print('\n###### Installing ssl_pinning_remover')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	os.system('python -m pip install ssl-pinning-remover')
	print('###### Done')
	print("###### Type 'ssl_pinning_remover' to start.")
	print("###### Usage: ssl_pinning_remover -i /path/file.apk -v")
	backtomenu_option()

def elpscrk():
	print('\n###### Installing elpscrk')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install colorama~=0.4.4 psutil~=5.8.0 click~=8.0.1 phonenumbers~=8.12.27')
	os.system('git clone https://github.com/D4Vinci/elpscrk')
	print('This mf tried to move elpscrk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilginx():
	print('\n###### Installing evilginx')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nginx python2 -y')
	os.system('git clone https://github.com/kgretzky/evilginx')
	print('This mf tried to move evilginx {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbht():
	print('\n###### Installing fbht')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('apt install python2-numpy')
	os.system('python2 -m pip install mechanize')
	os.system('git clone https://github.com/chinoogawa/fbht')
	print('This mf tried to move fbht {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fierce():
	print('\n###### Installing fierce')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install dnspython==1.16.0 fierce')
	print('###### Done')
	print("###### Usage: fierce -h")
	backtomenu_option()

def fuxploider():
	print('\n###### Installing fuxploider')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests coloredlogs bs4')
	os.system('git clone https://github.com/almandin/fuxploider')
	print('This mf tried to move fuxploider {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gasmask():
	print('\n###### Installing gasmask')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
	os.system('git clone https://github.com/twelvesec/gasmask')
	print('This mf tried to move gasmask {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

### Compiler/Interpreter
def python2():
	print('\n###### Installing Python2')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 -y')
	print('###### Done')
	print("###### Type 'python2' to start.")
	backtomenu_option()

def ecj():
	print('\n###### Installing ecj')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ecj -y')
	print('###### Done')
	print("###### Type 'ecj' to start.")
	backtomenu_option()

def golang():
	print('\n###### Installing Golang')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install golang -y')
	print('###### Done')
	print("###### Type 'go' to start.")
	backtomenu_option()

def ldc():
	print('\n###### Installing ldc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ldc -y')
	print('###### Done')
	print("###### Type 'ldc2' to start.")
	backtomenu_option()

def nim():
	print('\n###### Installing Nim')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nim -y')
	print('###### Done')
	print("###### Type 'nim' to start.")
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install shc -y')
	print('###### Done')
	print("###### Type 'shc' to start.")
	backtomenu_option()

def tcc():
	print('\n###### Installing TCC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tcc -y')
	print('###### Done')
	print("###### Type 'tcc' to start.")
	backtomenu_option()

def php():
	print('\n###### Installing PHP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php -y')
	print('###### Done')
	print("###### Type 'php' to start.")
	backtomenu_option()

def ruby():
	print('\n###### Installing Ruby')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ruby -y')
	print('###### Done')
	print("###### Type 'ruby' to start.")
	backtomenu_option()

def perl():
	print('\n###### Installing Perl')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install perl -y')
	print('###### Done')
	print("###### Type 'perl' to start.")
	backtomenu_option()

def vlang():
	print('\n###### Installing Vlang')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install vlang -y')
	print('###### Done')
	print("###### Type 'vlang' to start.")
	backtomenu_option()

def blogc():
	print('\n###### Installing BlogC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install blogc -y')
	print('###### Done')
	print("###### Type 'blogc' to start.")
	backtomenu_option()

def dart():
	print('\n###### Installing Dart')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dart -y')
	print('###### Done')
	print("###### Type 'dart' to start.")
	backtomenu_option()

def yasm():
	print('\n###### Installing Yasm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install yasm -y')
	print('###### Done')
	print("###### Type 'yasm' to start.")
	backtomenu_option()

def nasm():
	print('\n###### Installing Nasm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nasm -y')
	print('###### Done')
	print("###### Type 'nasm' to start.")
	backtomenu_option()

### termux games
def street_car():
	print('\n###### Installing street-car')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python python2 -y')
	os.system('git clone https://github.com/JustaHackers/street_car')
	print('This mf tried to move street_car {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def flappy_bird():
	print('\n###### Installing flappy-bird')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/flappy_bird')
	print("[DEV] Homedir:" + format(homeDir))
	print('This mf tried to move flappy_bird {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def speed_typing():
	print('\n###### Installing Speed Typing')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/typing-speed-test')
	print('This mf tried to move typing-speed-test {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nsnake():
	print('\n###### Installing nsnake')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nsnake -y')
	print('###### Done')
	print("###### Type 'nsnake' to start.")
	backtomenu_option()

def nudoku():
	print('\n###### Installing Sudoku')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nudoku -y')
	print('###### Done')
	print("###### Type 'nudoku' to start.")
	backtomenu_option()

def moon_buggy():
	print('\n###### Installing Moon-Buggy')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install moon-buggy -y')
	print('###### Done')
	print("###### Type 'moon-buggy' to start.")
	backtomenu_option()

def ttysolitaire():
	print('\n###### Installing tty-solitaire')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tty-solitaire -y')
	print('###### Done')
	print("###### Type 'ttysolitaire' to start.")
	backtomenu_option()

def pacman4console():
	print('\n###### Installing Pacman4Console')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install pacman4console -y')
	print('###### Done')
	print("###### Type 'pacman' to start.")
	backtomenu_option()

### bash function ---
def fbvid():
	print('\n###### Installing fbvid')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python ffmpeg -y')
	os.system('python -m pip install youtube-dl')
	fbvid_code = open(".myshfunc/fbvid.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(fbvid_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: fbvid "POST_URL"')
	backtomenu_option()

def cast2video():
	print('\n###### Installing cast2video')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang python ffmpeg -y')
	os.system('python -m pip install CPython ttygif')
	cast2video_code = open(".myshfunc/cast2video.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(cast2video_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: cast2video file.cast')
	backtomenu_option()

def iconset():
	print('\n###### Installing iconset')
	iconset_code = open(".myshfunc/iconset.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(iconset_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: iconset project_name icon.png')
	backtomenu_option()

def readme():
	print('\n###### Installing readme')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl -y')
	readme_code = open(".myshfunc/readme.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(readme_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: readme User/Repo')
	backtomenu_option()

def makedeb():
	print('\n###### Installing makedeb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg neovim -y')
	makedeb_code = open(".myshfunc/makedeb.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(makedeb_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: makedeb')
	backtomenu_option()

def quikfind():
	print('\n###### Installing quikfind')
	quikfind_code = open(".myshfunc/quikfind.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(quikfind_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: quikfind')
	backtomenu_option()

def pranayama():
	print('\n###### Installing pranayama')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install termux-api -y')
	pranayama_code = open(".myshfunc/pranayama.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(pranayama_code)
	os.system('source '+os.getenv("HOME")+"./bashrc")
	print('###### Done')
	print('###### Usage: pranayama')
	print('######            or')
	print('######        pranayama [n]')
	backtomenu_option()

def sqlc():
	print('\n###### Installing sqlc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python sqlite3 -y')
	sqlc_code = open(".myshfunc/sqlc.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(sqlc_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: sqlc db_file sql_script')
	backtomenu_option()

def main():
	banner()
	print("   [01] Information Gathering")
	print("   [02] Vulnerability Analysis")
	print("   [03] Web Hacking")
	print("   [04] Database Assessment")
	print("   [05] Password Attacks")
	print("   [06] Wireless Attacks")
	print("   [07] Reverse Engineering")
	print("   [08] Exploitation Tools")
	print("   [09] Sniffing and Spoofing")
	print("   [10] Reporting Tools")
	print("   [11] Forensic Tools")
	print("   [12] Stress Testing")
	print("   [13] Install Linux Distro")
	print("   [14] Termux Utility")
	print("   [15] Shell Function [.bashrc]")
	print("   [16] Install CLI Games")
	print("   [17] Malware Analysis")
	print("   [18] Compiler/Interpreter")
	print("   [19] Social Engineering Tools \n")
	print("   [00] Exit the Lazymux\n \n")
	print("IMPORTANT INFO: Files are saved into ./ due to root downloading problem")
	lazymux = input("lzmx > set_install ")

	# 01 - Information Gathering
	if lazymux.strip() == "1" or lazymux.strip() == "01":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [03] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [04] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [05] Infoga: Tool for Gathering Email Accounts Informations")
		print("    [06] ReconDog: Information Gathering and Vulnerability Scanner tool")
		print("    [07] AndroZenmap")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [10] MapEye: Accurate GPS Location Tracker (Android, IOS, Windows phones)")
		print("    [11] Easymap: Nmap Shortcut")
		print("    [12] BlackBox: A Penetration Testing Framework")
		print("    [13] XD3v: Powerful tool that lets you know all the essential details about your phone")
		print("    [14] Crips: This Tools is a collection of online IP Tools that can be used to quickly get information about IP Address's, Web Pages and DNS records")
		print("    [15] SIR: Resolve from the net the last known ip of a Skype Name")
		print("    [16] EvilURL: Generate unicode evil domains for IDN Homograph Attack and detect them")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Xshell: ToolKit")
		print("    [19] OWScan: OVID Web Scanner")
		print("    [20] OSIF: Open Source Information Facebook")
		print("    [21] Devploit: Simple Information Gathering Tool")
		print("    [22] Namechk: Osint tool based on namechk.com for checking usernames on more than 100 websites, forums and social networks")
		print("    [23] AUXILE: Web Application Analysis Framework")
		print("    [24] inther: Information gathering using shodan, censys and hackertarget")
		print("    [25] GINF: GitHub Information Gathering Tool")
		print("    [26] GPS Tracking")
		print("    [27] ASU: Facebook Hacking ToolKit")
		print("    [28] fim: Facebook Image Downloader")
		print("    [29] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [30] pwnedOrNot: OSINT Tool for Finding Passwords of Compromised Email Accounts")
		print("    [31] Mac-Lookup: Finds information about a Particular Mac address")
		print("    [32] BillCipher: Information Gathering tool for a Website or IP address")
		print("    [33] dnsrecon: Security assessment and network troubleshooting")
		print("    [34] zphisher: Automated Phishing Tool")
		print("    [35] Mr.SIP: SIP-Based Audit and Attack Tool")
		print("    [36] Sherlock: Hunt down social media accounts by username")
		print("    [37] userrecon: Find usernames across over 75 social networks")
		print("    [38] PhoneInfoga: One of the most advanced tools to scan phone numbers using only free resources")
		print("    [39] SiteBroker: A cross-platform python based utility for information gathering and penetration testing automation")
		print("    [40] maigret: Collect a dossier on a person by username from thousands of sites")
		print("    [41] GatheTOOL: Information Gathering - API hackertarget.com")
		print("    [42] ADB-ToolKit")
		print("    [43] TekDefense-Automater: Automater - IP URL and MD5 OSINT Analysis")
		print("    [44] EagleEye: Stalk your Friends. Find their Instagram, FB and Twitter Profiles using Image Recognition and Reverse Image Search")
		print("    [45] EyeWitness: EyeWitness is designed to take screenshots of websites, provide some server header info, and identify default credentials if possible")
		print("    [46] InSpy: A python based LinkedIn enumeration tool")
		print("    [47] Leaked: Leaked? 2.1 - A Checking tool for Hash codes, Passwords and Emails leaked")
		print("    [48] fierce: A DNS reconnaissance tool for locating non-contiguous IP space")
		print("    [49] gasmask: Information gathering tool - OSINT")
		print("\n    [00] Back to main menu\n")
		infogathering = input("lzmx > set_install ")
		if infogathering == "@":
			infogathering = ""
			for x in range(1,201):
				infogathering += f"{x} "
		if len(infogathering.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for infox in infogathering.split():
			if infox.strip() == "01" or infox.strip() == "1": nmap()
			elif infox.strip() == "02" or infox.strip() == "2": red_hawk()
			elif infox.strip() == "03" or infox.strip() == "3": dtect()
			elif infox.strip() == "04" or infox.strip() == "4": sqlmap()
			elif infox.strip() == "05" or infox.strip() == "5": infoga()
			elif infox.strip() == "06" or infox.strip() == "6": reconDog()
			elif infox.strip() == "07" or infox.strip() == "7": androZenmap()
			elif infox.strip() == "08" or infox.strip() == "8": sqlmate()
			elif infox.strip() == "09" or infox.strip() == "9": astraNmap()
			elif infox.strip() == "10": mapeye()
			elif infox.strip() == "11": easyMap()
			elif infox.strip() == "12": blackbox()
			elif infox.strip() == "13": xd3v()
			elif infox.strip() == "14": crips()
			elif infox.strip() == "15": sir()
			elif infox.strip() == "16": evilURL()
			elif infox.strip() == "17": striker()
			elif infox.strip() == "18": xshell()
			elif infox.strip() == "19": owscan()
			elif infox.strip() == "20": osif()
			elif infox.strip() == "21": devploit()
			elif infox.strip() == "22": namechk()
			elif infox.strip() == "23": auxile()
			elif infox.strip() == "24": inther()
			elif infox.strip() == "25": ginf()
			elif infox.strip() == "26": gpstr()
			elif infox.strip() == "27": asu()
			elif infox.strip() == "28": fim()
			elif infox.strip() == "29": maxsubdofinder()
			elif infox.strip() == "30": pwnedOrNot()
			elif infox.strip() == "31": maclook()
			elif infox.strip() == "32": billcypher()
			elif infox.strip() == "33": dnsrecon()
			elif infox.strip() == "34": zphisher()
			elif infox.strip() == "35": mrsip()
			elif infox.strip() == "36": sherlock()
			elif infox.strip() == "37": userrecon()
			elif infox.strip() == "38": phoneinfoga()
			elif infox.strip() == "39": sitebroker()
			elif infox.strip() == "40": maigret()
			elif infox.strip() == "41": gathetool()
			elif infox.strip() == "42": adbtk()
			elif infox.strip() == "43": tekdefense()
			elif infox.strip() == "44": eagleeye()
			elif infox.strip() == "45": eyewitness()
			elif infox.strip() == "46": inspy()
			elif infox.strip() == "47": leaked()
			elif infox.strip() == "48": fierce()
			elif infox.strip() == "49": gasmask()
			elif infox.strip() == "00" or infox.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 02 - Vulnerability Analysis
	elif lazymux.strip() == "2" or lazymux.strip() == "02":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] AndroZenmap")
		print("    [03] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [04] Easymap: Nmap Shortcut")
		print("    [05] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [06] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [07] Damn Small SQLi Scanner: A fully functional SQL injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code")
		print("    [08] SQLiv: massive SQL injection vulnerability scanner")
		print("    [09] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [10] sqlscan: Quick SQL Scanner, Dorker, Webshell injector PHP")
		print("    [11] Wordpresscan: WPScan rewritten in Python + some WPSeku ideas")
		print("    [12] WPScan: Free wordPress security scanner")
		print("    [13] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [14] termux-wordpresscan")
		print("    [15] TM-scanner: websites vulnerability scanner for termux")
		print("    [16] Rang3r: Multi Thread IP + Port Scanner")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [19] Xshell: ToolKit")
		print("    [20] SH33LL: Shell Scanner")
		print("    [21] BlackBox: A Penetration Testing Framework")
		print("    [22] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [23] OWScan: OVID Web Scanner")
		print("    [24] XPL-SEARCH: Search exploits in multiple exploit databases")
		print("    [25] AndroBugs_Framework: An efficient Android vulnerability scanner that helps developers or hackers find potential security vulnerabilities in Android applications")
		print("    [26] Clickjacking-Tester: A python script designed to check if the website if vulnerable of clickjacking and create a poc")
		print("    [27] Sn1per: Attack Surface Management Platform | Sn1perSecurity LLC")
		print("\n    [00] Back to main menu\n")
		vulnsys = input("lzmx > set_install ")
		if vulnsys == "@":
			vulnsys = ""
			for x in range(1,201):
				vulnsys += f"{x} "
		if len(vulnsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for vulnx in vulnsys.split():
			if vulnsys.strip() == "01" or vulnsys.strip() == "1": nmap()
			elif vulnsys.strip() == "02" or vulnsys.strip() == "2": androZenmap()
			elif vulnsys.strip() == "03" or vulnsys.strip() == "3": astraNmap()
			elif vulnsys.strip() == "04" or vulnsys.strip() == "4": easyMap()
			elif vulnsys.strip() == "05" or vulnsys.strip() == "5": red_hawk()
			elif vulnsys.strip() == "06" or vulnsys.strip() == "6": dtect()
			elif vulnsys.strip() == "07" or vulnsys.strip() == "7": dsss()
			elif vulnsys.strip() == "08" or vulnsys.strip() == "8": sqliv()
			elif vulnsys.strip() == "09" or vulnsys.strip() == "9": sqlmap()
			elif vulnsys.strip() == "10": sqlscan()
			elif vulnsys.strip() == "11": wordpreSScan()
			elif vulnsys.strip() == "12": wpscan()
			elif vulnsys.strip() == "13": sqlmate()
			elif vulnsys.strip() == "14": wordpresscan()
			elif vulnsys.strip() == "15": tmscanner()
			elif vulnsys.strip() == "16": rang3r()
			elif vulnsys.strip() == "17": striker()
			elif vulnsys.strip() == "18": routersploit()
			elif vulnsys.strip() == "19": xshell()
			elif vulnsys.strip() == "20": sh33ll()
			elif vulnsys.strip() == "21": blackbox()
			elif vulnsys.strip() == "22": xattacker()
			elif vulnsys.strip() == "23": owscan()
			elif vulnsys.strip() == "24": xplsearch()
			elif vulnsys.strip() == "25": androbugs()
			elif vulnsys.strip() == "26": clickjacking()
			elif vulnsys.strip() == "27": sn1per()
			elif vulnsys.strip() == "00" or vulnsys.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)

	# 03 - Web Hacking
	elif lazymux.strip() == "3" or lazymux.strip() == "03":
		print("\n    [01] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [02] WebDAV: WebDAV File Upload Exploiter")
		print("    [03] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [04] Webdav Mass Exploit")
		print("    [05] Atlas: Quick SQLMap Tamper Suggester")
		print("    [06] sqldump: Dump sql result sites with easy")
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] inther: Information gathering using shodan, censys and hackertarget")
		print("    [10] HPB: HTML Pages Builder")
		print("    [11] Xshell: ToolKit")
		print("    [12] SH33LL: Shell Scanner")
		print("    [13] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [14] XSStrike: Most advanced XSS Scanner")
		print("    [15] Breacher: An advanced multithreaded admin panel finder")
		print("    [16] OWScan: OVID Web Scanner")
		print("    [17] ko-dork: A simple vuln web scanner")
		print("    [18] ApSca: Powerful web penetration application")
		print("    [19] amox: Find backdoor or shell planted on a site via dictionary attack")
		print("    [20] FaDe: Fake deface with kindeditor, fckeditor and webdav")
		print("    [21] AUXILE: Auxile Framework")
		print("    [22] xss-payload-list: Cross Site Scripting ( XSS ) Vulnerability Payload List")
		print("    [23] Xadmin: Admin Panel Finder")
		print("    [24] CMSeeK: CMS Detection and Exploitation suite - Scan WordPress, Joomla, Drupal and over 180 other CMSs")
		print("    [25] CMSmap: A python open source CMS scanner that automates the process of detecting security flaws of the most popular CMSs")
		print("    [26] CrawlBox: Easy way to brute-force web directory")
		print("    [27] LFISuite: Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner")
		print("    [28] Parsero: Robots.txt audit tool")
		print("    [29] Sn1per: Attack Surface Management Platform | Sn1perSecurity LLC")
		print("    [30] Sublist3r: Fast subdomains enumeration tool for penetration testers")
		print("    [31] WP-plugin-scanner: A tool to list plugins installed on a wordpress powered website")
		print("    [32] WhatWeb: Next generation web scanner")
		print("    [33] fuxploider: File upload vulnerability scanner and exploitation tool")
		print("\n    [00] Back to main menu\n")
		webhack = input("lzmx > set_install ")
		if webhack == "@":
			webhack = ""
			for x in range(1,201):
				webhack += f"{x} "
		if len(webhack.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for webhx in webhack.split():
			if webhx.strip() == "01" or webhx.strip() == "1": sqlmap()
			elif webhx.strip() == "02" or webhx.strip() == "2": webdav()
			elif webhx.strip() == "03" or webhx.strip() == "3": maxsubdofinder()
			elif webhx.strip() == "04" or webhx.strip() == "4": webmassploit()
			elif webhx.strip() == "05" or webhx.strip() == "5": atlas()
			elif webhx.strip() == "06" or webhx.strip() == "6": sqldump()
			elif webhx.strip() == "07" or webhx.strip() == "7": websploit()
			elif webhx.strip() == "08" or webhx.strip() == "8": sqlmate()
			elif webhx.strip() == "09" or webhx.strip() == "9": inther()
			elif webhx.strip() == "10": hpb()
			elif webhx.strip() == "11": xshell()
			elif webhx.strip() == "12": sh33ll()
			elif webhx.strip() == "13": xattacker()
			elif webhx.strip() == "14": xsstrike()
			elif webhx.strip() == "15": breacher()
			elif webhx.strip() == "16": owscan()
			elif webhx.strip() == "17": kodork()
			elif webhx.strip() == "18": apsca()
			elif webhx.strip() == "19": amox()
			elif webhx.strip() == "20": fade()
			elif webhx.strip() == "21": auxile()
			elif webhx.strip() == "22": xss_payload_list()
			elif webhx.strip() == "23": xadmin()
			elif webhx.strip() == "24": cmseek()
			elif webhx.strip() == "25": cmsmap()
			elif webhx.strip() == "26": crawlbox()
			elif webhx.strip() == "27": lfisuite()
			elif webhx.strip() == "28": parsero()
			elif webhx.strip() == "29": sn1per()
			elif webhx.strip() == "30": sublist3r()
			elif webhx.strip() == "31": wppluginscanner()
			elif webhx.strip() == "32": whatweb()
			elif webhx.strip() == "33": fuxploider()
			elif webhx.strip() == "00" or webhx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 04 - Database Assessment
	elif lazymux.strip() == "4" or lazymux.strip() == "04":
		print("\n    [01] DbDat: DbDat performs numerous checks on a database to evaluate security")
		print("    [02] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [03] NoSQLMap: Automated NoSQL database enumeration and web application exploitation tool")
		print("    [04] audit_couchdb: Detect security issues, large or small, in a CouchDB server")
		print("    [05] mongoaudit: An automated pentesting tool that lets you know if your MongoDB instances are properly secured")
		print("\n    [00] Back to main menu\n")
		dbssm = input("lzmx > set_install ")
		if dbssm == "@":
			dbssm = ""
			for x in range(1,201):
				dbssm += f"{x} "
		if len(dbssm.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for dbsx in dbssm.split():
			if dbsx.strip() == "01" or dbsx.strip() == "1": dbdat()
			elif dbsx.strip() == "02" or dbsx.strip() == "2": sqlmap()
			elif dbsx.strip() == "03" or dbsx.strip() == "3": nosqlmap
			elif dbsx.strip() == "04" or dbsx.strip() == "4": audit_couchdb()
			elif dbsx.strip() == "05" or dbsx.strip() == "5": mongoaudit()
			elif dbsx.strip() == "00" or dbsx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 05 - Password Attacks
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		print("\n    [01] Hydra: Network logon cracker supporting different services")
		print("    [02] FMBrute: Facebook Multi Brute Force")
		print("    [03] HashID: Software to identify the different types of hashes")
		print("    [04] Facebook Brute Force 3")
		print("    [05] Black Hydra: A small program to shorten brute force sessions on hydra")
		print("    [06] Hash Buster: Crack hashes in seconds")
		print("    [07] FBBrute: Facebook Brute Force")
		print("    [08] Cupp: Common User Passwords Profiler")
		print("    [09] InstaHack: Instagram Brute Force")
		print("    [10] Indonesian Wordlist")
		print("    [11] Xshell")
		print("    [12] Aircrack-ng: WiFi security auditing tools suite")
		print("    [13] BlackBox: A Penetration Testing Framework")
		print("    [14] Katak: An open source software login brute-forcer toolkit and hash decrypter")
		print("    [15] Hasher: Hash cracker with auto detect hash")
		print("    [16] Hash-Generator: Beautiful Hash Generator")
		print("    [17] nk26: Nkosec Encode")
		print("    [18] Hasherdotid: A tool for find an encrypted text")
		print("    [19] Crunch: Highly customizable wordlist generator")
		print("    [20] Hashcat: World's fastest and most advanced password recovery utility")
		print("    [21] ASU: Facebook Hacking ToolKit")
		print("    [22] Credmap: An open source tool that was created to bring awareness to the dangers of credential reuse")
		print("    [23] BruteX: Automatically brute force all services running on a target")
		print("    [24] Gemail-Hack: python script for Hack gmail account brute force")
		print("    [25] GoblinWordGenerator: Python wordlist generator")
		print("    [26] PyBozoCrack: A silly & effective MD5 cracker in Python")
		print("    [27] brutespray: Brute-Forcing from Nmap output - Automatically attempts default creds on found services")
		print("    [28] crowbar: Crowbar is brute forcing tool that can be used during penetration tests")
		print("    [29] elpscrk: An Intelligent wordlist generator based on user profiling, permutations, and statistics")
		print("    [30] fbht: Facebook Hacking Tool")
		print("\n    [00] Back to main menu\n")
		passtak = input("lzmx > set_install ")
		if passtak == "@":
			passtak = ""
			for x in range(1,201):
				passtak += f"{x} "
		if len(passtak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for passx in passtak.split():
			if passx.strip() == "01" or passx.strip() == "1": hydra()
			elif passx.strip() == "02" or passx.strip() == "2": fmbrute()
			elif passx.strip() == "03" or passx.strip() == "3": hashid()
			elif passx.strip() == "04" or passx.strip() == "4": fbBrute()
			elif passx.strip() == "05" or passx.strip() == "5": black_hydra()
			elif passx.strip() == "06" or passx.strip() == "6": hash_buster()
			elif passx.strip() == "07" or passx.strip() == "7": fbbrutex()
			elif passx.strip() == "08" or passx.strip() == "8": cupp()
			elif passx.strip() == "09" or passx.strip() == "9": instaHack()
			elif passx.strip() == "10": indonesian_wordlist()
			elif passx.strip() == "11": xshell()
			elif passx.strip() == "12": aircrackng()
			elif passx.strip() == "13": blackbox()
			elif passx.strip() == "14": katak()
			elif passx.strip() == "15": hasher()
			elif passx.strip() == "16": hashgenerator()
			elif passx.strip() == "17": nk26()
			elif passx.strip() == "18": hasherdotid()
			elif passx.strip() == "19": crunch()
			elif passx.strip() == "20": hashcat()
			elif passx.strip() == "21": asu()
			elif passx.strip() == "22": credmap()
			elif passx.strip() == "23": brutex()
			elif passx.strip() == "24": gemailhack()
			elif passx.strip() == "25": goblinwordgenerator()
			elif passx.strip() == "26": pybozocrack()
			elif passx.strip() == "27": brutespray()
			elif passx.strip() == "28": crowbar()
			elif passx.strip() == "29": elpscrk()
			elif passx.strip() == "30": fbht()
			elif passx.strip() == "00" or passx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 06 - Wireless Attacks
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		print("\n    [01] Aircrack-ng: WiFi security auditing tools suite")
		print("    [02] Wifite: An automated wireless attack tool")
		print("    [03] Wifiphisher: The Rogue Access Point Framework")
		print("    [04] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [05] PwnSTAR: (Pwn SofT-Ap scRipt) - for all your fake-AP needs!")
		print("    [06] Pyrit: The famous WPA precomputed cracker, Migrated from Google")
		print("\n    [00] Back to main menu\n")
		wiretak = input("lzmx > set_install ")
		if wiretak == "@":
			wiretak = ""
			for x in range(1,201):
				wiretak += f"{x} "
		if len(wiretak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for wirex in wiretak.split():
			if wirex.strip() == "01" or wirex.strip() == "1": aircrackng()
			elif wirex.strip() == "02" or wirex.strip() == "2": wifite()
			elif wirex.strip() == "03" or wirex.strip() == "3": wifiphisher()
			elif wirex.strip() == "04" or wirex.strip() == "4": routersploit()
			elif wirex.strip() == "05" or wirex.strip() == "5": pwnstar()
			elif wirex.strip() == "06" or wirex.strip() == "6": pyrit()
			elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 07 - Reverse Engineering
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		print("\n    [01] Binary Exploitation")
		print("    [02] jadx: DEX to JAVA Decompiler")
		print("    [03] apktool: A utility that can be used for reverse engineering Android applications")
		print("    [04] uncompyle6: Python cross-version byte-code decompiler")
		print("    [05] ddcrypt: DroidScript APK Deobfuscator")
		print("    [06] CFR: Yet another java decompiler")
		print("    [07] UPX: Ultimate Packer for eXecutables")
		print("    [08] pyinstxtractor: PyInstaller Extractor")
		print("    [09] innoextract: A tool to unpack installers created by Inno Setup")
		print("    [10] pycdc: C++ python bytecode disassembler and decompiler")
		print("    [11] APKiD: Android Application Identifier for Packers, Protectors, Obfuscators and Oddities - PEiD for Android")
		print("    [12] DTL-X: Python APK Reverser & Patcher Tool")
		print("    [13] APKLeaks: Scanning APK file for URIs, endpoints & secrets")
		print("    [14] apk-mitm: A CLI application that automatically prepares Android APK files for HTTPS inspection")
		print("    [15] ssl-pinning-remover: An SSL Pinning Remover for Android Apps")
		print("\n    [00] Back to main menu\n")
		reversi = input("lzmx > set_install ")
		if reversi == "@":
			reversi = ""
			for x in range(1,201):
				reversi += f"{x} "
		if len(reversi.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for revex in reversi.split():
			if revex.strip() == "01" or revex.strip() == "1": binploit()
			elif revex.strip() == "02" or revex.strip() == "2": jadx()
			elif revex.strip() == "03" or revex.strip() == "3": apktool()
			elif revex.strip() == "04" or revex.strip() == "4": uncompyle()
			elif revex.strip() == "05" or revex.strip() == "5": ddcrypt()
			elif revex.strip() == "06" or revex.strip() == "6": cfr()
			elif revex.strip() == "07" or revex.strip() == "7": upx()
			elif revex.strip() == "08" or revex.strip() == "8": pyinstxtractor()
			elif revex.strip() == "09" or revex.strip() == "9": innoextract()
			elif revex.strip() == "10": pycdc()
			elif revex.strip() == "11": apkid()
			elif revex.strip() == "12": dtlx()
			elif revex.strip() == "13": apkleaks()
			elif revex.strip() == "14": apkmitm()
			elif revex.strip() == "15": ssl_pinning_remover()
			elif revex.strip() == "00" or revex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 08 - Exploitation Tools
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		print("\n    [01] Metasploit: Advanced open-source platform for developing, testing and using exploit code")
		print("    [02] commix: Automated All-in-One OS Command Injection and Exploitation Tool")
		print("    [03] BlackBox: A Penetration Testing Framework")
		print("    [04] Brutal: Payload for teensy like a rubber ducky but the syntax is different")
		print("    [05] TXTool: An easy pentesting tool")
		print("    [06] XAttacker: Website Vulnerability Scanner & Auto Exploiter")  
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [09] A-Rat: Remote Administration Tool")
		print("    [10] BAF: Blind Attacking Framework")
		print("    [11] Gloom-Framework: Linux Penetration Testing Framework")
		print("    [12] Zerodoor: A script written lazily for generating cross-platform  backdoors on the go :)")
		print("\n    [00] Back to main menu\n")
		exploitool = input("lzmx > set_install ")
		if exploitool == "@":
			exploitool = ""
			for x in range(1,201):
				exploitool += f"{x} "
		if len(exploitool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for explx in exploitool.split():
			if explx.strip() == "01" or explx.strip() == "1": metasploit()
			elif explx.strip() == "02" or explx.strip() == "2": commix()
			elif explx.strip() == "03" or explx.strip() == "3": blackbox()
			elif explx.strip() == "04" or explx.strip() == "4": brutal()
			elif explx.strip() == "05" or explx.strip() == "5": txtool()
			elif explx.strip() == "06" or explx.strip() == "6": xattacker()
			elif explx.strip() == "07" or explx.strip() == "7": websploit()
			elif explx.strip() == "08" or explx.strip() == "8": routersploit()
			elif explx.strip() == "09" or explx.strip() == "9": arat()
			elif explx.strip() == "10": baf()
			elif explx.strip() == "11": gloomframework()
			elif explx.strip() == "12": zerodoor()
			elif explx.strip() == "00" or explx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 09 - Sniffing and Spoofing
	elif lazymux.strip() == "9" or lazymux.strip() == "09":
		print("\n    [01] KnockMail: Verify if Email Exists")
		print("    [02] tcpdump: A powerful command-line packet analyzer")
		print("    [03] Ettercap: Comprehensive suite for MITM attacks, can sniff live connections, do content filtering on the fly and much more")
		print("    [04] hping3: hping is a command-line oriented TCP/IP packet assembler/analyzer")
		print("    [05] tshark: Network protocol analyzer and sniffer")
		print("\n    [00] Back to main menu\n")
		sspoof = input("lzmx > set_install ")
		if sspoof == "@":
			sspoof = ""
			for x in range(1,201):
				sspoof += f"{x} "
		if len(sspoof.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for sspx in sspoof.split():
			if sspx.strip() == "01" or sspx.strip() == "1": knockmail()
			elif sspx.strip() == "02" or sspx.strip() == "2": tcpdump()
			elif sspx.strip() == "03" or sspx.strip() == "3": ettercap()
			elif sspx.strip() == "04" or sspx.strip() == "4": hping3()
			elif sspx.strip() == "05" or sspx.strip() == "5": tshark()
			elif sspx.strip() == "00" or sspx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 10 - Reporting Tools
	elif lazymux.strip() == "10":
		print("\n    [01] dos2unix: Converts between DOS and Unix text files")
		print("    [02] exiftool: Utility for reading, writing and editing meta information in a wide variety of files")
		print("    [03] iconv: Utility converting between different character encodings")
		print("    [04] mediainfo: Command-line utility for reading information from media files")
		print("    [05] pdfinfo: PDF document information extractor")
		print("\n    [00] Back to main menu\n")
		reportls = input("lzmx > set_install ")
		if reportls == "@":
			reportls = ""
			for x in range(1,201):
				reportls += f"{x} "
		if len(reportls.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for reportx in reportls.split():
			if reportx.strip() == "01" or reportx.strip() == "1": dos2unix()
			elif reportx.strip() == "02" or reportx.strip() == "2": exiftool()
			elif reportx.strip() == "03" or reportx.strip() == "3": iconv()
			elif reportx.strip() == "04" or reportx.strip() == "4": mediainfo()
			elif reportx.strip() == "05" or reportx.strip() == "5": pdfinfo()
			elif reportx.strip() == "00" or reportx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 11 - Forensic Tools
	elif lazymux.strip() == "11":
		print("\n    [01] steghide: Embeds a message in a file by replacing some of the least significant bits")
		print("    [02] tesseract: Tesseract is probably the most accurate open source OCR engine available")
		print("    [03] sleuthkit: The Sleuth Kit (TSK) is a library for digital forensics tools")
		print("    [04] CyberScan: Network's Forensics ToolKit")
		print("    [05] binwalk: Firmware analysis tool")
		print("\n    [00] Back to main menu\n")
		forensc = input("lzmx > set_install ")
		if forensc == "@":
			forensc = ""
			for x in range(1,201):
				forensc += f"{x} "
		if len(forensc.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for forenx in forensc.split():
			if forenx.strip() == "01" or forenx.strip() == "1": steghide()
			elif forenx.strip() == "02" or forenx.strip() == "2": tesseract()
			elif forenx.strip() == "03" or forenx.strip() == "3": sleuthkit()
			elif forenx.strip() == "04" or forenx.strip() == "4": cyberscan()
			elif forenx.strip() == "05" or forenx.strip() == "5": binwalk()
			elif forenx.strip() == "00" or forenx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 12 - Stress Testing
	elif lazymux.strip() == "12":
		print("\n    [01] Torshammer: Slow post DDOS tool")
		print("    [02] Slowloris: Low bandwidth DoS tool")
		print("    [03] Fl00d & Fl00d2: UDP Flood tool")
		print("    [04] GoldenEye: GoldenEye Layer 7 (KeepAlive+NoCache) DoS test tool")
		print("    [05] Xerxes: The most powerful DoS tool")
		print("    [06] Planetwork-DDOS")
		print("    [07] Xshell")
		print("    [08] santet-online: Social Engineering Tool")
		print("    [09] dost-attack: WebServer Attacking Tools")
		print("    [10] DHCPig: DHCP exhaustion script written in python using scapy network library")
		print("\n    [00] Back to main menu\n")
		stresstest = input("lzmx > set_install ")
		if stresstest == "@":
			stresstest = ""
			for x in range(1,201):
				stresstest += f"{x} "
		if len(stresstest.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for stressx in stresstest.split():
			if stressx.strip() == "01" or stressx.strip() == "1": torshammer()
			elif stressx.strip() == "02" or stressx.strip() == "2": slowloris()
			elif stressx.strip() == "03" or stressx.strip() == "3": fl00d12()
			elif stressx.strip() == "04" or stressx.strip() == "4": goldeneye()
			elif stressx.strip() == "05" or stressx.strip() == "5": xerxes()
			elif stressx.strip() == "06" or stressx.strip() == "6": planetwork_ddos()
			elif stressx.strip() == "07" or stressx.strip() == "7": xshell()
			elif stressx.strip() == "08" or stressx.strip() == "8": sanlen()
			elif stressx.strip() == "09" or stressx.strip() == "9": dostattack()
			elif stressx.strip() == "10": dhcpig()
			elif stressx.strip() == "00" or stressx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 13 - Install Linux Distro
	elif lazymux.strip() == "13":
		print("\n    [01] Ubuntu (impish)")
		print("    [02] Fedora")
		print("    [03] Kali Nethunter")
		print("    [04] Parrot")
		print("    [05] Arch Linux")
		print("Errors for 05-09. Sorry for that.")
		print("    [10] Void Linux")
		print("\n    [00] Back to main menu\n")
		innudis = input("lzmx > set_install ")
		if innudis == "@":
			innudis = ""
			for x in range(1,201):
				innudis += f"{x} "
		if len(innudis.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for innux in innudis.split():
			if innux.strip() == "01" or innux.strip() == "1": ubuntu()
			elif innux.strip() == "02" or innux.strip() == "2": fedora()
			elif innux.strip() == "03" or innux.strip() == "3": nethunter()
			elif innux.strip() == "04" or innux.strip() == "4": parrot()
			elif innux.strip() == "05" or innux.strip() == "5": archlinux()
			elif innux.strip() == "10": voidLinux()
			elif innux.strip() == "00" or innux.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 14 - Termux Utility
	elif lazymux.strip() == "14":
		print("\n    [01] SpiderBot: Curl website using random proxy and user agent")
		print("    [02] Ngrok: tunnel local ports to public URLs and inspect traffic")
		print("    [03] Sudo: sudo installer for Android")
		print("    [04] google: Python bindings to the Google search engine")
		print("    [05] kojawafft")
		print("    [06] ccgen: Credit Card Generator")
		print("    [07] VCRT: Virus Creator")
		print("    [08] E-Code: PHP Script Encoder")
		print("    [09] Termux-Styling")
		print("    [11] xl-py: XL Direct Purchase Package")
		print("    [12] BeanShell: A small, free, embeddable Java source interpreter with object scripting language features, written in Java")
		print("    [13] vbug: Virus Maker")
		print("    [14] Crunch: Highly customizable wordlist generator")
		print("    [15] Textr: Simple tool for running text")
		print("    [16] heroku: CLI to interact with Heroku")
		print("    [17] RShell: Reverse shell for single listening")
		print("    [18] TermPyter: Fix all error Jupyter installation on termux")
		print("    [19] Numpy: The fundamental package for scientific computing with Python")
		print("    [20] BTC-to-IDR-checker: Check the exchange rate virtual money currency to Indonesia Rupiah from Bitcoin.co.id API")
		print("    [21] ClickBot: Earn money using telegram bot")
		print("\n    [00] Back to main menu\n")
		moretool = input("lzmx > set_install ")
		if moretool == "@":
			moretool = ""
			for x in range(1,201):
				moretool += f"{x} "
		if len(moretool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for moret in moretool.split():
			if moret.strip() == "01" or moret.strip() == "1": spiderbot()
			elif moret.strip() == "02" or moret.strip() == "2": ngrok()
			elif moret.strip() == "03" or moret.strip() == "3": sudo()
			elif moret.strip() == "04" or moret.strip() == "4": google()
			elif moret.strip() == "05" or moret.strip() == "5": kojawafft()
			elif moret.strip() == "06" or moret.strip() == "6": ccgen()
			elif moret.strip() == "07" or moret.strip() == "7": vcrt()
			elif moret.strip() == "08" or moret.strip() == "8": ecode()
			elif moret.strip() == "09" or moret.strip() == "9": stylemux()
			elif moret.strip() == "10": passgencvar()
			elif moret.strip() == "11": xlPy()
			elif moret.strip() == "12": beanshell()
			elif moret.strip() == "13": vbug()
			elif moret.strip() == "14": crunch()
			elif moret.strip() == "15": textr()
			elif moret.strip() == "16": heroku()
			elif moret.strip() == "17": rshell()
			elif moret.strip() == "18": termpyter()
			elif moret.strip() == "19": numpy()
			elif moret.strip() == "20": btc2idr()
			elif moret.strip() == "21": clickbot()
			elif moret.strip() == "00" or moret.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 15 - Shell Function [.bashrc]
	elif lazymux.strip() == "15":
		print("\n    [01] FBVid (FB Video Downloader)")
		print("    [02] cast2video (Asciinema Cast Converter)")
		print("    [03] iconset (AIDE App Icon)")
		print("    [04] readme (GitHub README.md)")
		print("    [05] makedeb (DEB Package Builder)")
		print("    [06] quikfind (Search Files)")
		print("    [07] pranayama (4-7-8 Relax Breathing)")
		print("    [08] sqlc (SQLite Query Processor)")
		print("\n    [00] Back to main menu\n")
		myshf = input("lzmx > set_install ")
		if myshf == "@":
			myshf = ""
			for x in range(1,201):
				myshf += f"{x} "
		if len(myshf.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for mysh in myshf.split():
			if mysh.strip() == "01" or mysh.strip() == "1": fbvid()
			elif mysh.strip() == "02" or mysh.strip() == "2": cast2video()
			elif mysh.strip() == "03" or mysh.strip() == "3": iconset()
			elif mysh.strip() == "04" or mysh.strip() == "4": readme()
			elif mysh.strip() == "05" or mysh.strip() == "5": makedeb()
			elif mysh.strip() == "06" or mysh.strip() == "6": quikfind()
			elif mysh.strip() == "07" or mysh.strip() == "7": pranayama()
			elif mysh.strip() == "08" or mysh.strip() == "8": sqlc()
			elif mysh.strip() == "00" or mysh.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 16 - Install CLI Games
	elif lazymux.strip() == "16":
		print("\n    [01] Flappy Bird")
		print("    [02] Street Car")
		print("    [03] Speed Typing")
		print("    [04] NSnake: The classic snake game with textual interface")
		print("    [05] Moon buggy: Simple game where you drive a car across the moon's surface")
		print("    [06] Nudoku: ncurses based sudoku game")
		print("    [07] tty-solitaire")
		print("    [08] Pacman4Console")
		print("\n    [00] Back to main menu\n")
		cligam = input("lzmx > set_install ")
		if cligam == "@":
			cligam = ""
			for x in range(1,201):
				cligam += f"{x} "
		if len(cligam.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for clig in cligam.split():
			if clig.strip() == "01" or clig.strip() == "1": flappy_bird()
			elif clig.strip() == "02" or clig.strip() == "2": street_car()
			elif clig.strip() == "03" or clig.strip() == "3": speed_typing()
			elif clig.strip() == "04" or clig.strip() == "4": nsnake()
			elif clig.strip() == "05" or clig.strip() == "5": moon_buggy()
			elif clig.strip() == "06" or clig.strip() == "6": nudoku()
			elif clig.strip() == "07" or clig.strip() == "7": ttysolitaire()
			elif clig.strip() == "08" or clig.strip() == "8": pacman4console()
			elif clig.strip() == "00" or clig.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 17 - Malware Analysis
	elif lazymux.strip() == "17":
		print("\n    [01] Lynis: Security Auditing and Rootkit Scanner")
		print("    [02] Chkrootkit: A Linux Rootkit Scanners")
		print("    [03] ClamAV: Antivirus Software Toolkit")
		print("    [04] Yara: Tool aimed at helping malware researchers to identify and classify malware samples")
		print("    [05] VirusTotal-CLI: Command line interface for VirusTotal")
		print("    [06] avpass: Tool for leaking and bypassing Android malware detection system")
		print("    [07] DKMC: Dont kill my cat - Malicious payload evasion tool")
		print("\n    [00] Back to main menu\n")
		malsys = input("lzmx > set_install ")
		if malsys == "@":
			malsys = ""
			for x in range(1,201):
				malsys += f"{x} "
		if len(malsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for malx in malsys.split():
			if malx.strip() == "01" or malx.strip() == "1": lynis()
			elif malx.strip() == "02" or malx.strip() == "2": chkrootkit()
			elif malx.strip() == "03" or malx.strip() == "3": clamav()
			elif malx.strip() == "04" or malx.strip() == "4": yara()
			elif malx.strip() == "05" or malx.strip() == "5": virustotal()
			elif malx.strip() == "06" or malx.strip() == "6": avpass()
			elif malx.strip() == "07" or malx.strip() == "7": dkmc()
			elif malx.strip() == "00" or malx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 18 - Compiler/Interpreter
	elif lazymux.strip() == "18":
		print("\n    [01] Python2: Python 2 programming language intended to enable clear programs")
		print("    [02] ecj: Eclipse Compiler for Java")
		print("    [03] Golang: Go programming language compiler")
		print("    [04] ldc: D programming language compiler, built with LLVM")
		print("    [05] Nim: Nim programming language compiler")
		print("    [06] shc: Shell script compiler")
		print("    [07] TCC: Tiny C Compiler")
		print("    [08] PHP: Server-side, HTML-embedded scripting language")
		print("    [09] Ruby: Dynamic programming language with a focus on simplicity and productivity")
		print("    [10] Perl: Capable, feature-rich programming language")
		print("    [11] Vlang: Simple, fast, safe, compiled language for developing maintainable software")
		print("    [12] BeanShell: Small, free, embeddable, source level Java interpreter with object based scripting language features written in Java")
		print("    [13] fp-compiler: Free Pascal is a 32, 64 and 16 bit professional Pascal compiler")
		print("    [14] Octave: Scientific Programming Language")
		print("    [15] BlogC: A blog compiler")
		print("    [16] Dart: General-purpose programming language")
		print("    [17] Yasm: Assembler supporting the x86 and AMD64 instruction sets")
		print("    [18] Nasm: A cross-platform x86 assembler with an Intel-like syntax.")
		print("\n    [00] Back to main menu\n")
		compter = input("lzmx > set_install ")
		if compter == "@":
			compter = ""
			for x in range(1,201):
				compter += f"{x} "
		if len(compter.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for compt in compter.split():
			if compt.strip() == "01" or compt.strip() == "1": python2()
			elif compt.strip() == "02" or compt.strip() == "2": ecj()
			elif compt.strip() == "03" or compt.strip() == "3": golang()
			elif compt.strip() == "04" or compt.strip() == "4": ldc()
			elif compt.strip() == "05" or compt.strip() == "5": nim()
			elif compt.strip() == "06" or compt.strip() == "6": shc()
			elif compt.strip() == "07" or compt.strip() == "7": tcc()
			elif compt.strip() == "08" or compt.strip() == "8": php()
			elif compt.strip() == "09" or compt.strip() == "9": ruby()
			elif compt.strip() == "10": perl()
			elif compt.strip() == "11": vlang()
			elif compt.strip() == "12": beanshell()
			elif compt.strip() == "13": fpcompiler()
			elif compt.strip() == "14": octave()
			elif compt.strip() == "15": blogc()
			elif compt.strip() == "16": dart()
			elif compt.strip() == "17": yasm()
			elif compt.strip() == "18": nasm()
			elif compt.strip() == "00" or compt.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 19 - Social Engineering Tools
	elif lazymux.strip() == "19":
		print("\n    [01] weeman: HTTP server for phishing in python")
		print("    [02] SocialFish: Educational Phishing Tool & Information Collector")
		print("    [03] santet-online: Social Engineering Tool")
		print("    [04] SpazSMS: Send unsolicited messages repeatedly on the same phone number")
		print("    [05] LiteOTP: Multi Spam SMS OTP")
		print("    [06] F4K3: Fake User Data Generator")
		print("    [07] Hac")
		print("    [08] Cookie-stealer: Crappy cookie stealer")
		print("    [09] zphisher: Automated Phishing Tool")
		print("    [10] Evilginx: Advanced Phishing With Two-factor Authentication Bypass")
		print("\n    [00] Back to main menu\n")
		soceng = input("lzmx > set_install ")
		if soceng == "@":
			soceng = ""
			for x in range(1,201):
				soceng += f"{x} "
		if len(soceng.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for socng in soceng.split():
			if socng.strip() == "01" or socng.strip() == "1": weeman()
			elif socng.strip() == "02" or socng.strip() == "2": socfish()
			elif socng.strip() == "03" or socng.strip() == "3": sanlen()
			elif socng.strip() == "04" or socng.strip() == "4": spazsms()
			elif socng.strip() == "05" or socng.strip() == "5": liteotp()
			elif socng.strip() == "06" or socng.strip() == "6": f4k3()
			elif socng.strip() == "07" or socng.strip() == "7": hac()
			elif socng.strip() == "08" or socng.strip() == "8": cookiestealer()
			elif socng.strip() == "09" or socng.strip() == "9": zphisher()
			elif socng.strip() == "10": evilginx()
			elif socng.strip() == "00" or socng.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	elif lazymux.strip() == "0" or lazymux.strip() == "00":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(1)
		restart_program()

x = 1;

if x == 1:
	x = x + 1;
	os.system("clear")
	main()