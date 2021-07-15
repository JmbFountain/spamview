#!/usr/bin/env python3
from email.parser import BytesParser, Parser
from email.policy import default
import os
import shutil
import mimetypes
import fsops

def analyze(file):
    """

    :param file: Path to file
    :return:
    """
    working_dir = fsops.parentPath(file)
    filetype = mimetypes.guess_type(file)
    if filetype is not 'message/rfc822':
        return "not a valid eml file"

if __name__ == '__main__':
    print('hello world!\n')
