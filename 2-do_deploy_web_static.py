#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.91.126.79', '18.208.141.223']


def do_deploy(archive_path):
    """deploy func"""
    if exists(archive_path):
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current".format(path, no_ext))
        run(" rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    return False
