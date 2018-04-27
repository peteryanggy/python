# -*- coding: UTF-8 -*-

import cgi,cgitb
import CGI.html_build as html

form = cgi.FieldStorage()
if form.getvalue('google'):
    google_flag = 'Yes'
else:
    google_flag = 'No'

if form.getvalue('baidu'):
    baidu_flag = 'Yes'
else:
    baidu_flag = 'No'

content = '''<h2>Google selected: {google}</h2>
<h2>Baidu selected:{baidu}</h2>'''.format(google=google_flag, baidu=baidu_flag)
htmlText = html.html('Checkbox', content)

print(htmlText)

