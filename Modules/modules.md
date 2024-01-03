# setup module
    ansible centos1 -m setup
    ansible centos1 -m setup | more

# file module
    ansible all -m file -a "path=/tmp/test.txt state=touch"
    ansible all -m file -a "path=/tmp/test.txt state=file mode=600"

# copy module
    ansible all -m copy -a  "src=/tmp/test.txt dest=/var/www/index.html"
    ansible all -m copy -a  "remote_src=yes src=/tmp/test.txt dest=/var/www/index.html"

# command module
    ansible all -a "hostname" -o
    ansible all -a "touch /tmp/test creates=/tmp/test"
    ansible all -a "rm /tmp/test removes=/tmp/test"

