##Setup
```

sudo apt-get install git
git clone https://github.com/richardchen331/boson.git

sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev
sudo mkdir -p /var/log/uwsgi/
sudo chown ubuntu /var/log/uwsgi/
sudo apt-get install python-pip
sudo pip install -r requirements.txt
python manage.py migrate
sudo uwsgi --ini uwsgi.ini
```

##Deploy
```
(git checkout HEAD cancer-db/db.sqlite3)
git pull origin master
touch /home/ubuntu/boson/cancer-db/uwsgi.ini
```

##Deploy React Apps (example)
```
cd dashboard/react/react_example
npm install
npm run build
```
