# commands for controlling various programs

from aenea import *

gitCommandArray = [
    'add',
    'branch',
    'checkout',
    'clean',
    'clone',
    'commit',
    'diff',
    'difftool',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'submodule',
    'tag',
    'remote',
]
gitCommand = {}
for command in gitCommandArray:
    gitCommand[command] = command

tmuxCommand= {
    'new': 'new',
    'list': 'ls',
    'attach': 'attach',
    'detach': 'detach',
    'kill session': 'kill-session',
}

sbtCommand= {
    'test': 'test',
    'compile': 'compile',
    'clean': 'clean',
}

aptCommandArray = [
    'update',
    'install',
    'remove',
]
aptCommand = {}
for command in aptCommandArray:
    aptCommand[command] = command

def directoryUp(n=1):
    command = "cd "
    s = "../"
    for i in range(0, n):
        command = command + s
    Text("%(command)s").execute({"command": command})

class TerminalRule(MappingRule):
    prefix = "shell "
    mapping = {
        prefix + "sudo": Text("sudo "),
        prefix + "apt <aptCommand>": Text("apt %(aptCommand)s "),
        prefix + "(them|vim)": Text("vim "),
        prefix + "direct": Text("cd "),
        prefix + "direct up [<n>]": Function(directoryUp),
        prefix + "copy": Text("cp "),
        prefix + "cat": Text("cat "),
        prefix + "list": Text("ls "),
        prefix + "make": Text("make "),
        prefix + "manual": Text("man "),
        prefix + "mutt": Text("mutt "),
        prefix + "(grep|grip)": Text("grep "),
        prefix + "move": Text("mv "),
        prefix + "remove": Text("rm "),
        prefix + "make direct": Text("mkdir "),
        prefix + "remove direct": Text("rmdir "),
        prefix + "(git|get) <gitCommand>": Text("git %(gitCommand)s "),
        prefix + "see tags": Text("ctags"),
        prefix + "tea (mucks|box|monks) <tmuxCommand>": Text("tmux %(tmuxCommand)s "),
        prefix + "mount": Text("mount "),
        prefix + "umount": Text("umount "),
        prefix + "i three message": Text("i3-msg "),
        prefix + "SSH": Text("ssh "),
        prefix + "exit": Text("exit"),
        prefix + "change mode": Text("chmod "),
        prefix + "VPN": Text("vpn"),
        prefix + "less": Text("less "),
        prefix + "GTK wave": Text("gtkwave "),
        prefix + "SBT <sbtCommand>": Text("sbt %(sbtCommand)s "),
        prefix + "ping": Text("ping "),
        prefix + "working directory": Text("pwd "),
        prefix + "Z shell": Text("zsh "),
        prefix + "secure copy": Text("scp "),
        prefix + "PDF latex": Text("pdflatex "),
        prefix + "bibtex": Text("bibtex "),
        prefix + "bash": Text("bash "),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 8),
        Choice('aptCommand', aptCommand),
        Choice('gitCommand', gitCommand),
        Choice('tmuxCommand', tmuxCommand),
        Choice('sbtCommand', sbtCommand),
    ]
    default = {
        "n": 1,
    }
