# Importing streamlit and openai
import os
import streamlit as st
from openai import OpenAI

client = OpenAI(
  api_key='' # Enter your api_key
)

def generate_response(input_text):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-0613',  # Choose the appropriate GPT model
        messages=[{"role": "system", "content": input_text},
    {"role": "user", "content": input_text}],
    )
    return response.choices[0].message.content

def main():
    st.title("GPT-4 Chat")
    
    # Input field for the user's OpenAI API key
    api_key = st.text_input("Enter your OpenAI API key:")
    
    # Chat box for user input
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if api_key:
            client.api_key = api_key
        
        
        # Display user input in chat format
        st.text("You: " + '\n'+ user_input)
        st.text("Model: " + '\n' + generate_response(user_input))
        st.text("")

if __name__ == "__main__":
    main()
