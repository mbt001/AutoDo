from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool , wiki_tool, save_tool

class ResearchClass(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]



load_dotenv()



llm = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatAnthropic (model="claude-3-5-sonnet-20241022")

tools = [search_tool, wiki_tool, save_tool]
#response = llm.invoke("Attension is all you need")
#print(response)

parser = PydanticOutputParser(pydantic_object=ResearchClass)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())


agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_execute = AgentExecutor(agent=agent, tools = tools, verbose= True)
query = input("What is the topic you want your research to be about ? ")
raw_response = agent_execute.invoke({"query": query})
print(raw_response)
