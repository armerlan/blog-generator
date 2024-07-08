# Blog Generator

This application generates a blog based on the specifications provided by the user. It takes the blog topic, word limit and type of blog required (one out of common people, researchers and data scientists) and returns a customized write-up.

![](common_blog.png)

## Tools and Frameworks

The application uses Streamlit for the UI and Llama2 as the LLM. Langchain framework with Ctransformerss is implemented and the large language model has been taken from HuggingFace, ```https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin ```.

## Installation and Execution in Windows

1. Clone this repository to your local machine using, 
```
git clone https://github.com/armerlan/blog-generator.git
```

2. Go to the project directory,
```
cd blog-generator
```

3. Install the required packages using,
```
pip install -r requirements.txt
```

4. In the command prompt, execute ```streamlit run app.py```

## Project Structure

- llm_helper: Contains the function to get the response from Llama2 model through Langchain

- model: Downloaded llama-2-7b-ggml model (around 6.9 GB)

- requirements.txt: List of packages required for the application

- app.py: Script to run the application in Streamlit
