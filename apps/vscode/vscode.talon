app: Code
-
tag(): user.find_and_replace
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.snippets
tag(): user.splits
tag(): user.tabs

# Tabs 
action(app.tab_close): user.vscode("workbench.action.closeActiveEditor")
action(app.tab_next): user.vscode("workbench.action.nextEditorInGroup")
action(app.tab_previous): user.vscode("workbench.action.previousEditorInGroup")
action(app.tab_reopen): user.vscode("workbench.action.reopenClosedEditor")
action(app.window_close): user.vscode("workbench.action.closeWindow")
action(app.window_open): user.vscode("workbench.action.newWindow")

# App Actions

# talon code actions  
action(code.toggle_comment): user.vscode(editor.action.commentLine)

# Talon edit actions
action(edit.indent_more): user.vscode('editor.action.indentLines') 
action(edit.indent_less): user.vscode('editor.action.outdentLines') 
action(edit.save): user.vscode('workbench.action.files.save') 
action(edit.save_all): user.vscode('workbench.action.files.saveAll') 

# splits.py support begins here
action(user.split_clear_all): user.vscode("View: Single Column Editor Layout")
# multiple_cursor.py support begins here
# multiple_cursor.py support ends here
please [<user.text>]:
  user.vscode("Show All Commands")
  insert(user.text or "")

# Sidebar
bar explore: user.vscode("workbench.view.explorer")
bar extensions: user.vscode("workbench.view.extensions")
bar outline: user.vscode("outline.focus")
bar run: user.vscode("workbench.view.debug")
bar search: user.vscode("workbench.view.search")
bar source: user.vscode("workbench.view.scm")
bar switch: user.vscode("workbench.action.toggleSidebarVisibility")

# Panels
panel control: user.vscode("workbench.panel.repl.view.focus")
panel output: user.vscode("workbench.panel.output.focus")
panel problems: user.vscode("workbench.panel.markers.view.focus")
panel switch: user.vscode("workbench.action.togglePanel")
panel terminal: user.vscode("workbench.action.terminal.focus")
# Settings

# Display

# File commands

# Language features

# Code navigation

# Bookmarks (requires plugin)

# Folding

# Git / Github (not using verb-noun-adjective pattern, mirroring terminal commands.)
git branch: user.vscode("git.branchFrom")
git branch this: user.vscode("git.branch")
git checkout: user.vscode("git.checkout")
git commit: user.vscode("git.commitStaged")
git commit undo: user.vscode("git.undoCommit")
git commit amend: user.vscode("git.commitStagedAmend")
git diff: user.vscode("git.openChange")
git ignore: user.vscode("git.ignore")
git merge: user.vscode('git.merge')
git output: user.vscode('git.showOutput')
git pull: user.vscode('git.pullRebase')
git push: user.vscode('git.push')
git push focus: user.vscode('git.pushForce')

git rebase abort: user.vscode('git.rebaseAbort')
git reveal: user.vscode('git.revealInExplorer')
git revert: user.vscode('git.revertChange')
git stash: user.vscode('git.stash')
git stash pop: user.vscode('git.stashPop')
git stage: user.vscode('git.stage')
git stage all: user.vscode('git.stageAll')
git unstage: user.vscode('git.unstage')
git unstage all: user.vscode('git.unstageAll')

# Debugging

# Terminal
terminal external: user.vscode("workbench.action.terminal.openNativeConsole")
terminal new: user.vscode("workbench.action.terminal.new")
^(new|launch) terminal$: user.vscode("workbench.action.terminal.new")
terminal next: user.vscode("workbench.action.terminal.focusNextPane")
terminal last: user.vscode("workbench.action.terminal.focusPreviousPane")
terminal split: user.vscode("workbench.action.terminal.split")
terminal copy: user.vscode("workbench.action.terminal.selectAll")
terminal (trash|kill): user.vscode("Terminal:Kill")
terminal scroll up: user.vscode("Terminal:ScrollUp")
terminal scroll down: user.vscode("Terminal:ScrollDown")

#TODO: should this be added to linecommands?
copy line down: user.vscode("editor.action.copyLinesDownAction")
copy line up: user.vscode("editor.action.copyLinesUpAction")

#Expand/Shrink AST Selection
select less: user.vscode("editor.action.smartSelect.shrink")
select (more|this): user.vscode("editor.action.smartSelect.expand")
select to bracket: user.vscode("editor.action.selectToBracket")
# Refactor

# Find and replace