import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def como_puedo_reciclar_el_plastico(ctx):
    await ctx.send("En la actualidad, la manera más conocida de reciclar plástico es depositando los desechos de este material en el contenedor amarillo. Una vez aquí, los responsables de su manipulación se encargarán de recoger los desechos para llevarlos a un centro de reciclaje especializado.")

@bot.command()
async def como_hacer_una_maceta_con_una_botella(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=Bezx_0guv0k&pp=ygUlY29tbyBoYWNlciB1bmEgbWFjZXRhIGNvbiB1bmEgYm90ZWxsYQ%3D%3D")

@bot.command(name="ayuda")
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles:")
    embed.add_field(name="$hola", value="Saludar al bot.", inline=False)
    embed.add_field(name="$heh", value="hace he", inline=False)
    embed.add_field(name="$como_hacer_una_maceta_con_una_botella", value="te da un link a youtube para hacert una maceta", inline=False)
    embed.add_field(name="$como_puedo_reciclar_el_plastico", value="te da una recomendacion", inline=False)
    await ctx.send(embed=embed)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Cada vez que se llama a la solicitud de pato, el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("MTE1MDA3NTg1NjU2NDI3MzMzMg.GwnBaw.vQgeaNK-sXnGINs7W_s8d4PGHfuCRf5Z2QnIVc")