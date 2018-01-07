## Take one directory and find any files that are duplicated inside
## the tree. Do this using filenames, sizes, and then SHA-1 hashes if
## needed. Therefore, it ASSUMES files with different names contain
## different bytes. (This is to help performance, because my files are
## all called IMG_7732.JPG etc. and highly unlikely to have same bytes
## w/ different names.)

from subprocess import getoutput
import os
from dedup_lib import escape, File

ROOT_DIR = escape("/Users/ajz/Pictures/Photos Library.photoslibrary/Masters/")
YEAR = '2014'
COMMAND_BASE = "find {}{} -type f"
COMMAND = COMMAND_BASE.format(ROOT_DIR, YEAR)
FILES = [File(p) for p in getoutput(COMMAND).splitlines()]
print(len(FILES), 'files found....')

FILENAME_LIST = [f.filename for f in FILES]
FILES_DUP_NAMES = []
for f in FILES:
    if FILENAME_LIST.count(f.filename) > 1:
        FILES_DUP_NAMES.append(f)

N_FILES = len(FILES_DUP_NAMES)
N_NAMES = len(set([f.filename for f in FILES_DUP_NAMES]))
print(N_FILES, 'files with duplicate names....')
print(N_NAMES, 'filenames shared among them....')
print(N_FILES / N_NAMES, 'ratio....')

## next we need to pair them up somehow

for f in FILES_DUP_NAMES:
    continue ## DELETE ME
    # use that to generate list of filenames. "path2file()"
    # sublist of those filenames that have dups
    size = os.path.getsize(f.pathname)
    sha = ' '*40
    if size in size_list:
    # for each f in sublist, does its size match sibs?
    # if yes, then for each f in sublist, does its hash match sibs?
        path_a = PATH_LIST_A[SIZE_LIST_A.index(size_b)]
        PATH_MATCHING_A.append(path_a)
        sha_a = sha_path(path_a)
        sha_b = sha_path(f)
        if sha_a == sha_b:
        # if yes, then mark it as a dup. CONTINUE.
            UNIQ_B.append(False)
        else:
        # if no, then it needs to be renamed. CONTINUE.
            UNIQ_B.append(True)
    else: # size of file B is unique
    # if no, then it needs to be renamed. CONTINUE.
        UNIQ_B.append(True)
        PATH_MATCHING_A.append(None)
