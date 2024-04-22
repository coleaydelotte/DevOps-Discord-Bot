# Overview:
A Discord bot that when prompted in a Discord text channel, will simulate a game of blackjack.

# Description:
When Main.py is ran and the bot is in a Discord server, it will appear online. After, when prompted appropriately in a text channel, the bot will respond by displaying the player cards or "total", and dealers first card. The bot will then do a quick check to see if the player has a "BlackJack", this occurs when the two initial cards they recieved have a total of 21, this results in an automatic win. The bot will then prompt the user if they would like to "hit" or "stand". If the player chooses "hit", the bot will provide them another card, increasing their total. The bot will continue prompting the player until they bust, total goes over 21, or the player chooses to "stand". After the player stands or busts, the bot will then give themself a card until their total reaches 17 or they bust.


# How To Run On Docker
#### Public Docker Repository: https://hub.docker.com/r/franthe3rd/discordblackjackbot

### 1. Pull the Docker Image

```bash
docker pull franthe3rd/discordblackjackbot:latest
```

### 2. Run the Docker Container

```bash
docker run franthe3rd/discordblackjackbot:latest
```

This command will start the Discord bot container in detached mode.

### 3. Stop the Docker Container

To stop the running container, use the following command:

```bash
docker ps
```

```bash
docker stop <container_id_or_name>

```

### 4. Remove the Docker Container

If you want to remove the container from your system, use the following command:

```bash
docker rm <container_id_or_name>
```
```bash
docker rmi franthe3rd/discordblackjackbot:latest
```

# Contributors
- Cole Aydelotte - coleaydelotte
- Francisco Figueroa - franthe3rd
- Collin Cabral-Castro - CollinmcCastro
