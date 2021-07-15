#!/usr/bin/env python3
import os
import shutil
import pathlib

def cleanup(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        return 0
    else:
        return 1


def createFile(path, file):
    if not os.path.exists(path):
        file.save(path)
        return 0
    else:
        return 1

def createDir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return 0
    else:
        return 1


def cwd():
    os.getcwd()


def parentPath(path):
    ppath = pathlib.Path(path).parent.absolute()
    return str(ppath)


def getChildFiles(path):
    if os.path.isdir(path):
        files = []
        for f in os.listdir(path):
            if os.path.isfile(path + f):
                files.append(f)
        return files


if __name__ == '__main__':
    print('hello world!\n')
