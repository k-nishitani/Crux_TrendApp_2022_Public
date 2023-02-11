import streamlit as st
import registration
import confirmation
import edit

st.title('家計簿アプリ')

tab1, tab2, tab3 = st.tabs(["家計簿登録", "家計簿確認", "項目編集"])

with tab1:
    registration.init()

with tab2:
    confirmation.init()

with tab3:
    edit.init()
