import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key=st.secrets["api_key"])

# Creating a system prompt
sys_prompt="""Assume you are an expert python code debugger.
              you should analyze the submitted code and identify potential bugs, errors, or areas of improvement.
              In case if user asks any query or code outside the python scope,politely decline and tell them to enter python code so you can debug and help them.
              Bug report(Bold Heading):give the bug report for user given code.
              Fixed code(Bold Heading):Give the clear and proper code.
              At last give the changes made
                                                                """
# Setting up Gemini model
gemini = genai.GenerativeModel(model_name="gemini-2.0-flash-exp",system_instruction=sys_prompt)

st.title("🤖 An AI Code Reviewer")

# User Input
user_prompt = st.text_area("Enter your python code here....")

# Output is generated if button is clicked and user input is not empty
if st.button("Generate Answer"):
    if user_prompt.strip():  # Check if input is not empty
        response = gemini.generate_content(user_prompt)
        st.subheader("Code Review")
        st.write(response.text)  # Display response
    else:
        st.warning("Please enter a python code before generating an answer.")

