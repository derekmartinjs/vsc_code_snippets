# define the various mode commands
mode: all
-
welcome back:
  user.mouse_wake()
  user.history_enable()
  user.talon_mode()

sleep all: 
  user.switcher_hide_running()
  user.history_disable()
  user.homophones_hide()
  user.help_hide()
  user.mouse_sleep()
  speech.disable()
  user.engine_sleep()
talon sleep: speech.disable()
talon wake: speech.enable()
^dication mode$:
  mode.disable("sleep")
  mode.disable("command")
  mode.enable("dictation")
  user.code_clear_language_mode()
  mode.disable("user.gdb")
^command mode$:
  mode.disable("sleep")
  mode.disable("dictation")
  mode.enable("command")
#^force see sharp$: user.code_set_language_mode("csharp")
#^force see plus plus$: user.code_set_language_mode("cplusplus")
#^force go (lang|language)$: user.code_set_language_mode("go")
#^force java script$: user.code_set_language_mode("javascript")
#^force type script$: user.code_set_language_mode("typescript")
#^force markdown$: user.code_set_language_mode("markdown")
#^force python$: user.code_set_language_mode("python")
#^force talon [language]$: user.code_set_language_mode("talon")
#^clear language modes$: user.code_clear_language_mode("csharp")