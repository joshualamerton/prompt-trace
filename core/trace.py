class PromptTracer:
    def __init__(self):
        self.history = []

    def record(self, prompt, response):
        event = {"prompt": prompt, "response": response}
        self.history.append(event)
        print(event)

    def get_history(self):
        return self.history

    def search(self, query: str) -> list:
        """Search prompt history by text in prompt or response.

        Parameters
        ----------
        query : str
            Case-insensitive text to search for in prompt or response fields.

        Returns
        -------
        list
            List of matching prompt-response pairs.
        """
        query_lower = query.lower()
        return [
            entry for entry in self.history
            if query_lower in entry["prompt"].lower()
            or query_lower in entry["response"].lower()
        ]

    def filter(self, keyword: str) -> list:
        """Filter prompt history by keyword in the prompt field.

        Parameters
        ----------
        keyword : str
            Case-insensitive keyword to filter prompts by.

        Returns
        -------
        list
            List of prompt-response pairs where the prompt contains the keyword.
        """
        keyword_lower = keyword.lower()
        return [
            entry for entry in self.history
            if keyword_lower in entry["prompt"].lower()
        ]

    def filter_by_response(self, keyword: str) -> list:
        """Filter prompt history by keyword in the response field.

        Parameters
        ----------
        keyword : str
            Case-insensitive keyword to filter responses by.

        Returns
        -------
        list
            List of prompt-response pairs where the response contains the keyword.
        """
        keyword_lower = keyword.lower()
        return [
            entry for entry in self.history
            if keyword_lower in entry["response"].lower()
        ]
