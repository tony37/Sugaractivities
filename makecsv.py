#!/usr/bin/env python

import sys, os
from subprocess import call
from path import path

#read aslo.js and produce as csv

pages = ['var aslo','var fructose','var gtk3','var gtk3x','var gtk2','var gtk2x','var github','var githubx']

"""
var fructose = [
["4069","Chat","activity-chat.svg","Chat-84.xo","Chat provides a simple interface for collaborative discussion, be it between two 
individuals or among a group as large as an entire classroom.","help/chat.html"],
"""

def parse(line):
    if not line:
        return []
    entry = []
    item = ""
    state = 'start'
    for i in range(len(line)):
        letter = line[i]
        if state == 'start':
            match = ord(letter) == 34
            if match:
                item = letter
                state = 'copy'
            continue
        if state == 'copy':
            if ord(line[i]) == 34:
                item += letter
                entry.append(item)
                state = 'start'
                item = ''
            else:
                item += letter
            continue
        if item:
            entry.append(item)
    return entry
fin = open('aslo.js','r')
txt = fin.read()
fin.close()
lines = txt.split('\n')
print len(lines)

inpage = False
fout = open('aslo.csv','w')
count = 0
thispage = ""
total = 0
debug = False
count = 0
counti = 0
counta = 0
countn = 0
counth = 0

cmd = 'rm -rf allactivites/*'
call(cmd, shell=True)

for line in lines:
    if not line:
        continue
    if not inpage:
        if 'var ' in line:
            inpage = True
            thispage = line.replace('= [','').strip()
    if line.startswith(']') or (len(line) < 10 and ']' in line):
        if count > 0:
            print thispage, count
        thispage = ""
        count = 0
        inpage = False
    else:
        count += 1
        total += 1
        lineout = ""
        temp = ""
        entry = parse(str(line))
        if entry:
            if entry[0].replace('"','') == "0000":
                continue
            for i in range(len(entry)):
                if i == 2:
                   fn = path('icons/'+entry[2].replace('"',''))
                   if not fn.exists():
                       counti += 1
                       print 'not found', counti, entry[0], fn
                if i == 3:
                   fn = path('activities/'+entry[3].replace('"',''))
                   if not path(fn).exists():
                       print 'not found', entry[0], fn
                       counta += 1
                if i == 4:
                   if len(entry[i])<3:
                       lineout += 'nodesc' + ','
                   else:
                       lineout += 'desc' + ','
                   continue
                if i == 5:
                   if counth > 0:
                       print 'counth', 1
                   if len(entry[5])>=3:
                       fn = path(entry[5].replace('"','').strip())
                       if not fn.exists():
                           print 'help not found', entry[5], fn
                           counth += 1
                           print 'counth incremented', counth
                           lineout += "nohelp,"
                       else:
                           lineout += entry[5] + ','
                   continue
                if i == 6:
                   fn = entry[6].replace('"','').strip()
                   if path(fn).exists():  
                       fin = open(fn,'r')
                       notetxt = fin.read() + ','
                       fin.close()
                       pos1 = notetxt.find('<p>')
                       pos2 = notetxt.find('</p>')
                       lineout += notetxt[pos1+3:pos2]+','
                   else:
                       lineout +=  'not found:' + fn + ','
                       print 'note not found', fn
                       print 'note not found', entry[0],entry[6]
                       countn += 1
                   continue
                if not(entry[i]):
                    lineout += ','
                else:
                    lineout += entry[i] + ','
            print >> fout, lineout
print total

print 'missing links: bundles', counta, 'icons', counti, 'help', counth, 'notes', countn
