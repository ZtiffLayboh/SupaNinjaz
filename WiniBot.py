import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Inició sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}, el único bot anti-contaminacion!')
@bot.command()
async def facto(ctx):
    await ctx.send(f'¿Sabías que mientras escribo estas lineas de codigo faltan 30 minutos para que empiecen las clases?, ahora ya lo sabes.')
@bot.command()
async def info_contaminacion(ctx):
    await ctx.send('¿Qué es la contaminación? \n'
                   'La contaminación se refiere a la introducción de sustancias o agentes nocivos en el medio ambiente que causan efectos perjudiciales para la vida, ya sea para los seres humanos, los animales o los ecosistemas en su conjunto. Estas sustancias contaminantes pueden ser de origen natural o generado por actividades humanas.')



@bot.command()
async def facto_random(ctx):
    fact = random.randint(1, 6)
    if fact == 1:
        await ctx.send("Microplásticos en lugares remotos: \n"
                       "Incluso en áreas remotas como el Ártico, se han encontrado microplásticos, lo que demuestra la capacidad de los contaminantes para viajar largas distancias a través del aire y el agua.")
        with open('images/fact1.jpeg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if fact == 2:
        await ctx.send("Contaminación sonora y vida marina: \n"
                       "La contaminación acústica en los océanos, principalmente debido al ruido del tráfico marítimo, puede interferir con la comunicación, la búsqueda de alimento y la orientación de muchas especies de vida marina.")
        with open('images/fact2.jpeg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if fact == 3:
        await ctx.send("Contaminación del aire y esperanza de vida: \n"
                       "Se estima que la contaminación del aire reduce la esperanza de vida promedio de las personas en áreas altamente contaminadas en varios años, debido a enfermedades respiratorias y cardiovasculares.")
        with open('images/fact3.jpeg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if fact == 4:
        await ctx.send("Contaminación lumínica y vida silvestre: \n"
                       "La contaminación lumínica puede alterar los patrones de migración y reproducción de la vida silvestre, así como afectar el comportamiento de insectos, aves y mamíferos nocturnos.")
        with open('images/fact4.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if fact == 5:
        await ctx.send("Basura espacial y contaminación orbital: \n"
                       "La acumulación de desechos espaciales en órbita alrededor de la Tierra plantea riesgos de colisiones con satélites operativos y naves espaciales, lo que podría generar más desechos y dificultar futuras misiones espaciales.")
        with open('images/fact5.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if fact == 6:
        await ctx.send("Contaminación del suelo y seguridad alimentaria: \n"
                       "La contaminación del suelo con metales pesados y productos químicos tóxicos puede afectar la calidad de los cultivos y reducir la seguridad alimentaria, especialmente en áreas agrícolas cercanas a fuentes de contaminación industrial.")
        with open('images/fact6.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def repetir(ctx,*,mesaje):
    await ctx.send(mesaje)

@bot.command()
async def guardar_y_enviar(ctx,*,texto):
    canal_id = "1204481855500451892"
    canal_destino=bot.get_channel(int(canal_id))
    if canal_destino in None:
        await ctx.send("el canal no existe")
        return
    await canal_destino.send(texto)
    await ctx.send("la de wini")

@bot.command()
async def meme(ctx):
    mem = random.randint(1, 6)
    if mem == 1:
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if mem == 2:
        with open('images/mem2.jpeg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if mem == 3:
        with open('images/mem3.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if mem == 4:
        with open('images/mem4.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if mem == 5:
        with open('images/mem5.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if mem == 6:
        with open('images/mem6.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("ingresa tu token acá")
