build:
	python setup.py bdist_wheel sdist

deploy:
	twine upload dist/* --verbose

clean:
	rm -rf build dist autoact.egg-info

