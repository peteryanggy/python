# -*- coding: UTF-8 -*-

import os
import Cookie

data = object
if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
    except KeyError:
        data = 'cookie 没有设置或已过期!'
else:
    data = '没有设置cookie!'

htmlText = '''Content-Type: text/html\r\n\r\n
<html>
    <head>
        <meta charset="utf-8">
        <title>Cookie</title>
    </head>
    <body>
        <h1>Reading Cookie...</h1>
        {cookie}
    </body>
</html>
'''.format(cookie=data)

print(htmlText)