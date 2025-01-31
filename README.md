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

## Apache config
```
WSGIApplicationGroup %{GLOBAL}
WSGIDaemonProcess ourtravels.ai python-path=/var/www/html/OurTravels/django python-home=/var/www/html/OurTravels/venv
WSGIProcessGroup ourtravels.ai
WSGIScriptAlias / /var/www/html/OurTravels/django/OurTravels/wsgi.py
<VirtualHost *:80>


ServerAdmin admin@ourtravels.ai
ServerName ourtravels.ai
ServerAlias www.ourtravels.ai
DocumentRoot /var/www/html/OurTravels

ErrorLog ${APACHE_LOG_DIR}/ourtravels.ai_error.log
CustomLog ${APACHE_LOG_DIR}/ourtravels.ai_access.log combined

Alias /static /var/www/html/OurTravels/static
<Directory /var/www/html/OurTravels/static>
Require all granted
</Directory>

Alias /media /var/www/html/OurTravels/media
<Directory /var/www/html/OurTravels/media>
Require all granted
</Directory>

<Directory /var/www/html/OurTravels/django/OurTravels>
<Files wsgi.py>
Require all granted
</Files>
</Directory>


RewriteEngine on
RewriteCond %{SERVER_NAME} =www.ourtravels.ai [OR]
RewriteCond %{SERVER_NAME} =ourtravels.ai
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
<VirtualHost *:443>


ServerAdmin admin@ourtravels.ai
ServerName ourtravels.ai
ServerAlias www.ourtravels.ai
DocumentRoot /var/www/html/OurTravels

ErrorLog ${APACHE_LOG_DIR}/ourtravels.ai_error.log
CustomLog ${APACHE_LOG_DIR}/ourtravels.ai_access.log combined

Alias /static /var/www/html/OurTravels/static
<Directory /var/www/html/OurTravels/static>
Require all granted
</Directory>

Alias /media /var/www/html/OurTravels/media
<Directory /var/www/html/OurTravels/media>
Require all granted
</Directory>

<Directory /var/www/html/OurTravels/django/OurTravels>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

</VirtualHost>
```
## SSL Certificate installation 
```
sudo apt install certbot python3-certbot-apache
sudo certbot --apache
apache2ctl configtest
```
