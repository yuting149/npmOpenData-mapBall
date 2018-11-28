#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from flask import Flask, stream_with_context, request, Response, flash, render_template
from time import sleep
from flask import jsonify

app = Flask(__name__)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


@app.route('/')
def index():
    return render_template('index.html')


def generate():
    for item in data:
        yield str(item)
        sleep(1)


current = datetime.datetime.now()


@app.route('/stream')
def stream_view():
    rows = generate()
    return Response(stream_with_context(rows))


@app.route('/current')
def aa():
    return Response(stream_with_context('aaa'))


@app.route('/current')
def current():
    return Response(stream_with_context('aaa'))


if __name__ == '__main__':
    app.debug = True
    app.run()
