doc-build:
	cd docs/src && hugo --destination ../ && cd ..

doc-get-theme:
	# Clone the Fresh theme
	git clone https://github.com/StefMa/hugo-fresh docs/src/themes/hugo-fresh

doc-clean:
	cd docs && ls -1 | grep -v "src" | xargs rm -r && cd ..

lint:
	poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=pythonlings/exercises,tests/fixtures
