# Akhbaar padhke sunaao
# Attempt it yourself and watch the series for solution and shoutouts for this lecture!
#My API Key: 4b00b028993b4a5c820a66865d8fab75


import requests
import json
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("News for Today")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4b00b028993b4a5c820a66865d8fab75"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving onto next news....Listen carefully")

else:
    print("Something went wrong!")
    speak("Something went wrong!")


    speak("Thanks for listening.")




