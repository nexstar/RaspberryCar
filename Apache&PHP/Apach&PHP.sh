#! /bin/bash
#aothor:Nianbao

echo "******install-Apache******"
sudo apt-get install apache2 -y

echo "Create html like test.html"
cd /var/www/html && echo "<html> <p>123</p> <html/>" >> test.html


echo "******install-PHP******"
sudo apt-get install php5 libapache2-mod-php5 -y
systemctl restart apache2
echo "write info.php"
echo "<?php phpinfo(); ?>" >> info.php
sudo chown www-data:www-data /var/www/html/info.php
echo "http://127.0.0.1/info.php if you finish."

#echo "*****Get MySQL********"
#sudo apt-cache search php5 -y

#sudo apt-get install php5-mysqlnd php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl -y

#sudo systemctl restart apache2
echo "***Write Video******"
sudo apt-get install git -y
git clone https://github.com/nexstar/RaspberryCar.git 
cp ~/RaspberryCar/Apache&PHP/Video.html .

echo "run under three websit if you Finsh above."
echo "1.firefox http://127.0.0.1/test.html"
echo "2.firefox http://127.0.0.1/info.php"
echo "3.firefox http://127.0.0.1/Video.html"


