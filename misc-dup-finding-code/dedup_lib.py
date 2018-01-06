import os
from subprocess import getoutput

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
