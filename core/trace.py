class PromptTracer:
    def __init__(self):
        self.history = []

    def record(self, prompt, response):
        event = {"prompt": prompt, "response": response}
        self.history.append(event)
        print(event)

    def get_history(self):
        return self.history
