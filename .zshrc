# Created by newuser for 5.9
autoload compinit
compinit -i

setopt autocd
HISTFILE=~/.cache/zsh/history
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/fzf-tab-git/fzf-tab.zsh

zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza -1 --color=always $realpath'

alias ls='ls --color=auto -a'
alias grep='grep --color=auto'
alias sudo='sudo -v; sudo'
export SUDO_PROMPT="$(tput setaf 3 bold)[sudo]$(tput sgr0)password for %p: "

eval "$(starship init zsh)"
eval "$(fzf --zsh)"

krabby random 7
