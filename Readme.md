Glacier tools
========================

Ad-hoc scripts for uploading photos to my Amazon Web Services Glacier
vault, and for figuring out when the upload is likely to finish up.

Finds likely image/movie files in the directory where it's run and
generates a list of filenames. Then runs the command line `aws
glacier` on each filename, logging details including key:value data
returned from Glacier.

Usage examples
--------

* My usual workflow:

`make clean`
`make files.txt`
`#### pause and inspect files.txt ####`

`make test`
`#### pause and inspect log.txt   ####`

`make rest # concurrent w/ the next line`
`python3 estimate.py # in separate terminal`

* To instead run the whole enchilada (if you trust it without
  inspecting the list of filenames or doing a test upload):

`make clean`
`make`

Tips/warnings
--------

* The names of subdirectories get transmitted to Glacier in the
  archive description, so consider making directory names somewhat
  descriptive.

* If you Control-C it in the middle of an upload, remember to save
  your `log.txt` file. It will get clobbered the next time you run an
  upload (using makefile). Also you'd have to figure out where the
  upload left off and edit `files.txt` or `rest.txt` or whatever,
  because we don't remove lines one by one from the list of filenames.

* Real-life example: start at 14:46, end at 17:37. Took 10,323 sec, or
  2 hr, 50 min. Size 2.86 GB, for **276 kB/sec,** or **0.995 GB/hr**
  (from my home cable connection from RCN Telecom). About 1350 files,
  mostly 1-2 MB .jpg files, and a few 10-50 MB .mov files.
