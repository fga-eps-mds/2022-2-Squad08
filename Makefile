default: black test lint

test:
	@pytest .

black:
	@black .

lint:
	@find . -type f -name "*.py" -exec pylint --disable=C0103,C0114,C0301,E0402,W0703,R0903 -j 0 --exit-zero {} \;