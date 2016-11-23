sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djbase;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'qwerty';"
mysql -uroot -e "GRANT ALL ON djbase.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"