test:
	nosetests --with-cover
	pep8 --show-source --show-pep8 .

install:
	pip install -r requirements.txt --use-mirrors
