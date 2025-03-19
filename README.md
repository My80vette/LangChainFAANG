# Daily Grind: Your Personalized FAANG Interview Prep Agent

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Langchain](https://img.shields.io/badge/Langchain-latest-orange.svg)](https://python.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Project Status: In Progress](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Overview

"Daily Grind" is an autonomous AI agent designed to help aspiring software engineers prepare for technical interviews at FAANG (Meta, Apple, Amazon, Netflix, Google) and similar tech companies. Leveraging the power of Langchain and Large Language Models (LLMs), this agent creates personalized daily study plans focused on mastering the LeetCode Blind 75 problem list and the 15 essential LeetCode patterns.

The agent understands your daily study availability through natural language input, dynamically generates study plans that balance learning new concepts with practicing relevant LeetCode problems, and tracks your progress through the curriculum. By incorporating end-of-day feedback and knowledge checks, "Daily Grind" aims to provide a structured and adaptive learning experience tailored to your individual pace and understanding.

## Key Features

* **Natural Language Schedule Input:** Simply tell the agent how much time you have to study each day using natural language (e.g., "I have 2 hours today").
* **Intelligent Daily Planning:** The agent analyzes your available time and its current understanding of your progress to generate a realistic and achievable study plan.
* **Focus on High-Yield Topics:** The curriculum is centered around the LeetCode Blind 75 and the 15 essential LeetCode patterns, critical for FAANG interview preparation.
* **Resource Curation:** The agent utilizes LLMs to find relevant learning resources (articles, documentation, videos) for each topic.
* **LeetCode Problem Integration:** The daily plan includes specific LeetCode problems to practice based on the day's topic(s).
* **Progress Tracking:** The agent keeps track of completed topics and solved LeetCode problems.
* **Knowledge Checks:** Upon indicating you've learned a topic, the agent will administer short knowledge checks to solidify your understanding.
* **End-of-Day Feedback:** Provide natural language feedback on your progress, allowing the agent to adapt future plans.
* **Simple User Interface:** A straightforward UI (built with Cursor) allows for easy interaction with the agent.

## System Design

1.  **Hardcoded User Goals:** The agent is pre-configured with the LeetCode Blind 75 categories and the 15 essential LeetCode patterns as the `target_topics`. A `leetcode_problem_pool` (likely a JSON object or Python dictionary) maps each topic to a list of relevant LeetCode problem identifiers.

2.  **Daily Schedule Input (Natural Language via UI):** Each day, you inform the agent about your available study time using natural language through the UI.

3.  **Agent's Understanding of Schedule (LLM):** Langchain and an LLM are used to parse your natural language schedule input and extract the estimated study duration.

4.  **Agent State Analysis:** The agent maintains a state including:
    * `target_topics`: The remaining topics to learn.
    * `completed_topics`: Topics you have successfully finished (passed knowledge checks).
    * `completed_problems`: LeetCode problems you have solved, associated with their topics.

5.  **Dynamic Topic and Activity Selection (Time-Aware LLM Planning):** Based on your available time and the current state, the LLM generates a daily study plan, suggesting topics, resources, and LeetCode problems.

6.  **Resource Generation (LLM):** For the selected topic(s), the LLM finds and suggests relevant learning materials.

7.  **End-of-Day Feedback (Natural Language via UI):** You provide feedback on your study session in natural language.

8.  **Agent's Understanding of Feedback (LLM):** The LLM analyzes your feedback to understand your progress.

9.  **Updating State and Knowledge Checks:** When you mark a topic as finished in the UI, the agent presents a knowledge check (LLM-generated). Passing this check moves the topic to `completed_topics` and records the solved problems. The agent adjusts the learning roadmap based on your progress.

10. **Progress Tracking:** The `completed_topics` and `completed_problems` are tracked to visualize your learning journey.

## What's Completed So Far

This section will be updated regularly to showcase the progress of the "Daily Grind" agent.

* **[3/18/24]**: UI setup complete, happy with the basic layout and look, we have a good way to view tasks, and contanerization looks great, so I feel confident in moving forward to the deeper AI integration! Lots of fun new features im thinking of adding!
* **[3/17/24]**: Initial project setup complete. GitHub repository created. Basic file structure established (`agent.py`, `planner.py`, etc.). Langchain library installed.
* **[3/17/24]**: High-level system design flushed out and documented. Understanding of core interactions established.



## Planned Features (Future Enhancements)

* More sophisticated tracking of learning speed and difficulty.
* Integration with LeetCode's API (optional, for direct submission tracking).
* Personalized review schedules for previously completed topics.
* More advanced knowledge check generation and evaluation.
* Potential for user-defined goals beyond the default curriculum.
* Enhanced UI with progress visualizations.
* Data Visualization technique to show progress for portfolio.

## UI Updates

The UI has been redesigned from Streamlit to a custom Flask-based implementation with the following layout:

- Left sidebar (15-25% of screen): Navigation menu for different sections of the app
- Middle section (40-50% of screen): Chat interface with the learning assistant
- Right section: Task cards with the top task displayed and others hidden behind a "View Other Tasks" button

### Features

- Modern, responsive design with a clean interface
- Fixed-size chat window where old messages disappear as they reach the top
- Expandable task list to show additional learning materials
- Interactive elements with smooth animations

### Running the Application

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python main.py
   ```

3. Open your browser and navigate to `http://localhost:5000`
