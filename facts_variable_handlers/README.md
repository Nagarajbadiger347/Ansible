# Facts:
        - hosts: all
        tasks:
        - name: print all available facts
            ansible.builtin.debug:
            var: ansible_facts

1. The setup module is run automatically as the first task, therefore it is not specified explicitly
2. With the setup module, ansible facts variables are populated with facts of all target machines


        ansible-playbook -i inventory.yaml facts.yaml

# Variable reference:
variable reference syntax: {{ variable }}
Variable reference demonstrates how variables are used
{ansible_distribution} holds information about the linux distribution of target machine
The reference variable is enclosed in quotes in YAML
The curly braces may be interpreted as objects so quotes are used
ex: 

        - hosts: all
          tasks:
          - name: print the distribution
            ansible.builtin.debug
            msg: "{{ ansible_distribution }}"

       ansible-playbook -i inventory.yaml distribution.yaml

# Referencing variables for fields 

syntax: to ectract a field named "nodename" inside ansible_facts data structure

        {{ ansible_facts['nodename']}}

ex

        - hosts: all
          tasks:
          - name: print the target machine's hostname
          ansible.builtin.debug:
          msg: "{{ ansible_facts['nodename']}}"

        ansible-playbook -i inventory.yaml nodename.yaml
