
from pyrogram import filters
from userbot import UserBot
from userbot.helpers.PyroHelpers import GetChatID
from userbot.plugins.help import add_command_help

import socket

    # 21 – FTP
    # 22 – SSH
    # 25 – SMTP (sending email)
    # 53 – DNS (domain name service)
    # 80 – HTTP (web server)
    # 110 – POP3 (email inbox)
    # 123 – NTP (Network Time Protocol)
    # 143 – IMAP (email inbox)
    # 443 – HTTPS (secure web server)
    # 465 – SMTPS (send secure email)
    # 631 – CUPS (print server)
    # 993 – IMAPS (secure email inbox)
    # 995 – POP3 (secure email inbox)
    # 135   filtered msrpc


    # CPanel: 2082 or 2083(SSL)
    # CPanel Webmail: 2095 or 2096(SSL)
    # WHM: 2086 or 2087(SSL)


SUCCESS = 0

@UserBot.on_message(filters.me & filters.text & filters.command("scan","."))
async def send_all(client, message):
    cmd = message.command
    doamin = cmd[1]
    try:
        ip = socket.gethostbyname(doamin)
    except:
        ip = doamin
    print(str(doamin) + " ip is " + str(ip))
    ports = [21,22,23,25,53,80,110,123,135,139,143,443,8080,445,465,631,993,995,1027,2082,2083,2095,2096,2086,2087,9898,8888]
    m = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="\tScaning Started")

    try:
        for port in ports:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # socket.setdefaulttimeout(1)
            s.settimeout(2)
            status = s.connect_ex((ip,port))
            if status == 0:
                print(str(port) + " is open")
                print(status)
                try:
                    text = m.text
                    m = await m.edit(text + "\n\n" + str(port) + "/tcp is Open")
                except Exception as error:
                    if "you tried to edit it using the same content" in str(error):
                        continue
                    else:
                        print(text + " + " + str(port))
                        print(error)
                        continue
            s.close()
    except socket.error as error:
        await m.edit(str(error))
        s.close()

    except socket.gaierror as error:
        await m.edit(str(error))
        s.close()
    await m.reply("finished Scanning")

add_command_help(

    "hackers",
    [
        [
            ".scan",
            "Simple Open Port Scanner\nUsage: ``.scan <domain/ip>``",
        ],
    ],
)
