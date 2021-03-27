#!/bin/bash
echo "running! 脚本执行中，请稍后..."

git clone git@gitee.com:Tangkz/tang-long.git

mv tang-long mysite

sudo chmod -R 644 mysite
sudo find mysite -type d | xargs chmod 755

sudo chgrp www-data mysite
sudo chmod g+w mysite
sudo chgrp www-data mysite/db.sqlite3
sudo chmod g+w mysite/db.sqlite3

cd ./mysite/

sudo chgrp -R www-data media
sudo chmod -R g+w media

echo "grant seccess"

python manage.py makemigrations

python manage.py migrate

# sudo mv ./mysite.conf /etc/apache2/sites-available/

# sudo chmod 644 /etc/apache2/sites-available/mysite.conf


ls -l /etc/apache2/sites-available/

# sudo a2dissite mysite.conf
# sudo a2ensite mysite2.conf
# systemctl reload apache2
# 重新载入“apache2.service”需要认证
# raspberry

# sudo service apache2 relaod

sudo service apache2 restart



echo "All right!"

