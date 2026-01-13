import google.generativeai as genai

genai.configure(api_key="AIzaSyDvHpIpsZy5aSBWCBBrmY3wnIwcd4qOKG4")

for m in genai.list_models():
    print(m.name)