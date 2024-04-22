from datetime import datetime
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands
from blackjack import BlackjackGame
import redis
from time import time

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
REDIS_HOST: Final[str] = os.getenv('REDIS_HOST')
REDIS_PORT: Final[int] = int(os.getenv('REDIS_PORT') or '6379')
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

intents: Intents = Intents.default()
intents.message_content = True
bot: commands.Bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='blackjack', aliases=['bj'])
async def blackjack(ctx):
    timestamp = int(time())
    r.set(f'blackjack:{ctx.author.id}', timestamp)

    game = BlackjackGame()
    player_total, dealer_total = game.deal_cards()

    await ctx.send("BlackJack game started!")
    await ctx.send(f"Your cards: {game.player}, Total: {player_total}")
    await ctx.send(f"Dealer's cards: {game.dealer[:1]}")

    while True:
        response = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        if response.content.lower() == "hit":
            player_total, _ = game.hit()
            await ctx.send(f"Your cards: {game.player}, Total: {player_total}")
            if player_total > 21:
                await ctx.send("Busted! Dealer wins.")
                break
        elif response.content.lower() == "stand":
            while dealer_total < 17:
                dealer_total, _ = game.hit()
            await ctx.send(f"Dealer's cards: {game.dealer}, Total: {dealer_total}")
            if dealer_total > 21:
                await ctx.send("Dealer busted! You win.")
            elif dealer_total >= player_total:
                await ctx.send("Dealer wins.")
            else:
                await ctx.send("You win!")
            break
        else:
            await ctx.send("Invalid move. Please type 'hit' or 'stand'.")

@bot.command(name='players', aliases=['p'])
async def players(ctx):
    keys_with_timestamp = [(key.decode(), int(r.get(key))) for key in r.keys("blackjack:*")]
    recent_entries = keys_with_timestamp[-10:]
    if recent_entries:
        message = "\n".join([f"{index + 1}. <@{data[0].split(':')[1]}>: Last played on {datetime.utcfromtimestamp(data[1]).strftime('%Y-%m-%d')}" for index, data in enumerate(recent_entries)])
        await ctx.send(f"**Recent Players:**\n{message}")
    else:
        await ctx.send("No recent players found.")

@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    # response = responses.get_response(message.content)
    # if response:
    #     await message.channel.send(response)

def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()


