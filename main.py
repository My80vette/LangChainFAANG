from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Sample data for tasks (replace with your actual data source)
study_tasks = [
    {
        "title": "Arrays & Two Pointers",
        "time": "2 Hours 45 minutes",
        "description": "Learn how to efficiently solve problems using the two pointers technique.",
        "resources": [
            {"text": "Two Pointers Technique - Article", "url": "#"},
            {"text": "Visual Explanation", "url": "#"}
        ],
        "practice": [
            {"text": "LeetCode #1: Two Sum", "url": "#"},
            {"text": "LeetCode #15: 3Sum", "url": "#"}
        ]
    },
    {
        "title": "Linked Lists",
        "time": "60 minutes",
        "description": "Understand the fundamentals of linked lists and their operations.",
        "resources": [
            {"text": "Linked List Basics", "url": "#"},
            {"text": "Visualizing Linked List Operations", "url": "#"}
        ],
        "practice": [
            {"text": "LeetCode #206: Reverse Linked List", "url": "#"},
            {"text": "LeetCode #21: Merge Two Sorted Lists", "url": "#"}
        ]
    },
    {
        "title": "Binary Trees",
        "time": "75 minutes",
        "description": "Explore binary trees and common traversal methods.",
        "resources": [],
        "practice": []
    }
]

# Sample chat responses (replace with your actual chatbot logic)
def get_bot_response(message):
    return f"Understood, Generating study plan!"

#This is the default directory, when it runs, it calls the index function (when we laod the home page)
@app.route('/')
def index():
    # this is going to load the index.html file, this step right here causes the site to actually load
    return render_template('index.html', tasks=study_tasks)

# A route function dictates what code runs when we call an action on an endpoint
# here we are calling a POST to the /chat endpoint, this code will run when we send a chat to the application
@app.route('/chat', methods=['POST'])
def chat():
    # The prompt will be sent in the body of the POST request
    user_message = request.json.get('message', '')
    # We will pass the prompt to the chatbot and get the response
    # if we want to pass other stuff to the bot, pass it here, and adjust the function prototype for get_bot_response
    response = get_bot_response(user_message)
    # Return a JSON object with the response and a timestamp
    return jsonify({
        'message': response,
        'timestamp': datetime.now().strftime('%H:%M')
    })

if __name__ == '__main__':
    app.run(debug=True)
