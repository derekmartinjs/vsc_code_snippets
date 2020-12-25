from talon import Module, screen, ui, actions, clip, app, settings
from datetime import datetime
import os, subprocess

active_platform = app.platform
default_command = None

if active_platform == "mac":
  default_folder = os.path.join("~", "Desktop")

mod = Module()
screenshot_folder = mod.setting(
  "screenshot_folder",
  type=str,
  default=default_folder,
  desc="Where to save screenshots. Note this folder must exist.",
)

screenshot_selection_command = mod.setting(
  "screenshot_selection_command",
  type=str,
  default=default_command,
  desc="Commandline trigger for taking a selection of the screen. By default, only linux uses this.",
)

def get_screenshot_path():
  filename = "screenshot-%s.png" % datetime.now().strftime("%Y%m%d%H%M%S")
  folder_path = screenshot_folder.get()
  path = os.path.expanduser(os.path.join(folder_path, filename))

  return os.path.normpath(path)

@mod.action_class
class Actions:
  def screenshot():
    """
    Takes a screenshot of the entire screen and saves it to desktop as screenshot.png
    """
    img = screen.capture_rect(ui.main_screen().rect)
    path = get_screenshot_path()

    img.write_file(path)
    app.notify(subtitle="Screenshot: %s" % path)

  def screenshot_window():
    """
    Takes a screenshot of the current window and saves it to desktop as screenshot.png
    """
    img = screen.capture_rect(ui.active_window().rect)
    path = get_screenshot_path()
    img.write_file(path)
    app.notify(subtitle="Screenshot: %s" % path)
    
  def screenshot_selection():
    """
    Triggers an application that is capable of taking a screenshot of portion of the screen
     """
    command = screenshot_selection_command.get()
    if command:
      path = get_screenshot_path()
      command = command.split()
      command.append(path)
      subprocess.Popen(command)
      app.notify(subtitle="Screenshot: %s" % path)
    else:
      if active_platform == "windows":
        actions.key("super-shift-s")
      elif active_platform == "mac":
        actions.key("ctrl-shift-cmd-4")

  
  def screenshot_clipboard():
    """"
    Takes a screenshot of the entire screen and saves it to the clipboard
    """
    img = screen.capture_rect(screen.main_screen().rect)
    clip.set_image(img)
      
  def screenshot_window_clipboard():
    """"
    Takes a screenshot of the window and saves it to the clipboard
    """
    img = screen.capture_rect(ui.active_window().rect)
    clip.set_image(img)
