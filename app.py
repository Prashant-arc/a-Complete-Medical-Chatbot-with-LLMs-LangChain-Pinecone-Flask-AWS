import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from src.helper import load_llm, load_retriever
from src.prompt import prompt

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🩺 Medical Chatbot")

# Load once, cache across reruns
@st.cache_resource
def setup():
    return load_llm(), load_retriever()

llm, retriever = setup()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def ask(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)

    messages = prompt.invoke({
        "context": context,
        "input": question,
        "chat_history": st.session_state.chat_history,
    })
    response = llm.invoke(messages)
    answer = response.text

    st.session_state.chat_history.append(HumanMessage(content=question))
    st.session_state.chat_history.append(AIMessage(content=answer))
    return answer

# Render past messages
for msg in st.session_state.chat_history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# Chat input
if user_input := st.chat_input("Ask about your medical records..."):
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask(user_input)
        st.write(answer)

if st.sidebar.button("Clear chat"):
    st.session_state.chat_history = []
    st.rerun()