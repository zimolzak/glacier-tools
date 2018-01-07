## Take one directory and find any files that are duplicated inside
## the tree. Do this using filenames, sizes, and then SHA-1 hashes if
## needed. Therefore, it ASSUMES files with different names contain
## different bytes. (This is to help performance, because my files are
## all called IMG_7732.JPG etc. and highly unlikely to have same bytes
## w/ different names.)

## Assumes a directory called "2014-photoslibrary" or similar exists.

from subprocess import getoutput
import os
from dedup_lib import escape, File

# Any DIR variable must end in slash.
ROOT_DIR = escape("/Users/ajz/Pictures/Photos Library.photoslibrary/Masters/")
YEAR = '2014'
COMMAND_BASE = "find {}{} -type f"
DESTINATION_DIR = '/Users/ajz/Desktop/GlacierActive/'
MOVE_BASIC = 'mv {} {}{}-photoslibrary' # three format args
MOVE_RENAME = 'mv {} {}{}-photoslibrary/{}' # four format args

COMMAND = COMMAND_BASE.format(ROOT_DIR, YEAR)
FILES = [File(p) for p in getoutput(COMMAND).splitlines()]
print(len(FILES), 'files found....')

FILENAME_LIST = [f.filename for f in FILES]
FILES_WITH_DUP_NAMES = []
for f in FILES:
    if FILENAME_LIST.count(f.filename) > 1:
        FILES_WITH_DUP_NAMES.append(f)

DUP_SET = set([f.filename for f in FILES_WITH_DUP_NAMES])
N_FILES = len(FILES_WITH_DUP_NAMES)
N_NAMES = len(DUP_SET)
print(N_FILES, 'files with duplicate names....')
print(N_NAMES, 'filenames shared among them....')
print(N_FILES / N_NAMES, 'ratio....')

COUNT_MOVES = {}
for fn in DUP_SET:
    COUNT_MOVES[fn] = 0

for myfile in FILES:
    if myfile.filename not in DUP_SET:
        print(MOVE_BASIC.format(escape(myfile.pathname),
                                DESTINATION_DIR,
                                YEAR))
        continue
    else:
        # list all files that share my name
        files_that_share = []
        for fo in FILES_WITH_DUP_NAMES:
            if fo.filename == myfile.filename:
                files_that_share.append(fo)
        # get sizes of all files in that list
        sizes = [f.size() for f in files_that_share]
        myfile_size_appearances = sizes.count(myfile.size())
        assert myfile_size_appearances > 0
        if myfile_size_appearances == 1:
            fn = myfile.filename
            COUNT_MOVES[fn] += 1
            n = COUNT_MOVES[fn]
            ext = fn[fn.index('.'):]
            newname = fn.replace(ext, '_' + str(n) + ext)
            print(MOVE_RENAME.format(escape(myfile.pathname),
                                     DESTINATION_DIR,
                                     YEAR,
                                     newname))
        else:
            assert myfile_size_appearances > 1
            print("  ** MY FILE'S SIZE EQUALS ANOTHER!", myfile.filename)
            ## FIXME - insert SHA-1 business here!
