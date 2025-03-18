import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="FAANG Learning Assistant",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main color scheme */
    :root {
        --primary-blue: #3090c0;
        --primary-purple: #ae44d5;
    }

    /* Global background */
    .stApp {
        background: linear-gradient(135deg, #f5f0ff, #e8d9ff);
    }

    /* Scrollable container for study cards */
    .scrollable-cards {
        max-height: calc(100vh - 100px);
        overflow-y: auto;
        padding-right: 10px;
    }

    /* Card styling */
    .study-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 10px;
        border-left: 4px solid var(--primary-purple);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* View more tasks button */
    .task-button button {
        background: white !important;
        border-radius: 10px !important;
        padding: 15px 0 !important;
        border: 2px solid var(--primary-purple) !important;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #333 !important;
        font-weight: 600 !important;
        box-shadow: none !important;
    }

    .task-button button:hover {
        background: #f0e6ff !important;
        box-shadow: 0 4px 8px rgba(174, 68, 213, 0.2) !important;
    }

    /* Link styling */
    .resource-link, .practice-link {
        color: var(--primary-blue);
        text-decoration: none;
    }

    /* Chat messages styling */
    .chat-area {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        height: calc(100vh - 230px);
        overflow-y: auto;
    }

    .message {
        padding: 10px 15px;
        border-radius: 18px;
        margin-bottom: 10px;
        max-width: 75%;
        word-wrap: break-word;
    }

    .user-message {
        background-color: var(--primary-blue);
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 5px;
    }

    .assistant-message {
        background-color: #e1e1e1;
        color: #333;
        margin-right: auto;
        border-bottom-left-radius: 5px;
    }
    
    /* Send button styling */
    .stButton > button {
        background-color: var(--primary-blue);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to handle sending messages
def send_message():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        
        # Simulate assistant response (replace with actual logic later)
        assistant_response = f"Hello! I received your message: '{user_message}'"
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
        
        # Clear the input field
        st.session_state.user_input = ""

# Sidebar
with st.sidebar:
    st.title("🎯 Learning Assistant")
    st.markdown("---")

    selected = st.radio(
        "Navigation",
        ["💭 Chat", "📈 Progress", "📚 Resources", "⚙️ Settings"]
    )

# Main layout with columns
col1, col2 = st.columns([2, 1], gap="small")

# Main chat area
with col1:
    st.header("Chat with Your Learning Assistant")
    
    # Chat messages area
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="message user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input and send button in a row
    cols = st.columns([4, 1])
    with cols[0]:
        st.text_input("", placeholder="Ask me anything...", key="user_input", on_change=send_message)
    with cols[1]:
        st.button("Send", on_click=send_message)

# Study plan cards column
with col2:
    st.header("Today's Study Plan")

    # Example study cards
    study_cards = [
        {
            "title": "Arrays & Two Pointers",
            "time": "45 minutes",
            "description": "Learn how to efficiently solve problems using the two pointers technique.",
            "resources": [
                {"text": "📄 Two Pointers Technique - Article", "url": "https://example.com/article"},
                {"text": "🎥 Visual Explanation of Two Pointers", "url": "https://example.com/video"}
            ],
            "practice": [
                {"text": "🧩 LeetCode #1: Two Sum", "url": "https://leetcode.com/problems/two-sum"},
                {"text": "🧩 LeetCode #15: 3Sum", "url": "https://leetcode.com/problems/3sum"}
            ]
        },
        {
            "title": "Linked Lists",
            "time": "60 minutes",
            "description": "Understand the fundamentals of linked lists and their operations.",
            "resources": [
                {"text": "📄 Linked List Basics", "url": "https://example.com/linked-lists"},
                {"text": "🎥 Visualizing Linked List Operations", "url": "https://example.com/linked-list-video"}
            ],
            "practice": [
                {"text": "🧩 LeetCode #206: Reverse Linked List", "url": "https://leetcode.com/problems/reverse-linked-list"},
                {"text": "🧩 LeetCode #21: Merge Two Sorted Lists", "url": "https://leetcode.com/problems/merge-two-sorted-lists"}
            ]
        },
        {
            "title": "Binary Trees",
            "time": "75 minutes",
            "description": "Explore binary trees and common traversal methods.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Graph Algorithms",
            "time": "90 minutes",
            "description": "Learn about BFS, DFS, and Dijkstra's algorithm.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Dynamic Programming",
            "time": "120 minutes",
            "description": "Master memoization and bottom-up approaches.",
            "resources": [],
            "practice": []
        },
        {
            "title": "System Design",
            "time": "60 minutes",
            "description": "Learn how to design scalable systems.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Behavioral Interview Prep",
            "time": "60 minutes",
            "description": "Practice STAR method responses.",
            "resources": [],
            "practice": []
        },
    ]

    # Create scrollable container
    st.markdown('<div class="scrollable-cards">', unsafe_allow_html=True)

    # Add session state to track if cards are expanded or collapsed
    if 'show_all_cards' not in st.session_state:
        st.session_state.show_all_cards = False

    # Display the first card regardless
    if study_cards:
        first_card = study_cards[0]
        st.markdown(f"""
        <div class="study-card">
            <h3>{first_card['title']}</h3>
            <p>⏱️ Estimated time: {first_card['time']}</p>
            <p>{first_card['description']}</p>
            <h4>Resources:</h4>
            <ul>
                {"".join(f'<li><a href="{resource["url"]}" target="_blank" class="resource-link">{resource["text"]}</a></li>' for resource in first_card['resources']) if first_card['resources'] else '<li>No resources available</li>'}
            </ul>
            <h4>Practice Problems:</h4>
            <ul>
                {"".join(f'<li><a href="{problem["url"]}" target="_blank" class="practice-link">{problem["text"]}</a></li>' for problem in first_card['practice']) if first_card['practice'] else '<li>No practice problems available</li>'}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Show "View X Other Tasks" button if there are more than 1 cards
    remaining_cards = len(study_cards) - 1
    if remaining_cards > 0:
        view_more_text = f"View {remaining_cards} Other Tasks" if not st.session_state.show_all_cards else "Hide Other Tasks"

        # Add a class to target this button specifically
        st.markdown('<div class="task-button">', unsafe_allow_html=True)
        if st.button(f"📚 {view_more_text} 📚", key="view_more_button", use_container_width=True):
            st.session_state.show_all_cards = not st.session_state.show_all_cards
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Display the remaining cards if expanded
        if st.session_state.show_all_cards:
            for card in study_cards[1:]:
                st.markdown(f"""
                <div class="study-card">
                    <h3>{card['title']}</h3>
                    <p>⏱️ Estimated time: {card['time']}</p>
                    <p>{card['description']}</p>
                    <h4>Resources:</h4>
                    <ul>
                        {"".join(f'<li><a href="{resource["url"]}" target="_blank" class="resource-link">{resource["text"]}</a></li>' for resource in card['resources']) if card['resources'] else '<li>No resources available</li>'}
                    </ul>
                    <h4>Practice Problems:</h4>
                    <ul>
                        {"".join(f'<li><a href="{problem["url"]}" target="_blank" class="practice-link">{problem["text"]}</a></li>' for problem in card['practice']) if card['practice'] else '<li>No practice problems available</li>'}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    # Close container
    st.markdown('</div>', unsafe_allow_html=True)