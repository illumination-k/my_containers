### Set up the prompt ###
autoload -Uz promptinit
promptinit
prompt adam1
setopt histignorealldups sharehistory
### Keep 1000 lines of history within the shell and save it to ~/.zsh_history: ###
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history
#### Use modern completion system ###
autoload -Uz compinit
compinit
zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'
### color ###
autoload -Uz colors ; colors
# --------------------------------------------------
#  カレントディレクトリ表示（左）
# --------------------------------------------------
PROMPT='
%F{green}%(5~,%-1~/.../%2~,%~)%f
%F{green}%B●%b%f'
# --------------------------------------------------
#  git branch状態を表示（右）
# --------------------------------------------------
autoload -Uz vcs_info
setopt prompt_subst
# true | false
# trueで作業ブランチの状態に応じて表示を変える
zstyle ':vcs_info:*' check-for-changes false
# addしてない場合の表示
zstyle ':vcs_info:*' unstagedstr "%F{red}%B＋%b%f"
# commitしてない場合の表示
zstyle ':vcs_info:*' stagedstr "%F{yellow}★ %f"
# デフォルトの状態の表示
zstyle ':vcs_info:*' formats "%u%c%F{green}【 %b 】%f"
# コンフリクトが起きたり特別な状態になるとformatsの代わりに表示
zstyle ':vcs_info:*' actionformats '【%b | %a】'
precmd () { vcs_info }
RPROMPT=$RPROMPT'${vcs_info_msg_0_}'
### option ###
# cdなしで移動
setopt auto_cd
function chpwd() { ls -a --color }
# ()を自動補完
setopt auto_param_keys
# コマンドのスペルチェック
setopt correct
### env ###
# 言語設定
export LANG=ja_JP.UTF-8
# 色の設定
export LSCOLORS=Exfxcxdxbxegedabagacad
export LS_COLORS='di=01;34:ln=01;35:so=01;32:ex=01;31:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'
### ailias ###
alias ls="ls --color"
alias la="ls -a --color"
alias tree="pwd;find . | sort | sed '1d;s/^\.//;s/\/\([^/]*\)$/|--\1/;s/\/[^/|]*/| /g'"
# git関連
alias ga="git add ."
alias gc="git commit -m"
alias gpush="git push -u origin"
alias gpull="git pull origin"
alias gfetch="git fetch"
alias gmerge='git merge'
### その他設定 ###
# タブに名前を付ける
function tab_rename() {
    BUFFER="echo -ne \"\e]1;"
    CURSOR=$#BUFFER
    BUFFER=$BUFFER\\a\"
}




