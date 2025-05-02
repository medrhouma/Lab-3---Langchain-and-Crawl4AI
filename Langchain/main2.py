from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chains import LLMMathChain
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor, Tool
from langchain.agents.structured_chat.base import StructuredChatAgent

from dotenv import load_dotenv
import os

load_dotenv()
# Initialize the Groq chat model
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=1024,
)

# Custom prompt for LLMMathChain
math_prompt = PromptTemplate.from_template(
    "Calculate the following expression and return the result in the format 'Answer: <number>': {question}"
)

# Set up the math chain
llm_math_chain = LLMMathChain.from_llm(llm=llm, prompt=math_prompt, verbose=True)

# To get the latest information from the web
# Initialize tools
search = DuckDuckGoSearchRun()

# to garantee that the results are computed properly
calculator = Tool(
    name="calculator",
    description="Use this tool for arithmetic calculations. Input should be a mathematical expression.",
    func=lambda x: llm_math_chain.run({"question": x}),
)

# List of tools for the agent
tools = [
    Tool(
        name="search",
        description="Search the internet for information about current events, data, or facts. Use this for looking up population numbers, statistics, or other factual information.",
        func=search.run
    ),
    calculator
]

# Create the agent using StructuredChatAgent
agent = StructuredChatAgent.from_llm_and_tools(
    llm=llm,
    tools=tools
)

# Initialize the agent executor
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True
)

# Run the agent
result = agent_executor.invoke({"input": "What is the population difference between TUN and ALG?"})
print(result["output"])