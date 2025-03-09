from flask import Flask, render_template, request
import spacy
from spacy import displacy

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/entity", methods=["POST"])
def entity():
    if "file" not in request.files:
        return "No file part", 400  # Handle missing file

    file = request.files['file']
    
    if file.filename == "":
        return "No selected file", 400  # Handle empty file

    if file:
        # Read file content
        readable_file = file.read().decode('utf-8', errors='ignore')
        doc = nlp(readable_file)
        html = displacy.render(doc, style='ent')  # Render named entities
        
        return render_template('index.html', html=html, text=readable_file)

if __name__ == '__main__':
    app.run(debug=True)
