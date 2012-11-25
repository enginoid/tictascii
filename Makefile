test:
	nosetests --with-cover
	pep8 --show-source --show-pep8 .

install:
	$(if pip --version, echo "pip is installed.", easy_install pip)
	pip install -r requirements.txt --use-mirrors
