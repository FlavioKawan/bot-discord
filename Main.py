import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


byte = commands.Bot(command_prefix='.', description='description', intents=intents)



#CARREGAMENTO DO BOT
@byte.event
async def on_ready():
        print('Iniciando...', byte.user)




            
#MENSAGEM DE OLA
@byte.command(name = 'ola')
async def on_ola(ctx):
    await ctx.send('ola ' + ctx.author.name )



# ABERTURA DO MENU
@byte.command(name= 'menu')
async def on_menu(ctx):
        menu = '1. Pesquisa Google \n 2. jogo da velha \n 3 . funções adicionais '
        name = ctx.author.name 
        saida = f'aqui está o menu caro {name} \n {menu}'
        await ctx.send(saida)



@byte.event
async def on_member_join(member):
    bv = byte.get_channel(1056999339442045022)
    menu = byte.get_channel(on_menu)
    msg  = await bv.send(f"Salve {member.mention} Digite .menu")



        #APREDIZAGEM DO BOT
        #//////////////////
        #///////////////////

        #PESQUISA GOOGLE
        #//////////////////
        #///////////////////

#fechamento da classe





# Solução do erro Myclient








#token
byte.run('MTA1NzAwMDIwMzYxMTI5MTgxOQ.GpEWWZ.RDGCCx39r_gslC7kEgPNlWcEgEGt2kh8d2Xx1M')