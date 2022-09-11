# Discord Bot

So I made a discord bot for me and my friends. It's full of inside jokes(most of it of bad taste) and also has a few functionnalities.

I was bad at coding when I began this project, still am. So expect bugs. I will eventually cleanup the code. 

I know, the code is definitely not perfect and will not work out of the box so don't forget to look at Missing parts section

## !help

use !help to see available commands

## Bot Functionnalities

The bot loads all the cogs in the main.py file.

The cogs are the ones interacting with the discord server.

### games

coinflip: basic coinflip
russian roulette: 1/6 chances to get kicked out of the voice channel when someone calls !rr. Stops whenever someone is kicked

### reddit

You can use this bot to get random posts on subreddits.

I also made some commands for specific subreddits which are all jokes.

### music

You can play music from youtube with !play and the url in question. Some links dont work for some reason.

### wallet

I made wallets for fake currency that is stocked in mongodb

## Devops features

I decided to let my jenkinsfile and kubernetes manifests in the project if you ever want to deploy the bot via a pod or add CI/CD elements with your bot.

## Environment variables

Create a .env file where variables are going to be loaded in the settings.py file


```
TOKEN=OTgyNjI4NjEwMjM2MDk2NTIy.G5j7Uv.I0G7TaIYGReHPKO7fhx4-jCqzdq0_n7OcHGLTs
TXTCHANNEL=769577020920561667
VOICECHANNEL=969754635294343209

REDDIT_ID=dBaYC5jZUmX5kAFlMnVJvA
REDDIT_SECRET=7Dz68Q7MIHWOVP1_PBi-FEwXWKeWXg

These are discord id's
FILOU=388902413358071819
RURU=389820854311059457
ALESS=622136882049974272
CORBIN=167753085337337858
BRIDO=258267042489171969
PEPI=769706704098164747
MARTIN=769630884495097896

database informations
DB = "databasename"
HOST = "hostnameoripaddress"
PORT = 9999
DBUSER = "user"
DBPASS = "password"

CONN_STRING="mongodb://hostnameoripaddress:port/"
```