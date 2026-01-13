from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from finance_tools import finance_tools
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

finance_manager = create_agent(
    model, 
    tools = finance_tools,
    system_prompt="You are a helpful finance manager/assistant to insert or retrieve spends in a database."
)



