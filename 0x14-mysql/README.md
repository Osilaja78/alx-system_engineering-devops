# 0x14. MySQL

### How to install MySQL version 5.7.*

- Add the apt repo
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

- Import missing gpg key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29

- Update apt repository
sudo apt-get update

- Now install MySQL 5.7
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

- Then secure the root user account (follow he prompts)
sudo mysql_secure_installation

- Check mysql version
mysql --version
