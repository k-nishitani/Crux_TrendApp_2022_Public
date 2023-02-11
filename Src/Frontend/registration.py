import streamlit as st


def init():
    st.write('家計簿登録画面の内容')

    with st.form("my_form", clear_on_submit=False):
        aaa = st.selectbox(
            '家系項目:',
            [1, 2, 3],
        )

        col1, col2 = st.columns(2)

        with col1:
            bbb = st.date_input('日時')

        with col2:
            ccc = st.number_input('金額', min_value=0, max_value=9999999)

        submitted = st.form_submit_button("登録")

        if submitted:
            st.subheader(aaa)
            st.subheader(bbb)
            st.subheader(ccc)
