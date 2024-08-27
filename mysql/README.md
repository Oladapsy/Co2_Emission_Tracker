# Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...

$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

# Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye

# create a new user after installing mysql
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';

# grant the user permission/privileges
GRANT PRIVILEGE ON database.table TO 'username'@'host';

# additional priviledges just in case using the GRANT
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'username'@'localhost' WITH GRANT OPTION;

<note that with grant option, makes the user able to grant others>

# GRANT ALL PRIVILEGES ON co2db.* TO 'oladapsy'@'localhost';

# granting all priviledges very risky
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

# after creating a user
FLUSH PRIVILEGES;

<note needed for it to take effect>
<more https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql>


