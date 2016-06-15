.PHONY: all
all: install

.PHONY: install
install: clean
	sudo python setup.py install

.PHONY: uninstall
uninstall: clean
	sudo rm -rf /usr/lib/python3.5/site-packages/pymple*
	sudo rm -rf /usr/bin/pymple

.PHONY: clean
clean:
	sudo rm -rf dist
	sudo rm -rf MANIFEST
	sudo rm -rf build
	sudo rm -rf pymple.egg-info

.PHONY: pypi
pypi: clean
	python setup.py sdist upload

.PHONY: update
update: uninstall install

.PHONY: lint
lint:
	pycodestyle pymple

.PHONY: test
test: lint typecheck
	python3 -m unittest

.PHONY: typecheck
typecheck:
	python3 -m mypy $(CURDIR)/pymple --disallow-untyped-defs --disallow-untyped-calls
