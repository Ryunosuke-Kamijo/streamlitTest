import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Progress bar')
status = 'Start!'
st.write(status)

latest_iter = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iter.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

status = 'Done!'
