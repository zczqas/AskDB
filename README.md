# AskDB
## Retrieval-Augmented Generation (RAG) Application with Database Access

### Overview

This application is a Retrieval-Augmented Generation (RAG) system that allows users to query a database in natural language and receive detailed answers. It combines natural language processing (NLP), database querying, and large language model (LLM) generation to provide meaningful and user-friendly responses.

### System Architecture
![System Architecture](<media/System Flowchart.png>)

1. User Interface:
    - Entry point for user queries.
    - I do not know much about Frontend. I might comeback to it and build using Streamlit.
    - I am interacting with APIs using swagger UI.

2. Backend:
    - Query Understanding: Uses NLP to interpret user questions and generate database queries.
    - Retriever: Executes database queries to fetch relevant data.
    - Generator: Utilizes an LLM to create natural language responses based on retrieved data.

3. Database:
    - Stores the data that the system queries.
    - Supports both relational and non-relational databases. (I am starting with SQL database first)

3. Final Response:
    - Displays enriched responses to users in a clear, user-friendly format.

### Contributing
Feel free to submit issues, fork the repository, and create pull requests. Contributions are welcome!
