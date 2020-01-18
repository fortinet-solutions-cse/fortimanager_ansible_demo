# FortiManager Ansible demo

The purpose of this project is to show a basic set of operations that can be done with Ansible modules for FortiManager.
The modules uses httpapi plugin and hosts inventory

To run the playbooks do:

Open a shell and change directory to the root of this repository

```pip3 install ansible==2.9.1```

```ansible-playbook -i hosts 1-create_adom.yml``` 

Repeat for the rest of playbooks (.yml)


----

Note: At time to writing, the httpapi plugin released by Ansible needs to receive an update which is still pending and will be completed shortly. To solve this temporarily please replace your local copy of fortimanager.py for the httpplugin with the one included in this repo:

```cp plugins/fortimanager.py ~/.local/lib/python3.7/site-packages/ansible/plugins/httpapi/fortimanager.py```
