upload : files.txt
	./glacier.pl files.txt | tee log-`date "+%Y-%m-%d-%H%M"`.txt

test : files.txt
	head -n 10 files.txt > test.txt
	./glacier.pl test.txt | tee log-`date "+%Y-%m-%d-%H%M"`.txt

rest : files.txt
	tail -n +11 files.txt > rest.txt
	./glacier.pl rest.txt | tee log-`date "+%Y-%m-%d-%H%M"`.txt

files.txt : 
	find . -iname '*.jpg' > files.txt
	find . -iname '*.mov' >> files.txt
	find . -iname '*.png' >> files.txt
	find . -iname '*.gif' >> files.txt
	perl -pi -e 's{^\./}{}' files.txt

clean :
	rm files.txt
