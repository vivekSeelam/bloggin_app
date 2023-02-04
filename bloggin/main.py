import pandas as pd
from google_trend_boy import google_trend_boy
from chatGPT_agent import chatgpt_agent
from wordpress import WordPress
import requests
import credential
import logging

Google_Trend_Boy = google_trend_boy()
trending_topics_list = Google_Trend_Boy.trending_searches('india')
TextGen = chatgpt_agent()
wordpress_agent = WordPress()

for topic in trending_topics_list:

    blog_ideas = TextGen.get_bloggin_ideas(topic=topic, word_limit=20, no_of_ideas=2)
    print(blog_ideas)
    # hopefully it is a list; if not we will convert it to one

    for idea in blog_ideas:
        blog_text = TextGen.get_blog_text(topic=idea,word_limit=1000)

        wordpress_agent.login(username=credential.username, password=credential.password)
        wordpress_agent.update_text(title=idea ,text=blog_text)
        wordpress_agent.publish()
        wordpress_agent.close_the_window()
        print("created the blog please verify manually")
    





    # How to get the code into a blog
    # Does it even make sense to create a blog on your own??
    # Open the wordpress website and go to the create new blog page.

    

b'{"id":"cmpl-6g5Dv4OMjapxC3tpIlmxd2387QarB","object":"text_completion","created":1675487875,"model":"text-davinci-003","choices":[{"text":"\\n\\n1. Expl","index":0,"logprobs":null,"finish_reason":"length"}],"usage":{"prompt_tokens":11,"completion_tokens":5,"total_tokens":16}}\n'