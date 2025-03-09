# Named Entity Recognition (NER) App

This is a Flask-based web application that performs Named Entity Recognition (NER) on uploaded text files using spaCy.

![NER App](web demo.png)

## Features

- Upload a text file for processing.
- Extract named entities such as persons, locations, organizations, and more.
- Display the original text and highlighted named entities.
- Uses spaCy's `en_core_web_sm` model for entity recognition.

## Technologies Used

- Python
- Flask
- spaCy
- HTML, CSS

## Installation & Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/SamiUllah568/Named_Entity_Recognition-NER-.git
    cd NER-App
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate    # On Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download spaCy Model**
    ```bash
    python -m spacy download en_core_web_sm
    ```

5. **Run the Application**
    ```bash
    python app.py
    ```

The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## File Structure

```
NER-App/              # Static files (CSS, JS)
│── templates/
│   └── index.html        # Frontend HTML template
│── app.py                # Main Flask application
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

## Usage

1. Open the app in your browser.
2. Upload a text file (.txt) containing the text you want to analyze.
3. Click "Analyze Entities" to extract named entities.
4. View the results with highlighted named entities.

## Example Output

After uploading a text file, named entities such as organizations, persons, locations, and dates will be highlighted.

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.