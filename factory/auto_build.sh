#!/bin/bash

my_path=$(dirname $0)
cd $my_path

python3 ad.py
python3 gfwlist.py
python3 build_confs.py
python3 qrcode.py
cd ..

git add .
git commit -m "Nightly build" -m "已合并最新的去广告规则及 GFWList"
git push
