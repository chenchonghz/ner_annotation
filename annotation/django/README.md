##Setup
```
sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev
sudo mkdir -p /var/log/uwsgi/
sudo chown ubuntu /var/log/uwsgi/
sudo apt-get install rabbitmq-server
pip install -r requirements.txt
[log into mysql] CREATE DATABASE boson_file_state CHARACTER SET utf8;
python manage.py migrate
uwsgi --ini uwsgi.ini
```

##Deploy
```
git pull origin master
touch /root/boson/annotation/django/uwsgi.ini
sudo service rabbitmq-server start
cd /root/boson/annotation/django/tokenizer; C_FORCE_ROOT=true DJANGO_SETTINGS_MODULE=tokenizer.settings celery -A ner.tasks worker --loglevel=info
```
