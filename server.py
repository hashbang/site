#!/usr/bin/python2.7

import os
import sys
import traceback
import ssl
from flask import Flask, send_file, send_from_directory, redirect, request, make_response
from flask.ext.restful import Resource, Api
from flask.ext.restful.reqparse import RequestParser
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)
app.config['RESTFUL_JSON'] = {"indent": 4}

port = 8080

def security_headers(response, secure=False):
    csp = "default-src 'none'; "                            \
          "style-src https://fonts.googleapis.com 'self'; " \
          "font-src https://fonts.gstatic.com; "            \
          "img-src data:; script-src 'self'; "              \
          "sandbox allow-same-origin allow-scripts; "       \
          "frame-ancestors 'none'"

    response.headers['Content-Security-Policy'] = csp
    response.headers['Referrer-Policy']         = 'no-referrer'
    response.headers['X-Content-Type-Options']  = 'nosniff'
    response.headers['X-Frame-Options']         = 'DENY'
    response.headers['X-XSS-Protection']        = '1; mode=block'

    if secure:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000'

    return response


@app.route('/', methods=["GET"])
def root():
    useragent = request.headers.get('User-Agent')

    if 'curl' in useragent:
        resp = send_from_directory('static', 'warn.sh.asc')
    else:
        resp = send_from_directory('static', 'index.html')

    return security_headers(resp, secure=request.is_secure)


@app.route('/LICENSE.md', methods=['GET'])
def license():
    return security_headers(send_file('LICENSE.md', mimetype='text/markdown'),
                            secure=request.is_secure)

# HE.net domain validation
@app.route('/s73rmwh.txt', methods=['GET'])
def he_net():
    return security_headers(make_response('Hello IPv6!'),
                            secure=request.is_secure)

@app.route('/assets/<path:filename>', methods=['GET'])
def assets(filename):
    return security_headers(send_from_directory('src', filename),
                            secure=request.is_secure)

if __name__ == '__main__':

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()
