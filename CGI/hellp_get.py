# -*- coding: UTF-8 -*-

import cgi, cgitb
import CGI.html_build as html

#创建 FieldStorage 的实例
form = cgi.FieldStorage()

#获取数据，不管是 get 还是 post 的请求，都可以正常接收
site_name = form.getvalue('name')
site_url = form.getvalue('url')

htmlText = html.html('GET', '<h2>{}: {}</h2>'.format(site_name, site_url))
print(htmlText)






