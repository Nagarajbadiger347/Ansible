# host variables inventory

    host01 ansible_host=<IP addess> node_version=16
    host02 ansible_host=<ip address> postgresql_version=14
any custom variable can be added to hosts by key-value pair

or 

       [webservers]
       host01 ansible_host=<ip address> 
       host02 ansible_host=<ip address>

       [dbservers]
       host01 ansible_host=<ip address> 
       host02 ansible_host=<ip address>

       [webservers:vars]
       node_version=16

       [dbservers:vars]
       postgresql_version=14

or in YAML

        all:
          children:
            vars:
              name: server
            webservers:
              hosts:
                host01:
                  ansible_host: <ip address>
                host02:
                  ansible_host: <ip address>
              vars:
                node_version: 16
            dbservers:
              hosts:
                host01:
                  ansible_host: <ip address>
                host02:
                  ansible_host: <ip address>
              vars:
                postgresql_version: 14


        

