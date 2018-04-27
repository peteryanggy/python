# -*- coding: UTF-8 -*-

import os

print('Content-type: text/html\r\n\r\n')
print('<meta> charset="utf-8"')
print('<b>环境变量</b>')
print('<ul>')
for key in os.environ.keys():
    print('<li><span style="color:green">{}</span> : {}</li>'.format(key, os.environ[key]))
print('</ul>')
