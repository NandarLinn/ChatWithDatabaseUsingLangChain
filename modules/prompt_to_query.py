import os
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from dotenv import load_dotenv


def convert_prompt_to_query(prompt):
    llm = OpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_APIKEY'), model_name='gpt-3.5-turbo')
    db_uri = os.getenv('DB_URI')
    db = SQLDatabase.from_uri(db_uri)
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

    result = db_chain.run(prompt)
    return result


def main():
    load_dotenv("../.env")
    user_prompt = input("Enter a prompt: ")
    print(convert_prompt_to_query(user_prompt))


if __name__ == "__main__":
    main()