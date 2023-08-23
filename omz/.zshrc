# Include local scripts in PATH
export PATH="/home/oscarm3615/.local/bin:$PATH"

# Path to your oh-my-zsh installation.
export ZSH="/home/oscarm3615/.oh-my-zsh"

ZSH_THEME="oscarm3615"

# Uncomment the following line if pasting URLs and other text is messed up.
DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable auto-setting terminal title.
DISABLE_AUTO_TITLE="true"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
	git
	zsh-autosuggestions
	zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# Deno path
export DENO_INSTALL="/home/oscarm3615/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# Highlight theme (for ranger)
export HIGHLIGHT_STYLE=base16/onedark

# Default editor
export EDITOR='vim'

# Fuzzy files args
export FZF_DEFAULT_OPTS="--preview 'bat --color=always --style=numbers --line-range=:500 {}'"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
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

# Activate NVM
source /usr/share/nvm/init-nvm.sh
