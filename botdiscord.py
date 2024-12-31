import discord
from discord.ext import commands
import asyncio

# Insira o token do seu bot aqui
TOKEN = ''

# Defina os intents do bot
intents = discord.Intents.all()
intents.members = True  # Permite acesso aos membros do servidor

# Inicializando o bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

@bot.command()
async def enviar_dm(ctx, cargo: discord.Role, *, mensagem: str):
    # Verifica se o comando está sendo executado por um administrador
    if ctx.author.guild_permissions.administrator:
        membros_do_cargo = [member for member in ctx.guild.members if cargo in member.roles]
        
        if not membros_do_cargo:
            await ctx.send(f"Nenhum membro encontrado com o cargo {cargo.name}.")
            return
        
        await ctx.send(f"Enviando mensagens para membros com o cargo: {cargo.name}...")

        for member in membros_do_cargo:
            try:
                if not member.bot:  # Não enviar mensagens para bots
                    await member.send(mensagem)
                    print(f'Mensagem enviada para {member.name}')
                    await asyncio.sleep(1)  # Pausa de 1 segundo para evitar rate limits
                else:
                    print(f'Não enviando mensagem para o bot {member.name}.')
            except discord.Forbidden:
                print(f'Não consegui enviar mensagem para {member.name} (DMs fechadas).')
            except Exception as e:
                print(f'Erro ao enviar mensagem para {member.name}: {e}')
        await ctx.send(f"Mensagens enviadas para todos os membros com o cargo {cargo.name}.")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

bot.run(TOKEN)