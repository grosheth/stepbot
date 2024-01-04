#!/bin/bash

sh ./stop_script.sh
docker run --name stepbot -d -v "/home/bot/discord-bot/src/soundboard":/mnt/sb stepbot

while true
do
sleep 120
done
