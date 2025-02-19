# Grok Synapse: Multi-Input Parallel Processing System

Grok Synapse is a cutting-edge application built on Streamlit, leveraging Elon Musk's latest Grok 2 model from his AI startup. This system is designed to handle and process multiple human inputs in parallel, efficiently generating outputs by utilizing advanced AI capabilities.

## Features

- **Multi-Input Processing**: Allows users to input multiple questions simultaneously.
- **Parallel Execution**: Utilizes asynchronous programming to handle multiple inputs concurrently, ensuring quick and efficient processing.
- **Dynamic Input System**: Users can dynamically add questions as needed before submitting them for processing.
- **Intuitive UI**: Built using Streamlit, the interface is user-friendly, allowing for easy navigation and interaction.
- **Customizability**: Includes a sidebar with options to choose functionalities like Q&A, summarization, humanization, and grammar checking.

## Installation

To set up this project locally, you'll need Python and several dependencies installed on your system. Follow these steps to get started:

### Clone the Repository:
```bash
git clone https://github.com/yourusername/grok-synapse.git
cd grok-synapse
```

### Install Requirements:
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:
Create a .env file in the project root and add your Grok API key:
```bash
MUSK_KEY='your_grok_api_key_here'
```

### Run the Application:
```bash
streamlit run app.py
```

### Usage
After starting the application, navigate to localhost:8501 in your web browser to access the Grok Synapse interface.

  - **Add Questions**: Click the "Add question" button to input new questions.
  - **Submit Questions**: Once all your questions are inputted, click "Submit Questions" to process them through the Grok 2 model.
  - **View Responses**: Responses will be displayed below each question after processing.
