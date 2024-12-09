from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)
    
    #mixtral-8x7b-32768
    # llama3-70b-8192
    # gemma2-9b-it
    # llama-3.1-70b-versatile - this model works well - i found this best amon all models. it gives better line counts and better tags
    # llama-3.2-90b-vision-preview
    # llama3-groq-70b-8192-tool-use-preview  - it also works
    
   # model rating descending
   # llama-3.1-70b-versatile > llama3-groq-70b-8192-tool-use-preview