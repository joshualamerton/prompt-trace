import pytest
from . import prompt_tracer  # Import the module under test

class TestPromptTracer:
    def test_init(self):
        """Test that PromptTracer initializes correctly."""
        tracer = prompt_tracer.PromptTracer()
        assert tracer.history == []

    def test_record_interaction(self):
        """Test that record_interaction records an interaction correctly."""
        tracer = prompt_tracer.PromptTracer()
        tracer.record_interaction("What is your name?", "John Doe")
        assert len(tracer.history) == 1
        assert tracer.history[0]["prompt"] == "What is your name?"
        assert tracer.history[0]["response"] == "John Doe"

    def test_record_interaction_multiple(self):
        """Test that record_interaction records multiple interactions correctly."""
        tracer = prompt_tracer.PromptTracer()
        tracer.record_interaction("What is your name?", "John Doe")
        tracer.record_interaction("How old are you?", "30")
        assert len(tracer.history) == 2
        assert tracer.history[0]["prompt"] == "What is your name?"
        assert tracer.history[0]["response"] == "John Doe"
        assert tracer.history[1]["prompt"] == "How old are you?"
        assert tracer.history[1]["response"] == "30"

    def test_get_interaction_history(self):
        """Test that get_interaction_history returns the complete history."""
        tracer = prompt_tracer.PromptTracer()
        tracer.record_interaction("What is your name?", "John Doe")
        tracer.record_interaction("How old are you?", "30")
        assert tracer.get_interaction_history() == [{"prompt": "What is your name?", "response": "John Doe"}, {"prompt": "How old are you?", "response": "30"}]

    def test_get_interaction_history_empty(self):
        """Test that get_interaction_history returns an empty list when no interactions have been recorded."""
        tracer = prompt_tracer.PromptTracer()
        assert tracer.get_interaction_history() == []

    def test_record_interaction_invalid_prompt(self):
        """Test that record_interaction handles an invalid prompt correctly."""
        tracer = prompt_tracer.PromptTracer()
        with pytest.raises(TypeError):
            tracer.record_interaction(123, "John Doe")

    def test_record_interaction_invalid_response(self):
        """Test that record_interaction handles an invalid response correctly."""
        tracer = prompt_tracer.PromptTracer()
        with pytest.raises(TypeError):
            tracer.record_interaction("What is your name?", 123)

    def test_record_interaction_none_prompt(self):
        """Test that record_interaction handles a None prompt correctly."""
        tracer = prompt_tracer.PromptTracer()
        with pytest.raises(TypeError):
            tracer.record_interaction(None, "John Doe")

    def test_record_interaction_none_response(self):
        """Test that record_interaction handles a None response correctly."""
        tracer = prompt_tracer.PromptTracer()
        with pytest.raises(TypeError):
            tracer.record_interaction("What is your name?", None)