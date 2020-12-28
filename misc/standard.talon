-
settings():
  key_wait = 4.0

^(slap | break)$:
  edit.line_end()
  key(enter)

# Word/Text Processing Functions
file save: edit.save()

# Terminal Functionsp
cd <text>: "cd {text}"
change cd : "cd \n"
grep: "grep \n"
elle less: "ls "
run L S: "ls\n"
run (S S H | S H): "ssh"

diff: "diff "
dot pie: ".py"
run vim: "vim "
run make: "make\n"
run make (durr | dear): "mkdir "
(jay son | jason ): "json"
elle son lint: "eslint"
lint err: "linter"
(http | htp): "http"

tls: "tls"
M D five: "md5"
(regex | rejex): "regex"
word queue: "queue"
word eye: "eye"
word iter: "iter"
word no: "NULL"
word cmd: "cmd"
word dup: "dup"
word streak: 
  insert("streq()") 
  key(left)
word printf : "printf"
word shell: "shell"
dunder in it: "__init__"

spotlight: key(cmd-space)

empty array: "[]"
args: 
	insert("()")
  key(left)

[inside] (index | array): 
  insert("[]") 
  key(left)  

(dickt in it | inside bracket | in bracket):
  insert("{}") 
  key(left) 

dee block:
  insert("{}") 
	key(left enter enter up tab)

(in | inside) percent:
  insert("%%") 
  key(left) 

state pass: 
  "pass"
	key(left enter enter right)

(page | scroll) up: key(pgup)
(page | scroll) down: key(pgdown)
copy that: edit.copy()
cut that: edit.cut()
paste that: edit.paste()
paste match: edit.paste_match_style()
undo that: edit.undo()
redo that: edit.redo()
wipe: key(backspace)
(pad | padding): 
	insert("  ") 
	key(left)
funny: "ha ha"

list in it:
	insert("[]")
	key(left)

string U T F eight: 
  insert("'utf8'")

# System functions
zoom [in]: edit.zoom_in()
more zoom: edit.zoom_in()
less zoom: edit.zoom_out()
zoom out: edit.zoom_out()

# Be Focused Pro
^(start | stop) timer$: key(shift-cmd-R)
^skip interval$: key(shift-cmd-B)
