Ansible is written in python we need python in all the all machine
# Steps to install ansible (only in control machine)
    sudo apt install -y python3-pip
    sudo pip install ansible
    ansible --version

# Ansible ad-hoc command
    ansible all -c local -i inventory, -m ping
    

