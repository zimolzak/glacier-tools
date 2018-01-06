## Take two directories and find any MP3 or M4U files that are
## duplicated from one directory to the other. Do this using file
## sizes and then SHA-1 hashes if needed. Therefore, it works even if
## the files have different names but identical bytes.

from subprocess import getoutput
import os

command_b = "find /Users/ajz/Music/iTunes/iTunes\ Media/Music"
#command_b = "find /Users/ajz/Music/iTunes/iTunes\ Media/Music/Weezer"
command_a = "find /Users/ajz/powerbook/Users/ajz/Music/iTunes/iTunes\ Music"

debug = False

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

find_lines_a = getoutput(command_a).splitlines()
[path_list_a, size_list_a] = reference_lists(find_lines_a)

######## Begin processing of B. Depends on these global vars: size_list_a, path_list_a.

find_lines_b = getoutput(command_b).splitlines()
ub = []
size_list_b = []
path_list_b = []
sha_list_a = []
sha_list_b = []
path_matching_a = []

for line in find_lines_b:
    if 'mp3' in line or 'm4a' in line:
        path_b = line
        size_b = os.path.getsize(path_b)
        sha_a = sha_b = ' '*40
        if size_b in size_list_a:
            path_a = path_list_a[size_list_a.index(size_b)]
            path_matching_a.append(path_a)
            sha_a = sha_path(path_a)
            sha_b = sha_path(path_b)
            if sha_a == sha_b:
                ub.append(False)
            else:
                ub.append(True)
        else: # size of file B is unique
            ub.append(True)
            path_matching_a.append(None)
        size_list_b.append(size_b)
        sha_list_a.append(sha_a)
        sha_list_b.append(sha_b)
        path_list_b.append(path_b)

######## print

for i, p in enumerate(path_list_b):
    if sha_list_a[i] == ' '*40: # Element of B is unique in size
        assert ub[i]
        print(p)
    elif sha_list_a[i] != ' '*40 and ub[i]: # same exact size different hash
        print(p)
        print('    #### ' + path_matching_a[i])
    else:
        if debug:
            print([size_list_b[i], sha_list_a[i], sha_list_b[i], ub[i], path2file(p)])
        else:
            pass
