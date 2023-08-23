
from sqlalchemy import create_engine
import pandas as pd




# Create a database connection using sqlalchemy

db_config = {
    "username": "root",
    "password": "Anu@77852286",
    "host": "localhost",
    "database": "ineuron",
}



# Create a database connection using sqlalchemy
db_url = f"mysql+mysqlconnector://{db_config['username']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
engine = create_engine(db_url, echo=True)  # Set echo to True to see SQL commands in the console

# Load CSV data into a Pandas DataFrame

df = pd.read_csv("F:/PYTHAN/PYTHAN/iNeuron/My_SQL/bank/bank-full.csv")

# Define the target table name

#cursor.execute("create table ineuron.bulk_vscode(age int(3),job varchar(30),marital varchar(30),education varchar (30),`default` varchar(30),balance int(10),housing varchar(30),loan varchar(30),contact varchar(30),`day` int(20),`month` varchar(30),duration int(3),campaign int(10),pdays int(10),previous int(10),poutcome varchar(30),y varchar(30))")


# Insert data into MySQL using sqlalchemy

df.to_sql(name= 'bulk_vscode', con = engine , if_exists= 'replace' , index= False)





