upload : files.txt
	./glacier.pl files.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt

test : files.txt
	head -n 10 files.txt > test.txt
	./glacier.pl test.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt

rest : files.txt
	tail -n +11 files.txt > rest.txt
	./glacier.pl rest.txt | tee log.txt
	cp log.txt log-`date "+%Y-%m-%d-%H%M"`.txt

move :
# would fail if run at stroke of midnight
	mkdir -pv /Users/ajz/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`
	mv -nv files.txt log-* ~/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`
	echo Please remember to MOVE YOUR MEDIA out of this GlacierActive folder!

movephotos : move
	mv -nv sourceme.txt ~/Dropbox/SYSADMIN/glacier/`date "+%Y-%m-%d"`

files.txt : 
	find . -iname '*.jpg' > files.txt
	find . -iname '*.mov' >> files.txt
	find . -iname '*.png' >> files.txt
	find . -iname '*.gif' >> files.txt
	find . -iname '*.avi' >> files.txt
	perl -pi -e 's{^\./}{}' files.txt

clean :
	rm -f files.txt test.txt rest.txt *~ log.txt
