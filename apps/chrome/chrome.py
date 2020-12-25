from talon import ctrl, ui, Module, Context, actions, clip, app

import os
ctx = Context()
mod = Module()

mod.apps.chrome = "app.name: Google Chrome"

ctx.matches = r"""
app: Google Chrome
"""

@ctx.action_class("user")
class user_actions:
#  def talk(text: str):
#    os.system("say 'hello world'") 

  def tab_jump(number: int):
    if number < 9:
      if app.platform == "mac":
        actions.key("cmd-{}".format(number))
      else:
        actions.key("ctrl-{}".format(number))
    

  def tab_final():
    if app.platform == "mac":
      actions.key("cmd-9")
    else:
      actions.key("ctrl-9")

#@ctx.action_class("browser")
#class browser_actions:
#  def duplicate_tab():
#    """ Duplicates live tab in the browser """
