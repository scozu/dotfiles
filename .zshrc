# ~~~ Prompt ~~~
autoload -U promptinit; promptinit

zmodload zsh/nearcolor
zstyle :prompt:pure:git:dirty color '#c1c1c1'

prompt pure


# ~~~ Bun ~~~

# bun completions
[ -s "/Users/scozu/.bun/_bun" ] && source "/Users/scozu/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

# boot.dev testing
export PATH="$PATH:/Users/scozu/worldbanc/private/bin"


# Generated for envman. Do not edit.
[ -s "$HOME/.config/envman/load.sh" ] && source "$HOME/.config/envman/load.sh"
