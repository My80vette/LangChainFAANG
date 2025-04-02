from config import claude_llm, claude_client
from planner import Resource, Problem, TaskCard, Planner
from langchain.prompts import ChatPromptTemplate



class DailyGrindAgent:
    def __init__(self):
        self.planner = Planner()
    
    def pick_response_type(self, message):
        """ 
        This function will determine what the bot needs to do based on the message 
        For example, if there is no active card, we should be trying to create a new one.
        If there is an active card, and we dont have our time available for this session, we need to find it so we can generate a plan.
        If there is an active card and we have our time available, and the user ask us something, its probably a question, so we need more
        resource centric responses/web based responses.

        This function is going to need context, but we are calling it everytime we chat so we gotta do this shit efficiently
        we will make a drawio file and do the data flow, then we can see if we cant leverage AI to assist us in the function design
        """
        pass

    def parse_time_availability(self, message):
        # Extract available study time from natural language input
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an AI that extracts the available study time from user messages. Extract the number of hours or minutes the user has available to study. only return the time that the user has available, nothing else."),
            ("human", message)
        ])
        
        response = claude_llm(prompt.format_messages())
        # Process the response to extract time information
        # For now, return a simple response
        return response.content
    
    def generate_response(self, message):
        self.pick_response_type(message)
        return f"test response given"
