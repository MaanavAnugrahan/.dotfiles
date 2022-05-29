# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$HOME/.local/bin:$PATH
export EDITOR=nvim

# Path to your oh-my-zsh installation.
#installation via script from github
#export ZSH="/home/$USER/.oh-my-zsh"
#installation via paru -S oh-my-zsh-git
export ZSH=/usr/share/oh-my-zsh/

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# if you installed the package oh-my-zsh-powerline-theme-git then you type here "powerline" as zsh theme
# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
ZSH_THEME=powerlevel10k/powerlevel10k
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

ZSH_THEME_RANDOM_IGNORED=(pygmalion tjkirch_mod)

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    zsh-completions
)

source $ZSH/oh-my-zsh.sh

# Uncomment the following line to use case-sensitive completion.
 CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
 DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
 DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable 
fm6000 -c green
#alsi
#paleofetch
#fetch
#hfetch
#sfetch
#ufetch
#ufetch-arco
#pfetch
#sysinfo
#sysinfo-retro
#cpufetch

# Alias
alias v="nvim"

# Taskwarrior aliases
# general commands
alias t="task"
alias ta="task add"
alias td="task done"
alias t-="task delete"
alias te="task edit"
alias tst="task start"
alias tm="task modify"
alias tu="task undo"
alias tv="vit rc.alias.next=list"
alias tw1="task modify wait:1d"
# alias tw2="task modify wait:2d"
# alias tw3="task modify wait:3d"
# alias tw1w="task modify wait:1w"
# alias tw2w="task modify wait:2w"
# alias tw3w="task modify wait:3w"
# alias tw1m="task modify wait:1m"
# alias tw2m="task modify wait:2m"
# alias tw3m="task modify wait:3m"

# context control
alias tc="task context"
alias tt="task rc.context=none"
alias ttv="vit rc.alias.next=list rc.context=none"
# alias tfoss="task rc.context=foss"
# alias thome="task rc.context=home"
# alias tmisc="task rc.context=misc"
# alias tfin="task rc.context=fin"
# alias tinc="task rc.context=inc"

# reports, in current context
alias tb="task burndown.daily"
alias tbw="task burndown.weekly"
alias tbm="task burndown.monthly"
alias tclosedtoday='t end:today all'
alias tdonetoday='t end:today status:completed all'
alias tl="clear; task list -BLOCKED"
alias tn="clear; task newest"
# list main categories (projects)
alias tp="task projects rc.list.all.projects=yes 2>/dev/null | grep -E '^\w'"
# list uncompleted projects
alias tpp="task projects"
# list all projects
alias tppp="task projects rc.list.all.projects=yes"
alias tr="clear; task +READY"
alias ts="task summary"
alias tss="task summary rc.summary.all.projects=yes"

# reports, ignoring current context
alias ttb="tt burndown.daily"
alias ttbw="tt burndown.weekly"
alias ttbm="tt burndown.monthly"
alias ttl="clear; tt list -BLOCKED"
alias ttp="tt projects rc.list.all.projects=yes 2>/dev/null | grep -E '^\w'"
alias ttpp="tt projects"
alias ttppp="tt projects rc.list.all.projects=yes"
alias ttr="clear; tt +READY"

# main categories
alias tadm="t project:adm"
alias tbiz="t project:biz"
alias tfam="t project:fam"
alias tfos="t project:fos"
alias tfri="t project~fr.$"
alias thom="t project:hom"
alias tinc="t project:inc"
alias tper="t project:per"
alias tser="t project:ser"

# misc.
alias twfeedback="t fe1226d4"  # taskwarrior feedback task
alias flog="t 5b343cc0"
alias ls="exa --icons"

export NNN_BMS="n:$HOME/notes;c:$HOME/.config;D:$HOME/Downloads/"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# To customize prompt, run `p10k configure` or edit ~/.dotfiles/zsh/.p10k.zsh.
[[ ! -f ~/.dotfiles/zsh/.p10k.zsh ]] || source ~/.dotfiles/zsh/.p10k.zsh
