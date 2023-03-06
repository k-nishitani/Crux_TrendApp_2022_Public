import streamlit as st
from gsheetsdb import connect
import pandas as pd

# 接続オブジェクト
conn = connect()

def run_query(query):
   rows = conn.execute(query, headers=1)
   rows = rows.fetchall()
   return rows

def init():    
   sheet_url = "https://docs.google.com/spreadsheets/d/1w1vadKkHs0GRLHplFqDpehj1r1Y7bYtkwcHvxBXDiqU/edit?usp=sharing"
   rows = run_query(f'SELECT * FROM "{sheet_url}"')

   # スプレッドシートの内容をstreamlitに表示する
   row_list = []
   for row in rows: row_list.append(row)
   df=pd.DataFrame(row_list)
   # st.table(df)
   st.dataframe(df, 600, 400)
   
   # st.text(df['家計項目'].value_counts())

   

