from flask import Flask

from apscheduler.schedulers.background import BackgroundScheduler

from cryptomon.jobs import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

app.config.from_pyfile('config.py', silent=True)
app.config.from_envvar('CRYPTOMON_SETTINGS', silent=True)

cron = BackgroundScheduler()
job_kwargs = {
    'ether_scan_api_root': app.config['ETHER_SCAN_API_ROOT'],
    'ether_scan_api_key':  app.config['ETHER_SCAN_API_KEY'],
    'check_threshold_min': app.config['CHECK_THRESHOLD_MIN'],
    'check_threshold_max': app.config['CHECK_THRESHOLD_MAX'],
    'mail_from':           app.config['MAIL_FROM'],
    'mail_to':             app.config['MAIL_TO'],
    'mail_server':         app.config['MAIL_SERVER'],
    'mail_user':           app.config['MAIL_USER'],
    'mail_pass':           app.config['MAIL_PASS']
}

cron.add_job(last_price_alarm,
             'interval',
             kwargs=job_kwargs,
             minutes=app.config['CHECK_LAST_PRICE_INTERVAL'])
cron.start()

import cryptomon.views
