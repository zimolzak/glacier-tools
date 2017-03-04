Glacier tools
========================

Very ad-hoc things for uploading photos to my AWS Glacier vault, and
for figuring out when the upload is likely to finish up.

Usage examples
--------

* To start the whole enchilada:

`make`

* While it's running:

`python3 estimate.py`

* If you're scared and just want to see what it's finding and planning
to upload:

`make clean; make files.txt; more files.txt`
