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

#Ignore vector warnings.
warnings.filterwarnings("ignore", message=r"\[W007\]", category=UserWarning)
warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)

#Spacyyyy
nlp = spacy.load("en_core_web_sm")
spacy.tokens.Token.set_extension('spell_check_result', default=None)

#Responses
response_1 = "Check <#1043126415454904413> for a step by step guide. Make sure to follow the instructions and read carefully! Make sure to install both the .apk & .obb files! If you require further assistance go to <#1013752682051280967>."
response_2 = "Check https://github.com/TriangleFactory/Breachers/wiki/Android-Guide for a step by step guide. Make sure to follow the instructions and read carefully! If you require further assistance go to <#1013752682051280967>."
response_3 = "Check if you have the `.obb` file inside of `Android/obb/com.TriangleFactory.Breachers`, if you have: do *up to* 6 headset restarts. Check if the game boots between each restart."
#Blacklisted words so the bot doesn't trigger.
blacklist = ["up to", "someone", "installed", "breach"]
words_to_remove = ["get", "how", "to", "good"]
# Tokenize the trigger phrases
bot_response1 = nlp(u"how do i download? where can i find the game? how do I install the game? where do I download breachers? how do I get bugjaeger? where can I find the latest version? how do i update?")
bot_response2 = nlp(u"w bot")


#Bot client and events.
intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)

#Bot itself :)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Tokenize the input text.
    doc = nlp(message.content.lower())
    statement = nlp(message.content.lower())
    
    # Calculate the overall similarity between the input text and each trigger phrase.
    if len(statement) > 0:
        bot_response1_similarity = sum(token1.similarity(token2) for token1 in statement for token2 in bot_response1) / len(statement)
    else:
        bot_response1_similarity = 0

    # Set the minimum similarity required to trigger a response.
    min_similarity = 0.33
    
    # Check if either trigger phrase is similar enough to the input text.
    if any (word in message.content.lower() for word in blacklist):
        return
    elif "black screen" in message.content.lower():
        await message.channel.send(response_3)
    elif bot_response2.similarity(statement) >= 0.752:
        await message.channel.send("Thanks.")
    else:
        if bot_response1_similarity >= min_similarity:
            words = re.findall(r'\b[a-zA-Z]+\b', message.content)[::-1]
            breachers = nlp(u"breachers")
            bugjaeger = nlp(u"bugjaeger")
            game = nlp(u"game")
            download = nlp("download")
            play = nlp("play")
            join = nlp("join")
            alpha = nlp("alpha")
            min_similarity1 = 0.752
            filtered_words = [word for word in words if word not in words_to_remove]
            for word in filtered_words:
                token = nlp(word)
                print(f"{token} similarity with {bugjaeger} is: {token.similarity(bugjaeger)}")
                print(f"{token} similarity with {breachers} is: {token.similarity(breachers)}")
                print(f"{token} similarity with {game} is: {token.similarity(game)}")
                print(f"{token} similarity with {download} is: {token.similarity(download)}")
                print(f"{token} similarity with {play} is: {token.similarity(play)}")
                if token.similarity(bugjaeger) >= min_similarity1:
                    await message.channel.send(response_2)
                    break
                elif token.similarity(breachers) >= min_similarity1:
                    await message.channel.send(response_1)
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
                elif token.similarity(alpha) >= min_similarity1:
                    await message.channel.send(response_1)
                    break
                elif token.similarity(join) >= min_similarity1:
                    await message.channel.send(response_1)
                    break
        if bot_response2.similarity(statement) >= 0.752:
            await message.channel.send("Thanks.")

client.run('TOKEN')
