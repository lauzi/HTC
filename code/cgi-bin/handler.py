# -*- encoding: utf-8 -*-

import cgi

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()
line = form['input'].value

print 'jizz'
print line
