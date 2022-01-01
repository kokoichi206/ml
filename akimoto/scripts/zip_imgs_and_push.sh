#!/bin/bash -eu
#
# Description:
#   前処理後のファイルをzip化し、remoteにpushする
#
# Usage:
#   bash scripts/<file name>
#   上の階層で使う事

cd imgs
zip -r archive akb_pre > /dev/null
mv archive.zip ../akb.zip
zip -r archive saka_pre > /dev/null
mv archive.zip ../saka.zip
cd ..

git add saka.zip akb.zip
git commit -m 'make dataset'
git push
