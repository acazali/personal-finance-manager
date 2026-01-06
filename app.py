import os
from openai_utils import financial_agent
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not found in environment variables")

def main():

    # create model
    while(True):
        try:
            user_input = input()
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()