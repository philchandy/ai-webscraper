import streamlit as st
from scraper import getHTMLElements, getBodyContent, cleanBodyContent, splitDOMContent
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the Website")
    result = getHTMLElements(url)

    body = getBodyContent(result)
    body_clean = cleanBodyContent(body)

    st.session_state.body = body_clean

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", body_clean, height=300)

if "body" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = splitDOMContent(st.session_state.body)

            response = parse_with_ollama(dom_chunks, parse_description)

            st.write(response)
