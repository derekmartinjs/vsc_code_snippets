from talon import Module, app, Context, actions
mod = Module()
#<@mod.action_class

#@ctx.action_class("user")
# osascript.osascript("set volume output volume 100")
#mod.tag('media', desc='Tag for enabling media commands')
def run_script(script):
  applescript.run("set volume output volume 100")

@mod.action_class
class Actions:
  def media_set_volume(number: int):
   """ Go to first tab """
   if number >= 0 and number <= 100:
#     cmd = """'set Volume 4''""" #%number
     cmd = "set volume output volume 100"
     results = run_script(cmd)
     print(results)
   else:
     error = "volume range {} is out of range (1-{})".format(  number, 100)

     app.notify(error)
     raise error
 
