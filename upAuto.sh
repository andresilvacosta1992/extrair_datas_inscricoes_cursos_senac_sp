#!/bin/bash

while true; do
git add .
git commit -m "commit automático"
git push origin
  sleep 300
done