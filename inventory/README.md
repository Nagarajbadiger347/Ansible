# Secure shell (ssh)
Creates encrypted connection to remote machine
Used to copy files and run command on remote machine

setting up target machine

        ssh-keyscan - H <ip of target machine 1> >> .shh/known_hosts
        ssh-keyscan - H <ip of target machine 2> >> .shh/known_hosts


generate private key 

        ssh-keygen -t rsa
        ssh-copy-id <target machine 1 id>
        ssh-copy-id <target machine 2 id>


# inventory file

Its either in INI or YAML format

        ansible-playbook -i <file name> playbook.yaml







  
        