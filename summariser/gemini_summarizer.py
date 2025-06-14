import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# Load environment variables from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def summarize_content(contents):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=GEMINI_API_KEY,
        temperature=0.5
    )

    prompt = PromptTemplate(
        input_variables=["content"],
        template="""
        You are an expert summarizer.
        Summarize the following text clearly and concisely:

        {content}

        Summary:
        """
    )

    chain = prompt | llm
    summary = chain.invoke({"content": contents})
    return summary.content
