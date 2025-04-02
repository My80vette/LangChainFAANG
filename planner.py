import uuid
import datetime
import openai
import langchain
from pymongo import MongoClient
# this file is responsible for containing all of the task card creation functions that the agent will need to use

class Resource:
    def __init__(self, title, url):
        self.id = str(uuid.uuid4())
        self.title = title
        self.url = url
        self.resource_type = None
        self.time_estimate = None
        self.completed = False
        self.time_completed = None

    def mark_completion(self):
        self.completed = True
        self.time_completed = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'resource_type': self.resource_type,
            'time_estimate': self.time_estimate,
            'completed': self.completed,
            'time_completed': self.time_completed
        }

class Problem:
    def __init__(self, title, url):
        self.id = str(uuid.uuid4())
        self.title = title
        self.url = url
        self.difficulty = None
        self.time_estimate = None
        self.completed = False
        self.time_completed = None

    def mark_completion(self):
        self.completed = True
        self.time_completed = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'difficulty': self.difficulty,
            'time_estimate': self.time_estimate,
            'completed': self.completed,
            'time_completed': self.time_completed
        }

class TaskCard:
    def __init__(self, id, topic, description):
        self.id = id
        self.topic = topic
        self.description = description
        self.resources = []
        self.problems = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.status = 'incomplete'
    
    def add_resource(self, resource):
        self.resources.append(resource)

    def add_problem(self, problem):
        self.problems.append(problem)

    def remove_resource(self, resource):
        self.resources.remove(resource)

    def remove_problem(self, problem):
        self.problem.remove(problem)

    def get_completion_percentage(self):
        total_items = len(self.resources) + len(self.problems)
        if total_items == 0:
            return 0
        completed_resources = sum(1 for resource in self.resources if resource.completed)
        completed_problems = sum(1 for problem in self.problems if problem.completed)
        completed_items = completed_resources + completed_problems
        return (completed_items / total_items) * 100

    def mark_resource_completed(self, resource):
        resource.mark_completion()

    def mark_problem_completed(self, problem):
        problem.mark_completion()

    def update_status(self, status):
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'description': self.description,
            'resources': [resource.to_dict() for resource in self.resources],
            'problems': [problem.to_dict() for problem in self.problems],
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status': self.status
        }
    
class Planner:
    def __init__(self, mongo_uri="mongodb://localhost:27017/"):
        # establish MongoDB connection
        self.client = MongoClient(mongo_uri)
        # select the DB we want to connect to
        self.db = self.client.LangChaingFAANG
        # pick the collections we want to access
        self.topics_collection = self.db.topics
        self.resources_collection = self.db.resources
        self.task_cards_collection = self.db.task_cards

    def create_task_card(self, topic, description, available_time):
        # Create a unique ID for the task card
        id = str(uuid.uuid4())
        
        # Create a task card
        task_card = TaskCard(id, topic, description)
        
        # Fetch problems and resources
        problems = self.fetch_problems_for_topic(topic, id, None)  # Get all difficulties
        resources = self.fetch_resources_for_topic(topic, id, None)
        
        # Add resources and problems based on available time
        # This is a simple allocation strategy - in the real implementation, 
        # you would use the LLM to make more intelligent decisions
        
        remaining_time = available_time
        
        # Add resources first (prioritize learning before practice)
        for resource in resources:
            if remaining_time >= resource.time_estimate:
                task_card.add_resource(resource)
                remaining_time -= resource.time_estimate
        
        # Then add problems, starting with easy ones
        sorted_problems = sorted(problems, key=lambda p: {"easy": 1, "medium": 2, "hard": 3}[p.difficulty])
        
        for problem in sorted_problems:
            if remaining_time >= problem.time_estimate:
                task_card.add_problem(problem)
                remaining_time -= problem.time_estimate
        
        return task_card

    def get_available_topics(self):
        # Query the topics collection and retrieve just the names
        topics = self.topics_collection.find({}, {"name": 1, "_id": 0})
        
        # Extract the names into a list
        topic_names = [topic["name"] for topic in topics]
        
        return topic_names

    def fetch_problems_for_topic(self, topic, id=None, difficulty=None):
        # Find the topic in the database
        topic_doc = self.topics_collection.find_one({"name": topic})
        if not topic_doc:
            return []  # Topic not found
        
        # Extract problems dictionary
        problems_dict = topic_doc.get("problems", {})
        
        # Convert the problems dictionary to Problem objects
        problems = []
        
        for title, problem_data in problems_dict.items():
            # For your current structure, problem_data is just the URL
            # But we need to handle both formats - URL as string or as object with URL and difficulty
            
            if isinstance(problem_data, str):
                # Simple format: "Problem Name": "URL"
                url = problem_data
                problem_difficulty = "medium"  # Default if not specified
            else:
                # Object format: "Problem Name": {"url": "URL", "difficulty": "easy"}
                url = problem_data.get("url")
                problem_difficulty = problem_data.get("difficulty", "medium")
            
            # Create a Problem object
            problem = Problem(title, url)
            problem.difficulty = problem_difficulty
            
            # We'll leave time_estimate to be determined by the agent later
            # For now, assign a rough estimate based on difficulty
            if problem_difficulty == "easy":
                problem.time_estimate = 25
            elif problem_difficulty == "medium":
                problem.time_estimate = 40
            else:  # hard
                problem.time_estimate = 55
            
            # Filter by difficulty if specified
            if difficulty and problem.difficulty != difficulty:
                continue
                
            problems.append(problem)
        
        return problems

    def fetch_resources_for_topic(self, topic, id, difficulty):
        # This would eventually call an API to get resources
        # For now, return mock data
        
        # Create some mock resources
        mock_resources = {
            "Array / String": [
                {"title": "Introduction to Arrays", "url": "https://example.com/arrays-intro", "resource_type": "article", "time_estimate": 15},
                {"title": "Array Manipulation Techniques", "url": "https://example.com/array-techniques", "resource_type": "article", "time_estimate": 20},
                {"title": "Two Pointers Technique", "url": "https://example.com/two-pointers", "resource_type": "video", "time_estimate": 25}
            ],
            "Two Pointers": [
                {"title": "Linked List Basics", "url": "https://example.com/linkedlist-basics", "resource_type": "article", "time_estimate": 15},
                {"title": "Reversing a Linked List", "url": "https://example.com/reverse-linkedlist", "resource_type": "video", "time_estimate": 20}
            ]
        }
        
        # Return resources for the requested topic
        if topic in mock_resources:
            resources_data = mock_resources[topic]
            
            # Convert to Resource objects
            resources = []
            for r_data in resources_data:
                resource = Resource(r_data["title"], r_data["url"])
                resource.resource_type = r_data["resource_type"]
                resource.time_estimate = r_data["time_estimate"]
                resources.append(resource)
            
            return resources
        else:
            return []  # No resources found for this topic

    def reccomend_next_steps(self, curent_card, available_time):
        #We need to make an API call here to plan which tasks on the card we are 'assigned' for the session
        pass
    
    def save_task_card(self, TaskCard):
        # save the TaskCard object 'task_card' in the DB (the card should be complete upon instertion)
        try:
            card_dict = TaskCard.to_dict()
            result = self.task_cards_collection.insert_one(card_dict)
            return result.acknowledged
        except Exception as FuckSomethingBroke:
            print(f"Error Saving Task Card:  {FuckSomethingBroke}")
        pass

    def get_task_card(self, card_id):
        card_dict = self.task_cards_collection.find_one({"id": card_id})
        if not card_dict:
            return None
        
    def mark_card_complete(self, task_card):
        # Check if all resources and problems are completed
        all_resources_complete = all(resource.completed for resource in task_card.resources)
        all_problems_complete = all(problem.completed for problem in task_card.problems)
        
        if not (all_resources_complete and all_problems_complete):
            return False
        
        # Update the card's status and timestamp
        task_card.status = 'complete'
        task_card.updated_at = datetime.datetime.now()
        
        try:
            # Update the card in the database
            result = self.task_cards_collection.update_one(
                {"id": task_card.id},
                {"$set": task_card.to_dict()}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating task card status: {e}")
            return False
