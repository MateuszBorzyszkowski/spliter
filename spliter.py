#!/usr/bin/python

#import libraries
import argparse
import logging
import os
import subprocess

#const
FOUR_GB = 4294967296.0

#check if 7z is installed
def check_zip():
    process = subprocess.Popen('7z', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if not process.returncode == 0:
        return True
    else:
        logging.error('Do not find 7z!')

#run command
def init(command):
    if check_zip():
        subprocess.call(command, shell=True)

#create dst dir
def create_dst_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
        logging.info('The new directory has been created at the file location.')
    else:
        logging.warning('The directory already exists! The files will be saved in this dir!')

#prepare command to split
def prepare_command(dir, tmpdir, filename, size):
    zipfile = os.path.splitext(filename)
    command = "7z -v" + str(int(size)) + "b a " + dir + zipfile[0] + ".7z " + tmpdir + filename
    return command

#return size in bytes
def prepare_file_size(size, path):
    if not size:
        filesize = os.stat(path)
        size = filesize.st_size
        while size > FOUR_GB:
            size = size / 2
        logging.warning('The file size not specified! The size will be set automatically: %0.2f GB', size/1073741824)
    else:
        size = size * 1073741824
    return size

#prepare dest dir
def prepare_dir(path, filename):
    dstdir = os.path.dirname(path) + '/'
    tmpdir = dstdir
    subdir = os.path.splitext(filename)[0] + '/'
    dstdir += str(subdir)
    return dstdir, tmpdir

#check if file exists
def file_exists(path):
    if not os.path.isfile(path):
        logging.error('The fiile not exists!')
        return False
    return True

def main():
    desc = 'The program to split large files (>4GB).'

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(prog='spliter', description=desc)
    parser.add_argument('path', help='the path to the file which should be splitted')
    parser.add_argument('-s', '--size', type=int, help='the size into which the file should be split [in GB]')

    #Read args from cmd
    args = parser.parse_args()

    if args.path and file_exists(args.path):
        filename = os.path.basename(args.path)
        dir, tmpdir = prepare_dir(args.path, filename)
        size = prepare_file_size(args.size, args.path)

        create_dst_dir(dir)
        command = prepare_command(dir, tmpdir, filename, size)
        init(command)

if __name__ == "__main__":
    main()
