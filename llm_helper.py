from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getLlamaResponse(input_text, no_words, blog_style):

    #Llama 2 model
    llm = CTransformers(model = 'model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens': 256,
                                  'temperature': 0.01})

    #Prompt Template

    template = """
    Write a blog for {blog_style} job profile on the topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"], template = template)

    #Generate the response from the llama2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)
    return response