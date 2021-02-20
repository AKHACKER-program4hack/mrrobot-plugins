# MR.ROBOT Userbot
![Python Version](https://img.shields.io/badge/Python-v3.9-blue)
[![Join Group](https://img.shields.io/badge/Telegram-Join%20Group-informational)](https://t.me/program4hack)
[![HitCount](http://hits.dwyl.com/AKHACKER-program4hack/mrrobot-plugins.svg)](http://hits.dwyl.com/AKHACKER-program4hack/mrrobot-plugins)
![Last Commit](https://img.shields.io/github/last-commit/AKHACKER-program4hack/mrrobot-plugins/main)
![Issues](https://img.shields.io/github/issues/AKHACKER-program4hack/mrrobot-plugins)
![Pull Requests](https://img.shields.io/github/issues-pr/AKHACKER-program4hack/mrrobot-plugins)

<img src="https://telegra.ph/file/0549cdcecfadeab0dfd40.jpg" width="160" align="right">

> MR.ROBOT Plugins [MR.Robot](https://github.com/AKHACKER-program4hack/mrrobot)

This repository contains the source code of plugins of Telegram Userbot MR.ROBOT and the instructions for running a
copy yourself. Beside its main purpose, the bot is featuring [**Pyrogram Asyncio**](https:////github.com/pyrogram/pyrogram/issues/181) and
[**Smart Plugins**](https://docs.pyrogram.org/topics/smart-plugins); feel free to explore the source code to
learn more about these topics.

I assume you will read this whole README.md file before continuing.

## Installing

*how to install plugins in MR.Robot* :

<details>
  <summary> Video Tutorial </summary>

```
Official YouTube Channel Of MR.Robot Owner.
Click on the link below to get tutorial on 
How To Deploy MR.Robot.
```
<a href="https://youtu.be/BCBhoLJzz6w"><img src="https://img.shields.io/badge/How%20To%20Install%20plugins-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/BCBhoLJzz6w"><img src="https://img.shields.io/youtube/views/BCBhoLJzz6w?style=social"></a>

</details>

Reply to the plugin file

```bash
.download
```
After Downloading the file 

check the file in your download directory and copy the name

```
.ls downloads
```
After copying the name of the file you have to type

```
.load_plugin <plugin name with extention>
```
For Example 
```
.load_plugin portscanner.py
```
After Loading plugin you want to restart using this command :

```
.restart
```


## Developing
```python
from pyrogram import filters

from userbot import UserBot

@UserBot.on_message(filters.command('sample', ['.']))
async def module_name(client, message):
    await message.edit(
        "This is a sample module"
    )
```

This example is only for Pyrogram on_message events. 

## Credits, and Thanks to

*  [AKHACKER](https://github.com/AKHACKER-program4hack) Owner Of the Userbot. 

---


