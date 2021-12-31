#!/bin/bash -eu
#
# Description:
#
# Usage:
#

cd imgs
zip -r archive akb_pre > /dev/null
mv archive.zip ../akb.zip
zip -r archive saka_pre > /dev/null
mv archive.zip ../saka.zip
cd ..

git add saka.zip akb.zip
git commit -m 'make dataset'
git push
