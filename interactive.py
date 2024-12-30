import streamlit as st
from PIL import Image

st.title('Streamlit 超入門')

st.write('Dislpay image')

# チェックボックスONだと画像表示
if st.checkbox('Show Image'):
    img = Image.open("C:\\Users\\ryuns\\Downloads\\extras\\1.png")
    st.image(img, caption='sample image', use_column_width=True)

st.write('Interactive Widgets')

# セレクトボックス
option = st.selectbox(
    label='好きな数字を入力してください',
    options=list(range(1, 11))
)
# st.write('あなたの好きな数字は', option, 'です。')
'あなたの好きな数字は', option, 'です。'

# テキストボックス
text = st.text_input('あなたの趣味を教えてください。')
text, 'ですか？ くそみたいな趣味ですね笑'

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション: ', condition
