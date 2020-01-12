default: static-files

static-files:
	python3 -c "from generate_static_files import GenerateStaticFiles; GenerateStaticFiles().main()" generate_static_files.py
