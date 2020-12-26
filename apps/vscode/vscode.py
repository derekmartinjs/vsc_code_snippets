from talon import Context, actions, ui, Module, app, clip
from typing import List, Union

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()
#wmod.apps.vscode = "app.name: Code.exe"
#mod.apps.vscode = "app.name: Visual Studio Code"
#mod.apps.vscode = "app.name: Code"
#mod.apps.vscode = "app.name: Code - OSS"

ctx.matches = r"""
app: vscode
"""

@ctx.action_class("win")
class win_actions: 
  def filename():
    title = actions.win.title

    if is_mac:
      result = title.split(" - ")[0]

    if "." in result:
      return result

  def file_ext():
    return actions.win.filename().split(".")[-1]

@ctx.action_class("edit")
class edit_actions:
  def find(text: str):
    if is_mac:
      actions.key("cmd-f")
    else:
      actions.key("ctrl-f")

    actions.insert(text)

  def line_swap_up():
    actions.key("alt-up")

  def line_swap_down():
    actions.key("alt-down")

  def line_clone():
    actions.key("shift-alt-down")

 # def jump_line(n: int):
 #   actions.user.vscode("workbench.action.gotoLine")
 #   actions.insert(str(n))
#    actions.key("enter")
    
@mod.action_class
class Actions:
  def vscode(command: str):
    """ 
      Execute command via the command palette. 
      Preserves the clipboard
    """
    if not is_mac:
      actions.key("ctrl-shift-p")
    else:
      actions.key("cmd-shift-p")

    actions.user.paste(f"{command}")
    actions.key("enter")

  def vscode_ignore_clipboard(command: str):
    """ 
      Execute command via the command palette. 
      Does NOT preserve the clipboard for commands like copyFilePath
    """
    clip.set_text(f"{command}")
    if not is_mac:
      actions.key("ctrl-shift-p")
    else:
      actions.key("cmd-shift-p")

    actions.edit.paste()
    actions.key("enter")
 
class user_actions:
  # snippet.py support beginHelp close 
  def snippet_search(text: str):
    pass

  def snippet_insert(text: str):
    """ Inserts a snippet """
    pass

  def snippet_create():
    """ Triggers snippet creation """
    pass

  """ snippet.py support end """

  def tab_jump(number: int):
    pass

  def tab_final():
    pass
  
  """ splits.py support begins """
  def split_number(index: int):
    """Navigates to a the specified split"""
    if index < 9:
      if is_mac:
        actions.key("cmd-{}".format(index))
      else:
        actions.key("ctrl-{}".format(index))

  """ splits.py support ends """

  """ find_and_replace.py support begins """
  def find(text: str):
    """ Triggers find in current editor """
    pass

  def find_next():
    """ Triggers find_next in current editor """
    pass

  def find_previous():
    """ Triggers find_previous in current editor """
    pass

  def find_everywhere(text: str):
    """ Triggers find_next in current editor """
    pass

  def find_toggle_match_by_case():
    """ Triggers find match by case sensitivity """
    pass

  def find_toggle_match_by_word():
    """ Triggers find match by whole words """
    pass

  def find_toggle_match_by_regex():
    """ Triggers find match by regex """
    pass

  def replace(text: str):
    """ Search and replace in active editor """
    pass

  def replace_everywhere(text: str):
    """ Search and replace in entire project """
    pass

  def replace_confirm():
    """ Confirms replace at current position """
    pass

  def replace_confirm_all():
    """ Confirms replace in entire project """
    pass

  def select_previous_occurrence(text: str):
    pass

  def select_next_occurrence(text: str):
    pass

  """ find_and_replace.py support ends """

