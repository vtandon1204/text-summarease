# AI Text Summarizer

<!-- ![Project Logo](https://via.placeholder.com/150) Replace with your project logo if available -->

## Overview

The **AI Text Summarizer** is a web application that utilizes state-of-the-art natural language processing (NLP) techniques to summarize long pieces of text into concise summaries. The application is built using Flask for the backend and integrates with Hugging Face's Transformers library for text summarization. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps to Install](#steps-to-install)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **User-Friendly Interface**: A clean and interactive UI for seamless text input and summarization.
- **Character Count**: Displays the number of characters in the input text, with a limit of 5000 characters.
- **Dynamic Summary Generation**: Quickly generates summaries using advanced machine learning models.
- **Clear Functionality**: Easily clear both input text and summary with a single click.
- **Loading Spinner**: Indicates processing status during summarization.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, [Flask](https://flask.palletsprojects.com/)
- **NLP Model**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- **Libraries**: `transformers`, `Flask`, `numpy`

## Snapshots

Here are some snapshots of the application:

<img src="https://github.com/vtandon1204/text-summarizer-project/blob/main/snaps/flask02.jpg" alt="Main Interface" width="500"/>  
<img src="https://github.com/vtandon1204/text-summarizer-project/blob/main/snaps/flask03.jpg" alt="Summary Result" width="500"/>  

## Installation

### Prerequisites

Ensure you have Python installed (3.6 or higher). You also need `pip` for package management.

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/vtandon1204/text-summarizer-project.git
   cd text-summarizer-project

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
4. Download and set up the pre-trained model (if applicable).


## Usage
1. Start the Flask server:
    ```bash
    python app_flask.py
2. Open your web browser and go to http://127.0.0.1:5000.
3. Paste your text into the input box, and click the Generate Summary button to get your summary. You can clear the input and output using the Clear button.

## Examples
### Example Input
    The rise of artificial intelligence (AI) has led to significant changes in various industries. AI technologies are being used in healthcare, finance, education, and more to improve efficiency and provide better services.
### Example Output
    AI technologies have transformed industries like healthcare and finance, enhancing efficiency and service quality.
## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a pull request.

## License

This project is licensed under the [MIT License](https://github.com/vtandon1204/text-summarizer-project/blob/main/LICENSE) - see the [LICENSE](https://github.com/vtandon1204/text-summarizer-project/blob/main/LICENSE) file for details.

## Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for providing powerful NLP models.
- [Flask](https://flask.palletsprojects.com/) community for an amazing web framework.