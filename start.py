# -*- coding: utf-8 -*-
import asyncio
import os
import socket
import botpy
import time
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message
from lz import myworld
test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
ban = "banlist.txt"
bir = "brirthday.txt"
shyaoq ="审核要求.txt"
with open(ban, "r", encoding='utf-8') as f:  #打开文本
    data = f.read()
with open("list.txt", "r", encoding='utf-8') as f:  #打开文本
    openlist = f.read()
with open(bir, "r", encoding='utf-8') as f:  #打开文本
    birthday = f.read()
with open(shyaoq, "r", encoding='utf-8') as f:  #打开文本
    shenghe = f.read()


class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message: GroupMessage):
        if "/help" in message.content:
            await message.reply(content = "指令帮助：\n/banlist 查看封禁列表\n/list 服务器公告（管理员）\n机器人制作者：TYW\n机器人制作者qq号：3671199392（乱加拉黑）")
        elif "/banlist" in message.content:
            await message.reply(content="封禁列表:\n" + data)
        elif "/list" in message.content:
            await message.reply(content=openlist)
        elif "/ban" in message.content:
            await message.reply(content="封禁成功")
        elif "/审核要求" in message.content:
            await message.reply(content=shenghe)
        elif "/birthday" in message.content:
            await message.reply(content=birthday)
        else:
            await message.reply(content="❌OOPS，请输入正确的指令，使用/help查看帮助")

intents = botpy.Intents(public_messages=True)
client = MyClient(intents=intents)
client.run(appid=test_config["appid"], secret=test_config["secret"])
