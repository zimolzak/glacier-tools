## Finds JPGs and PNGs in the many subdirectories of Photos Library
## and generates (1) "dups.txt", which notes any duplicate filenames,
## and (2) "sourceme.txt", which contains shell commands to move them
## to GlacierActive. You should run this from ~/Desktop I suppose, for
## now.

## 1. edit year
## 2. make hard
## 3. make easy
## 4. make clean

year = 2014
photoslibrary = /Users/ajz/Pictures/Photos Library.photoslibrary/Masters/

easy :
	perl -pe 's{.*/(.*)}{$$1}' stage1.txt > stage2.txt # prepare to find dups
	sort stage2.txt | uniq -c | sort -nr > dups.txt     # find dups
	perl -ne 'chomp; s{ }{\\ }g; print "mv $$_  ~/Desktop/GlacierActive/$(year)-photoslibrary\n" ' stage1.txt > sourceme.txt

all : hard easy

hard :
	find '$(photoslibrary)$(year)' -iname '*.jpg' > ~/Desktop/stage1.txt
	find '$(photoslibrary)$(year)' -iname '*.png' >> ~/Desktop/stage1.txt

clean :
	rm -f stage2.txt
