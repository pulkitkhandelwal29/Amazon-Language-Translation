#Google Cloud Translate
from google.cloud import translate_v2 as translate


translate_client = translate.Client()

source = open("source.txt","r")
source=source.read()

result = translate_client.translate(source, target_language='en',model="base")

print(u"Text: {}".format(result["input"]))
print(u"Translation: {}".format(result["translatedText"]))
print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

print('Writing to text file')

translated = open("translated.txt","w+")
translated.write(str(result["translatedText"]))