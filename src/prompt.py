from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system_prompt = (
    "You are a helpful medical assistant. Answer the question using only the "
    "context below. If the answer is not in the context, say you don't know.\n\n"
    "Context:\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])