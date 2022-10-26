"""_summary_
https://kedro.readthedocs.io/en/stable/get_started/hello_kedro.html

illustrates kedro concepts
"""

# node - wrapper for python function w/ named inputs, outputs
from kedro.pipeline import node


# Prepare first node
def return_greeting():
    return "Hello"


node1 = node(func=return_greeting, inputs=None, outputs="my_salutation")

# Prepare second node
def join_statements(greeting):
    return f"{greeting} Kedro!"


node2 = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

print("fin")