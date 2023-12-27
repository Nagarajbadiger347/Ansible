# Application deployment
provide a web interface to store and display tasks to be completed. call it as "todos"
Run the application in javascript on node.js and store the task in postgresSQL database.

# Steps to deploy the application:
Run both the web application and postgresSQL via docker
Divide the web and database parts between two target machine
provide docker on both machines and difffernet docker containers on each machine. This connnects the web application on one machine to the database on the other 


run the ansible-playbook

        ansible-playbook -i inventory.yaml playbook.yaml