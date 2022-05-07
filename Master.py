from asyncore import read
from dotenv import load_dotenv
from pyparsing import null_debug_action
import supabase   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
import os
from supabase import create_client, client

SB_URL = os.environ.get('SUPABASE_URL')
SB_KEY = os.environ.get('SUPABASE_KEY')

supabase: client=create_client(SB_URL,SB_KEY)

def read_data(table_name):
    data=supabase.table(table_name).select("*").execute()
    return data

def insert_data(input_var):
    supabase.table("city_bike").insert(input_var).execute()

def delete_row(col,value):
    supabase.table("city_bike").delete().eq(col,value).execute()
    print(f"deleted {col} with value {value}")


#my_input={"Mydata":"5"}
#insert_data(my_input)

#print(delete_row("Mydata","5"))

data=read_data("city_bike")
print(data)


