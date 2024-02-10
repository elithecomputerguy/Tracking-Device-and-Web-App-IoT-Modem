# Tracking-Device-and-Web-App-IoT-Modem
Tracking Device and Web App IoT Modem (Blues, Python, Bottle, Google Maps API)

This project creates a portable tracking device that sends its location to your server.  Your server stores that data in a SQLite database, and users can access a web app that shows the last 5 locations of the tracking device in embedded Google Maps.

We use Blues Cell+Wifi modem that comes in their dev kit - https://shop.blues.com/products/blues-global-starter-kit

## YouTube Video

https://youtu.be/CN1ue8C2lQI

## Requirements

Blues Global Starter Kit - [https://notehub.io](https://shop.blues.com/products/blues-global-starter-kit)

Web facing server. (Digital Ocean)

pip3 install bottle

Google Maps API Key - https://developers.google.com/maps

PlatformIO VScode extension


## Setup

### Notehub Setup

Create an Account and Project in Notehub - https://notehub.io

Under Settings -> Triangulation Events -> Set to unlimited

Under Routes -> Create Webhook to your server

### Modem Setup

Setup modem based on blues-config.txt file

### Arduino Setup

Upload code to Arduino using PlatformIO VScode extension

### Webserver Setup

Install Bottle

SQLlite should be installed by default, if not install.

SQLite auto configures from the Python script

Run Script - Note the webs services will only function while the script is running.  For continuous use make the script a service, or auto start the script with rc.local

### Google Maps API

Create a Google Maps API Account and get a key.

WARINING - You cannot set max spend limits so be careful using the key.
