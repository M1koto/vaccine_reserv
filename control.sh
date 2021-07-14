#!/bin/sh
n=$2
python3 -m venv web
source web/bin/activate
if [ $1 -eq 0 ]; then
  file='rong.py'
else
  file='rong2.py'
fi
while [ $n -gt 0 ]; do
  python3 $file
  let n=$n-1
done
