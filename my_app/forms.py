# -*- coding: utf-8 -*-

from my_app import exam_plan
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, ValidationError

from .mapper import id_type_mapper, ExamPlan

from functools import reduce


class EnrollmentForm(Form):
    """
    表单

    进行一些数据合法性的验证，与数据库无关的。
    """
    name = StringField('name', validators=[DataRequired()])
    id_number = StringField('id_number', validators=[DataRequired()])
    # :id_type 的下拉菜单，是 choices参数指定的列表生成的，二元元组
    id_type = SelectField('id_type', validators=[DataRequired()],
                          choices=[(d['value'], d['name']) for d in id_type_mapper.data])
    exam_site = SelectField('exam_site', validators=[DataRequired()],
                            choices=[(exam_site['code'], exam_site['label']) for exam_site in exam_plan.exam_plan['exam_sites']])
    subject = SelectField('subject', validators=[DataRequired()],
                          choices=)

    def validate_exam_site(form, field):
        """
        通过给定的考点代码看看能否找到对应的考点信息
        :param field:
        :return:
        """
        if exam_plan.site(field.data) == False:
            raise ValidationError('未知的考点信息')

    def validate_id_type(form, field):
        if not id_type_mapper.is_contains(field.data):
            raise ValidationError('证件类型未知')

    def validate_id_number(form, field):
        id_number = field.data.upper()
        # 长度
        if len(id_number) != 18:
            raise ValidationError('身份证长度不够')
        # 是否有字母
        if not (id_number[0:17].isnumeric() and (id_number[-1].isnumeric() or id_number[-1] in ['x', 'X'])):
            raise ValidationError('不是真实的身份证号')

        id_number = list(map(lambda x: x, id_number[0:18])) # 转为列表
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # :这个权重乘积和 用了lambda表达式，看起来简洁一些，不过确实难懂
        mul_and_sum = reduce(lambda x, y: x+y, list(map(lambda x: int(x[0])*x[1], zip(id_number[0:17], weight))))
        mapper = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        check_number = mapper[mul_and_sum % 11]
        if id_number[-1] != check_number:
            raise ValidationError('不是真实的身份证号')