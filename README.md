# CDP Chatbot

The **CDP Chatbot** is a web-based application designed to assist users with questions related to Customer Data Platforms (CDP). Built using Python, Flask, and Hugging Face's `transformers` library, this chatbot delivers intelligent responses to user queries about CDP usage and integration. The application features a user-friendly interface and seamless communication between users and the chatbot.

---

## Features

- **Interactive Chat**: Provides intelligent responses to CDP-related queries.
- **Web Interface**: A clean and responsive design using Bootstrap for user interactions.
- **Natural Language Processing (NLP)**: Powered by Hugging Face's `transformers` for accurate query interpretation.
- **Customizable**: Easy to enhance with additional intents or features.

---

## Technologies Used

- **Python**: Backend programming language.
- **Flask**: Web framework for handling requests and rendering templates.
- **HTML, CSS, JavaScript**: Frontend technologies for building the user interface.
- **Bootstrap**: For responsive and professional web design.
- **Hugging Face Transformers**: Provides the NLP capabilities of the chatbot.
- **Jinja2**: Template engine used within Flask for dynamic HTML rendering.

---

## File Structure

```
/project-folder
├── .venv/              # Virtual environment folder (optional)
├── chatbot-env/        # Environment-specific settings (if used)
├── templates/          # HTML templates
│     └── chat.html     # Main chatbot interface
├── venv/               # Another virtual environment folder (optional)
├── app.py              # Main Python application file
├── README.md           # Documentation file
├── requirements.txt    # Python dependencies
├── script.js           # JavaScript for frontend logic
├── style.css           # Custom styles for the chatbot
```

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)
- A text editor or IDE (e.g., VSCode, PyCharm)

### 2. Clone the Repository

Navigate to the directory where you want to store the project and run:
```bash
$ git clone <repository-url>
$ cd project-folder
```

### 3. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:
```bash
$ python -m venv .venv
$ source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies

Install the required packages listed in `requirements.txt`:
```bash
$ pip install -r requirements.txt
```

### 5. Run the Application

Start the Flask development server:
```bash
$ python app.py
```

Access the application at `http://127.0.0.1:5000` in your web browser.


Executed output link "https://www.loom.com/share/cc499648473c4c47b9081068729ca5a7?sid=b6c1ee0e-24e7-46ec-9ae4-88ab9c9a65bb"

---

## Usage Instructions

1. Open the chatbot application in your web browser.
2. Type your question into the input box, such as:
   - "How do I integrate Segment with Salesforce?"
   - "What is a Customer Data Platform?"
3. Click the **Send** button to receive a response from the chatbot.

---

## Customization

### Update Chatbot Responses

The responses are generated using Hugging Face's `transformers`. To modify the model or fine-tune it for specific intents:

1. Open `app.py` and locate the model initialization:
   ```python
   from transformers import pipeline
   model = pipeline("text-generation", model="gpt2")
   ```
2. Replace `gpt2` with a different model or adjust the pipeline settings.

### Modify Frontend

- **HTML**: Edit `templates/chat.html` for structural changes.
- **CSS**: Update `style.css` for design customizations.
- **JavaScript**: Modify `script.js` for additional interactivity.

---

## Contact

For any queries or feedback, feel free to reach out:

**Premsing**  
Email: premsing.venkat@campusuvce.in
GitHub: (https://github.com/premsing123)
