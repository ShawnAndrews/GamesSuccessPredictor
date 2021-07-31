# Description: Start a Discord bot which responds to game prediction requests from users based on a given trained model.

import sys
import os
import discord
import numpy as np
from keras.models import load_model

if len(sys.argv) != 3:
    sys.exit(-1)

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # force CPU-only

TOKEN = sys.argv[2]
client = discord.Client()
model = load_model(sys.argv[1])


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    command = message.content.lower()

    if message.author == client.user or str(message.channel) != "🎲┋gsp-bot":
        return
    if command.startswith("!predict"):
        if command == "!predict":
            return_msg = (
                f"```"
                f"Description:\n"
                f"  This bot has been trained as a Feed Forward Neural Network (FFNN) on the success and parameters of "
                f"over 20,000+ Steam games! Given the parameters of any hypothetical game, we can use this neural "
                f"network model to predict the game's future success on the Steam market. I hope this will be useful "
                f"as a "
                f"tool during game development to answer questions such as: what is the best price point for my game, "
                f"which month should i release my game, should i invest time into porting to other platforms, "
                f"or will adding multiplayer boost the chance of my game's success or not.\n\n "
                f"Parameters:\n"
                f"  1.) Price - <float>\n"
                f"      Acceptable values - [0.00, 80.00]\n"
                f"  2.) Age_required - <integer>\n"
                f"      Acceptable values - [0, 18]\n"
                f"  3.) DLC available - <boolean>\n"
                f"  4.) Steam Achievements - <boolean>\n"
                f"  5.) Windows port - <boolean>\n"
                f"  6.) Mac port - <boolean>\n"
                f"  7.) Linux port - <boolean>\n"
                f"  8.) Month of release - <integer>\n"
                f"      Acceptable values - [0, 12], [jan, dec], [january, december]\n"
                f"  9.) Categories - <string> ... <string>\n"
                f"      Acceptable values - singleplayer, mmo, coop, inapppurchases, controllersupport, pvp\n"
                f"  10.) Genres - <string> ... <string>\n"
                f"      Acceptable values - adventure, casual, indie, simulation, action, multiplayer, rpg, strategy, "
                f"racing, sports, 2d, puzzle, vr, platformer, horror, shooter, firstperson, survival, turnbased, "
                f"space\n\n "
                f"Examples:\n"
                f"  1.) !predict free 18 false true true false false august singleplayer action adventure puzzle\n"
                f"  2.) !predict 19.99 0 true false true true true december multiplayer mmo controllersupport horror "
                f"survival\n "
                f"```"
            )
            await message.channel.send(return_msg)
            return

        # build parameters
        params = dict()
        params['price'] = 0
        params['age_required'] = 0
        params['dlc'] = 0
        params['achievements'] = 0
        params['windows'] = 0
        params['mac'] = 0
        params['linux'] = 0
        params['release_month'] = 0
        params['c_singleplayer'] = 0
        params['c_mmo'] = 0
        params['c_coop'] = 0
        params['c_inapppurchases'] = 0
        params['c_controllersupport'] = 0
        params['c_pvp'] = 0
        params['g_adventure'] = 0
        params['g_casual'] = 0
        params['g_indie'] = 0
        params['g_simulation'] = 0
        params['g_action'] = 0
        params['g_multiplayer'] = 0
        params['g_rpg'] = 0
        params['g_strategy'] = 0
        params['g_racing'] = 0
        params['g_sports'] = 0
        params['g_2d'] = 0
        params['g_puzzle'] = 0
        params['g_vr'] = 0
        params['g_platformer'] = 0
        params['g_horror'] = 0
        params['g_shooter'] = 0
        params['g_firstperson'] = 0
        params['g_survival'] = 0
        params['g_turnbased'] = 0
        params['g_space'] = 0

        # validate input
        commandArr = command.split()
        if commandArr[1] == 'free':
            params['price'] = 0.00
        elif float(commandArr[1]) >= 0 and float(commandArr[1]) <= 80.00:
            params['price'] = round(float(commandArr[1]) / 80.00, 2)
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Price must be either 'free' or a number "
                                       f"between 0 and 80. You entered '{commandArr[1]}'.")
            return
        if commandArr[2].isnumeric() and int(commandArr[2]) >= 0 and int(commandArr[2]) <= 18:
            params['age_required'] = round(int(commandArr[2]) / 18, 2)
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Age restriction must be a number between 0 and 18. You entered '{commandArr[2]}'.")
            return
        if commandArr[3] == "false" or commandArr[3] == "true":
            if commandArr[3] == "false":
                params['dlc'] = 0
            else:
                params['dlc'] = 1
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: DLC availability must be a value of 'false' or 'true'. You entered '{commandArr[3]}'.")
            return
        if commandArr[4] == "false" or commandArr[4] == "true":
            if commandArr[4] == "false":
                params['achievements'] = 0
            else:
                params['achievements'] = 1
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Achievements availability must be a value of 'false' or 'true'. You entered '{commandArr[4]}'.")
            return
        if commandArr[5] == "false" or commandArr[5] == "true":
            if commandArr[5] == "false":
                params['windows'] = 0
            else:
                params['windows'] = 1
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Windows availability must be a value of 'false' or 'true'. You entered '{commandArr[5]}'.")
            return
        if commandArr[6] == "false" or commandArr[6] == "true":
            if commandArr[6] == "false":
                params['mac'] = 0
            else:
                params['mac'] = 1
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Mac availability must be a value of 'false' or 'true'. You entered '{commandArr[6]}'.")
            return
        if commandArr[7] == "false" or commandArr[7] == "true":
            if commandArr[7] == "false":
                params['linux'] = 0
            else:
                params['linux'] = 1
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Linux availability must be a value of 'false' or 'true'. You entered '{commandArr[7]}'.")
            return
        if params['linux'] == 0 and params['windows'] == 0 and params['mac'] == 0:
            await message.channel.send(
                f"<@{message.author.id}> Validation failed: You need to port to at least one platform, windows, linux, or mac. You entered false for all.")
            return
        if commandArr[8].isnumeric() and int(commandArr[8]) >= 0 and int(commandArr[8]) <= 12:
            params['release_month'] = round(int(commandArr[8]) / 12, 2)
        elif commandArr[8].startswith('jan') or commandArr[8].startswith('feb') or commandArr[8].startswith('mar') or commandArr[8].startswith('apr') or commandArr[8].startswith('may') or commandArr[8].startswith('jun') or commandArr[8].startswith('jul') or commandArr[8].startswith('aug') or commandArr[8].startswith('sep') or commandArr[8].startswith('oct') or commandArr[8].startswith('nov') or commandArr[8].startswith('dec'):
            if commandArr[8].startswith('jan'): params['release_month'] = 0.08
            if commandArr[8].startswith('feb'): params['release_month'] = 0.16
            if commandArr[8].startswith('mar'): params['release_month'] = 0.25
            if commandArr[8].startswith('apr'): params['release_month'] = 0.33
            if commandArr[8].startswith('may'): params['release_month'] = 0.41
            if commandArr[8].startswith('jun'): params['release_month'] = 0.50
            if commandArr[8].startswith('jul'): params['release_month'] = 0.58
            if commandArr[8].startswith('aug'): params['release_month'] = 0.66
            if commandArr[8].startswith('sept'): params['release_month'] = 0.75
            if commandArr[8].startswith('oct'): params['release_month'] = 0.83
            if commandArr[8].startswith('nov'): params['release_month'] = 0.91
            if commandArr[8].startswith('dec'): params['release_month'] = 1.00
        else:
            await message.channel.send(f"<@{message.author.id}> Validation failed: Month of release must be a value between [0, 12], [jan, dec], or [january, december]. You entered '{commandArr[8]}'.")
            return

        for i in commandArr[9:]:
            if i == "singleplayer" or i == "mmo" or i == "coop" or i == "inapppurchases" or i == "controllersupport" or i == "pvp":
                if i == "singleplayer": params['c_singleplayer'] = 1
                if i == "mmo": params['c_mmo'] = 1
                if i == "coop": params['c_coop'] = 1
                if i == "inapppurchases": params['c_inapppurchases'] = 1
                if i == "controllersupport": params['c_controllersupport'] = 1
                if i == "pvp": params['c_pvp'] = 1
            elif i == "adventure" or i == "casual" or i == "indie" or i == "simulation" or i == "action" or i == "multiplayer" or i == "rpg" or i == "racing" or i == "sports" or i == "2d" or i == "puzzle" or i == "racing" or i == "vr" or i == "platformer" or i == "horror" or i == "shooter" or i == "firstperson" or i == "survival" or i == "turnbased" or i == "space" or i == "strategy":
                if i == "adventure": params['g_adventure'] = 1
                if i == "casual": params['g_casual'] = 1
                if i == "indie": params['g_indie'] = 1
                if i == "simulation": params['g_simulation'] = 1
                if i == "action": params['g_action'] = 1
                if i == "multiplayer": params['g_multiplayer'] = 1
                if i == "rpg": params['g_rpg'] = 1
                if i == "strategy": params['g_strategy'] = 1
                if i == "racing": params['g_racing'] = 1
                if i == "sports": params['g_sports'] = 1
                if i == "2d": params['g_2d'] = 1
                if i == "puzzle": params['g_puzzle'] = 1
                if i == "vr": params['g_vr'] = 1
                if i == "platformer": params['g_platformer'] = 1
                if i == "horror": params['g_horror'] = 1
                if i == "shooter": params['g_shooter'] = 1
                if i == "firstperson": params['g_firstperson'] = 1
                if i == "survival": params['g_survival'] = 1
                if i == "turnbased": params['g_turnbased'] = 1
                if i == "space": params['g_space'] = 1
            else:
                await message.channel.send(f"<@{message.author.id}> Validation failed: Category or genre entered was not "
                                           f"an acceptable value. You entered '{i}'.")
                return

        # predict
        modelParameters = np.array([[params['price'], params['age_required'], params['dlc'], params['achievements'],
                                     params['windows'], params['mac'], params['linux'], params['release_month'],
                                     params['c_singleplayer'], params['c_mmo'], params['c_coop'],
                                     params['c_inapppurchases'], params['c_controllersupport'], params['c_pvp'],
                                     params['g_adventure'], params['g_casual'], params['g_indie'], params['g_simulation'],
                                     params['g_action'], params['g_multiplayer'], params['g_rpg'], params['g_strategy'],
                                     params['g_racing'], params['g_sports'], params['g_2d'], params['g_puzzle'],
                                     params['g_vr'], params['g_platformer'], params['g_horror'], params['g_shooter'],
                                     params['g_firstperson'], params['g_survival'], params['g_turnbased'],
                                     params['g_space']]], "float32")
        prediction = model.predict(modelParameters)[0][0]

        # send
        predictionPercent = round(prediction * 100, 2)
        await message.channel.send(f"<@{message.author.id}>\nI predict your game has a **{predictionPercent}%** chance of "
                                   f"success on the Steam market!\n"
                                   f"{'Is it too late to start over?' if predictionPercent < 50 else ''}"
                                   f"{'Consider making a few changes to improve your chances!' if predictionPercent >= 50 and predictionPercent < 70 else ''}"
                                   f"{'Your game has real potential! 👀' if predictionPercent >= 70 and predictionPercent < 90 else ''}"
                                   f"{'Ship it right now!! 📦' if predictionPercent >= 90 and predictionPercent <= 100 else ''}\n")

# connect to Discord
client.run(TOKEN)
