#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static"""

from datetime import datetime
from fabric.api import local
from os.path import isdir, exists, getsize


def do_pack():
    """test"""
    date = datetime.now().strftime("%y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir versions")
    name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(name))
    size = getsize(name)
    print("web_static packed: {} -> {}Bytes".format(name, size))
    if exists(name):
        return name
    return None
