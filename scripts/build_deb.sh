#!/usr/bin/env bash
cd ..
rm -rf dist
mkdir dist
cp requirements.txt setup.py dist/
cp -r pynocchio linux/debian dist/
cp -r linux dist/debian
cd dist
#virtualenv env
#cd env
#source bin/activate
#cd ..
dpkg-buildpackage -us -uc -b
#deactivate