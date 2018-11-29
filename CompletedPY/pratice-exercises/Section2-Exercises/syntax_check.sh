#!/bin/sh

# Check if Pip is installed
if [ "$(pip3 --version | grep 'not found')" != "" ] ;
then
	sudo apt install python3-pip
#else
	#echo "Pip found"
fi

# Check if Flake8 is installed
if [ "$(pip3 list --disable-pip-version-check | grep flake8)" = "" ] ;
then
	echo "Flake8 not found. Installing flake8"
	pip3 install flake8 --user
fi

# Run Flake8 on all file to check coding style
python3 -m flake8
