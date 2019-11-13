#!/usr/bin/

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

API_CREDENTIALS='AIzaSyAFPH9FTNK1iU1BVgQV9ase8beQbtyjawU'

# Instantiate a client
client = language.LanguageServiceClient(credentials=API_CREDENTIALS)

# ask user to input text to be analyzed
text = raw_input("enter text you wish to analyze: ")
document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

# detect sentiment
sentiment = client.analyze_sentiment(document=document).document_sentiment

# print results
print 'Text: {}'.format(text)
print 'Sentiment: {} {}'.format(sentiment.score, sentiment.magnitude)

def classify_text():
    # [START language_classify_text]
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'Android is a mobile operating system developed by Google, ' \
           'based on the Linux kernel and designed primarily for ' \
           'touchscreen mobile devices such as smartphones and tablets.'

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))
    # [END language_classify_text]


