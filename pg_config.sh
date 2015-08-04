#!/usr/bin/env bash
# Install all updates to the base VM
apt-get -qqy update

# Install required packages
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip

# Install required python libraries from PyPi
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2

# Create postgre user and database, and import schema
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb tournament'
su vagrant -c 'psql tournament -f /vagrant/tournament.sql'

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd

