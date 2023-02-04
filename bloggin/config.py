class Config:

    
    def __init__(self):
        self.headers = None
        self.get_headers()


    def get_headers(self):
        self.headers =         {
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            # TODO: Need to store these API keys to some service like rollout
            'Authorization': 'Bearer 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',
        }
    

