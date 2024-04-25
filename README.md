# Overview:
A Discord bot that when prompted in a Discord text channel, will simulate a game of blackjack.

# Description:
When Main.py is ran and the bot is in a Discord server, it will appear online. After, when prompted appropriately in a text channel, the bot will respond by displaying the player cards or "total", and dealers first card. The bot will then do a quick check to see if the player has a "BlackJack", this occurs when the two initial cards they recieved have a total of 21, this results in an automatic win. The bot will then prompt the user if they would like to "hit" or "stand". If the player chooses "hit", the bot will provide them another card, increasing their total. The bot will continue prompting the player until they bust, total goes over 21, or the player chooses to "stand". After the player stands or busts, the bot will then give themself a card until their total reaches 17 or they bust.


# How To Run On Local Machine

### 1.
Clone the repository using `git clone https://github.com/cs220s24/DevOps-Discord-Bot.git`
You will need git installed to clone the repository.
Can be downloaded at: https://git-scm.com/download/mac

### 2.
Once cloned cd into the `black-jack-bot` directory using `cd <pathToDirectory>` where the "<pathToDirectory>" will be replaced with the actual path to the repo's black-jack-bot folder.

### 3.
Create a new file named `.env` and the contents of this file should be as follows:
```shell
DISCORD_TOKEN=<discordToken>
REDIS_HOST=redis
REDIS_PORT=6379
```
In `DISCORD_TOKEN=<discordToken>` replace `<discordToken>` with the actual token.

### 4. cd back into the repositories root folder, and then type `./up` in the terminal.
this will run the project using `docker-compose` so you will need docker installed.
to install docker it can be found at: https://docs.docker.com/desktop/install/mac-install/




# Contributors
- Cole Aydelotte - coleaydelotte
- Francisco Figueroa - franthe3rd
- Collin Cabral-Castro - CollinmcCastro
