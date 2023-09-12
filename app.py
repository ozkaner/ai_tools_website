import streamlit as st
from transformers import pipeline 
from googletrans import Translator

# Titles
st.sidebar.title("Tools")
st.title("<h1>NLP TOOLS</h1>")


# Functions 
def turkish_to_english(text): 
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='tr', dest='en')
        return translated_text.text
    except Exception as e:
        return str(e)
    
def recommend(text):
    result = sent_pipeline(text)
    return result
def summary(text):
    result = summarize(text)
    return result

#Pipelines
sent_pipeline = pipeline("sentiment-analysis")
summarize = pipeline("summarization")

# Widget Panel
selected_app = st.sidebar.radio("Choose a tool",("Sentimental Analysis", "Text Summary")) 

# Seçilen uygulamayı görüntüleyin
if selected_app == "Sentimental Analysis":
    st.header("Sentimental Analysis")
    user_input = st.text_area("Enter text:", "")
    translated_text = turkish_to_english(user_input)
    if st.button("Show"):
        final_result = recommend(translated_text)
        st.header("Results")
        for result in final_result:
            st.write(f"Emotion: {result['label']}, Score: {result['score']}")


    
    
elif selected_app == "Text Summary":
    st.header("Text Summary App")
    user_input_2 = st.text_area("Enter text")
    summary_button = st.button("Show")
    if summary_button:
        summary_result = summary(user_input_2)
        st.write(f"Summary of text : {list(summary_result[0].values())[0]}")











