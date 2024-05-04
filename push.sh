#! /bin/bash

git add .
echo "enter commit: "
read commit
git commit -m "${commit}"
git push movie_lens master <token.txt
