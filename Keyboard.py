# commands for controlling various programs

from aenea import *

letterMap = {
    "able": "a",
    "brave": "b",
    "cave": "c",
    "dive": "d",
    "edge": "e",
    "fox": "f",
    "gauge": "g",
    "hatch": "h",
    "inch": "i",
    "jab": "j",
    "kick": "k",
    "lime": "l",
    "mike": "m",
    "noun": "n",
    "own": "o",
    "poke": "p",
    "queen": "q",
    "rome": "r",
    "sink": "s",
    "tank": "t",
    "unit": "u",
    "voice": "v",
    "whisk": "w",
    "X": "x",
    "year": "y",
    "zoo": "z",
}

symbolMap = {
    "spike": "bar",
    "grave": "backtick",
    "mine": "hyphen",
    "drop": "dot",
    "drip": "comma",
    "line": "backslash",
    "score": "underscore",
    "star": "asterisk",
    "coal": "colon",
    "soul": "semicolon",
    "loco": "at",
    "dark": "dquote",
    "mark": "squote",
    "pounder": "hash",
    "dolly": "dollar",
    "percy": "percent",
    "amper": "ampersand",
    "rhine": "slash",
    "quake": "equal",
    "plus": "plus",
    "clam": "exclamation",
    "quest": "question",
    "carrot": "caret",
    "tile": "tilde",
    "lang": "langle",
    "rang": "rangle",
    "lace": "lbrace",
    "race": "rbrace",
    "lack": "lbracket",
    "rack": "rbracket",
    "lent": "lparen",
    "rent": "rparen",
    "punch": "enter",
    "ace": "space",
    "torque": "tab",
    "up": "pgup",
    "down": "pgdown",
}

def formatSymbol(symbols, repeat, gap):
    format = "%(s)s:%(r)d"
    if gap == GapTypes.gap or gap == GapTypes.lap:
        format = "space, " + format
    if gap == GapTypes.gap or gap == GapTypes.rap:
        format = format + ", space"
    Key(format).execute({"s": symbols, "r": repeat})

def formatLetter(sky, letters, repeat, gap):
    format = "%(l)s:%(r)d"
    if gap == GapTypes.gap or gap == GapTypes.lap:
        format = "space, " + format
    if gap == GapTypes.gap or gap == GapTypes.rap:
        format = format + ", space"
    l = letters
    if sky:
        l = letters.upper()
    Key(format).execute({"l": l, "r": repeat})

keyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
    'insert': 'insert',
    'up': 'up',
    'down': 'down',
    'right': 'right',
    'left': 'left',
    'page up': 'pgup',
    'page down': 'pgdown',
}

repeatMap = {
  "wink": 2,
  "blink": 3,
  "squint": 4
}
 
class GapTypes:
    lap = 1
    rap = 2
    gap = 3
    none = 4

gapMap = {
    "leach": GapTypes.lap,
    "reach": GapTypes.rap,
    "each": GapTypes.gap,
}

skyMap = {
    "sky": True,
}

class KeyboardRule(MappingRule):
    mapping = {
        "[<sky>] <letters> [<repeat>] [<gap>]": Function(formatLetter),
        "<symbols> [<repeat>] [<gap>]": Function(formatSymbol),
        "count <num>": Text("%(num)d"),
        "<n>": Text("%(n)d"),
        "scratch [<n1>]": Key("backspace:%(n1)d"),
        "chuck [<n1>]": Key("delete:%(n1)d"),
        "clutch": Key("escape"),
        "key <key> [<n1>]": Key("%(key)s:%(n1)d"),
        "tram": Key("ctrl:down/3"),
        "shift": Key("shift:down/3"),
        "train": Key("alt:down/3"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 0, 100),
        IntegerRef("n1", 1, 30),
        IntegerRef("num", 0, 10000),
        Choice("letters", letterMap),
        Choice("symbols", symbolMap),
        Choice("key", keyMap),
        Choice("repeat", repeatMap),
        Choice("gap", gapMap),
        Choice("sky", skyMap),
    ]
    defaults = {
        "n": 1,
        "n1": 1,
        "repeat": 1,
        "gap": GapTypes.none,
        "sky": False,
    }
