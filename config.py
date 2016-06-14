# -*- coding: utf-8 -*-


DEBUG = False

MONGODB_HOST = ''
MONGODB_PORT = 27017
MONGODB_DATABASE = 'ncre'   # flask-MongoKit使用

EXAM_PLAN = {
    'exam_sites':
    [
        {
            'code': '0',
            'label': '请选择'
        },
        {
            'code': '410084',
            'label': '华北水利水电大学（郑东新区）',
            'max_cap': 1000,
            'subjects':
            {
                '111': {'label': '二级 —— MS office', 'max_cap': 100},
                '24': {'label': '二级 —— C语言程序设计'},
                '26': {'label': '二级 —— VB语言程序设计'},
                '27': {'label': '二级 —— VFP据库程序设计'},
                '29': {'label': '二级 —— Access数据库程序设计'},
                '35': {'label': '三级 —— 网络技术'},
                '36': {'label': '三级 —— 数据库技术'},
                '41': {'label': '四级 —— 网络工程师'},
                '42': {'label': '四级 —— 数据库工程师'}
            }
        },
        {
            'code': '410067',
            'label': '华北水利水电大学（北环路36号）',
            'max_cap': 1000,
            'subjects': {
                '24': {'label': '二级 —— C语言程序设计'},
                '26': {'label': '二级 —— VB语言程序设计'},
                '27': {'label': '二级 —— VFP据库程序设计'},
                '29': {'label': '二级 —— Access数据库程序设计'},
                '35': {'label': '三级 —— 网络技术'},
                '36': {'label': '三级 —— 数据库技术'},
                '41': {'label': '四级 —— 网络工程师'},
                '42': {'label': '四级 —— 数据库工程师'}
            }
        }
    ]
}
