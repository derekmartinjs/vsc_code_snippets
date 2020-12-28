tag: user.code_block_comment
-

talon block comment: user.code_block_comment()
block comment line: 
  edit.line_start()
  user.code_block_comment_prefix()
  key(space)
    edit.line_end()
  key(space)
  user.code_block_comment_suffix()
block comment line <user.text> over:
  edit.line_start()
  user.code_block_comment()
  insert(user.text)

block comment <user.text> over:
  user.code_block_comment()
  insert(user.text)

block comment <user.text>$:
  user.code_block_comment()
  insert(user.text)

(line | inline) block comment <user.text> over:
  edit.line_end()
  user.code_block_comment_prefix()
  key(space)
  insert(user.text)
  key(space)
  user.code_block_comment_suffix()

(line | inline) block comment <user.text>$: user.code_block_comment()
  edit.line_end()
  user.code_block_comment_prefix()
  key(space)
  insert(user.text)
  key(space)
  user.code_block_comment_suffix()

open block comment:
  user.code_block_comment_prefix()

close block comment:
  user.code_block_comment_suffix()

