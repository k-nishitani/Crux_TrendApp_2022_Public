import streamlit as st

stList = ["家賃", "光熱費", "食費","日用品","交際費","秘密のお金"]

#各処理-----------------------------------------------------------------
#追加
def add_item():
    if st.session_state["input_new"] == '':
        st.session_state.retFlg = False
        st.session_state.retMsg = '空文字は登録できません'
    else:
        if st.session_state["input_new"] in st.session_state.ItemList:
            st.session_state.retFlg = False
            st.session_state.retMsg = '既に存在しています'
        else:
            st.session_state.ItemList.append(st.session_state["input_new"])
            st.session_state.retFlg = True
            st.session_state.retMsg = f'"{st.session_state["input_new"]}"を登録しました'

    #入力内容初期化
    st.session_state["input_new"] = ""

#編集
def chg_item():
    if st.session_state["input"] == "":
        st.session_state.retFlg = False
        st.session_state.retMsg = '空文字は登録できません'
    else:
        if st.session_state["input_new"] in st.session_state.ItemList:
            st.session_state.retFlg = False
            st.session_state.retMsg = '既に存在しています'
        else:
            #インデックス取得
            tmpIndex = st.session_state.ItemList.index(st.session_state["selectbox"])
            #置き換え
            st.session_state.ItemList[tmpIndex]=st.session_state["input"]
            st.session_state.retFlg = True
            st.session_state.retMsg = f'"{st.session_state["selectbox"]}"を"{st.session_state["input"]}"に編集しました'

    #入力内容初期化
    st.session_state["input"] = ""

#削除
def del_item():
    st.session_state.ItemList.remove(st.session_state["selectbox"])

    st.session_state.retFlg = True
    st.session_state.retMsg = f'"{st.session_state["selectbox"]}"を削除しました'

#画面------------------------------------------------------------------
def init():
    edit_tab1, edit_tab2 = st.tabs(["追加", "編集・削除"])

    if "ItemList" not in st.session_state: 
            st.session_state.ItemList = stList 
    if "retFlg" not in st.session_state: 
            st.session_state.retFlg = False 
    if "retMsg" not in st.session_state: 
            st.session_state.retMsg = ""        
   
    with edit_tab1:
        add_tab()
    with edit_tab2:
        chg_tab()  

#入力画面
def add_tab():
    with st.form("sub_form1", clear_on_submit=False):

        #登録値を入力する項目
        st.text_input('追加項目',key="input_new")

        #登録ボタン
        submitted = st.form_submit_button("追加",on_click=add_item)
        
        if submitted:
            if st.session_state.retFlg == True:
                st.success(st.session_state.retMsg, icon="✅")
            else:
                st.error(st.session_state.retMsg, icon="🚨")
           

#編集・削除画面
def chg_tab():
    with st.form("sub_form2", clear_on_submit=False):

        #編集・削除する値を選択する項目
        st.selectbox('項目:',st.session_state.ItemList, key="selectbox")
        #変更値を入力する項目
        st.text_input('編集名',key="input")
        
        col1_1, col2_1 = st.columns(2)
        #編集ボタン
        with col1_1:
            submitted_upd = st.form_submit_button("編集",on_click=chg_item)
        #削除ボタン
        with col2_1:
            submitted_del = st.form_submit_button("削除",on_click=del_item)

        if submitted_upd or submitted_del:
            if st.session_state.retFlg == True:
                st.success(st.session_state.retMsg, icon="✅")
            else:
                st.error(st.session_state.retMsg, icon="🚨")