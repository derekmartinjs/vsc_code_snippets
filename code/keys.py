from typing import Set

from talon import Module, Context, actions
import sys

default_alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split(
  " "
)
letters_string = 'abcdefghijklmnopqrstuvwxyz'

default_digits = 'zero one two three four five siz seven eight nine'.split(' ')
numbers = [str(i) for i in range(10)]
default_f_digits = 'one two three four five six seven eight nine ten eleven twelve'.split(' ')

mod = Module()
mod.list('letter', desc="The spoken phonetic alphabet")
mod.list('symbol_key', desc="All symbols from the keyboard")
mod.list('arrow_key', desc="All arrow keys")
mod.list('number_key', desc="All number keys")
mod.list('modifier_key', desc="All modifier keys")
mod.list('function_key', desc="All function keys")
mod.list('special_key', desc="All special keys")

@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
  """ One or more modifier keys """
  return "-".join(m.modifier_key_list)

@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
  """ One directional arrow key """
  return m.arrow_key
  
@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
  """ One or more arrows seperated by a space """
  return str(m)

@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
  """ One number key """
  return m.number_key

@mod.capture(rule="{self.letter}")
def letter(m) -> str:
  """ One letter key  """
  return m.letter

@mod.capture(rule="{self.letter}+")
def letters(m) -> list:
  """ Multiple letter keys """
  return "".join(m.letter_list)

@mod.capture(rule="<self.key>+")
def keys(m) -> str:
  """ A sequence of one or more keys with optional modifers """
  return "".join(m.key_list)

@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
  """ One special key"""
  return m.special_key

@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
  """One symbol key """
  return m.symbol_key

@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
  """ One f(x) key """
  return m.function_key

@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
  """ A single key w/ optional modifiers"""
  try:
    mods = m.modifier_key_list
  except AttributeError:
    mods =[]
  return "-".join(mods + [m.unmodified_key])
  
@mod.capture(rule='{self.modifier_key}+')
def modifiers(m) -> str:
  return "-".join(m.modifier_key_list)

@mod.capture(rule='{self.arrow_key}')
def arrow_key(m) -> str:
  return m.arrow_key

@mod.capture(rule='<self.arrow_key>+')
def arrow_keys(m) -> str:
  return str(m)

@mod.capture(rule='{self.number_key}')
def number_key(m) -> str:
  return m.number_key

@mod.capture(rule='{self.letter}')
def letter(m) -> str:
  """ One letter key """
  return m.letter

@mod.capture(rule='{self.special_key}')
def special_key(m) -> str:
  """ One speo#cial key """
  return m.special_key

@mod.capture(rule='{self.symbol_key}')
def symbol_key(m) -> str:
  return m.symbol_key

@mod.capture(rule='{self.function_key}')
def function_key(m) -> str:
  return m.function_key

@mod.capture(rule='(<self.arrow_key> | <self.number_key> | <self.letter> | <self.symbol_key> | <self.function_key> | <self.special_key>)')
def unmodified_key(m) -> str:
  return str(m)

@mod.capture(rule='<self.modifier_key>* <self.unmodified_key>')
def key(m) -> str:
  """ A single key with no modifiers """
  try:
    mods = m.modifier_key_list
  except AttributeError:
    mods = []
  return "-".join([mods] + [m.unmodified_key])

@mod.capture(rule='{self.letter}+')
def letters(m) -> str:
  return "".join(m.letter_list)

ctx = Context()
ctx.lists['self.modifier_key'] = {
  'command': 'cmd',
  'control': 'ctrl',   #'troll':   'ctrl',
  'shift':   'shift',  #'sky':     'shift',
  'alt':     'alt',    'option':  'alt',
  'super':   'super',
   "option": "alt",
}

alphabet = dict(zip(default_alphabet, letters_string))

ctx.lists['self.letter'] = alphabet
ctx.lists['self.symbol_key'] = {
  "back tick": "`",
  "`": "`",
  "comma": ",",
  ",": ",",
  "dot": ".",
  "period": ".",
  "semi": ";",
  "semicolon": ";",
  "quote": "'",
  "L square": "[",
  "left square": "[",
  "square": "[",
  "R square": "]",
  "right square": "]",
  "forward slash": "/",
  "slash": "/",
  "backslash": "\\",
  "minus": "-",
  "dash": "-",
  "equals": "=",
  "plus": "+",
  "question mark": "?",
  "tilde": "~",
  "bang": "!",
  "exclamation point": "!",
  "dollar": "$",
  "dollar sign": "$",
  "down score": "_",
  "under score": "_",
  "colon": ":",
  "paren": "(",
  "L paren": "(",
  "left paren": "(",
  "R paren": ")",
  "right paren": ")",
  "brace": "{",
  "left brace": "{",
  "R brace": "}",
  "right brace": "}",
  "angle": "<",
  "left angle": "<",
  "less than": "<",
  "rangle": ">",
  "R angle": ">",
  "right angle": ">",
  "greater than": ">",
  "star": "*",
  "asterisk": "*",
  "pound": "#",
  "hash": "#",
  "hash sign": "#",
  "number sign": "#",
  "percent": "%",
  "percent sign": "%",
  "caret": "^",
  "at sign": "@",
  "and sign": "&",
  "ampersand": "&",
  "amper": "&",
  "pipe": "|",
  "dubquote": '"',
  "double quote": '"',
}

ctx.lists['self.number_key'] = dict(zip(default_digits, numbers))
ctx.lists['self.arrow_key'] = {
  'left': 'left',
  'right': 'right',
  'up': 'up',
  'down': 'down',  
}

simple_keys = [
  "end",
    "enter",
    "escape",
    "home",
    "insert",
    "pagedown",
    "pageup",
    "space",
    "tab",
]

alternate_keys = {
    "delete": "backspace",
    "forward delete": "delete",
    #'junk': 'backspace',
} 

keys = {k: k for k in simple_keys}
keys.update(alternate_keys)
ctx.lists['self.special_key'] = keys
ctx.lists['self.function_key'] = {
  f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


@mod.action_class
class Actions:
  def keys_uppercase_letters(m: list):
    """ Inserts uppcase letters from list """
    actions.insert("".join(m).upper())

  def get_alphabet() -> dict:
    """ Provides the alphabet dictionary """    
    return alphabet