# -*- coding:UTF-8 -*-
def html(title, content):
    return '''Conent-type:text/html\r\n\r\n
    <html>
        <head>
            <meta charset='utf-8'>
            <title>{title}</title>
        </head>
        <body>
            {content}
        </body>
    </html>
    '''.format(title=title, content=content)


