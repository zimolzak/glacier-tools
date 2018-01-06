## Take two directories and find any MP3 or M4U files that are
## duplicated from one directory to the other. Do this using file
## sizes and then SHA-1 hashes if needed. Therefore, it works even if
## the files have different names but identical bytes.

from subprocess import getoutput
import os

COMMAND_B = "find /Users/ajz/Music/iTunes/iTunes\ Media/Music"
#COMMAND_B = "find /Users/ajz/Music/iTunes/iTunes\ Media/Music/Weezer"
COMMAND_A = "find /Users/ajz/powerbook/Users/ajz/Music/iTunes/iTunes\ Music"

DEBUG = False

########

def last_index(S, char):
    """Return the HIGHEST index in S where character char is found. Kind
    of like str.find(sub) but starts from the end of the string,
    instead of the beginning.
    """
    indices = list(range(len(S)))
    indices.reverse() # Like [4, 3, 2, 1, 0]
    for i in indices:
        if S[i] == char:
            return i
    return -1

def sha_path(pathname):
    escaped = pathname.replace(' ', '\ ').replace("'", "\\'").replace("(", "\(").replace(")", "\)").replace(",", "\,").replace("&", "\&")
    return getoutput("shasum " + escaped).split()[0]

def path2file(path):
    return path[last_index(path, '/') + 1 : ]

def reference_lists(find_lines):
    """Return list of pathnames containing mp3 or m4a, and the sizes of
    each file (in the same order.
    """
    pathnames = []
    sizes = []
    for line in find_lines:
        if 'mp3' in line or 'm4a' in line:
            pathnames.append(line)
            s = os.path.getsize(line)
            sizes.append(s)
    return [pathnames, sizes]

########

FIND_LINES_A = getoutput(COMMAND_A).splitlines()
[PATH_LIST_A, SIZE_LIST_A] = reference_lists(FIND_LINES_A)

######## Begin processing of B. Depends on these global vars: SIZE_LIST_A, PATH_LIST_A.

FIND_LINES_B = getoutput(COMMAND_B).splitlines()
UNIQ_B = []
SIZE_LIST_B = []
PATH_LIST_B = []
SHA_LIST_A = []
SHA_LIST_B = []
PATH_MATCHING_A = []

for line in FIND_LINES_B:
    if 'mp3' in line or 'm4a' in line:
        path_b = line
        size_b = os.path.getsize(path_b)
        sha_a = sha_b = ' '*40
        if size_b in SIZE_LIST_A:
            path_a = PATH_LIST_A[SIZE_LIST_A.index(size_b)]
            PATH_MATCHING_A.append(path_a)
            sha_a = sha_path(path_a)
            sha_b = sha_path(path_b)
            if sha_a == sha_b:
                UNIQ_B.append(False)
            else:
                UNIQ_B.append(True)
        else: # size of file B is unique
            UNIQ_B.append(True)
            PATH_MATCHING_A.append(None)
        SIZE_LIST_B.append(size_b)
        SHA_LIST_A.append(sha_a)
        SHA_LIST_B.append(sha_b)
        PATH_LIST_B.append(path_b)

######## print

for i, p in enumerate(PATH_LIST_B):
    if SHA_LIST_A[i] == ' '*40: # Element of B is unique in size
        assert UNIQ_B[i]
        print(p)
    elif SHA_LIST_A[i] != ' '*40 and UNIQ_B[i]: # same exact size different hash
        print(p)
        print('    #### ' + PATH_MATCHING_A[i])
    else:
        if DEBUG:
            print([SIZE_LIST_B[i], SHA_LIST_A[i], SHA_LIST_B[i], UNIQ_B[i], path2file(p)])
        else:
            pass
