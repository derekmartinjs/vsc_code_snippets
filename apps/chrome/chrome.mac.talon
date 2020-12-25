
os: mac
app: Google Chrome
-
tag(): browser
tag(): user.tabs
  
action(browser.focus_address):
  key(cmd-l)

action(browser.focus_search):
  key(cmd-l)

action(browser.go_back):
  key(cmd-[)

action(browser.go_forward):
  key(cmd-])

action(browser.go_home):
  key(cmd-shift-h)

action(browser.open_private_window):
  key(cmd-shift-n)
  
action(browser.bookmark):
  key(cmd-d)

action(browser.bookmark_tabs):
  key(cmd-shift-d)

action(browser.bookmarks):
  key(cmd-alt-b)

action(browser.bookmarks_bar):
  key(shift-cmd-b)

action(browser.show_history):
  key(cmd-p)

#action(browser.terminal):
#  key(cmd-shift-j)

action(browser.reload):
  key(cmd-r)

action(browser.reload_hard):
  key(shift-cmd,-r)

