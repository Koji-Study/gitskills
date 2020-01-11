#!/usr/bin/python
# -*-coding: utf-8-*-
#import webbrowser
from wsgiref.simple_server import make_server

def Application(environ, start_response):                               # 一个符合wsgi协议的应用程序写法应该接受2个参数
    start_response('200 OK', [('Content-Type', 'text/html')])           #environ为http的相关信息，如请求头等 start_response则是响应信息
    return [#b'<!DOCTYPE html>'
            b'<html lang="en">'
            b'<head>'
            b'<meta charset="UTF-8">'
            b'<title>Koji-900</title>'
            b'<h1 style="color: red">Feedback for Jenkins!</h1>'
            b'<img src = "http://127.0.0.1:900/share/timgJOOR4WRM.jpg" width="165" height="60" alt="Can not show this picture for you~"/><br>'
            b'<img src = "../timgJOOR4WRM.jpg" width="165" height="60" alt="Can not show this picture for you~"/><br>'
            b'</head>'
            #b'<a href="">http://www.baidu.com/ target = "_blank" </a>'
            b'<body>'
            b'<a href="#i1">第一部分_宋词</a><br>'
            b'<a href="#i2">第二部分_函数解答</a><br>'
            b'<a href="#i3">第三部分_超链接</a><br>'
            b'<a href="#i4">第四部分_其他</a><br>'
            b'<a id="i1"><style="color: red""height:60px">第一部分_宋词</a><br>'
            b'<pre>'
            b'<strong>雨霖铃·寒蝉凄切</strong><br>'
            b'宋代：柳永<br>'
            b'寒蝉凄切，对长亭晚，骤雨初歇。都门帐饮无绪，留恋处，兰舟催发。执手相看泪眼，竟无语凝噎。念去去，千里烟波，暮霭沉沉楚天阔。<br>'
            b'更那堪，冷落清秋节！今宵酒醒何处？杨柳岸，晓风残月。此去经年，应是良辰好景虚设。便纵有千种风情，更与何人说？<br>'
            b'</pre>'
            b'<a id="i2"><style="color: yellow""height:60px">第二部分_函数解答</a><br>'
            b'求解数学方程x<sup>2</sup>+x+6=0.<br/>'
            b'所得解:x<sub>1</sub>=-3,x<sub>2</sub>=2.<br>'
            b'<a id="i3"><style="color: blue""height:600px">第三部分_超链接</a><br>'
            #<!--新建一个浏览器窗口并打开-->
            b'<a href="http://www.baidu.com" target="_blank"> 百度</a><br>'
            b'<a id="i4"><style="color: green""height:600px">第四部分_其他</a><br>'
            b'</body>']     #return出来是响应内容

if __name__ == '__main__':
    a = 900
   # webbrowser.open('http://www.baidu.com/')
    httpd = make_server('', a, Application)
    httpd.serve_forever()
