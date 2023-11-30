# Naica website
Naica's official website. It provides info about Naica and its services. It is also Naica's main online selling platform. 

## Installation
These are the installation procedures for MacOS and Debian based Linux distros (hereafter Linux). At the moment there are no installation guides for Microsoft Windows.

### Prerequisites
Necessary programs and packages: `Python3.8`, `pip3`.
The easiest way in MacOS to install packages bia terminal is to use Homebrew package manager. To install Homebrew refer to their [website](https://brew.sh)

MacOS:
```
brew install python@3.8
```
(`brew` installs `pip3` along with `Python3.8`)

Linux:
```
sudo apt update
sudo apt install python3.8
sudo apt install python3-pip
```
### Installation
This project uses `pipenv` for version management. To install it run:
```
sudo pip3 install pipenv
```
Now that you have the required packages, download the repository into your local machine. Go the project's root directory (where `Pipfile` is located) and run:
```
pipenv install
```
The installation process ends at this point, but you still need to set the right configurations before running the website.
### Configuration
The project uses a JSON file that contains all the settings variables. The file must be named `config.json`, and must be in the `/etc/` directory. The JSON file must have the next variables:
```
{
  "SECRET_KEY": "some secret",
  "SQLALCHEMY_DATABASE_URI": "sqlite:///naica.db",
  "MAIL_SERVER": "smtp.gmail.com",
  "MAIL_PORT": "587",
  "MAIL_USE_TLS": "True",
  "MAIL_USERNAME": "someones@gmail.com",
  "MAIL_PASSWORD": "someones_email_password",
  "SPPCLIENT": "paypalapiclientid",
  "IS_LIVE": false
}
```
`IS_LIVE` setting should only be set to `true` in the production server. Setting it to `true` in any other environment will cause some errors, although it won't prevent you from running it.

If you want to use your email account for testing purposes, you must go to your service provider (gmail, outlook, etc.) and follow their instructions. They will most likely ask you to change the 
`MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, and `MAIL_PASSWORD` settings.
### Creating a database (optional)
Some functionalities of the website, like landing page, make use of the database. To create a database start the virtual environment (see next section) and start a Python shell with the command `python`. In the shell run the commands:
```
from website import db
db.create_all()
```
And that's there is all to it. The database is created and ready to use.
## Running a test server
To run the server in your local host go the project's root directory and run the commands:
```
pipenv shell
python main.py
```
To open the test server to your local network run the commands:
```
export FLASK_APP:main.py
Flask run --host=0.0.0.0
```
Flask runs by default in port 5000, to change the port run the last command with the `--port` option. For instance:
```
Flask run --port=8080
```
## Built with
* [Python](https://www.python.org) - backend programming language
* [Flask](https://flask.palletsprojects.com) - web development framework

Although there is no user or login system, the site uses a database to store useful data. The database manager is `sqlite` at the moment.
## Authors
* Adrian Grepe
