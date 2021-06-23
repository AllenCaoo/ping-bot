import discord
from discord.ext import commands
import warnings
import ping_image


bot = commands.Bot(command_prefix='|')
warnings.filterwarnings("ignore", category=UserWarning)


@bot.event
async def on_ready():
    print("ClownBot is good to go!")


@bot.command()
async def ping(ctx):
    attachment = ctx.message.attachments[0]  # first attachment object
    in_path = 'images/recent_in.jpg'
    out_path = 'images/recent_out.jpg'
    await attachment.save(in_path)
    ping_image.draw_pings(in_path)
    await ctx.send(file=discord.File(out_path))


@bot.command(brief="Shows how trash Allen's internet is")
async def latency(ctx):
    await ctx.send('{latency} ms'.format(latency=bot.latency * 1000))


if __name__ == '__main__':
    bot.run(input("What is your token? "))