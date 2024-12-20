# OurTravels
Travel database of places that we have visited and we will.

MacOS Installation
Brew install: https://brew.sh
brew install mysql pkg-config
brew services start mysql
mysql_secure_installation
make sure to set a root password, remove test database and anonymous user

then setup mysql database and mysql user
mysql -p
create database ourtravels;
CREATE USER 'ourtravels'@'localhost' IDENTIFIED BY 'ourtravels';
GRANT ALL ON ourtravels.* TO 'ourtravels'@'localhost';

After checking out project from github
create python environment (via command palette) and make sure to select requirements.txt for install of dependencies.

in terminal to load python virtual environment, if it doesnt happen automatically
source .venv/bin/activate
