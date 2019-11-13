from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Instantiate a client
client = language.LanguageServiceClient()

def sentiment(text):
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document)
    return sentiment 
