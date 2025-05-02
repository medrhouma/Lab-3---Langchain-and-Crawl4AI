from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
)

# Create a prompt template for generating meal titles
prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

# Create a runnable chain using the pipe operator
chain = prompt_template | llm

# Run the chain with specific parameters
response = chain.invoke({
    "n": 5,
    "cuisine": "Italian"
})

# Print the response
print("\nPrompt: List 5 cooking/meal titles for Italian cuisine (name only).")
print("\nResponse:")
print(response.content)
# The description helps the LLM to know what it should put in there.
class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")
    
    
parser = PydanticOutputParser(pydantic_object=Movie)

prompt_template_text = """
Response with a movie recommendation based on the query:\n
{format_instructions}\n
{query}
"""

format_instructions = parser.get_format_instructions()
prompt_template = PromptTemplate(
    template=prompt_template_text,
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)