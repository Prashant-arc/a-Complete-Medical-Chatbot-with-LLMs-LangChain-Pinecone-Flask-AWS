a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS/tree/main


## Setup

1. Create a virtual environment and install dependencies:
   pip install -r requirement.txt
2. Create a `.env` file in the project root:
   GOOGLE_API_KEY=your_key_here
3. Build the vector store from `data/Medical_book.pdf` (run your indexing script or notebook).
4. Start the app:
   streamlit run app.py