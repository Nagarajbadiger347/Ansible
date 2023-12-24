# purpose of playbook 
Ansible can create and resue automation
As automation configuration is stored in file with playbooks, there is configuration management for automation
Playbooks allow running the same automation repeatedly and reliably
It can be stored in version control repository

# parts of playbook
A playbook is a list of one or more plays

        - host: all
          connection: local
          tasks:
            - name: say hello
              debug: msg="hello world"
            - name: print fact
              debug: msg="ansible is running on python {{ansible_python_version}}"
 in this example 
 Hyphen indicates list creation   
 list includes target info, ie where to run the play
 Tasks: 
    Parts of the task
    * name
    * module
    * Arguments

# To run ansible playbook
    ansible-playbook -c local -i localhost, playbook.yaml
