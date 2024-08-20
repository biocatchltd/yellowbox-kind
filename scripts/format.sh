#!/bin/sh
# run various linters
set -e
python -m ruff format .
python -m ruff check . --select I,F401 --fix --show-fixes
# run lint as a convenience
sh scripts/lint.sh