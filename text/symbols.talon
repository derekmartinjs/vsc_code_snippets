question [mark]: "?"
(downscore | underscore): "_"
double dash: "--"
(bracket | brack | left bracket| may brack): "{" 
(rbrack | are bracket | right bracket| ray brack): "}"
(bracks | brackets): 
    "[]"
    key(left)
# Dashes
^emm dash$: "—"
^near dash$: "–"
              
trademark: "™️"

triple quote: "'''"
(dot dot | dotdot): ".."

(dot dot dot | dotdotdot): "..."
#ellipses: "…"
ellipses: "..."
(comma and | spamma): ", "
plus: "+"
arrow: "⟼"
left arrow: "⟵"
dub arrow: "⟾"

new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"

empty dubstring:
    '""'
    key(left)
empty escaped (dubstring|dub quotes):
    '\\"\\"'
    key(left)
    key(left)
empty string:
    "''"
    key(left)
empty escaped string:
    "\\'\\'"
    key(left)
    key(left)
(in side parens | args):
	insert("()")
	key(left)
in side (squares | list): 
	insert("[]") 
	key(left)
in side (bracket | brack | braces): 
	insert("{}") 
	key(left)
in side percent: 
	insert("%%") 
	key(left)
in side quotes:
  insert('""')
  key(left)
  
brace this: 
    text = edit.selected_text()
    user.paste("({text})")
comment this: 
    text = edit.selected_text()
    user.paste("# {text}")
    user.line_end()
angle this: 
    text = edit.selected_text()
    user.paste("<{text}>")
(bracket | brack) this: 
    text = edit.selected_text()
    user.paste("[{text}]")
trip (bracket | brace) this: 
    text = edit.selected_text()
    user.paste("{{{text}}}")
(parens | args) this: 
    text = edit.selected_text()
    user.paste("({!text})")
percent this: 
    text = edit.selected_text()
    user.paste("%{text}%")
quote this:
    text = edit.selected_text()
    user.paste('\n"{text}"')
