from helper import get_completion

prompt = """
you act as a ai-fitness coach:
task: explain importance of fitness in short.
"""

response = get_completion(prompt)
print(prompt)
print("-"*50)
print(response)