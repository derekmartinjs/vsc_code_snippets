from talon import Module

mod = Module()
mod.tag("ide", desc="Tag for enabling generic IDE commands")

@mod.action_class
class Actions:
  def ide_go_first_tab():
    """ Go to first tab """

  def ide_command_palette():
    """ Opens the command palette""" 

  def ide_copy_path():
    """ Copy path of the file """

  def ide_go_first_tab():
    """Go to first tab"""
