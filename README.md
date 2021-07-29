<h1 align="center">
  <br>
  <a href="https://i.imgur.com/rYvoOls.png"><img src="https://i.imgur.com/rYvoOls.png" alt="logo" width="200"></a>
  <br>
  Games Success Predictor (GSP)
  <br>
</h1>

<h4 align="center">This project is a 3-layer Feed Forward Neural Network (FFNN) that trains on the success and parameters of video games in the <a href="https://store.steampowered.com/" target="_blank">Steam</a> library to predict the future success of your game!</h4>

<p align="center">
  <a href="https://discord.gg/SparkleParty">
        <img src="https://img.shields.io/discord/377121551104999424?logo=discord" alt="Discord"></a>
  <a href="https://github.com/ShawnAndrews/GamesSuccessPredictor" alt="GitHub release">
        <img src="https://img.shields.io/github/release/shawnandrews/GamesSuccessPredictor.svg" /></a>
    <a href="https://github.com/ShawnAndrews/GamesSuccessPredictor/blob/master/LICENSE" alt="GitHub license">
        <img src="https://img.shields.io/github/license/shawnandrews/GamesSuccessPredictor.svg" /></a>
</p>

<p align="center">
  <a href="#how-to-use">How To Use</a> •
  <a href="#neural-network">Neural Network</a> •
  <a href="#discords">Discords</a> •
  <a href="#faq">FAQ</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://i.imgur.com/30RdwKe.gif)

## Key Features

* Help determine the best month to release your game
* Help find the best price point for your game to sell as many copies as possible
* Help choose if it is worth the effort to port your game to other platforms
* Help weigh the benefits of additional features such a controller and VR support
* Help influence the direction of your game in terms of genres
* Help pick the gameplay modes such as pvp, singleplayer, or multiplayer
* Help decide the advantage of adding an achievements system
* Help gauge the value of Downloadable Content (DLC)
* Help choose whether an age restriction will negatively or positively effect the success of your game

## Neural Network

The tensorflow artificial neural network is comprised of 3 dense layers and 1225 total parameters.

<a href="https://i.imgur.com/BVxK2fZ.png"><img src="https://i.imgur.com/BVxK2fZ.png" alt="visual"></a>

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 34)                0
_________________________________________________________________
dense (Dense)                (None, 25)                875       
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 26        
=================================================================
Total params: 1225
Trainable params: 1225
Non-trainable params: 0
_________________________________________________________________
```

## How To Use

Pre-requisite: You must install both Discord.py and Tensorflow for Python. Additional installs needed to allow GPU-accelerated training.

```python
# Train on CSV training data file "TrainingData.txt" and output model with weights to a folder "model"
$ python train.py csvData.txt model

# Perform a prediction given a loaded model and game information
$ python predict.py model free 0 true false true true true december multiplayer mmo controllersupport horror survival

# Start Discord bot
$ python bot.py model DISCORD_BOT_TOKEN_KEY
```

Note: If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## Discords

Here is a list of discords with the bot currently active:

<a href="https://discord.gg/SparkleParty">
        <img src="https://img.shields.io/discord/377121551104999424?logo=discord" alt="Discord"></a>

Get the bot to join your discord today! [Click here](https://discord.gg)


## FAQ

**Question:** Where is the training data?

**Answer:** The Steam data was intentionally excluded from the project. To create the training data you'll need to scrape the game and review data from the Steam API, then write the records to a text file in the specified CSV format.

## License

MIT
