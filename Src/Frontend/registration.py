import streamlit as st


def init():
    with st.form("my_form", clear_on_submit=False):
        #項目
        tmpItem = st.selectbox(
            '項目:',
            ["家賃", "光熱費", "食費","日用品","交際費","秘密のお金"],
        )

        #日時、金額
        col1, col2 = st.columns(2)
        with col1:
            tmpDate = st.date_input('日時')
        with col2:
            tmpPrice = st.number_input('金額', min_value=0, max_value=9999999)
        
        #登録ボタン
        submitted = st.form_submit_button("登録")
        
        #登録ボタン押下処理
        if submitted and tmpPrice == 0:
            #0円の場合はエラーメッセージを出して処理中止
            st.error('0円は登録できません', icon="🚨")
            
        if submitted and tmpPrice > 0:
            st.success('登録しました', icon="✅")
            st.subheader(tmpItem)
            st.subheader(tmpDate)
            st.subheader(tmpPrice)
           
        