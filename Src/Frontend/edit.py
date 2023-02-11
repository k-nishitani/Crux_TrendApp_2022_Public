import streamlit as st


def init():
    st.write('項目編集画面の内容')

    aaa = st.selectbox(
        '家系項目:',
        [1, 2, 3],
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(label='登録'):
            test1(aaa)

    with col2:
        if st.button(label='削除'):
            test2(aaa)


def test1(aaa):
    st.text(aaa)


def test2(bbb):
    st.text(bbb)
