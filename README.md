# ncre-enrollment-system
with Python/Flask, MongoDB

这个项目是从我的另一个项目 [hs_ncre]() 迁移过来的，那个版本的项目用的是node.js和MariaDB，我想用Python和MongoDB重构一遍并加入新的功能
现在正处于第一阶段，将功能复刻一遍。

我想用mongokit做ORM，但是mongokit发布的最新正式版是0.9. 不支持python3
所以要用development分支的，也就是1.0.0，下载包自己安装

可是mongokit对于pymongo的新版本3.x支持不好，所以要将pymongo换成2.9.3版本


MongodbKit Docs: http://mongokit.readthedocs.io/