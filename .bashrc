#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

shopt -s autocd

alias ls='ls --color=auto -a'
alias grep='grep --color=auto'
alias sudo='sudo -v; sudo'
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\h \[$(tput setaf 5)\]\W\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"
export TERM="xterm-256color"

source /usr/share/bash-completion/bash_completion

export SUDO_PROMPT="$(tput setaf 3 bold)[sudo]$(tput sgr0)password for %p: "
LS_COLORS='di=1;35:fi=0:ln=31:pi=5:so=5:bd=5:cd=5:or=31:mi=0:ex=35:*.rpm=90:*.png=35:*.gif=36:*.jpg=35:*.c=92:*.jar=33:*.py=93:*.h=90:*.txt=94:*.doc=104:*.docx=104:*.odt=104:*.csv=102:*.xlsx=102:*.xlsm=102:*.rb=31:*.cpp=92:*.sh=92:*.html=96:*.zip=4;33:*.tar.gz=4;33:*.mp4=105:*.mp3=106'
export LS_COLORS
