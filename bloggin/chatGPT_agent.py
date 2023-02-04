import requests
from config import Config
import constants
import logging

class chatgpt_agent:

    def __init__(self):
        self.json_data = None
        self.config = Config()
        self.headers = self.config.headers
        logging.info("initiliased the chatgpt class")

    def clean_data(self, data_list):
        cleaned_data_list = []
        for x in data_list:
            if len(x)>0:
                cleaned_data_list.append(x)
        return cleaned_data_list


        
    def get_blog_text(self, topic, word_limit=400) -> str:
        self.json_data = {
            'model': 'text-davinci-003',
            'prompt': f'Write 2 paragraphs about {topic} in about {word_limit} words',
            'temperature': 0,
            'max_tokens': constants.MAX_TOKEN,
        }
        logging.info(f"Sent the request to openAI for blog text on topic {topic}")

        
        response = requests.post(constants.OPENAI_URL, headers=self.headers, json=self.json_data)
        response.raise_for_status()
        logging.info(f"Sent the response to openAI for blog text on topic {topic}")

        generated_text = response.json()['choices'][0]['text']

        return generated_text


    def get_bloggin_ideas(self, topic, word_limit, no_of_ideas=3) -> list: 
        self.json_data = {
            'model': 'text-davinci-003',
            'prompt': f'Give {no_of_ideas} hot bloggin ideas about {topic} each idea around {word_limit} words',
            'temperature': 0,
            'max_tokens': constants.MAX_TOKEN,
        }
        logging.info(f"Sent the reuest to openAI for blog ideas on topic {topic}")
        response = requests.post(constants.OPENAI_URL, headers=self.headers, json=self.json_data)
        response.raise_for_status()
        logging.info("Recieved the response to openAI for blog ideas")

        generated_text = response.json()['choices'][0]['text']

        # For some reason there are 2 \ns in the beginnging and i am trying to skip them.
        generated_text = generated_text.split('\n')[2:]
        generated_text = self.clean_data(generated_text)


        return generated_text

    def expand_the_blog_with_humor(self, word_limit=4000)->str:
        self.json_data = {
            'model': 'text-davinci-003',
            'prompt': f'Can you exapnd this blog with humour',
            'temperature': 0,
            'max_tokens': word_limit,
        }

        response = requests.post(constants.OPENAI_URL, headers=self.headers, json=self.json_data)
        response.raise_for_status()
        generated_text = response.json()['choices'][0]['text']

        return generated_text


