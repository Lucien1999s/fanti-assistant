import streamlit as st
import requests

def chat(id, content):
    url = 'http://61.219.221.92:9903/generate_post/'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "id": id,
        "content": content
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        resp_data = response.json()
        return resp_data.get("response", "no response data")
    else:
        return "Fail resp from api..."

def clear(id):
    url = 'http://61.219.221.92:9903/delete_cache/'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "id": id
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        resp_data = response.json()
        return resp_data.get("response", "no response data")
    else:
        return "Fail resp from api..."

# Streamlit interface
st.title("Fanti Assistant")

# Input fields for ID and Content
user_id = st.text_input("ID", value="")
content = st.text_area("Content", value="", height=150)

# Buttons for Chat and Clear
if st.button("Chat"):
    result = chat(user_id, content)
    st.text_area("Output", value=result, height=300, key="chat_output")

if st.button("Clear"):
    result = clear(user_id)
    st.text_area("Output", value=result, height=300, key="clear_output")

