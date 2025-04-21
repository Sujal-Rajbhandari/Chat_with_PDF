# import streamlit as st
# import main  # Assuming main.py contains the code from above

# st.title("Chat with PDFs using Deepseek")
# uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# if uploaded_file:
#     main.upload_pdf(uploaded_file)
#     file_path = f"{main.pdfs_directory}/{uploaded_file.name}"
#     db = main.create_vector_store(file_path)
#     question = st.text_input("Ask a question about the PDF:")
#     if question:
#         related_documents = main.retrieve_docs(db, question)
#         answer = main.question_pdf(question, related_documents)
#         st.write(answer)
import streamlit as st
import main as main

st.title("Chat with PDFs with Deepseek")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=False
)

if uploaded_file:
    main.upload_pdf(uploaded_file)
    db = main.create_vector_store(main.pdfs_directory + uploaded_file.name)
    question = st.chat_input()

    if question:
        st.chat_message("user").write(question)
        related_documents = main.retrieve_docs(db, question)
        answer = main.question_pdf(question, related_documents)
        st.chat_message("assistant").write(answer)