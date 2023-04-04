# https://blog.csdn.net/jyr2014/article/details/126712167
# 解决django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
# Did you install mysqlclient?
import pymysql

pymysql.install_as_MySQLdb()
