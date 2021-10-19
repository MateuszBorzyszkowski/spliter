# spliter

![](https://img.shields.io/badge/Linux-passing-green)

Script to split large files into smaller files. It has been created with the limitations of some file systems in mind, eg FAT32 (max 4GB). 7zip splits and packs the selected file into smaller archives.

## Instalation guide
#### 1. Download
```
$ git clone https://github.com/boszmate/spliter.git
$ cd spliter
```
#### 2. Installation
```
$ sudo ln -s $PWD/spliter.py /usr/local/bin/spliter
```
#### 3. Install required packages
```
sudo apt install python3 p7zip-full
```


## Description
The script takes a file from the given path. Then creates a directory  at the file location and places the smaller archives there. User can specify the size of the target files.

## Script management
```
$ spliter --help
usage: spliter [-h] [-s SIZE] path

The program to split large files (>4GB).

positional arguments:
  path                  the path to the file which should be splitted

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  the size into which the file should be split [in GB]
```

## Todo
 - feature to split more than one file
