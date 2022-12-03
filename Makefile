format:
	@poetry run isort .
	@poetry run black .
lint:
	@poetry run prospector --with-tool pydocstyle --doc-warning