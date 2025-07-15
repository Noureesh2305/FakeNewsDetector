import streamlit as st
from model import predict_news

st.set_page_config(page_title="📰 Fake News Detector")

st.title("📰 Fake News Detector")
st.markdown("Check whether a news article is **Real** or **Fake** using Machine Learning!")

input_text = st.text_area("Paste a news article or headline here 👇", height=250)

if st.button("Detect"):
    if input_text.strip():
        prediction = predict_news(input_text)
        st.success(f"The news is: **{prediction.upper()}**")
    else:
        st.warning("Please enter some news text.")
