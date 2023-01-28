import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()

df = pytrend.trending_searches(pn='india')
topic_list = []
for topic in df[0]:
    print(topic)
    topic_list.append(topic)

import requests

for topic in topic_list:

    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        # TODO: Need to store these API keys to some service like rollout
        'Authorization': 'Bearer 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',
    }

    json_data = {
        'model': 'text-davinci-003',
        'prompt': f'Write 2 paragraphs about {topic} in about 1000 words',
        'temperature': 0,
        'max_tokens': 3999,
    }

    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)

    if response.status_code != requests.codes.okay:
        raise ValueError("Need status code to be 200 OKAY")

    generated_text = response.json()['choices'][0]['text']

    # How to get the code into a blog
    # Does it even make sense to create a blog on your own??
    # Open the wordpress website and go to the create new blog page.
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome('./chromedriver.exe')

    driver.find_element(by=By.)

