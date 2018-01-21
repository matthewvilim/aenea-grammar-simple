from aenea import *

class TMuxRule(MappingRule):
    prefix = "tea "
    tmuxPrefix = "c-b"
    mapping = {
        "(" + prefix + "next" + "|nose)": Key(tmuxPrefix + ", n"),
        "(" + prefix + "previous" + "|pose)": Key(tmuxPrefix + ", p"),
        prefix + "new": Key(tmuxPrefix + ", c"),
        prefix + "kill": Key(tmuxPrefix + ", x"),
        prefix + "detach": Key(tmuxPrefix + ", d"),
        prefix + "<n>": Key(tmuxPrefix + ", %(n)d"),
        prefix + "pains": Key(tmuxPrefix + ", q"),
        prefix + "pain <n>": Key(tmuxPrefix + ", q, %(n)d"),
        prefix + "max": Key(tmuxPrefix + ", z"),
        prefix + "vertical split": Key(tmuxPrefix + ", dquote"),
        prefix + "horizontal split": Key(tmuxPrefix + ", percent"),
        "(" + prefix + "switch" + "|toes)": Key(tmuxPrefix + ", o"),
        prefix + "scroll": Key(tmuxPrefix + ", lbracket"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 0, 5),
    ]
    defaults = {
        "n": 1,
    }
