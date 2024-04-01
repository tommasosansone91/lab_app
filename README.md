# lab_app

### description

This is a simple app designed for a Raspberry Pi equipped with DHT22 sensor to record series of temperature and humidity.

### logic

The app records value of temperature and humidity whenever the lab_env_db/ API is triggered.

### install

The app should be installed in /var/www/ and exposed on internal port 8080, external port 80.

It is based on Flask, so it is not meant to be put on production environments.

### database

The app stores data into the file lab_app.db

### web server - reverse proxy

nginx

file with configurations for this app

> lab_app_nginx.conf

general config file

> /etc/nginx/nginx.conf


### application server

uWSGI

> lab_app_uwsgi.ini

### socket file

the app will create a socket file at path /var/www/lab_app/lab_app_uwsgi.sock

### references

The app is based on the project https://github.com/futureshocked/RaspberryPiFullStack_Raspbian

### a note on Adafruit_Python_DHT

The repo includes an edited copy of the Adafruit_Python_DHT module, in order to make it work on raspberry pi 4.
