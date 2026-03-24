from helper import get_completion

prompt = """
you act as a ai-fitness coach:
task: give 3 months diet plan for reducing weight
context: the person is 23 years old and his weight is 88 kg's and his goal is to reach 75 kg's.
 of weight.
give the diet plan in a table format with 3 colomns:day,breakfast,snacks,lunch,dinner keept it short.
"""

response = get_completion(prompt)
print(prompt)
print("-"*50)
print(response)