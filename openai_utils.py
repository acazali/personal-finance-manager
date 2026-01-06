from langchain.agents import create_agent
from langchain_openai import ChatOpenAI



model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

finantial_agent = create_agent(model, tools = [])

