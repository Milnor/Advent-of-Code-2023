SHELL=/bin/bash
VENV_DIR=venv

.PHONY: deps
deps:
	sudo apt install python3-pip python3.10-venv

.PHONY: create-venv
create-venv:
	python3 -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate; python3 -m pip install --upgrade pip; python3 -m pip install -r requirements.txt; deactivate

.PHONY: venv-on
venv-on:
	. $(VENV_DIR)/bin/activate

.PHONY: venv-off
venv-off:
	deactivate

.PHONY: test-run 
test-run:
	robot tests/aoc23.robot


.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
