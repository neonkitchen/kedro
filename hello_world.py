"""_summary_
https://kedro.readthedocs.io/en/stable/get_started/hello_kedro.html

illustrates kedro concepts
"""

# node - wrapper for python function w/ named inputs, outputs
from kedro.pipeline import node


# Prepare first node
def return_greeting():
    return "Hello"


return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

print("fin")