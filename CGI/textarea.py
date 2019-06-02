# -*- coding: UTF-8 -*-

import cgi,cgitb
import CGI.html_build as html
from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
    try:
        text = translator.translate(text_content, src='en', dest='zh-cn').text
    except IOError:
        text = 'IOError'
    else:
        text = 'Else Error'
else:
    text_content = 'Empty!'

content = '''<h2>{content}</h2>'''.format(content=text)
htmlText = html.html('TextArea', content)

print(htmlText)