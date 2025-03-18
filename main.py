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
    return f"Hello! I'm your FAANG Learning Assistant. How can I help you today?"

@app.route('/')
def index():
    return render_template('index.html', tasks=study_tasks)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    response = get_bot_response(user_message)
    
    return jsonify({
        'message': response,
        'timestamp': datetime.now().strftime('%H:%M')
    })

if __name__ == '__main__':
    app.run(debug=True)
