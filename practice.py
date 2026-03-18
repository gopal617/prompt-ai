from helper import get_completion

prompt = """
give step by process so that i can push my code into git repositry :

i had completed my project and now i want to push my code into github by creating new repo;
"""

response = get_completion(prompt)
print(response)