import base64
import requests
from dotenv import load_dotenv
load_dotenv()
from function import wp_paragrapg, heading_two,open_ai_answer

file = open('keywords.txt','r+')
keys = file.readlines()
file.close()
new_key = []
for key in keys:
    key = key.strip('\n')
    new_key.append(key)

for keys in new_key:

    title = open_ai_answer(f'write a seo friendly buying guide title 65 characters about {keys}')
    introduction = f'write a introduction 230 characters about {keys}'
    answer = open_ai_answer(introduction).strip().strip('\n')

    content_three = heading_two(open_ai_answer(f'create a unique seo friendly buying guide 65 characters subtitle about {keys}')).strip().strip('\n').replace('"','')
    content_four = wp_paragrapg(open_ai_answer(f'now write a unique seo friendly buying guide article about {content_three}'))

    content_five = heading_two(open_ai_answer(f'make a unique seo friendly buying instruction subtitle 60 characters about {keys}')).strip().strip('\n').replace('"','')
    content_six = wp_paragrapg(open_ai_answer(f'now write another unique seo friendly beneficial article about {content_five}'))

    content_seven = heading_two(open_ai_answer(f'create again another unique seo friendly subtitle 70 characters about {keys}')).strip().strip('\n').replace('"','')
    content_eight = wp_paragrapg(open_ai_answer(f'now write a unique seo friendly buying article about {content_seven}'))

    content_nine = heading_two('Conclusion')
    content_ten = wp_paragrapg(open_ai_answer(f'at last please write a unique seo friendly conclusion 220 characters about {keys}'))


    all_content = answer + content_three + content_four + content_five + content_six + content_seven + content_eight + content_nine + content_ten

    data = {
        'title': title.title().replace('Q:', '').strip().strip('"'),
        'content': all_content,
        'slug': keys.replace(' ', '-')
    }

    user = 'raselahmed'
    password = 'jJrE aCiC PBum kIHI faSF thNx'
    token = base64.b64encode(f'{user}:{password}'.encode())
    header = {'Authorization': f'Basic {token.decode("utf-8")}'}

    api_url = 'https://mysite.local/wp-json/wp/v2/posts'
    post = requests.post(api_url, data=data, headers=header, verify=False)

    if post.status_code == 201:
        print('Post Successful')
    else:
        print(' Wrong post')