import discord
from discord.ext.commands import Bot
from discord import Game
from discord.utils import get
import random
import requests
import re
import youtube_dl
from ctypes.util import find_library
import os
import subprocess

BOT_PREFIX = ("!")
scy = Bot(command_prefix=BOT_PREFIX)
scy.remove_command('help')


@scy.command(pass_context=True)
async def help(context):
    print(context.message.author, 'Requested !help')
    
    embed = discord.Embed(title="Welcome to the help. Here we help each other.", description="This bot has the following commands, as of right now:", color=0xff0000)
    embed.add_field(name="!help", value="You're looking at it right now.", inline=False)
    embed.add_field(name="!about", value="Shows useless information.", inline=False)
    embed.add_field(name="!shiba", value="Posts Shibas. *Cute* Shibas if I do say so myself.", inline=False)
    embed.add_field(name="!cat", value="Posts cats. Why? Because why not.", inline=False)
    embed.add_field(name="!fag", value="Dont talk to him like that.", inline=False)
    embed.add_field(name="!decide", value="""Type "`!decide a | b`" and the bot will choose what's best for you.""", inline=False)
    embed.add_field(name="!nudes", value="Don't pretend like you didn't know what it would do.", inline=False)
    embed.add_field(name="!f or !F", value="Press F to pay respects.", inline=False)    
    embed.add_field(name="!vote", value="Ask something.", inline=False)
    embed.add_field(name="!song", value="Official `Loser Squad` Song.", inline=False)
    embed.add_field(name="!quote", value="Say `!quote add *something*` to add a quote. Say `!quote show` to show a random quote.", inline=False)
    await scy.say(embed=embed)


@scy.command(pass_context=True)
async def about(context):
    print(context.message.author, 'Requested !about')
    
    embed = discord.Embed(title="What's the name of the loser that made this terrible bot?", description="Scyless#7469", color=0xff0000)
    
    embed.set_thumbnail(url="https://i.imgur.com/F1dLxoR.png?1")
    embed.set_author(name="Twitter", url="https://twitter.com/_Scyless", icon_url="https://i.imgur.com/JJjJBz2.jpg")
    embed.add_field(name="That's everything?", value="Yep, sorry.")    
    embed.add_field(name="Source code?", value="[Do you like spaghetti?](https://github.com/Scyless/lesserscy-discord-bot/)")
    embed.add_field(name="Invite?", value="[Here](https://discordapp.com/oauth2/authorize?client_id=462412143464284160&scope=client) is the link.")
    
    await scy.say(embed=embed)

@scy.command(pass_context=True)
async def shiba(context):
    print(context.message.author, 'Requested !shiba')
    shiba = requests.get('http://shibe.online/api/shibes?count=[1]&urls=[true]&httpsUrls=[true]')
    
    msg = await scy.say(shiba.json())
    msg2 = re.sub('[\[\]\']', '', msg.content)
    
    await scy.edit_message(msg, msg2)


@scy.command(pass_context=True)
async def cat(context):
    print(context.message.author, 'Requested !cat')
    shiba = requests.get('http://shibe.online/api/cats?count=[1]&urls=[true]&httpsUrls=[true]')
    
    msg = await scy.say(shiba.json())
    msg2 = re.sub('[\[\]\']', '', msg.content)
    
    await scy.edit_message(msg, msg2)

    
@scy.command(pass_context=True)
async def fag(context):
    print(context.message.author, 'Requested !fag')
    
    responses = [
        'no u',
        'More like {}'.format(context.message.author.name),
        'The only faggot in this server is {}.'.format(context.message.author.name),
        'Did you just call me a faggot? I\'m a bot, how many braincells do you have? Wait, don\'t tell me.'

]

    await scy.say(random.choice(responses))


@scy.command(pass_context=True)
async def decide(context):
    print(context.message.author, 'Requested !decide')
        
    decisions = (context.message.content) # Set loop
    filtered = re.sub('!decide', '', decisions) # Removes !decide from the decision
    splitted = filtered.split('|')    # Split the choices into multiple answers
    generator = random.choice(splitted) # Generates the answer
    
    msg = [
    '***{}*** sounds like the best choice.'.format(generator),
    '***{}*** is the only sane option.'.format(generator),
    '***{}*** is what a retard would pick. And you\'re retarded.'.format(generator),
    
    'Are you a retard? Of course you are. Pick ***{}***.'.format(generator),
    'Pick your poison. Nevermind, I already did it for you. Choose ***{}***.'.format(generator),
    'The Loser Squad demands you to take ***{}***.'.format(generator)
    ]
        
    await scy.say(random.choice(msg)) # Send a random choice
    

@scy.command(pass_context=True)
async def nudes(context):
    print(context.message.author, 'Requested !nudes')
    
    pics = [
        'https://i.imgur.com/JwHwf8e.jpg',
        'https://i.imgur.com/8lt3okl.jpg',    
        'https://i.imgur.com/KDTn3pK.jpg',
        'https://i.imgur.com/GrHH9lS.jpg',
        'https://i.imgur.com/MEWYr6o.jpg',
        'https://i.redd.it/jw3uzji58wt01.jpg',
        'https://s14-eu5.startpage.com/cgi-bin/serveimage?url=http%3A%2F%2Fi0.kym-cdn.com%2Fentries%2Ficons%2Fmobile%2F000%2F026%2F318%2Fbec_1_.jpg&sp=5fa6126760dca5a728183b7c55928bce'
]


    await scy.say(random.choice(pics))


@scy.command(name='f',
    aliases='F',        
    pass_context=True)
async def f(context):
    print(context.message.author, 'Requested !f')
    await scy.say(context.message.author.name + ' ' + 'paid his respects. And so should you.')


@scy.command(pass_context=True)
async def vote(context, *, arg):    
    print(context.message.author, 'Requested !vote')
    
    thonk = get(scy.get_all_emojis(), name='thonk')
    upvote = get(scy.get_all_emojis(), name='upvote')
    downvote = get(scy.get_all_emojis(), name='downvote')

    msg = await scy.say("Should {} {} {}".format(context.message.author.mention, arg, thonk))
    await scy.add_reaction(msg, upvote)
    await scy.add_reaction(msg, downvote)


@scy.command(pass_context=True)
async def song(context):
    print(context.message.author, 'Requested !song')
    
    song = ('''`
    [Intro]
He-he-here we go!

So they\'re finally here, performing for you
If you know the words, you can join in too
Put your hands together, if you want to clap
As we take you through this stupid rap!
Huh!

[Chorus]
LS
Loser Squad!

[Verse 1]
He\'s the leader of the bunch, you know him well
He\'s finally back to kick some tail
His Lesser Scy can‘t work in spurts!
If he mentions ya, it's gonna hurt!
He\'s bigger, slower, and weaker too
He\'s the first member of the LS crew!
Huh!

[Chorus]
LS
Loser Squad!
LS
Loser Squad is here!

[Verse 2]
This Grill‘s got style, so listen up dudes
She can sleep for hours, to suit her mood
She's quick and nimble when she needs to be
She can play through the night and get her blades!
If you choose her, you'll choose wrong
With a ron and a bo, she's one cool Girl!
Huh!

[Chorus]
LS
Loser Squad!

[Verse 3]
He has style, he no grace
Th-this Boi has a owo face
He can spam cute bois when he needs to
And stretch his arms out, just to hug you
Lachsfisch himself just like a balloon
This crazy Boi just digs his tunes!
Huh!
    `''')
    
    await scy.say(song + '\n \n`Credit: Adversary aka bu`:b::b:`er`')


@scy.command(pass_context=True)
async def play(context, *, arg):
    print(context.message.author, 'Requested !play')
    
    server = context.message.author.server
    library = r'/usr/lib/libopus.so'
    discord.opus.load_opus(library)
    author = context.message.author
    channel = author.voice_channel
                
    if re.match(r'None', str(channel)):
        await scy.say('Do you even know how to join a voice channel? I bet you don\'t.')
    else:
        if not scy.is_voice_connected(server):
            voice = await scy.join_voice_channel(channel)
            
        print(arg)
        url = 'https://www.youtube.com/results?search_query={}'.format(arg)
        print(url)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
        player.create_stream_player(player)
        player.start()
        
        
@scy.command(pass_context=True)
async def quote(context, *, arg):
    print(context.message.author, 'Requested !quote')

    if 'add' in arg:
        arg.split(' ', 1)
        quote = arg.split(' ', 1)[1]
        os.system(''' 
        echo {} \
        >> /home/scy/Documents/Scripts/python/discord-bot/bot/database/quotes 
        '''.format(quote))
        await scy.say('Added *{}* to the database!'.format(quote))
    elif 'show' in arg:
        lines = open('/home/scy/Documents/Scripts/python/discord-bot/bot/database/quotes').read().splitlines()
        quote = random.choice(lines)
        await scy.say('*{}*'.format(quote))
    else:
        await scy.say('''I think you meant something like `!quote add`, or `!quote show`. But you can't even type.\n***Pathetic***. ''')
    break
    
    
@scy.event
async def on_message(message):
    game = [
    'with ur mom lol',
    'say !help if you need help'
    ]
    await scy.change_presence(game=Game(name=random.choice(game)))
    
    if '<@462412143464284160>' in message.content:
        print('Someone mentioned the bot.')
        await scy.send_message(message.channel, '''Why the fuck would you mention a bot? Are you retarded or something?\n
Oh wait, I bet you thought "I'm gonna do something really random and mention a bot! \
How funny is that?". Well, let me tell you something. You're not funny. You're nothing. You're trash.''')

    await scy.process_commands(message)
    return


@scy.command(pass_context=True)
async def test(context):

    if not discord.opus.is_loaded():
        discord.opus.load_opus('/usr/lib/libopus.so')
    else:
        author = context.message.author
        channel = author.voice_channel
        voice = await scy.join_voice_channel(channel)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
        #player.create_stream_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
        player.start()   


@scy.event
async def on_ready():
    game = [
    'with ur mom lol',
    'say !help if you need help'
    ]
    await scy.change_presence(game=Game(name=random.choice(game)))
    print('ID - ' + scy.user.id)
    print('Connected.')
    print('----------')


TOKEN = 'MyToken'
scy.run(TOKEN)
