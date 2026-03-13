```python
class PromptTracer:
    """
    A class to record and track user prompts and responses.
    """

    def __init__(self):
        """
        Initializes a new instance of the PromptTracer class.
        """
        # Initialize an empty list to store the history of prompts and responses
        self.history = []

    def record_interaction(self, prompt: str, response: str) -> None:
        """
        Records a user interaction by storing the prompt and response.

        Args:
            prompt (str): The user's input or question.
            response (str): The system's response to the user's input or question.
        """
        # Create a dictionary to represent the interaction event
        event = {"prompt": prompt, "response": response}
        # Append the event to the history list
        self.history.append(event)
        # Print the event for immediate feedback
        print(event)

    def get_interaction_history(self) -> list:
        """
        Retrieves the complete history of user interactions.

        Returns:
            list: A list of dictionaries, where each dictionary represents an interaction event.
        """
        return self.history
```