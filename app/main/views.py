"""
views.py

url routing to '/', 'login'
"""

from flask import render_template, session, redirect, url_for, abort, current_app, flash, request
from datetime import datetime
from flask_moment import Moment

from . import main
from .datajkt import jkt_update
from .scrapejkt import updateJKTBlog, updateJKTEvents

@main.route('/')
def index():
    return redirect(url_for(".content"))

@main.route('/admin')
def admin():
    return render_template('admin.html',
                            time=datetime.utcnow())


@main.route('/content')
def content():
    # call jakarta api
    cctv = jkt_update()

    # scrape smartcity.jakarta.go.id news and events
    newsList = updateJKTBlog()
    eventsList = updateJKTEvents()

    # call iframe jakarta api html
    return render_template('content.html',
                            cctvName=cctv[0],
                            cctvURL=cctv[1],
                            newsList=newsList,
                            eventsList=eventsList)

@main.route('/content/puskesmas')
def jkt_puskesmas():
    return render_template('puskesmas_jkt.html')
