#!/bin/bash

cat /dev/null > orchestrator.log

declare -x FLASK_APP=orchestrator/orchestrator.py
unbuffer flask run --host=0.0.0.0 |tee orchestrator.log &
disown

