#    This file is part of the Comp byressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

APP_ID = config("APP_ID", cast=int, default=3092338)
API_HASH = config("API_HASH", default="e81747974ab64a3617807b06bec1ac0a")
BOT_TOKEN = config("BOT_TOKEN", default="6979551576:AAFIV4rCqxrODoAfhd6SUxCPJ2LAVPI-Tr0")
DEV = 6748415360
CREATOR = config(
    "CREATOR",
    default=6748415360,
)
SUDO_USERS = config("SUDO_USERS", default=6748415360)
AUTH_CHATS = config("AUTH_CHATS", default=-1002110075889)
FFMPEG = []
try:
    ffmpeg = config("FFMPEG",)
    FFMPEG.insert(0, ffmpeg)
    if ffmpeg == "":
        raise KeyError
except KeyError:
    LOGS.warning("FFMPEG Externally Not Provided")
THUMB = config("THUMBNAIL", default='https://telegra.ph/file/6c477e9ac15d25f09ff99.jpg')
PING_CMD = config(
    "PING_CMD",
    default="ping",
)
HELP_CMD = config(
    "HELP_CMD",
    default="help",
)
LOG_CMD = config(
    "LOG_CMD",
    default="logs",
)
DL_CMD = config(
    "DL_CMD",
    default="dl",
)
START_CMD = config(
    "START_CMD",
    default="start",
)
ENCODE_CMD = config(
    "ENCODE_CMD",
    default="encode",
)
SET_FFMPEG = config(
    "SET_FFMPEG",
    default="setffmpeg",
)
GET_FFMPEG = config(
    "GET_FFMPEG",
    default="getffmpeg",
)
USAGE_CMD = config(
    "USAGE_CMD",
    default="usage",
)
SHOW_THUMB_CMD = config(
    "SHOW_THUMB_CMD",
    default="showthumb",
)
SAVE_THUMB_CMD = config(
    "SAVE_THUMB_CMD",
    default="savethumb",
)
SYSTEM_INFO = config(
    "SYSTEM_INFO",
    default="sysinfo",
)
RENEW_CMD = config(
    "RENEW_CMD",
    default="renew",
)
CLEAR_CMD = config(
    "CLEAR_CMD",
    default="clearqueue",
)

"""
except Exception as e:
    print("Environment Variable(s) Missing !!")
    print("Something Went Wrong !! RECHECK !!")
    print(str(e))
    exit()
"""
