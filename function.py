def heading_two(text):
    code = f'<!-- wp:heading --><h2> {text}</h2><!-- /wp:heading -->'
    return code


def wp_paragrapg(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def open_ai_answer(prompt):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output

# import os
# from dotenv import load_dotenv
# load_dotenv()
# import openai
# name= openai.api_key = os.getenv('API_KEY')
# print(name)