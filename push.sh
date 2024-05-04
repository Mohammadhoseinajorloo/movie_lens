#! /bin/bash

git add .
read commit
git commit -m "${commit}"
git push movie_lens master <token.txt
