#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys
import subprocess
import getpass
import string
import json
import re
import time
import argparse
import zipfile
from io import BytesIO

from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.provider import APIProvider

try:
    import requests
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)


def readisdc():
    with open("master/isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes


def get_version():
    try:
        return open(".version", "r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():
	os.system('''
    printf "\n\e[1;32m▀█▀ █▀ █░█ █▄░█ ▄▀█ █▀▄▀█ █\n"
    printf "░█░ ▄█ █▄█ █░▀█ █▀█ █░▀░█ █\e[0m\n"
    printf "\e[31m═══════════════════════════\e[0m\n"
    printf "\e[31m\e[1;95mB O M B I N G   W E B A P P\n"
    printf "DEVELOPED BY UTSANJAN MAITY\e[0m\n"
    printf "\e[31m═══════════════════════════\e[0m\n"
        ''')


def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        print("Poor internet connection detected")
        sys.exit(2)


def format_phone(num):
    num = [n for n in num if n in string.digits]
    return ''.join(num).strip()


def do_zip_update():
    success = False
    if DEBUG_MODE:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/dev.zip"
        dir_name = "TBomb-dev"
    else:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/master.zip"
        dir_name = "TBomb-master"
    print(ALL_COLORS[0]+"Downloading ZIP ... "+RESET_ALL)
    response = requests.get(zip_url)
    if response.status_code == 200:
        zip_content = response.content
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.split(member)
                    if not filename[1]:
                        continue
                    new_filename = os.path.join(
                        filename[0].replace(dir_name, "."),
                        filename[1])
                    source = zip_file.open(member)
                    target = open(new_filename, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
            success = True
        except Exception:
            print("Error occured while extracting !!")
    if success:
        print("TBomb was updated to the latest version")
        print("Please run the script again to load the latest version")
    else:
        print("Unable to update TBomb.")

    sys.exit()


def do_git_update():
    success = False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL, end='')
        process = subprocess.Popen("git checkout . && git pull ",
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while process:
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except Exception:
        success = False

    if success:
        print("TBomb was updated to the latest version")
        print("Please run the script again to load the latest version")
    else:
        print("Unable to update TBomb.")
        print("Make Sure To Install 'git' ")
        print("Then run command:")
        print(
            "git checkout . && "
            "git pull https://github.com/TheSpeedX/TBomb.git HEAD")
    sys.exit()


def update():
    if shutil.which('git'):
        banner()
    else:
        banner()


def check_for_updates():
    fver = "2.1.2"
    if True:
      banner()
    else:
      banner()


def notifyen():
    try:
        if DEBUG_MODE:
            url = "https://github.com/TheSpeedX/TBomb/raw/dev/.notify"
        else:
            url = "https://github.com/TheSpeedX/TBomb/raw/master/.notify"
        noti = ""
    except Exception:
        pass

def get_phone_info():
    while True:
        target = ""
        banner()
        os.system(''' printf "\033[37;1m(Input appears after enter)\nEnter Victim's Country Code:\n" ''')
        cc = getpass.getpass("")

        # b = ""
        # for i in range(len(cc)):
        #   if (i%2)==0:
        #     b+=cc[i]
        # cc=b
      
        sys.stdout.write("\033[F")
        print("+"+cc)
      
        cc = format_phone(cc)
        if not country_codes.get(cc, False):
            clr()
            banner()
            print("Invalid Country Code...")
            continue
        os.system(''' printf "\033[37;1mEnter Victim's Phone No.:\n" ''')
        target = getpass.getpass("")
      
        # x = ""
        # for i in range(len(target)):
        #   if (i%2)==0:
        #     x+=target[i]
        # target=x
      
        sys.stdout.write("\033[F")
        print(target)
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            clr()
            banner()
            print("Invalid Phone Number...")
            continue
        return (cc, target)


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input("Enter target mail: ")
        if not re.search(mail_regex, target, re.IGNORECASE):
            print(
                "The mail ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    banner()
    requested = success+failed
    print("Victim     : +" + cc + " " + target)
    print("Requests   : " + str(requested))
    print("Success    : " + str(success))
    print("Failed     : " + str(failed))


def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)

    if len(APIProvider.api_providers) == 0:
        print("This Country isn't supported yet...")
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    print(
                        "Bombing limit for your target has been reached")
                    print("Try Again Later !!")
                    input("Press [ENTER] to exit")
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    print("Call Bombing Finished...")
    time.sleep(1.5)
    sys.exit()


def selectnode(mode="sms"):
    mode = mode.lower().strip()
    try:
        clr()
        notifyen()

        max_limit = {"sms": 500, "call": pow(10000,10000), "mail": 200}
        cc, target = "", ""
        if mode in ["sms", "call"]:
            cc, target = get_phone_info()
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                os.system(''' printf "\033[37;1mNow Enter the Call Count:\n" ''')
                count = getpass.getpass("")
              
                # z = ""
                # for i in range(len(count)):
                #   if (i%2)==0:
                #     z+=count[i]
                # count=z
              
                sys.stdout.write("\033[F")
                print(count)
                count=int(count)
                if count > limit or count == 0:
                    print("You have requested " + str(count)
                                            + " {type}".format(
                                                type=mode.upper()))
                    print(
                        "Automatically capping the value"
                        " to {limit}".format(limit=limit))
                    count = limit
                delay = 2.0
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = 1
                max_threads = max_threads if (
                    max_threads > 0) else max_thread_limit
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception:
                print("Read Instructions Carefully !!!")
                

        workernode(mode, cc, target, count, delay, max_threads)
    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit()


if sys.version_info[0] != 3:
    print("TBomb will work only in Python v3")
    sys.exit()

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    banner()


__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'Stefan']

ASCII_MODE = False
DEBUG_MODE = False

description = """TBomb - Your Friendly Spammer Application

TBomb can be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

TBomb is not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by SpeedX !!!')
parser.add_argument("-sms", "--sms", action="store_true",
                    help="start TBomb with SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true",
                    help="start TBomb with CALL Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                    help="start TBomb with MAIL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true",
                    help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                    help="update TBomb")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current TBomb contributors")
parser.add_argument("-v", "--version", action="store_true",
                    help="show current TBomb version")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
    if args.version:
        selectnode(mode="call")
    elif args.contributors:
        selectnode(mode="call")
    elif args.update:
        selectnode(mode="call")
    elif args.mail:
        selectnode(mode="call")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="call")
    else:
        choice = ""
        avail_choice = {
            "1": "SMS",
            "2": "CALL",
            "3": "MAIL"
        }
        try:
            while (choice not in avail_choice):
                clr()
                print("Available Options:\n")
                for key, value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,
                                                          value=value))
                choice = "2"
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            print("Stopping...")
            sys.exit()
    sys.exit()