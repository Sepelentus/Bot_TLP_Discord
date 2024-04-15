from interactions import Client, Intents, listen, slash_command, SlashContext
from interactions.api.events import MessageCreate, MemberAdd
import os
import sys
from dotenv import load_dotenv

load_dotenv()
# Revisar siempre los intents cuando no funcione algo, puede que no lo tenga disponible aqui
bot = Client(intents=
             Intents.DEFAULT |
             Intents.MESSAGE_CONTENT |
             Intents.MESSAGES |
             Intents.GUILD_MODERATION |
             Intents.GUILD_MEMBERS)


# Los comandos @listen deben ir arriba de que parta el bot
@listen()
async def on_ready():
    print("Ready")
    print(f"Este bot esta desarrollado por {bot.owner}")

@listen()
async def on_message_create(event: MessageCreate):
    print(f"Mensaje recibido: {event.message.content}, por el usuario @{event.message.author.username}")

@listen()
async def on_join(event: MemberAdd):
    print(f"Usuario se ha unido: {event.member.user.username}")
    await event.member.add_role(role=1216755690958360637)

token = os.environ.get("TOKEN")

@slash_command(name="obtener_fechas_relevantes", description="entrega las fechas de certamenes y laboratorios", scopes=[1216755690958360636])
async def send_dates(ctx: SlashContext):
    await ctx.send("Las fechas a los certamenes son: \n C1: 15/04/2024 \n C2: 27/05/2024 \n Proyecto: 01/07/2024 \n Recordar que todas las semanas (Se supone) hay laboratorios :)")

bot.start(token=token)
