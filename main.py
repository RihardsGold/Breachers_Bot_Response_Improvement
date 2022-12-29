#Comments - delete me before running the code.
#You'll need these dependencies before running the code:
#pip install discord
#pip install -U setuptools wheel
#pip install -U spacy
#pip install -m spacy download en_core_web_sm

#Import
import discord
import spacy
import re
import warnings

#Supress Userwarning W007
warnings.filterwarnings("ignore", message=r"\[W007\]", category=UserWarning)

#Spacyyyy
nlp = spacy.load("en_core_web_sm")
spacy.tokens.Token.set_extension('spell_check_result', default=None)

#Responses
response_1 = "Check <#1032710765238562928> for a step by step guide. Make sure to follow the instructions and read carefully! Make sure to install both the .apk & .obb files! If you require further assistance go to <#1057952666476609577>."
response_2 = "Check https://github.com/TriangleFactory/Breachers/wiki/Android-Guide for a step by step guide. Make sure to follow the instructions and read carefully! If you require further assistance go to <#1057952666476609577>."

#Bot
intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    doc = nlp(message.content.lower())
    bot_response1 = nlp(u"how do i download?")
    bot_response2 = nlp(u"w bot")
    black_screen = nlp(u"black screen")
    statement = doc
    min_similarity = 0.5
    print(f"-------- {doc}")
    print(bot_response1.similarity(statement))
    if bot_response1.similarity(statement) >= min_similarity:
        words = re.findall(r'\b[a-zA-Z]+\b', message.content)
        breachers = nlp(u"breachers")
        bugjaeger = nlp(u"bugjaeger")
        game = nlp(u"game")
        download = nlp("download")
        play = nlp("play")
        join = nlp("join")
        alpha = nlp("alpha")
        min_similarity1 = 0.7
        for word in words:
            token = nlp(word)
            print(f"{token} similarity with {breachers} is: {token.similarity(breachers)}")
            print(f"{token} similarity with {bugjaeger} is: {token.similarity(bugjaeger)}")
            print(f"{token} similarity with {game} is: {token.similarity(game)}")
            print(f"{token} similarity with {download} is: {token.similarity(download)}")
            if token.similarity(breachers) >= min_similarity1:
                await message.channel.send(response_1)
                break
            elif token.similarity(bugjaeger) >= min_similarity1:
                await message.channel.send(response_2)
                break
            elif token.similarity(game) >= min_similarity1:
                await message.channel.send(response_1)
                break
            elif token.similarity(download) >= min_similarity1:
                await message.channel.send(response_1)
                break
            elif token.similarity(play) >= min_similarity1:
                await message.channel.send(response_1)
                break
            elif token.similarity(join) >= min_similarity1:
                await message.channel.send(response_1)
                break
            elif token.similarity(alpha) >= min_similarity1:
                await message.channel.send(response_1)
                break
    if bot_response2.similarity(statement) >= min_similarity:
        await message.channel.send("Thanks.")
client.run('TOKEN')
