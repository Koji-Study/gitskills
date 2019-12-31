#!/usr/bin/python
# -*-coding: utf-8-*-
#import webbrowser
from wsgiref.simple_server import make_server

def Application(environ, start_response):                               # 一个符合wsgi协议的应用程序写法应该接受2个参数
    start_response('200 OK', [('Content-Type', 'text/html')])           #environ为http的相关信息，如请求头等 start_response则是响应信息
    return [b'<!DOCTYPE html>'
            b'<html lang="en">'
            b'<head>'
            b'<meta charset="utf-8">'
            b'<title>Koji-900</title>'
            b'<h1 style="color: red" >Feedback for Jenkins!</h1>'
            b'<img src = "http://127.0.0.1:900/share/timgJOOR4WRM.jpg" width="165" height="60" alt="Can not show this picture for you~"/><br>'
            b'<img src = "../timgJOOR4WRM.jpg" width="165" height="60" alt="Can not show this picture for you~"/><br>'
            b'</head>'
            #b'<a href="">http://www.baidu.com/ target = "_blank" </a>'
            b'<body>'
            b'<a href="#i1">THE FIRST PART</a><br>'
            b'<a href="#i2">THE SECOND PART</a><br>'
            b'<a href="#i3">THE THIRD PART</a><br>'
            b'<a href="#i4">THE FOURTH PART</a><br>'
            b'<div id="i1" style="color: red""height:60px">The First Part</div><br>'
            b'<div id="i2" style="color: yellow""height:60px">The second Part</div><br>'
            b'<div id="i3" style="color: blue""height:600px">The third Part</div><br>'            
            b'<div id="i4" style="color: green""height:600px">The fourth Part</div><br>'
            b'</body>']     #return出来是响应内容

if __name__ == '__main__':
    a = 900
   # webbrowser.open('http://www.baidu.com/')
    httpd = make_server('', a, Application)
    httpd.serve_forever()
