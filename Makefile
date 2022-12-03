format:
	@poetry run isort .
	@poetry run blue .
lint:
	@poetry run prospector --with-tool pydocstyle --doc-warning