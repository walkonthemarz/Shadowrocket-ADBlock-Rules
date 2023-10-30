#!/bin/bash

my_path=$(dirname $0)
cd $my_path

python3 ad.py
python3 gfwlist.py
python3 build_confs.py
python3 qrcode.py
cd ..

git add .
git commit -m "Daily build" -m "Already merged latest Ads rules and GFWList"
git push
