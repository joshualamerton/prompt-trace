from core.trace import PromptTracer

tracer = PromptTracer()

prompt = "What is the capital of France?"
response = "Paris"

tracer.record(prompt, response)

print("History:", tracer.get_history())
