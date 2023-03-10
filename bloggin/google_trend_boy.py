import pandas as pd
from pytrends.request import TrendReq
import logging

class google_trend_boy:
    def __init__(self):
        self.pytrend = TrendReq()

    def trending_searches(self, location='india'):
        """
        Returns a list which contains the trending searches given by that location
        """
        df = self.pytrend.trending_searches(pn=location)
        topic_list = []
        for topic in df[0]:
            topic_list.append(topic)
        logging.info("Received the google trends list")
        return topic_list
