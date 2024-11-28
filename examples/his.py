"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='Open the testsystem (https://cgm.demo-de.cloud.c3.cgm.ag/) and open the `MENÜ` in the left upper corner to open `FÄLLE & BESUCHE`.',
	llm=llm,
)


async def main():
	await agent.run()


asyncio.run(main())
