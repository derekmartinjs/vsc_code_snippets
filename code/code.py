from talon import Context, actions, ui, Module, settings 
import re
import os

ctx = Context()
mod = Module()

settings_private_function_formatter = mod.setting('code_private_function_formatter', str)
settings_protected_function_formatter = mod.setting('code_protected_function_formatter', str)
settings_public_function_formatter = mod.setting('code_public_function_formatter', str)
settings_private_variable_formatter = mod.setting('code_private_variable_formatter', str)
settings_protected_variable_formatter = mod.setting('code_protected_variable_formatter', str)
settings_public_variable_formatter = mod.setting('code_public_variable_formatter', str)

mod.tag("code_comment", desc='Tag for enabling generic comment commands')
mod.tag("code_operators", desc='Tag for enabling generic operator commands')
mod.tag("code_generic", desc='Tag for enabling other baisc programming commands, (loops, functions, etc')
key = actions.key

extension_lang_map = {
   "py": "python",
    "cs": "csharp",
    "cpp": "cplusplus",
    "h": "cplusplus",
    "talon": "talon",
    "gdb": "gdb",
    "md": "markdown",
    "java": "java",
    "sh": "bash",
    "go": "go",
    "js": "javascript",
    "ts": "typescript"
}

# flag indicating whether or not title tracking is enabled
forced_language = False

@ctx.action_class('code'):
class code_actions:
  def language():
    result = ""
    if not forced_language:
      file_extension = actions.mac.file_ext()
# create a mode for each defined language