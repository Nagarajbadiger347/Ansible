# Package module
A package module can install packages using different tool
It dectects the correct package management tool for each target machine

    -name: install latest version of apache version
    ansible.builtin.package:
        name:
          -httpd
        state: latest 
State: posible value
* Default- present
* absent- package will be removed
* latest -update to latest version if present
* present(including version)- install the specified version

# Apt & dnf module
  
    - name: install apache server
      ansible.builtin.apt:           
       name:apache2-2.4.52*
       state:present
       update_cache:yes
       cache_valid_time:3600


dnf module 

    -name:install apache web server
     ansible.builtin.dnf
      name:http>=2.4
      state:present
      update_cache:yes


