# -*- coding: utf-8 -*-

from flask import Flask
from flask_mongokit import MongoKit
from .mapper import ExamPlan


app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = MongoKit(app)

exam_plan = ExamPlan(app.config['EXAM_PLAN'])

from my_app import views
