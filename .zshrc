# Created by newuser for 5.9
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

export EDITOR="nvim"
alias ls='ls --color'

setopt autocd

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

source /usr/share/zsh/plugins/zsh-auto-notify/auto-notify.plugin.zsh
source /usr/share/zsh/plugins/zsh-you-should-use/you-should-use.plugin.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh/plugins/fzf-tab-git/fzf-tab.zsh

fpath=(/usr/share/zsh/functions $fpath)
autoload -Uz compinit
compinit

eval "$(fzf --zsh)"
eval "$(starship init zsh)"
