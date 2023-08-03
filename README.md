# Chat With Dabase Using LandChain

### Install the dependencies
- Create a new virtual environment
```sh
python3 -m venv testwork_env
source testwork_env/bin/activate
```
- install required library using pip
```sh
pip install -r requirement.txt
```

### Create SqliteDB
- make a directory `database` in current directory.
To execute the API, please use the following command:
```sh
uvicorn app:app --reload
```
- Upon executing the API, the database and corresponding tables were automatically created in `database/sql_app.db`. It is worth noting that an SQLite Database was utilized for this demonstration application.
- First of all, the denormalized dataset needs to be normalized that helps eliminate data redundancy and improve data integrity in the database. It involves organizing data into tables and applying a set of rules called normal forms to ensure efficient and accurate data storage. After the process of normalization, a total of four tables are obtained.
    - Orders
    - Products
- To review the table schema, kindly refer to the [Model](https://github.com/NandarLinn/ChatWithDatabaseUsingLangChain/tree/main/models) folder.
 
### Importing CSV Data
The first step involves mapping the CSV header to the respective column mapping. Following this, the sale data is read row by row, and the data is imported into specific tables using filter methods.
Dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/knightbearr/sales-product-data).
To import the CSV data, please execute the following command:
```sh
python3 -m venv testwork_env
source testwork_env/bin/activate
cd Testwork
python -m seeds.importer ~/Downloads/sales_data\ -\ sales.csv
```

### Building A Chat Bot
The current database is connected to Langchain, a tool known as large language models (LLMs), that helps connect advanced language software, with other sources of information, like databases.
```sh
def convert_prompt_to_query(prompt):
    llm = OpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_APIKEY'), model_name='gpt-3.5-turbo')
    db_uri = os.getenv('DB_URI')
    db = SQLDatabase.from_uri(db_uri)
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

    result = db_chain.run(prompt)
    return result
```
Please refer to the code in the [ask.py](https://github.com/NandarLinn/Testwork/blob/main/apis/v1/ask.py) and [prompt_to_query.py](https://github.com/NandarLinn/Testwork/blob/main/modules/prompt_to_query.py) file for further details and implementation.

### Run Demo App
To execute the API, please use the following command:
```sh
uvicorn app:app --reload
```
Through the Fast API, it is possible to inquire about the sale data by posing questions.
Try it out in browser
```sh
http://127.0.0.1:8000/docs
```
![Alt](https://github.com/NandarLinn/Testwork/raw/main/pictures/Screen%20Shot%202023-07-12%20at%201.45.52%20PM.png)
![Alt](https://github.com/NandarLinn/Testwork/raw/main/pictures/Screen%20Shot%202023-07-12%20at%201.45.52%20PM.png)

Or using curl
```sh
curl -X 'POST' \
  'http://localhost:8000/api/v1/ask' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "how much was earned in 2019"
}'
```
![Alt](https://github.com/NandarLinn/Testwork/raw/main/pictures/Screen%20Shot%202023-07-12%20at%201.45.52%20PM.png)

### Background Process in API
![Alt](https://github.com/NandarLinn/Testwork/raw/main/pictures/Screen%20Shot%202023-07-12%20at%201.45.52%20PM.png)



