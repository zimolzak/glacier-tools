files.txt :
	find . -iname '*.jpg' > files.txt
	find . -iname '*.mov' >> files.txt
	find . -iname '*.png' >> files.txt
	find . -iname '*.gif' >> files.txt
	find . -iname '*.avi' >> files.txt
	find . -iname '*.tif*' >> files.txt
	perl -pi -e 's{^\./}{}' files.txt
	@echo Hint: inspect files.txt
	@echo Hint: make test.... python3 estimate.py

test : files.txt
	head -n 10 files.txt > test.txt
	./glacier.pl test.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt
	@echo Hint: inspect log.txt
	@echo Hint: make rest.... python3 estimate.py

rest : files.txt
	tail -n +11 files.txt > rest.txt
	./glacier.pl rest.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt
	@echo SUCCESS!!
	@echo Hint: make move unless doing dedup workflow

move :
# would fail if run at stroke of midnight
	mkdir -pv /Users/ajz/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`
	mv -nv files.txt log-* ~/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`
	@echo Please remember to MOVE YOUR MEDIA out of this GlacierActive folder!
	@echo Such as mv out-of-dropbox-2019-09to12/ ../2-for-ext-hdd-glacier/
	@echo Hint: make clean if you want to be nice to future users.

#### Atypical workflows below this line.

sourceme.txt :
	python dedup_one_dir_using_names.py > sourceme.txt
	@echo Hint: Inspect sourceme.txt
	@echo Hint: mkdir ~/Desktop/GlacierActive/xxxx-photoslibrary
	@echo Hint: make move-initial

move-initial :
	sh sourceme.txt
	@echo Hint: make clean
	@echo Hint: make files.txt

clean :
	rm -f files.txt test.txt rest.txt *~ log.txt

movephotos : move
	mv -nv sourceme.txt ~/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`

upload : files.txt
	./glacier.pl files.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt
