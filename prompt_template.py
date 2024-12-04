memory_prompt_template = """<s>[INST] You are an AI chatbot having a conversation with a human. Answer his questions.[/INST]
    Previous conversation: {history}
    Human: {human_input}
    AI:"""

pdf_chat_prompt ="""<s>[INST] Use the given context and chat history to answer the user's question. If you don't know the answer, respond with 'I don't know.'[/INST]
Chat History: {history}
Context: {context}
Question: {human_input}
Answer:"""

# prompt_template = """

#     Human: Please use the given context to provide concise answer to the question
#     If you don't know the answer, just say that you don't know, don't try to make up an answer.
#     <context>
#     {context}
#     </context>

#     Question: {question}

#     Assistant:"""