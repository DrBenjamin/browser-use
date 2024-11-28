import streamlit as st
import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

async def browser_use_case(task):
    agent = Agent(
        task = task,
        llm = ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    return result

with st.form("browser_use_case_form"):
    st.title("Anthropic Browser Use")
    st.write("This is a demo of the Anthropic Browser Use.")

    task = st.text_input(label = "Enter a task", value = "Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights. Return me the cheapest option.")
    submitted = st.form_submit_button("Run")
    if submitted:
        st.write(browser_use_case(task))