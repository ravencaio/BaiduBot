import os
import discord
import random
import requests
import json
from replit import db
from keepalive import keep_alive
senha = os.environ['senha']



client = discord.Client()



def update_rule(regra):
  if 'rule' in db.keys():
    rule = db['rule']
    rule.append(regra)
    db['rule'] = rule
  else:
    db['rule'] = [regra]

def delete_rule(delrule):
  rule = db['rule']
  rule.pop(delrule)


def update_virus(viruses):
  if 'virus' in db.keys():
    virus = db['virus']
    virus.append(viruses)
    db['virus'] = virus
  else:
    db['virus'] = [viruses]


def delete_virus(deleto):
  virus = db['virus']
  virus.pop(deleto)
  

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)




@client.event
async def on_ready():
  print(f'Foi logado como {client.user}')

prefix = '&'
@client.event
async def on_message(message):
  usuario = str(message.author).split('#')[0]
  msg = message.content
  msgst = str(msg)
  up = msgst.upper()
  
  if up.startswith(f'{prefix}HELP'):
    embed=discord.Embed(title="你需要帮助AJUDA你需要帮助BAIDU你需要帮助", description="Prefixo do bot Baidu = &", color=0xff0000)
    embed.set_author(name="你需要帮BAIDU你需要帮助COMPANY你需要帮助", url="https://www.baidu.com/", icon_url="https://images-ext-2.discordapp.net/external/Y87IyQ7tAIw5TwYayCR1_Eev9R5aWW9iSLsKXRGnnKw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/919634663079837696/93dc79e2b6dd8019fe133a238452a298.webp?width=472&height=472")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/737772651723882546/920841255255175208/baidu-logo-image-sensorstechforum-com.png")
    embed.add_field(name="cr7", value="Gif do cr7", inline=False)
    embed.add_field(name="messi", value="Gif do messi", inline=False)
    embed.add_field(name="inspiração", value="Frase para inspirar você", inline=False)
    embed.add_field(name="ler", value="Lê quantos caracteres tem na(s) palavra(s)", inline=False)
    embed.add_field(name="novo", value="Adiciona um novo vírus a database", inline=False)
    embed.add_field(name="del", value="Deleta um vírus da database", inline=False)
    embed.add_field(name="virusdb", value="Database de vírus", inline=False)
    embed.add_field(name="regras", value="Regras (não oficiais) do servidor", inline=False)
    embed.add_field(name="novregra", value="Faz uma nova regra não oficial para o servidor", inline=False)
    embed.add_field(name="noregra", value="Deleta uma regra não oficial do servidor", inline=False)
    embed.add_field(name="rng", value="numero aleatorio com o limite de 10000000", inline=False)
    embed.add_field(name="moeda", value="Gire uma moeda!", inline=False)
    embed.add_field(name="virdbdel", value="Deleta a database de vírus", inline=False)
    embed.add_field(name="clearregra", value="Deleta as regras não oficiais do servidor", inline=False)
    embed.add_field(name="pfp", value="Foto de perfil da pessoa mencionada", inline=False)
    embed.add_field(name='soma', value ='soma dois valores', inline =False )
    embed.add_field(name='sub', value='subtrai dois valores', inline =False)
    embed.add_field(name = 'div', value='mostra a divisão, divisão inteira e o resto da divisão de um valor')
    embed.add_field(name='mult', value='multiplica dois valores')
    embed.add_field(name='raiz', value='mostra a raiz quadrada de um valor')
    embed.add_field(name='pot', value= 'mostra a potencia entre dois valores')
    await message.channel.send(embed = embed)

  if message.author == client.user:
    return
  

  if up.startswith('OI'):
    await message.channel.send(f'Oi `{usuario}`!')
  
  if '@everyone' in msg:
    await message.channel.send('pare de mandar @everyone, caceta')
  
  if up.startswith(f'{prefix}CR7'):
    gif = random.randint(1, 100)
    if gif > 50:
      await message.channel.send('https://tenor.com/bvsc8.gif')
    if gif < 50:
      await message.channel.send('https://tenor.com/bHFXt.gif')
   
 
  if msg.startswith(f'{prefix}pfp'):
    lista = message.mentions
    for user in lista:
      await message.channel.send(user.avatar_url)

  if up.startswith(f'{prefix}MECI') or message.content.startswith('&MESSI'):
    await message.channel.send('https://cdn.discordapp.com/attachments/760497493254864929/919662181170163752/ankara_meci.mp4')
  
 
  
  if msg.startswith(f'{prefix}inspiração'): 
    await message.channel.send(get_quote())
  
  if up.startswith(f'{prefix}LER'):
    mensagem = len(str(up.strip(f'{prefix}LER ')))
    palavr = up.strip(f'{prefix}LER ')
    palavras = len(palavr.split(' '))

    if mensagem == 0 or mensagem == -1:
      await message.channel.send('Você tem que botar pelo menos um caractere')
    else:
      await message.channel.send(f'Essa mensagem tem {mensagem} caracteres (contando com espaços!) e {palavras} palavras')
  
  if msg.startswith(f'{prefix}novo'):
    viruses = msg.split(f'{prefix}novo ', 1)[1]
    update_virus(viruses)
    await message.channel.send('O seu vírus foi adicionado a database.')
    return
 
  if up.startswith(f'{prefix}DEL'):
    msg = str(message.content)
    delet = up.split(f'{prefix}DEL ')[1]
    deleto = int(delet) - 1
    delete_virus(deleto)
    await message.channel.send('O virus foi deletado da database')
  

  for virus in db['virus']:
    if virus in msg:
      await message.delete()
      await message.channel.send(':rotating_light: A MENSAGEM FOI INDENTIFICADA COMO UM VIRUS E POR ISSO FOI DELETADA!, CUIDADO:rotating_light: ')
  
  if up.startswith(f'{prefix}VIRUSDB'):
    if db['virus'] == []:
      await message.channel.send(f'**A database está vazia, adicione um novo link de vírus com o comando {prefix}novo**')
    else:    embed=discord.Embed(title="DATABASE DE VÍRUS", description="Não clique em nenhum link!", color=0x000000)
    for num,virus in enumerate(db['virus']):
      embed.add_field(name=f'Vírus número: {num + 1}', value=virus, inline=False)
    await message.channel.send(embed = embed)                                     
  
  if msg.startswith(f'{prefix}novregra'):
    regra = msg.split('&novregra ', 1)[1]
    update_rule(regra)
    await message.channel.send('Você criou uma nova regra (não oficial) para o servidor!')
  
  if msg.startswith(f'{prefix}noregra'):
    msg = str(msg)
    bgl = msg.strip(f'{prefix}noregra ')
    delrule = int(bgl) - 1
    delete_rule(delrule)   
    await message.channel.send('A regra foi deletada')
  
  if up.startswith(f'{prefix}REGRAS'):
    regras = db['rule']
    if regras == []: 
      await message.channel.send('**Não existem regras não oficias no servidor, adicione com o comando &novregra.**')
    else:
          embed=discord.Embed(title="REGRAS", description="Regra não oficiais do servidor", color=0x844d4d)
    for num,rule in enumerate(db['rule']):
      embed.add_field(name=f'Regra número: {num + 1}', value=rule, inline=False)
    await message.channel.send(embed = embed)

  if up == f'{prefix}CLEARREGRA':
    if str(message.author.id) == '265881043096174594':
      db['rule'] = []
      await message.channel.send(':warning: **As regras foram deletadas**:warning: ')
    else:
      await message.channel.send('Você não tem permissão pra limpar as regras')

  if up.startswith(f'{prefix}RNG'):
    mensagem = msg.split()
    n1 = int(mensagem[1])
    n2 = int(mensagem[2])
    await message.channel.send(f'Aqui está o seu número {random.randint(n1, n2)}')
  
  if up.startswith(f'{prefix}MOEDA'):
    moeda = random.randint(1,100)
    if moeda > 50:
      await message.channel.send('**Cara!**')
    if moeda < 50:
      await message.channel.send('**Coroa!**')
  

  if f'{prefix}VIRDBDEL' == up:
    if str(message.author.id) == '265881043096174594':
      db['virus'] = []
      await message.channel.send('A database foi deletada.')
    else:
      await message.channel.send('Você não tem permissão para usar esse comando')
  
  if msg.startswith(f'{prefix}id'):
    lista = message.mentions
    for user in lista:
      await message.channel.send(user.id)
  
  if up.startswith(f'{prefix}SOMA'):
    num = msg.split()
    x = float(num[1])
    y = float(num[2])
    await message.channel.send(f'{x} + {y} = {x + y}')
  
  if up.startswith(f'{prefix}SUB'):
    num = msg.split()
    x = float(num[1])
    y = float(num[2])
    await message.channel.send(f'{x} - {y} = {x - y}')

  if up.startswith(f'{prefix}DIV'):
    num = msg.split()
    x = float(num[1])
    y = float(num[2])
    await message.channel.send(f'''{x} / {y} = {x / y}
    {x} // {y} = {x // y}
    {x} % {y} = {x % y}''')  

  if up.startswith(f'{prefix}MULT'):
    num = msg.split()
    x = float(num[1])
    y = float(num[2])
    await message.channel.send(f'{x} x {y} = {x * y}')
  
  if up.startswith(f'{prefix}RAIZ'):
    num = msg.split()
    x = float(num[1])
    await message.channel.send(f'√{x} = {x ** 0.5:.5f}')
  
  if up.startswith(f'{prefix}POT'):
    num = msg.split()
    x = float(num[1])
    y = float(num[2])
    await message.channel.send(f'{x} ^ {y} = {x ** y}')




keep_alive()
client.run(senha)