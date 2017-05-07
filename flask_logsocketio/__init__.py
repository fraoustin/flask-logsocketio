#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module flask_logsocketio
"""

__version_info__ = (0, 1, 0)
__version__ = '.'.join([str(val) for val in __version_info__])

__namepkg__ = "flask-logsocketio"
__desc__ = "Flask LogSocketIo module"
__urlpkg__ = "https://github.com/fraoustin/flask-logsocketio.git"
__entry_points__ = {}

from flask_logsocketio.main import LogSocketIo
