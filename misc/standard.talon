slap:
  edit.line_end()
  key(enter)

# Word/Text Processing Functions
file save: edit.save()

# Terminal Functions
cd: "cd "
change direcory: "cd \n"
grep: "grep \n"

empty array: "[]"

# System functions
zoom [in]: edit.zoom_in()
more zoom: edit.zoom_in()
less zoom: edit.zoom_out()
zoom out: edit.zoom_out()

# Be Focused Pro
^(start | stop) timer$: key(shift-cmd-R)
^skip interval$: key(shift-cmd-B)
