import os
from subprocess import call
from time import sleep

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

clear()
os.system('''
printf "\e[1;32m\n\n\n\n\n      ██░ ██  ██▓\n";   
printf "      ▓██░ ██▒▓██▒\n"; 
printf "      ▒██▀▀██░▒██▒\n";   
printf "      ░▓█ ░██ ░██░\n";   
printf "      ░▓█▒░██▓░██░\n";   
printf "       ▒ ░░▒░▒░▓  \n";   
printf "       ▒ ░▒░ ░ ▒ ░\n";   
printf "       ░  ░░ ░ ▒ ░\n";   
printf "       ░  ░  ░ ░\n";
''')
sleep(1.5)
clear()
os.system('''
printf "\e[1;32m\n\n\n\n\n    ██░ ██  ▒█████   █     █░\n";
printf "   ▓██░ ██▒▒██▒  ██▒▓█░ █ ░█░\n";
printf "   ▒██▀▀██░▒██░  ██▒▒█░ █ ░█ \n";
printf "   ░▓█ ░██ ▒██   ██░░█░ █ ░█ \n";
printf "   ░▓█▒░██▓░ ████▓▒░░░██▒██▓ \n";
printf "    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▓░▒ ▒  \n";
printf "    ▒ ░▒░ ░  ░ ▒ ▒░   ▒ ░ ░  \n";
printf "    ░  ░░ ░░ ░ ░ ▒    ░   ░  \n";
printf "    ░  ░  ░    ░ ░      ░    \n";
''')
sleep(1.5)
clear()  
os.system('''
printf "\e[1;32m\n\n\n\n\n     ▄▄▄       ██▀███  ▓█████ \n";
printf "   ▒████▄    ▓██ ▒ ██▒▓█   ▀ \n";
printf "   ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   \n";
printf "   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ \n";
printf "    ▓█   ▓██▒░██▓ ▒██▒░▒████▒\n";
printf "    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░\n";
printf "     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░\n";
printf "     ░   ▒     ░░   ░    ░   \n";
printf "         ░  ░   ░        ░  ░\n";
''')
sleep(1.5)
clear()
os.system('''
printf "\e[1;32m\n\n\n\n\n   ▓██   ██▓ ▒█████   █    ██ \n";
printf "    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒\n";
printf "     ▒██ ██░▒██░  ██▒▓██  ▒██░\n";
printf "      ░ ██▒▓░░ ████▓▒░▒▒█████▓\n";
printf "       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ \n";
printf "     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ \n";
printf "      ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░ \n";
printf "      ░ ░         ░ ░     ░\n";
printf "       ░ ░\n";
''')
sleep(1.5)
clear()
os.system('''
printf "\n\n\n\n\n\e[31m   █▀ ▄▀█ ▀█▀ ▄▀█ █▄░█ \n";
printf "   ▄█ █▀█ ░█░ █▀█ █░▀█ \n\n";
printf "          _____   \n";
printf "         /     \  \n";
printf "        | () () | \n";
printf "         \  ^  /  \n";
printf "          |||||   \n";
printf "          |||||   \n";
''')
sleep(1.5)
clear()
os.system('python main.py')