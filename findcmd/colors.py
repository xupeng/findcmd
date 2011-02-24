#coding=utf8

"""
colors.py

Created by Xupeng Yun <xupeng@xupeng.me> on 2010-05-30.
Copyright (c) 2010 xupeng.me. All rights reserved.
"""


def _color(code):
    def inner(text, bold=False):
        _code = code
        if bold:
            _code = "1;%s" % code
        return "\033[%sm%s\033[0m" % (_code, text)
    return inner

red = _color(31)
green = _color(32)
yellow = _color(33)
blue = _color(34)
magenta = _color(35)
cyan = _color(36)
white = _color(37)
