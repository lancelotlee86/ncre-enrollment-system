# -*- coding: utf-8 -*-

from mongokit import Document, ValidationError
from my_app import db


class EnrollmentData(Document):
    __collection__ = 'enrollment_data'
    __database__ = 'ncre'
    raise_validation_errors = False

    structure = {
        'name': str,
        'id_type': str,
        'id_number': str,
        'exam_site_code': str,
        'subject_code': str,
    }
    use_dot_notation = True
    required_fields = ['name', 'id_number', 'id_type', 'exam_site_code', 'subject_code']

    @staticmethod
    def count():
        res = db[EnrollmentData.__collection__].find()
        return res.count()

    def exist(self):
        """
        判断 对象 代表的记录是否已经在数据库中了
        依据是 id_number 和 id_type 的组合
        :return: bool
        """
        if db[self.__collection__].find({'id_number': self.id_number, 'id_type': self.id_type}).count():
            return True
        return False

    def __repr__(self):
        return '<User %r>' % self.name


db.register(EnrollmentData)
