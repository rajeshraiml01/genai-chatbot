from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict):
    """
    Represents the state of the state used in graph.
    
    Attributes:
        messages (list): A list of messages in the conversation.
        graph (object): The graph object representing the conversation flow.
        llm (object): The language model used for generating responses.
        user_input (str): The input provided by the user.
    """
    messages: Annotated[list, add_messages]  # type: ignore    