from config import claude_llm, claude_client
from planner import Resource, Problem, TaskCard, Planner
from langchain.prompts import ChatPromptTemplate



class DailyGrindAgent:
    def __init__(self):
        self.planner = Planner()
        self.availability = None  # Start with no availability
    
    def pick_response_type(self, message):
        """
        Classify user's message and determine appropriate response type
        """
        # Set up classification prompt for Claude
        classification_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a classifier for a programming interview study assistant.
            Analyze the user's message and classify it into exactly ONE of these categories:
            - "Question related to current task": Questions about data structures, algorithms, or programming concepts they're currently studying.
            - "Requesting More Resources": Requests for additional learning materials, exercises, or explanations.
            - "Unrelated Question": Questions not related to data structures, algorithms, or programming interviews.
            - "Unsure How to classify": If the message is ambiguous or you can't confidently classify it.
            
            Return ONLY the category label, nothing else."""),
            ("human", message)
        ])
        
        # Get classification from Claude
        classification = claude_llm.invoke(classification_prompt.format_messages()).content.strip()
        
        # Log the classification for debugging
        print(f"Message classified as: {classification}")
        
        # Handle each classification type
        if "Question related to current task" in classification:
            return self._handle_task_question(message)
        elif "Requesting More Resources" in classification:
            return self._handle_resource_request(message)
        elif "Unrelated Question" in classification:
            return "I'm focused on helping you prepare for coding interviews. Let's stay on topic!"
        else:  # This covers "Unsure How to classify"
            return "I'm not sure I understand. Could you rephrase your question specifically about data structures, algorithms, or coding interview preparation?"
    
    def _handle_task_question(self, message):
        """Handle questions related to current study task"""
        # Here we would use Claude Search or another knowledge base
        # For MVP, we'll use a direct Claude query with context about DS&A
        
        answer_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a programming interview preparation assistant.
            Answer the user's question about data structures, algorithms, or programming interviews.
            Provide concise, accurate information with examples where appropriate.
            If you're not certain about an answer, acknowledge that limitation."""),
            ("human", message)
        ])
        
        response = claude_llm.invoke(answer_prompt.format_messages())
        return response.content

    def _handle_resource_request(self, message):
        """Handle requests for additional learning resources"""
        # Extract the topic from the message
        topic_prompt = ChatPromptTemplate.from_messages([
            ("system", """Extract the main programming or algorithm topic the user is requesting resources for.
            Return only the topic name, nothing else."""),
            ("human", message)
        ])
        
        topic = claude_llm.invoke(topic_prompt.format_messages()).content.strip()
        
        # For MVP, we'll simulate finding resources rather than actually searching the web
        # In a full implementation, you'd use a search API here
        
        resources = []
        
        # Add these resources to the planner
        #for resource in resources:
            #self.planner.add_resource(resource)
        
        return f"I've added some resources about {topic} to your study plan. You can find them in the resources section."
    
    def parse_time_availability(self, message):
        """
        Try to extract time availability from user message
        Returns the time string if found, None otherwise
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an AI that extracts the available study time from user messages.
            Extract the number of hours or minutes the user has available to study. 
            If a specific time is mentioned, return ONLY that time value (e.g. "2 hours").
            If no specific time is mentioned, return "NO_TIME_FOUND"."""),
            ("human", message)
        ])
        
        response = claude_llm.invoke(prompt.format_messages()).content.strip()
        
        # Check if time was found
        if response == "NO_TIME_FOUND":
            return None
        return response
    
    def generate_response(self, message):
        """Main entry point for generating responses to user messages"""
        
        # If we don't have availability yet, focus on getting that first
        if not self.availability:
            # Try to extract time from the current message
            time_available = self.parse_time_availability(message)
            
            if time_available:
                # Great, we have an availability now
                self.availability = time_available
                # Create initial study plan based on time
                plan_message = self._create_study_plan(self.availability)
                return f"Great! I'll create a study plan for {self.availability}.\n\n{plan_message}"
            else:
                # We still don't have availability, ask for it
                return "To create a personalized study plan, I need to know how much time you have available. Could you tell me how many hours or minutes you can study today?"
        
        # If we already have availability, use normal classification
        return self.pick_response_type(message)
    
    def _create_study_plan(self, available_time):
        """Create a basic study plan based on available time"""
        # This would be expanded in the future to create a real study plan
        return "I'll help you make the most of your study time. What topic would you like to focus on?"
