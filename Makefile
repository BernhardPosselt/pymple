all: install

install: clean
	sudo python setup.py install

uninstall: clean
	sudo rm -rf /usr/lib/python3.4/site-packages/pymple*
	sudo rm -rf /usr/bin/pymple

clean:
	sudo rm -rf dist
	sudo rm -rf MANIFEST
	sudo rm -rf build
	sudo rm -rf pymple.egg-info

pypi: clean
	python setup.py sdist upload

update: uninstall install