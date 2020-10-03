#!/usr/bin/env python3

import urllib.request
from urllib.error import URLError
from os import path
from datetime import datetime
from git import Repo


def get_current_ip():
    try:
      ip4 = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
    except URLError:
      ip4 = None
    #try:
    #  ip6 = urllib.request.urlopen('https://v6.ident.me').read().decode('utf8')
    #except URLError:
    ip6 = None
    return ip4, ip6


def check_update_required(ip):
    if ip is None:
        print("don't know current ip!")
        return False

    if path.exists("lastIp.txt"):
        saveIp = open('lastIp.txt', 'r')
        lastIpAddr = saveIp.read()
    else:
        lastIpAddr = ""

    print("----------------------------------------")
    print("")
    print("last ip: ", lastIpAddr)
    print("external ip: ", ip)

    if lastIpAddr == ip:
        print("ip is already set correctly!")
        return False

    return True


def save_set_ip(ip):
    with open('lastIp.txt', 'w') as saveIp:
        saveIp.write(ip)


def generate_lua(ip4, ip6):
    lua = ""
    if ip4:
      lua += f'a("lexxxel.de", "{ip4}")\n'
    if ip6:
      lua += f'aaaa("lexxxel.de", "{ip6}")\n'

    lua += 'cname("*.lexxxel.de", "p1rmcfy9s5tbijab.myfritz.net")\n'

    with open("./lexxxel.de.lua", "w") as file:
        file.write(lua)


def git_commit(message):
    repo = Repo(".")
    repo.git.add("lexxxel.de.lua")
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()


if __name__ == "__main__":

    print("##################################################################################")
    update_time = f'DNS: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    print(update_time)
    run_local = False

    ip4, ip6 = get_current_ip()
    print('current ip: ', ip4, ip6)

    if not check_update_required(ip4):
        exit(0)

    generate_lua(ip4, ip6)

    git_commit(update_time)

    save_set_ip(ip4)
