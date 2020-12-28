-
project client: 
  user.vscode('workbench.action.terminal.focus')
  insert('cd client && yarn && yarn start\n')
project server: 
  user.vscode('workbench.action.terminal.focus')
  insert('cd server && yarn && yarn start\n')
  