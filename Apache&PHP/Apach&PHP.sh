#! /bin/bash
#aothor:Nianbao

#echo "input user"
#read user
#echo "******install-Apache******"
#sudo apt-get install apache2
#echo "Create html like test.html"
#sudo chown -R $user:$user /var/www/html/
#echo "******install-PHP******"
#sudo apt-get install php5 libapache2-mod-php5
#systemctl restart apache2
#echo "<?php phpinfo(); ?>" >> info.php
#echo "*****Get MySQL********"
#sudo apt-cache search php5
#sudo apt-get install php5-mysqlnd php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl
#sudo systemctl restart apache2
echo "快速安裝 LAMP Server ( Apache + MySQL + PHP5 )"
sudo tasksel install lamp-server
echo "sudo apt-get install tasksel if error is tasksel"

#echo "******phpmyadmin**********"
sudo apt-get install phpmyadmin
cd && cd /var/www/html
sudo ln -s /usr/share/phpmyadmin
