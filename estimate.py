from subprocess import check_output
from time import time, sleep, ctime

outpt = check_output(["wc", "files.txt"])
s = str(outpt)
num_files_total = float(s.split()[1])

def file_count():
    upload_count = 0
    for L in open('log.txt').readlines():
        if "FILE:" in L:
            upload_count = upload_count + 1
    return upload_count

## loop here

t = [time(), time()]
n = [0, 0]
t_first = t[0]
n_first = file_count()

while(1):

    t[0] = t[1]
    t[1] = time()

    upload_count = file_count()

    n[0] = n[1]
    n[1] = upload_count

    rate = (n[1] - n[0]) / (t[1] - t[0])
    try:
        est_sec = (num_files_total - upload_count) / rate
    except ZeroDivisionError:
        est_sec = 360000.0 # 100 hr
    eta = t[1] + est_sec

    rate_first = (n[1] - n_first) / (t[1] - t_first)
    try:
        est_sec_first = (num_files_total - upload_count) / rate_first
    except ZeroDivisionError:
        est_sec_first = 360000.0 # 100 hr
    eta_first = t[1] + est_sec_first

    print(upload_count, '\t files uploaded (per log.txt) out of')
    print(num_files_total, '\t files total (per files.txt)')
    print(round(upload_count / num_files_total, 3), '\t proportion complete')
    print(num_files_total - upload_count, '\t files remaining')
    print('---')
    print(round(t[1] - t[0], 1), '\t sec elapsed (interval)')
    print(n[1] - n[0], '\t uploaded in interval')
    print(round(rate, 2), '\t rate per sec')
    print(round(est_sec, 1), '\t est sec remain')
    print(ctime(eta), '\t est time completion')
    print('---')
    print(round(t[1] - t_first, 1), '\t sec elapsed since script run')
    print(n[1] - n_first, '\t uploaded since script run')
    print(round(rate_first, 2), '\t rate per sec')
    print(round(est_sec_first, 1), '\t est sec remain')
    print(ctime(eta_first), '\t est time completion')
    print()

    sleep(30)
