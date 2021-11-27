"""
@author: harumonia
@license: © Copyright 2021, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@homepage: https://harumonia.moe/
@file: manage.py
@time: 2021/11/27 6:32 下午
@desc:
"""
from settings import Base, sqlite_engine


def init_db():
    from plugins.server_monitor.models import Server

    Base.metadata.create_all(sqlite_engine)
