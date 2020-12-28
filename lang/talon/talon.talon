mode: user.talon
mode: command
and code.language: talon
-
tag(): user.code_operators
tag(): user.code_comment
#tag(): user.code_block_comment

settings():
  insert_wait = 2.0

action(user.code_operator_and): " and " 
action(user.code_operator_or): " or " 
action(user.code_operator_subtraction): " - " 
action(user.code_operator_addition): " + " 
action(user.code_operator_multiplication): " * " 
action(user.code_operator_division): " / " 
action(user.code_operator_assignment): " = " 
action(user.code_comment): "#" 


dot talon: insert(".talon")
insert: 
  insert("insert(''")
  edit.left()
  edit.left()

key:
  insert("insert('key()')")
  edit.left()

<user.modifiers> key: "{modifiers}"

user dot text: "<user.text>"

action:
  insert("action():")

os win:
  insert("os: windows")

os mac:
  insert("os: mac")

os linux:
  insert("os: linux")

app:
  insert("app: ")

setting:
  insert("settings(): \n")

tag set:
  insert("tag(): ")

tag require:
  insert("tag: ")
  
user:
  insert("user: ")

repeat:
  insert("repeat()")
  edit.left()


