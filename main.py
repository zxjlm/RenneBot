# -*-coding:utf-8 -*-

"""
# Company    : astute
# Author     ：zhang.xinjian
# Description：
"""

from settings import Base, sqlite_engine


def init_db():
    from plugins.server_monitor.models import Server

    Base.metadata.create_all(sqlite_engine)
