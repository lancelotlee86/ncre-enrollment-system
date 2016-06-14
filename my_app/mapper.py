# -*- coding: utf-8 -*-


class DataMapper(object):
    """
    使用时将上面那些 x_mapper 传给DataMapper
    """

    def __init__(self, mapper):
        self.label = mapper['label']
        self.label_zh_CN = mapper['label_zh_CN']
        self.data = mapper['data']

    def is_contains(self, value):
        """
        确认给定的 key 是否存在
        :param value:
        :return: True or False
        """
        for one_data in self.data:
            if value == one_data['value']:
                return True
        return False

    def __repr__(self):
        return '<Data %r>' % self.label


class ExamPlan(object):
    def __init__(self, exam_plan):
        self.exam_plan = exam_plan

    def site(self, site_code):
        """
        根据提供的考点代码，返回这个考点信息的字典
        :param site_code:
        :return: dict
        """
        for site in self.exam_plan['exam_sites']:
            if site['code'] == site_code:
                return site
        return False

id_type_mapper = {
    'label': 'id_type',
    'label_zh_CN': '证件类型',
    'data': [
        {'value': 'undefined', 'name': '请选择'},
        {'value': '1', 'name': '中华人民共和国居民身份证'},
        {'value': '2', 'name': '台湾居民往来大陆通行证'},
        {'value': '3', 'name': '港澳居民来往内地通行证'},
        {'value': '4', 'name': '军人证件'},
        {'value': '5', 'name': '护照'}
    ]
}

id_type_mapper = DataMapper(id_type_mapper)
