import streamlit as st

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

# サイドバーに表示する場合: st.sidebar.~~
# # テキストボックス
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# # スライダー
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# '趣味: ', text
# 'コンディション: ', condition

# 2カラム
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
