import os
from openai_utils import finance_manager
from dotenv import load_dotenv
from langchain.messages import HumanMessage

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not found in environment variables")

def main():
    # create model
    while(True):
        try:
            user_input = input()
            messages = [HumanMessage(content=user_input)]
            state = finance_manager.invoke({"messages": messages})
            print(state['messages'])
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()