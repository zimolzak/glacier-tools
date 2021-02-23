import os
import random
import subprocess

MYPATH = './out-of-dropbox-2020-08to12-'
FILES = os.listdir(MYPATH)
INP = ''
while INP != 'q':
    INP = input('q to quit, enter anything else to continue')
    file_choice = random.choice(FILES)
    pathname_choice = MYPATH + '/' + file_choice
    subprocess.run(["open", pathname_choice])
