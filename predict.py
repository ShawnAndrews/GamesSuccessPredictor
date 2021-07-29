# Description: Make a neural network classification given a trained model and input parameters.

import sys
import numpy as np
from keras.models import load_model

if len(sys.argv) < 3:
    sys.exit(-1)

# load model and weights
model = load_model("model")

# prepare arguments
args = sys.argv[2:]
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

if args[0] == 'free':
    params['price'] = 0.00
elif float(args[0]) >= 0 and float(args[0]) <= 80.00:
    params['price'] = round(float(args[0]) / 80.00, 2)
else:
    print(f"Validation failed: Price must be either 'free' or a number "
          f"between 0 and 80. You entered '{args[0]}'.")
    sys.exit(-1)
if args[1].isnumeric() and int(args[1]) >= 0 and int(args[1]) <= 18:
    params['age_required'] = round(int(args[1]) / 18, 2)
else:
    print(f"Validation failed: Age restriction must be a number between 0 and 18. You entered '{args[1]}'.")
    sys.exit(-1)
if args[2] == "false" or args[2] == "true":
    if args[2] == "false":
        params['dlc'] = 0
    else:
        params['dlc'] = 1
else:
    print(f"Validation failed: DLC availability must be a value of 'false' or 'true'. You entered '{args[2]}'.")
    sys.exit(-1)
if args[3] == "false" or args[3] == "true":
    if args[3] == "false":
        params['achievements'] = 0
    else:
        params['achievements'] = 1
else:
    print(
        f"Validation failed: Achievements availability must be a value of 'false' or 'true'. You entered '{args[3]}'.")
    sys.exit(-1)
if args[4] == "false" or args[4] == "true":
    if args[4] == "false":
        params['windows'] = 0
    else:
        params['windows'] = 1
else:
    print(f"Validation failed: Windows availability must be a value of 'false' or 'true'. You entered '{args[4]}'.")
    sys.exit(-1)
if args[5] == "false" or args[5] == "true":
    if args[5] == "false":
        params['mac'] = 0
    else:
        params['mac'] = 1
else:
    print(f"Validation failed: Mac availability must be a value of 'false' or 'true'. You entered '{args[5]}'.")
    sys.exit(-1)
if args[6] == "false" or args[6] == "true":
    if args[6] == "false":
        params['linux'] = 0
    else:
        params['linux'] = 1
else:
    print(f"Validation failed: Linux availability must be a value of 'false' or 'true'. You entered '{args[6]}'.")
    sys.exit(-1)
if params['linux'] == 0 and params['windows'] == 0 and params['mac'] == 0:
    print(f"Validation failed: You need to port to at least one platform, windows, linux, or mac. You entered false "
          f"for all.")
    sys.exit(-1)
if args[7].isnumeric() and int(args[7]) >= 0 and int(args[7]) <= 12:
    params['release_month'] = round(int(args[7]) / 12, 2)
elif args[7].startswith('jan') or args[7].startswith('feb') or args[7].startswith('mar') or args[7].startswith('apr') or \
        args[7].startswith('may') or args[7].startswith('jun') or args[7].startswith('jul') or args[7].startswith(
        'aug') or args[7].startswith('sep') or args[7].startswith('oct') or args[7].startswith('nov') or args[
    7].startswith('dec'):
    if args[7].startswith('jan'): params['release_month'] = 0.08
    if args[7].startswith('feb'): params['release_month'] = 0.16
    if args[7].startswith('mar'): params['release_month'] = 0.25
    if args[7].startswith('apr'): params['release_month'] = 0.33
    if args[7].startswith('may'): params['release_month'] = 0.41
    if args[7].startswith('jun'): params['release_month'] = 0.50
    if args[7].startswith('jul'): params['release_month'] = 0.58
    if args[7].startswith('aug'): params['release_month'] = 0.66
    if args[7].startswith('sept'): params['release_month'] = 0.75
    if args[7].startswith('oct'): params['release_month'] = 0.83
    if args[7].startswith('nov'): params['release_month'] = 0.91
    if args[7].startswith('dec'): params['release_month'] = 1.00
else:
    print(
        f"Validation failed: Month of release must be a value between [0, 12], [jan, dec], or [january, december]. You entered '{args[7]}'.")
    sys.exit(-1)

for i in args[8:]:
    if i == "singleplayer" or i == "mmo" or i == "coop" or i == "inapppurchases" or i == "controllersupport" or i == "pvp":
        if i == "singleplayer": params['c_singleplayer'] = 1
        if i == "mmo": params['c_mmo'] = 1
        if i == "coop": params['c_coop'] = 1
        if i == "inapppurchases": params['c_inapppurchases'] = 1
        if i == "controllersupport": params['c_controllersupport'] = 1
        if i == "pvp": params['c_pvp'] = 1
    elif i == "adventure" or i == "casual" or i == "indie" or i == "simulation" or i == "action" or i == "multiplayer" or i == "rpg" or i == "racing" or i == "sports" or i == "2d" or i == "puzzle" or i == "racing" or i == "vr" or i == "platformer" or i == "horror" or i == "shooter" or i == "firstperson" or i == "survival" or i == "turnbased" or i == "space":
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
        print(f"Validation failed: Category or genre entered was not "
              f"an acceptable value. You entered '{i}'.")
        sys.exit(-1)

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

sys.exit(prediction)
