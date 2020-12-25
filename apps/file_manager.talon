tag: file_manager 
-
settings(): 
  # enable if youd like the picker gui to automatically appear when explorer has focus
    user.file_manager_auto_show_pickers = 0

force title: user.file_manager_refresh_title()
show options: user.file_manager_show_pickers()
hide options: user.file_manager_hide_pickers()
go pictures: user.file_manager_open_user_directory("Pictures")
go downloads: user.file_manager_open_user_directory("Pictures")
go profile: user.file_manager_open_user_directory("Pictures")
go docks: user.file_manager_open_user_directory("Pictures")
go back: user.file_manager_open_user_directory("Pictures")
go forward: user.file_manager_open_user_directory("Pictures")
daddy: user.file_manager_open_parent()


# new folder 
new folder: user.file_manager_new_folder()   