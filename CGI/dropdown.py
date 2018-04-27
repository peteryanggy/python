# -*- coding: UTF-8 -*-

import cgi, cgitb
import CGI.html_build as html

form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = 'Empty!'

content = '''<h2>{select}</h2>'''.format(select=dropdown_value)
htmlText = html.html('Dropdown', content)

print(htmlText)

