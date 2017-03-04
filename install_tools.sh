#! /bin/bash
echo ***install apt***
sudo apt-get update
sudo apt-get install raspi-config -y
sudo apt-get install gcc -y
sudo apt-get install make -y
sudo apt-get install ssh -y
sudo apt-get install vim -y
sudo apt-get install git -y
sudo apt-get install ctags -y
#gnome-open
sudo apt-get install libgnome2-bin -y

echo "---Install vim && setting vimrc"
cd $HOME
git clone https://github.com/drose11244/vim.git

if [ -e $HOME/.vim]; then
	mv .vim vim_old
	mv vim .vim
else
	mv vim .vim
fi
bash $HOME/.vim/install_vim.sh

cd $HOME
echo "see Readme"
