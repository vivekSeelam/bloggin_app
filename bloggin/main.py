import pandas as pd
from google_trend_boy import google_trend_boy
from chatGPT_agent import chatgpt_agent
from wordpress import WordPress
import credential
import logging
import time


def main():
    logging.basicConfig(level=logging.INFO)

    gtrends = google_trend_boy()
    trending_topics_list = gtrends.trending_searches('india')
    TextGen = chatgpt_agent()
    wordpress_agent = WordPress()

    for topic in trending_topics_list:

        blog_ideas = TextGen.get_bloggin_ideas(topic=topic, word_limit=20, no_of_ideas=1)
        logging.info(blog_ideas)
        # hopefully it is a list; if not we will convert it to one

        for idea in blog_ideas:
            logging.info(f"creating the blog for idea {idea} in {topic}")
            blog_text = TextGen.get_blog_text(topic=idea,word_limit=1000)

            wordpress_agent.login(username=credential.username, password=credential.password)
            wordpress_agent.update_text(title=idea ,text=blog_text)
            wordpress_agent.publish()
            wordpress_agent.close_the_window()
            logging.info("created the blog please verify manually")
        
            time.sleep(100)

if __name__ == '__main__':
    main()


