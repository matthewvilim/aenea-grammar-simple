from aenea import *

class VimRule(MappingRule):
    prefix = "(vim|them) "
    mapping = {
        prefix + "save": Text(":w\n"),
        prefix + "force save": Text(":w!\n"),
        prefix + "quit": Text(":q\n"),
        prefix + "save and quit": Text(":x\n"),
        prefix + "force quit": Text(":q!\n"),
        prefix + "vertical split": Text(":vs "),
        prefix + "no highlight": Text(":noh\n"),
        "less [<n>]": Key("c-u:%(n)d"),
        "more [<n>]": Key("c-d:%(n)d"),
        "switch": Key("c-w, w"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 10),
    ]
    defaults = {
      "n": 1,
    }
