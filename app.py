import streamlit as st
from search.google_search import google_search
from scraping.scraper import scrape_website
from summariser.gemini_summarizer import summarize_content

st.set_page_config(page_title="AI Search Summarizer", layout="centered")
st.title("🔍 AI Search Summarizer")

query = st.text_input("Enter a topic to search", "")

if st.button("Search and Summarize") and query:
    with st.spinner("Searching Google..."):
        urls = google_search(query)
        st.write(f"Found {len(urls)} URLs:")
        for url in urls:
            st.write(url)

    all_content = ""
    st.subheader("🌐 Scraping Websites:")
    for url in urls:
        st.markdown(f"- {url}")
        content = scrape_website(url)
        if content:
            st.write(f"Content scraped from {url}:")
            st.write(content[:500])  # Show a preview of the scraped content
            all_content += content + "\n\n"
        else:
            st.write(f"No content found for {url}.")

    with st.spinner("Summarizing with Gemini..."):
        summary = summarize_content(all_content)
        st.subheader("📃 Summary:")
        st.write(f"Summary: {summary}")
