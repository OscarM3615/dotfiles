# Include local scripts in PATH
export PATH="/home/oscarm3615/.local/bin:$PATH"

# Path to your oh-my-zsh installation.
export ZSH="/home/oscarm3615/.oh-my-zsh"

# Oh My ZSH options
ZSH_THEME="oscarm3615"
DISABLE_MAGIC_FUNCTIONS="true"
DISABLE_AUTO_TITLE="true"

export FZF_DEFAULT_OPTS="--preview 'bat --color=always --style=numbers --line-range=:500 {}'"

plugins=(git)

source $ZSH/oh-my-zsh.sh

# Additional options
export HIGHLIGHT_STYLE=base16/onedark
export EDITOR='vim'

# Aliases
alias ls="lsd"
alias tree="lsd --tree"
alias lgit="lazygit"

unsetopt PROMPT_CR PROMPT_SP

function cd() {
	builtin cd $1

	if [[ -d ./venv ]]; then
		source venv/bin/activate
	fi
}

# Source external files
source /usr/share/nvm/init-nvm.sh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
