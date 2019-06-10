import urllib.request
from os import path
from datetime import datetime
from git import Repo


def get_current_ip():
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')


def check_update_required(ip):
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


def generate_lua(ip):
    lua = f'a("lexxxel.de", "{ip}")\n' \
        'cname("*.lexxxel.de", "tmhm3azy0r4qvauz.myfritz.net")'

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

    ip = get_current_ip()
    print('current ip: ', ip)

    if not check_update_required(ip):
        exit(0)

    generate_lua(ip)

    git_commit(update_time)

    save_set_ip(ip)
