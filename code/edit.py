import time
from talon import Module, Context, actions, ui, clip

ctx = Context()
mod = Module()

@ctx.action_class("edit")
class edit_actions:
  def selected_text() -> str:
    with clip.capture() as s:
      actions.edit.copy()
    try:
      return s.get()
    except clip.NoChange:
      return ""

@mod.action_class
class Actions:
  def paste(text: str):
    """Pastes text and preserves clipboard"""
    with clip.revert():
      clip.set_text(text)
      actions.edit.paste()
      # sleep here so that clip.revert doesn't revert the clipboard too soon
      actions.sleep("150ms")
