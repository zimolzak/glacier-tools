from subprocess import check_output
from time import time, sleep, ctime

outpt = check_output(["wc", "files.txt"])
s = str(outpt)
num_files_total = float(s.split()[1])

## loop here

t = [time(), time()]
n = [0, 0]

while(1):

    t[0] = t[1]
    t[1] = time()

    upload_count = 0
    for L in open('log.txt').readlines():
        if "FILE:" in L:
            upload_count = upload_count + 1

    n[0] = n[1]
    n[1] = upload_count

    rate = (n[1] - n[0]) / (t[1] - t[0])
    est_sec = (num_files_total - upload_count) / rate
    eta = t[1] + est_sec

    print(upload_count, '\t uploaded out of')
    print(num_files_total, '\t total')
    print(round(upload_count / num_files_total, 3), '\t proportion complete')
    print(round(t[1] - t[0], 1), '\t sec elapsed')
    print(n[1] - n[0], '\t uploaded in interval')
    print(round(rate, 2), '\t rate per sec')
    print(num_files_total - upload_count, '\t remaining')
    print(round(est_sec, 1), '\t est sec remain')
    print(ctime(eta), '\t est time completion')
    print()

    sleep(30)
