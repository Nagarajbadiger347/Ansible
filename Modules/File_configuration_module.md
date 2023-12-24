# Modules for handling files
ansible provides multiple modules for automating files existance, attributes and contents
1) file module- handles creating and removing files and directories (cannot change the content of existing files)

        -name:Ensure a directory exist
         ansible builtin.file:
          path:/var/www/html
          state:directory
          owner:root
          group:root
          mode:'0755'


2) copy module- handles copying of files from control machine to target machines (also from one place to another)

         -name:update apache web server configuration
         ansible builtin.copy:
          src:index.html
          dest:/var/www/html/index.html
          owner:root
          group:root
          mode:'0644'


        -name:replace apache config with template
         ansible builtin.copy:
          src:/usr/local/share/apache2/templates/index.html
          dest:/var/www/html/index.html
          remote_src:yes
          owner:root
          group:root
          mode:'0755'
remote_src:yes [the yes value indicates that source files already exist in target machine]