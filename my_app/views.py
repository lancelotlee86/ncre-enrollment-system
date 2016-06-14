# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect
from my_app import app, db, exam_plan
from .models import EnrollmentData
from .forms import EnrollmentForm

# 路由写在这里


@app.route('/enroll', methods=['GET'])
def enroll_get():
    import time
    time.sleep(10)
    form = EnrollmentForm(request.form)
    return render_template('enroll.html', form=form)


@app.route('/enroll', methods=['POST'])
def enroll_post():
    # 稍后这里验证验证码（暂时没有做验证码的模块）

    form = EnrollmentForm(request.form)

    # 检查 form 表单中数据的合法性
    if not form.validate_on_submit():   # form 层面先校验数据合法性
        return str(form.errors)

    one_data = db.EnrollmentData(form.data)

    # 检查提交的记录是否已经存在
    if one_data.exist():
        return '不能重复报名'

    # 检查名额是否超出限制
    if EnrollmentData.count() >= exam_plan.site(form.exam_site)['max_cap']:
        return '名额已满'

    #
    res = db.enrollment_data.find()
    one_data.save()
    return redirect(url_for('enroll_get'))

    # 写入数据的方法
    # 方法一
    # dic = {'name': 'John', 'id_number': '445566332222222222'}
    # one = db.enrollment.EnrollmentData(dic)
    # one.save()
    # 方法二
    # one = db.enrollment.EnrollmentData()
    # one['name'] = 'lancelot'
    # one['id_number'] = '410304199312140512'
    # one.save()
