# -*- coding: UTF-8 -*-

import cgi,cgitb
import CGI.html_build as html

form = cgi.FieldStorage()

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = 'Empty'

content = '''<h2>Your selected is : {site}</h2>'''.format(site=site)
htmlText = html.html('RadioButton', content)

print(htmlText)
