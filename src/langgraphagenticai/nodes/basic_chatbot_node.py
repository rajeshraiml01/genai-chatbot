from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a LangGraph workflow.
    This node is designed to handle simple chat interactions.
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        Processes the input state and generate a chatbot response.
                
        """
        return {"message":self.llm.invoke(state["messages"])}