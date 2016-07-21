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

echo ***install vimrc***
cd $HOME
cp .vim vim_old
git clone https://github.com/drose11244/vim.git
cp -r vim .vim
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp -r .vim/.vimrc ~/.vimrc


