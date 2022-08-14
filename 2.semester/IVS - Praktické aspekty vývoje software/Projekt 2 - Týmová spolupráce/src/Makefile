ENTRY_FILE=gui_calculator.py
PROFILING_ENTRY_FILE=profiling.py

all:
	@echo "Python project - no need to compile"

pack:
	@cd ../ && git archive --prefix xbella01_xjorio00_xmikes11_xzimme03/ \
				-o xbella01_xjorio00_xmikes11_xzimme03.zip $(shell git stash create)

clean:
	rm -rf ../dist
	rm -rf ../build
	rm -rf __pycache__

generate-executable:
	pyinstaller --add-data "calc.png:files" -i src/calc.png --onefile --windowed $(ENTRY_FILE) \
				--distpath ../dist --workpath ../build

test:
	python -m pytest test_*.py

doc:
	doxygen Doxyfile

run:
	python $(ENTRY_FILE)

profile:
	python $(PROFILING_ENTRY_FILE)
