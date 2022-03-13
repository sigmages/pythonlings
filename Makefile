doc-build:
	cd docs/src && hugo --destination ../ && cd ..

doc-get-theme:
	# Clone the Fresh theme
	git clone https://github.com/StefMa/hugo-fresh docs/src/themes/hugo-fresh

doc-clean:
	cd docs && ls -1 | grep -v "src" | xargs rm -r && cd ..
