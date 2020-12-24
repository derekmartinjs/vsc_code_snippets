# Microsoft - Visual Studio Code
# see app/vscode.talon for custom voice commands
# see ide.talon for common voice commands
app: Code
os: mac
-
tags(): tabs
tags(): ide
tags(): line_commands

# General 

# Window & File Management
action(app.window_open):
  key(shift-cmd-n)
