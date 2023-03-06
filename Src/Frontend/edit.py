import streamlit as st

stList = ["家賃", "光熱費", "食費","日用品","交際費","秘密のお金"]

def init():
    with st.form("my_form2", clear_on_submit=False):
        itemList = st.selectbox(
        '項目:',stList
        )

        col1, col2 = st.columns(2)

        #登録ボタン
        with col1:
            submitted = st.form_submit_button("登録")
        
        #削除ボタン
        with col2:
            submitted_del = st.form_submit_button("削除")
        
        if submitted:
            ret_submitted()
        if submitted_del:
            stList.remove(itemList)
            ret_submitted_del(itemList)


def ret_submitted():
    st.success('未実装')

def ret_submitted_del(deiItem):
    st.success(f'"{deiItem}"を削除しました', icon="✅")

