#!/usr/bin/env python

import random, subprocess

MIN=1
MAX=99
MSG="   Today's number is:   \n\n%s"
COWSAYFILES = ['default','turkey','turtle','tux','unipony','stegosaurus','snowman','pony','gnu','dragon','bud-frogs','bunny']
COWSAY='/usr/games/cowsay'
FIGLET='/usr/bin/figlet'

cowfile = random.choice(COWSAYFILES)
n = str(random.randint(MIN,MAX))

num = subprocess.Popen([FIGLET,'-W','-c','-w',str(len(MSG.splitlines()[0])), n],stdout=subprocess.PIPE)
n = num.communicate()[0]

mesg = MSG % n

proc = subprocess.Popen([COWSAY,'-f',cowfile,'-n'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out = proc.communicate(mesg)[0]
proc.stdin.close()

html = '''
<html><head><title>Number of the day!</title>
<style type='text/css'>
#content {
  display: table;
  margin: 0 auto;
</style></head>
<body><div id='container'><div id='content'><pre>%s</pre></div></div></body>
</html>''' % out

print html

