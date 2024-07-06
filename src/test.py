import requests
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

def search_pinecone_service(query: str, filters: dict = {}, top_k: int = 16):
    if top_k == 0:
        return []

    url = "https://qyyqlnwqwgvzxnccnbgm.supabase.co/functions/v1/sci_search"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['SP_ANON_KEY']}",
        "x-password": st.secrets['X_PASSWORD'],
        "x-region": "us-east-1"
    }

    request_body = {
        "query": query,
        "filter": filters,
        "topK": top_k
    }

    try:
        response = requests.post(url, headers=headers, json=request_body)
        response.raise_for_status()
        docs_list = response.json()
        return docs_list
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return []


query = "关键金属物质流的全球贸易特征是什么?"
filters = {"journal": ["JOURNAL OF INDUSTRIAL ECOLOGY"]}
top_k = 5


results = search_pinecone_service(query, filters, top_k)

print(results)
