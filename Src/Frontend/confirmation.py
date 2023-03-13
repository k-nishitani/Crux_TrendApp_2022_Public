import streamlit as st
from gsheetsdb import connect
import pandas as pd
import plotly.express as px
import datetime 

# 接続オブジェクト
conn = connect()

def run_query(query):
   rows = conn.execute(query, headers=1)
   rows = rows.fetchall()
   return rows

def init():    
   sheet_url = "https://docs.google.com/spreadsheets/d/1w1vadKkHs0GRLHplFqDpehj1r1Y7bYtkwcHvxBXDiqU/edit?usp=sharing"
   rows = run_query(f'SELECT * FROM "{sheet_url}"')

   #スプレッドシートの内容取得
   row_list = []
   for row in rows: row_list.append(row)
   df=pd.DataFrame(row_list)

   #全データの一覧を表示-------------------------------------------------------
   st.dataframe(df, 600, 400)
   

   #円グラフとか作ってみる------------------------------------------------------
   fig1 = px.pie(df, values='金額', names='家計項目',title='2023の家計簿')
   st.plotly_chart(fig1)


   #棒グラフとかも作ってみる-----------------------------------------------------
   #月別集計データに変換
   df2 = df
   df2["日時"] = pd.to_datetime(df2["日時"]).dt.strftime("%Y-%m")
   # st.dataframe(df2, 600, 400)
   fig2 = px.bar(df2, x='日時', y='金額',color="家計項目",title='月別家計簿')
   st.plotly_chart(fig2)




