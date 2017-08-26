#!/usr/bin/env python
# coding: utf-8

import argparse
import os

ARCHIVERS = {
             '.arj': 'arj e',
             '.bz2': 'bzip2 -d',
             '.cab': 'cabextract -d',
             '.chm': 'archmage',
             '.deb': 'ar x',
             '.dmg': '7z x',
             '.exe': '7z e',
             '.gz': 'gzip -d',
             '.iso': '7z x',
             '.img.gz': 'gunzip',
             '.lzh': '7z x',
             '.msi': '7z x',
             '.rar': 'unrar x',
             '.rpm': 'rpm2cpio',
             '.tar': 'tar -xvf',
             '.tar.bz2': 'tar -jxvf',
             '.tar.gz': 'tar -zxvf',
             '.tar.xz': 'tar xf',
             '.tbz': 'tar -jxvf',
             '.tbz2': 'tar -jxvf',
             '.tgz': 'tar -xvzf',
             '.udf': '',
             '.wim': '',
             '.xar': 'xar -x',
             '.xz': 'tar xf',
             '.zip': 'unzip',
             '.Z': 'uncompress',
             '.7z': '7za x',
            }


def execute_(command_line):
    os.system(command_line)


def build_command_line(command, f):
    command_line = '{} {}'.format(command, f)
    return command_line


def archives_extractor(f):
    extension = '.{}'.format(f.split('.', 1)[1])
    if extension in list(ARCHIVERS.keys()):
        command = ARCHIVERS[extension]
        if command:
            execute_(build_command_line(command, f))
        else:
            print("error: program not found to extract: {}".format(extension))
    else:
        print("error: extension not found: {}".format(extension))


def main():
    list(map(archives_extractor, args.files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+',
                        help='Type path of the different files to extract',
                        required=True)
    args = parser.parse_args()
    main()
