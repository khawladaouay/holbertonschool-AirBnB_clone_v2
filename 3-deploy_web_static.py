#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static"""

from datetime import datetime
from fabric.api import local, run, put, env
from os.path import isdir, exists, getsize
env.hosts = ['54.91.126.79', '18.208.141.223']


def do_pack():
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


def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path)"""
    if exists(archive_path):

        file_name = archive_path.split("/")[-1]
        remove = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.foremoveat(path, remove))

        run('tar -xzf /tmp/{} -C {}{}/'.foremoveat(file_name, path, remove))

        run('rm /tmp/{}'.format(file_name))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, remove))

        run('rm -rf {}{}/web_static'.format(path, remove))

        run('rm -rf /data/web_static/current')

        run('ln -s {}{}/ /data/web_static/current'.format(path, remove))

        print("New version deployed!")

        return True

    return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
