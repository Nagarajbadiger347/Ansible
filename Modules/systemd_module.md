# systemd module
ansible provides a systemd module to automate the management of systemd service
systemd
-starts,restarts and stop services
-monitors services while they are running to automatically restart if they exist
-manages the automated startup of services when the system boots
-manages system dependencies to ensure that the necessary services are running


        - name: start service
          ansible.builtin.systemd:
            state: started
            enabled: yes
            deamon_reload: yes
            name: application
        