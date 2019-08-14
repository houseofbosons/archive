#!/bin/bash
set -e

cd $(git rev-parse --show-cdup)

git add "content"

git status ./content

if [ "$1" ]; then
  git commit -m "$1"
else
  git commit -m "Content Update!"
fi

git push