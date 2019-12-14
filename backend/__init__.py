# ----------------------------------------------------------------------------#
# Own Notes.
"""
Description                         | Cmd
to login as the right user for psql | PGUSER=test PGPASSWORD=test psql -h localhost test
Give all right to role              | GRANT ALL PRIVILEGES ON database test to test;
adds temporary git\bit to path      | "c:\Program Files\Git\bin\sh.exe" --login

PGUSER=test PGPASSWORD=test psql -h localhost todoapp
"""
# ----------------------------------------------------------------------------#
import dateutil.parser
import sys
from datetime import datetime
import json
from sqlalchemy import func
import dateutil.parser
from sqlalchemy import distinct
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from model import *
from flask_migrate import Migrate

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()
    db.session.commit()


