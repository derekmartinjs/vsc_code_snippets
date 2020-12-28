# This file will add a notification to tell you what Talon heard you say
from talon import app, speech_system

def on_phrase(j):
  phrase = getattr(j["parsed"], "_unmapped", j["phrase"])
  phrase = " ".join(word.split("\\")[0] for word in phrase)
  print("Phrase heard: '{}'".format(phrase))
  app.notify(
    title="Hello world",
    subtitle="Welcome to Talon",
    body=phrase,
    sound=True)

#speech_system.register('post:phrase', on_phrase)
