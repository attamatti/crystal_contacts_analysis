#!/usr/bin/env python

import sys
try:
	data = open(sys.argv[1],'r').readlines()
	model = sys.argv[2]
except:
	sys.exit('USAGE: find_hbonds.py <hbonds list file> <model #> ')

allhbonds =[]
realdata = False
for i in data:
	if 'H-bonds (donor, acceptor, hydrogen, D..A dist, D-H..A dist):' in i:
		realdata = True
	if realdata ==True and 'H-bonds (donor, acceptor, hydrogen, D..A dist, D-H..A dist):' not in i:
		line = i.split('#')
		linemod  = line[1].split()[0]
		linechain = line[1].split('.')[1].split()[0]
		#print (linemod,linechain)
		#print line
		if linemod == model:
			allhbonds.append(i.replace('\n',''))
comlist = []
for i in allhbonds:
	line = i.split()
	if line[0] != line[4]:
		comlist.append('{0}:{1}'.format(model,line[2]))

print('\nfound {0} residues with H-bonds'.format(len(comlist)))
if len(comlist) > 0:
	print('\nsel {0}\n'.format(' '.join(comlist)))
