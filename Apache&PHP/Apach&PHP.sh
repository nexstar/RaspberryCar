#! /bin/bash
#aothor:Nianbao

echo "input user"
read user

echo "******install-Apache******"
sudo apt-get install apache2 -y
echo "Create html like test.html"
sudo chown -R $user:$user /var/www/
cd /var/www/html && echo "<html> <p>123</p> <html/>" >> test.html

echo "******install-PHP******"
sudo apt-get install php5 libapache2-mod-php5 -y
systemctl restart apache2
echo "<?php phpinfo(); ?>" >> info.php

#echo "*****Get MySQL********"
#sudo apt-cache search php5 -y

#sudo apt-get install php5-mysqlnd php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl -y

#sudo systemctl restart apache2
echo "***Write Video******"
sudo apt-get install git -y
#git clone https://github.com/nexstar/RaspberryCar.git
cd $HOME
sudo cp ~/RaspberryCar/Apache\&PHP/Video.html /var/www/html/

echo "Check apache, html, php and video, if have problem can try more browser."
echo "Check apache please input http://127.0.0.1/"
echo "Check html please input http://127.0.0.1/test.html "
echo "Check php please input http://127.0.0.1/info.php"
echo "Check video please input http://127.0.0.1/Video.html"


