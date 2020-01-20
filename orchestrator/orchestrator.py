#!/usr/bin/python3
from flask import Flask, Response, request, jsonify
from json import loads, dumps
from functools import reduce
import traceback

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# Playbooks available
playbooks = [
    '1-create_adom.yml',
    '2-add_fgt.yml',
    '3-modify_interface_access.yml',
    '4-create_policy_package.yml',
    '5-create_fw_policies.yml',
    '6-install_policy_package.yml']


@app.route("/playbook", methods=['GET'])
def playbook():

    response = Response()
    response.headers.add('Access-Control-Allow-Origin', '*')

    try:
        fgt_id = request.args.get('number')
        fgt_id = int(fgt_id)

        response.data = _start_vm(fgt_id, auto_throughput=False)
        return response
    except:
        response.data = traceback.format_exc()
        return response


@app.route("/execute_playbook", methods=['POST'])
def execute_playbook():

    response = Response()
    response.headers.add('Access-Control-Allow-Origin', '*')

    try:
        fgt_id = request.args.get('number')
        fgt_id = int(fgt_id)

        response.data = _start_vm(fgt_id, auto_throughput=False)
        return response
    except:
        response.data = traceback.format_exc()
        return response
