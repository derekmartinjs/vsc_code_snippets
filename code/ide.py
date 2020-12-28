from talon import Module

mod = Module()

mod.tag("ide", desc="Tag for enabling generic IDE commands")

@mod.action_class
class Actions:
  def ide_refactor():
    """Trigger refactoring menu of the ide"""
  def ide_perfect():
    """
    Trigger better autocomplete in the ide
    """
    pass

  

  def ide_smart(): 
    """ Trigger suggestion / type completion in the ide """

  def ide_finish():     
    """Trigger auto complete statement """

  def ide_done():
    """Trigger auto complete statement """

  def ide_intellisense_suggest_parameters(): 
    """ Trigger parameter hints """
  
  def ide_toggle_tools(): 
    """ Hide all windows """

  def ide_go_first_tab():
    """ Go to first tab """

  def ide_command_palette():
    """ Opens the command palette""" 

  def ide_copy_path():
    """ Copy path of the file """

  def ide_go_first_tab():
    """Go to first tab"""
