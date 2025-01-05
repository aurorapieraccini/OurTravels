# OurTravels
OurTravels is a website that allows users to save locations they have visited, and get new recommendations of places to visit with their friends.

## Technical Diagram
![Diagram](images/backend_diagram.png)

### Development setup information
MacOS Installation
Brew install: https://brew.sh
```
# brew install mysql pkg-config
# brew services start mysql
# mysql_secure_installation
make sure to set a root password, remove test database and anonymous user
Then setup mysql database and mysql user
# mysql -p
# create database ourtravels;
# CREATE USER 'ourtravels'@'localhost' IDENTIFIED BY 'ourtravels';
# GRANT ALL ON ourtravels.* TO 'ourtravels'@'localhost';
```
After checking out project from github
create python environment (via command palette) and make sure to select requirements.txt for install of dependencies.

in terminal to load python virtual environment, if it doesnt happen automatically
    # source .venv/bin/activate
