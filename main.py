#Discord bot for playing music
#author: @gpank1

#Discord library
#Communicates with Discord API, handles events, command parsing and execution, voice channel connectivity
import discord
from discord.ext import commands
#Handles everything related to retrieving audio
#Searching YouTube for songs
#Fetching video metadata
#Downloading audio streams
#Converts video formats to audio formats
#Supports various video platforms beyond YouTube
import youtube_dl
#Manages timeouts for asynchronous operations
#Helps prevent the bot from getting stuck if operations take too long
#Used for timing out voice connections and downloads
import asyncio
from async_timeout import timeout
import functools
import itertools
import math
import random