upload : files.txt
	./glacier.pl files.txt | tee log.txt

files.txt : 
	find . -name '*.jpg' > files.txt
	perl -pi -e 's{^\./}{}' files.txt

clean :
	rm files.txt
