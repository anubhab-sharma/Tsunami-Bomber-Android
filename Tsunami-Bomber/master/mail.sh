#!/bin/bash
detect_distro() {
    if [[ "$OSTYPE" == linux-android* ]]; then
            distro="termux"
    fi
    if [ -z "$distro" ]; then
        distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] != "os") {print groups[1]}}')
    fi
    if [ -z "$distro" ]; then
        if [ -f "/etc/os-release" ]; then
            distro="$(source /etc/os-release && echo $ID)"
        elif [ "$OSTYPE" == "darwin" ]; then
            distro="darwin"
        else 
            distro="invalid"
        fi
    fi
}

banner() {
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
    echo ' '
    fi
    echo ''
}

init_environ(){
    declare -A backends; 
        backends=(
        ["arch"]="pacman -S --noconfirm"
        ["debian"]="apt-get -y install"
        ["ubuntu"]="apt -y install"
        ["termux"]="apt -y install"
        ["fedora"]="yum -y install"
        ["redhat"]="yum -y install"
        ["SuSE"]="zypper -n install"
        ["sles"]="zypper -n install"
        ["darwin"]="brew install"
        ["alpine"]="apk add"
        )

    INSTALL="${backends[$distro]}"

    if [ "$distro" == "termux" ]; then
        PYTHON="python"
        SUDO=""
    else
        PYTHON="python3"
        SUDO="sudo"
    fi
    PIP="$PYTHON -m pip"
}

set_alias(){
    if [ "$distro" == "termux" ]; then
        cd;cd ..;cd usr;cd etc
	if grep -q "bomb" bash.bashrc; then
	    echo "Found...Skipping"
	    sleep 2
	    clear
	else    
	    echo 'alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";' >> bash.bashrc
	    echo 'clear' >> bash.bashrc
	    echo 'PS1="\033[1;91mRoot[\033[1;93m\W\033[1;91m]:-\033[1;36m"' >> bash.bashrc
	    alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";
	    clear
        fi
    else
        if grep -q "bomb" /root/.bashrc; then
	    echo "Found...Skipping"
	    sleep 2
	    clear
	else
            echo ' ' >> /root/.bashrc
	    echo 'alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";' >> /root/.bashrc
	    alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";
        fi	    
    fi
}

detect_distro
init_environ
if [ -f .update ];then
    echo ""
else
    echo ''
    echo .
    echo .
    $PYTHON version_check.py || $PYTHON core/version_check.py
    echo '' > .update
    set_alias
fi
while :
do
    banner
    cd core
        $PYTHON ./master/Core/bomber.py --mail
        exit
done