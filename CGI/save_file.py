# -*- coding:UTF-8 -*-

import cgi, os
import cgitb
import CGI.html_build as html
import Dictionary.direx as direx, Dictionary.pathex as pathex

form = cgi.FieldStorage()

#获取文件名称
fileItem = form['filename']

#获取当前文件执行路径
root = pathex.getCurrentPath()
#构造文件存储目录
fileTmpDir = os.path.join(root, 'tempdir')
#创建目录
direx.mkdir(fileTmpDir)

try:
    # 检查文件是否上传
    if fileItem.filename:
        # 设置文件路径
        fn = os.path.basename(fileItem.filename)
        buffer = fileItem.file.read()
        dstPath = '{root}\{file}'.format(root=fileTmpDir, file=fn)

        open(dstPath, 'wb').write(buffer)

        message = '文件 "{}" 上传成功'.format(fn)
    else:
        message = '文件上传失败!'

    content = '''<h2>{}</h2>'''.format(message)
except IOError as ex:
    content = '读取文件异常!' + '<br/>' + fileItem.filename + '<br/>' + fn + '<br/>' + \
              ex.message + "<br/>" + ex.strerror

htmlText = html.html('Uploadfile', content)
print(htmlText)

