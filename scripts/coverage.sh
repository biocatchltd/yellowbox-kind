#!/bin/sh
set -e
#coverage run --branch --context=ut --include="yellowbox_kind/*" -m pytest tests/unittest "$@"
coverage run -a --branch --context=app --include="yellowbox_kind/*" -m pytest tests/blackbox "$@"
coverage html
coverage report -m
coverage xml