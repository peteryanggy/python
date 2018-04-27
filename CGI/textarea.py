# -*- coding: UTF-8 -*-

import cgi,cgitb
import CGI.html_build as html

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = 'Empty!'

content = '''<h2>{content}</h2>'''.format(content=text_content)
htmlText = html.html('TextArea', content)

print(htmlText)