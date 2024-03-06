#!/bin/bash
# To use the script run:
# bash commit.sh 'commit message'

git add --all
git commit -m "$1"
git push
