from ast import Break
from textblob import TextBlob
def detect_mood(text):
    analysis = TextBlob(text)
    pol=analysis.sentiment.polarity
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😔"
    else:
        return "Neutral 😑"
    return analysis, pol

def chat_with_user():
  print("Hi I am Moodbot!! Tell me how are you feeling today? ")
  while True:
    inp=input("You: ")
    if inp.lower() in ["exit", "bye", "done"]:
      print("Moodbot: Take care! 💕")
      break
    mood=detect_mood(inp)
    print("Moodbot: Your mood seems to be ",mood)

if __name__=="__main__":
  chat_with_user()
