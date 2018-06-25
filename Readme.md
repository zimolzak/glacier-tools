Glacier tools
========================

Ad-hoc scripts for uploading photos to my Amazon Web Services Glacier
vault, and for figuring out when the upload is likely to finish up.

Optionally: move highly-nested files from Photos Library to the
"GlacierActive" directory.

Finds likely image/movie files in the directory where it's run and
generates a list of filenames. Then runs the command line `aws
glacier` on each filename, logging details like the key:value data
returned from Glacier.

My usual usage
--------

    #### Start here if moving files to working dir & deduplicating.
    #### edit dedup_one_dir_using_names.py to point to right dir(s) as approp.
    make sourceme.txt
    mkdir ~/Desktop/GlacierActive/xxxx-photoslibrary
    make move-initial # 60 sec / 13000.

    #### Start here if files are already in the working directory.
    make clean
    make files.txt
    make test
    make rest # concurrent w/ the next line
    python3 estimate.py # in separate terminal
    #### WAIT ####
    make movephotos # or make move
    mv [any folders] ../Glacier\ fully\ done/
    #### Consider writing a description of a random sample of the pics

Fire-and-forget usage
--------

If you trust it without inspecting the list of filenames or doing a
test upload:

`make clean`

`make upload`

Tips/warnings
--------

* The names of subdirectories get transmitted to Glacier in the
  archive description, so consider making directory names somewhat
  descriptive.

* If you Control-C it (or it dies) in the middle of an upload,
  remember to save your `log.txt` file. It will get clobbered the next
  time you make `upload` or `test` or `rest`. Also you'd have to
  figure out where the upload left off and edit `files.txt` or
  `rest.txt` or whatever, because we don't remove lines one by one
  from the list of filenames.

Benchmarks
========

Oldest
--------

Real-life example: start at 14:46, end at 17:37. Took 10,323 sec, or 2
hr, 50 min. Size 2.86 GB, for **276 kB/sec,** or **0.995 GB/hr** (from
my home cable connection from RCN Telecom). About 1350 files, mostly
1-2 MB .jpg files, and a few 10-50 MB .mov files.

Prior
--------

Here "kilo" and "mega" mean 1E3 and 1E9, not "kibi" etc. But I'm not
sure if input should be GB or GiB.

    5.9 GB / (2.5 hours)
    2.36 GB/h (gigabytes per hour)
    660 kB/s (kilobytes per second)
    5.2 Mb/s (megabits per second)

    24 GB / (10.2 hours)
    2.353 GB/h (gigabytes per hour)
    653.6 kB/s (kilobytes per second)

    25 minutes per GB

most recent (2018-01-04)
--------

    start 14:25
    end 16:19
    114 minutes
    5.3 GiB (5587016 KiB)
    836.4 kB/s (kilobytes per second)

    20 minutes per GB
