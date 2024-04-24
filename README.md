# Overview:
A Discord bot that when prompted in a Discord text channel, will simulate a game of blackjack.

# Description:
When Main.py is ran and the bot is in a Discord server, it will appear online. After, when prompted appropriately in a text channel, the bot will respond by displaying the player cards or "total", and dealers first card. The bot will then do a quick check to see if the player has a "BlackJack", this occurs when the two initial cards they recieved have a total of 21, this results in an automatic win. The bot will then prompt the user if they would like to "hit" or "stand". If the player chooses "hit", the bot will provide them another card, increasing their total. The bot will continue prompting the player until they bust, total goes over 21, or the player chooses to "stand". After the player stands or busts, the bot will then give themself a card until their total reaches 17 or they bust.


# How To Run On Docker

### 1. Create docker image from the dockerfile

- `docker build -t discord-bot .`

#### 2. Use a named Docker network and connect both containers to it:

- `docker network create my-network`

#### 3. Then, run your Redis container and connect it to the newly created network:

- `docker run --name redis --network my-network -d redis`

#### 4. Finally, run your Python application container and connect it to the same network, using the name of the Redis container as the REDIS_HOST:

- `docker run --network my-network -e DISCORD_TOKEN=<Your Token> -e REDIS_HOST=redis discord-bot`

#### 4. To Remove the network:

- `docker network rm my-network`





# Contributors
- Cole Aydelotte - coleaydelotte
- Francisco Figueroa - franthe3rd
- Collin Cabral-Castro - CollinmcCastro
