from flask import Flask, request, render_template,url_for
from flask_cors import cross_origin
import boto3
from google.cloud import translate_v2 as translate


app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/sound", methods = ["GET", "POST"])
@cross_origin()
def sound():
    if request.method == "POST":
        text = request.form['texttotranslate']  
        sourcelanguage = request.form['sourcelanguage']
        targetlanguage = request.form['targetlanguage']
        translate = boto3.client(service_name='translate',region_name='us-east-1') 

        result = translate.translate_text(Text=text, SourceLanguageCode=sourcelanguage,TargetLanguageCode=targetlanguage) 

        translated = open("static/language/translated.txt","w+")
        translated.write(str(result["TranslatedText"]))

    return render_template("index.html",conversion="Your Text has been converted to your required language...")


if __name__ == "__main__":
    app.run(debug=True)
