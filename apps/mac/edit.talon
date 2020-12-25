os: mac
-
action(edit.copy):
  key(cmd-c)

action(edit.cut):
  key(cmd-x)

action(edit.delete):
  key(backspace)

action(edit.delete_word):
  actions.edit.select_word()
  actions.edit.delete()  
  
action(edit.down):
  key(down)
  
#action(edit.extend_again):
#action(edit.extend_column):
action(edit.extend_down):
  key(shift-down)

action(edit.extend_file_end):
  key(shift-cmd-down)

action(edit.extend_file_start):
  key(cmd-shift-up)

action(edit.extend_left):
  key(shift-left)
#action(edit.extend_line):

action(edit.extend_line_down):
  key(shift-down cmd-shift-right)

action(edit.extend_line_end):
  key(cmd-shift-right)

action(edit.extend_line_start):
  key(cmd-shift-left)

action(edit.extend_line_end):
  key(cmd-shift-right)

action(edit.extend_line_up):
  key(shift-up cmd-shift-left)

action(edit.extend_page_down):
  key(cmd-shift-pagedown)

action(edit.extend_page_up):
  key(cmd-shift-pageup)

action(edit.extend_right):
  key(shift-right)

action(edit.extend_up):
  key(shift-up)

action(edit.extend_word_left):
  key(shift-alt-left)

action(edit.extend_word_right):
  key(shift-alt-right)

action(edit.file_end):
  key(cmd-down cmd-left)

action(edit.file_start):
  key(cmd-up cmd-left)

action(edit.find):
  key(cmd-f)

action(edit.find_next):
  key(cmd-g)

action(edit.find_previous):
  key(cmd-shift-g)

action(edit.indent_less):
  key(cmd-left delete)

action(edit.indent_more):
  key(cmd-left tab)

action(edit.left):
  key(left)

action(edit.line_down):
  key(down home)

action(edit.line_end):
  key(cmd-right)

action(edit.line_insert_down):
  key(end enter)

action(edit.line_insert_up):
  key(cmd-left enter up)

action(edit.line_start):
  key(cmd-left)

action(edit.line_up):
  key(up cmd-left)

action(edit.page_down):
  key(pagedown)

action(edit.page_up):
  key(pageup)
  
action(edit.paste):
  key(cmd-v)

action(edit.paste_match_style):
  key(cmd-alt-shift-v)

action(edit.print):
  key(cmd-p)

action(edit.redo):
  key(cmd-shift-z)

action(edit.right):
  key(right)

action(edit.save):
  key(cmd-s)

action(edit.save_all):
  key(cmd-shift-s)

action(edit.select_all):
  key(cmd-a)

action(edit.select_line):
  key(cmd-right cmd-shift-left)

action(edit.select_none):
  key(right)

action(edit.select_word):
  key(left shift-right left alt-left alt-right shift-aft-left)

action(edit.undo):
  key(cmd-z)

action(edit.up):
  key(up)

action(edit.word_left):
  key(alt-left)

action(edit.word_right):
  key(alt-right)

action(edit.zoom_in):
  key(cmd-+)

action(edit.zoom_out):
  key(cmd--)

action(edit.zoom_reset):
  key(cmd-0)