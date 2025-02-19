import os
import streamlit as st
import asyncio
from asyncio import Semaphore
from typing import List
from openai import AsyncOpenAI

from dotenv import load_dotenv

load_dotenv()


# Custom CSS styling
st.markdown("""
    <style>
        /* Sidebar styling adjustments */
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
        }
        .stTextInput textarea {
            color: #ffffff !important;
        }
        .stSelectbox div[data-baseweb="select"] {
            color: white !important;
            background-color: #3d3d3d !important;
        }
        .stSelectbox svg {
            fill: white !important;
        }
        .stSelectbox option {
            background-color: #2d2d2d !important;
            color: white !important;
        }
        div[role="listbox"] div {
            background-color: #2d2d2d !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar configuration
with st.sidebar:
     st.image("data:image/jpeg;base64,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"
            , width=300)
    
     
     functionality = st.radio(
            "Choose Functionality",
            ("Python Expert", "Q&A Bot", "Summarizer", "Humanizer", "Grammar Checker")
        )
     






# Initialize the AsyncOpenAI client
api_key = os.getenv("MUSK_KEY")
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)


function_descriptions = {
    "Q&A Bot": "answering questions and providing information based on user queries",
    "Summarizer": "condensing large texts into concise summaries",
    "Humanizer": "making interactions more engaging and human-like",
    "Grammar Checker": "analyzing text for grammatical errors and suggesting corrections"
}


async def send_question(sem: Semaphore, question: str) -> dict:
    """Send a single question to xAI with semaphore control."""
    async with sem:
        response = await client.chat.completions.create(
            model="grok-2-latest",  # Adjust the model as per the latest or specific requirements
            messages =[{"role" : "system", "content": "You are a helpful AI, currently configured as a {functionality}. This setting allows you to focus on tasks such as {task_description}."}, 
                       {"role": "user", "content": question}]
        )
        return response

async def handle_questions(questions: List[str], max_concurrent: int = 3) -> List:
    """Handle multiple questions with controlled concurrency."""
    sem = Semaphore(max_concurrent)
    tasks = [send_question(sem, question) for question in questions]
    return await asyncio.gather(*tasks)

def main():
    st.title("Grok Synapse: A Multi-Input Parallel Processing AI System")
    
    

    # Session state to manage dynamic input fields
    if 'num_inputs' not in st.session_state:
        st.session_state.num_inputs = 1

    # Button to add new input fields
    if st.button("Add question"):
        st.session_state.num_inputs += 1

    # Generate input fields dynamically
    questions = []
    for i in range(st.session_state.num_inputs):
        question = st.text_input(f"Question {i + 1}", key=f"question_{i}")
        if question:
            questions.append(question)

    # Button to submit all questions
    if st.button("Submit Questions"):
        # Run the async function to handle questions
        with st.spinner('Fetching responses...'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            responses = loop.run_until_complete(handle_questions(questions, max_concurrent=5))
            loop.close()

        # Display each response
        for i, response in enumerate(responses):
    # Using Markdown to format the question in bold and add a line gap before the response
            st.markdown(f"<h3 style='font-weight:bold'>{questions[i]}</h3>", unsafe_allow_html=True)
            st.text("")
            st.markdown(f"\n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
