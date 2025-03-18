import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="FAANG Learning Assistant",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS for styling - DIRECT APPROACH
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

    /* SIMPLE SCROLLABLE CONTAINER - just like popular sites */
    div[data-testid="column"]:nth-of-type(2) {
        height: 100vh;
    }
    
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
    .view-more-tasks {
        background: white;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        border: 2px dashed var(--primary-purple);
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .view-more-tasks:hover {
        background: #f0e6ff;
        box-shadow: 0 4px 8px rgba(174, 68, 213, 0.2);
    }

    /* Link styling */
    .resource-link, .practice-link {
        color: var(--primary-blue);
        text-decoration: none;
    }

    /* Chat container styling */
    .chat-container {
        border-radius: 10px;
        background: white;
        padding: 20px;
        margin: 10px 0;
        min-height: 400px;
    }

    /* Custom Input Container */
    .input-container {
        display: flex;
        position: relative;
        margin-top: 10px;
    }
    
    /* Style for input field */
    .input-container .stTextInput {
        flex-grow: 1;
    }
    
    .input-container input {
        width: 100%;
        padding-right: 100px; /* Make space for the button */
        border-radius: 20px;
        border: 1px solid #ccc;
        padding: 12px 110px 12px 15px;
        height: 46px;
    }
    
    /* Style for button inside input */
    .input-container .stButton {
        position: absolute;
        right: 5px;
        top: 5px;
        margin: 0;
    }
    
    .input-container .stButton button {
        border-radius: 20px;
        padding: 8px 20px;
        background-color: var(--primary-blue);
        color: white;
        border: none;
        height: 36px;
    }
    
    /* Hide the label */
    .input-container .stTextInput > label {
        display: none;
    }
    
    /* Additional styles for the button */
    div[data-testid="stButton"] > button:first-child {
        background-color: var(--primary-blue);
        color: white;
    }
    
    /* Custom style for the view more tasks button */
    .task-button div[data-testid="stButton"] > button:first-child {
        background-color: white;
        color: #333;
        border: 2px solid var(--primary-purple);
        border-radius: 10px;
        padding: 15px 0;
        font-weight: 600;
        box-shadow: none;
    }
    
    .task-button div[data-testid="stButton"] > button:hover {
        background-color: #f0e6ff;
        box-shadow: 0 4px 8px rgba(174, 68, 213, 0.2);
        color: #333;
        border: 2px solid var(--primary-purple);
    }
</style>
""", unsafe_allow_html=True)

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

    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    chat_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

    # Custom input area with button inside
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    user_input = st.text_input("", placeholder="Ask me anything...", key="user_input")
    send_button = st.button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

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
            "description": "Understand the fundamentals of linked lists.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Trees",
            "time": "75 minutes",
            "description": "Explore different types of tree data structures.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Graphs",
            "time": "90 minutes",
            "description": "Learn about graph representations and algorithms.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Dynamic Programming",
            "time": "120 minutes",
            "description": "Master the art of dynamic programming.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Another Topic",
            "time": "60 minutes",
            "description": "Just adding more content.",
            "resources": [],
            "practice": []
        },
        {
            "title": "Yet Another Topic",
            "time": "60 minutes",
            "description": "To ensure scrolling.",
            "resources": [],
            "practice": []
        },
    ]

    # Simple scrollable container - direct approach
    st.markdown('<div class="scrollable-cards">', unsafe_allow_html=True)

    # Add session state to track if cards are expanded or collapsed
    if 'show_all_cards' not in st.session_state:
        st.session_state.show_all_cards = False

    # Define a function to toggle card visibility
    def toggle_cards():
        st.session_state.show_all_cards = not st.session_state.show_all_cards

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
        if st.button(f"📚 {view_more_text} 📚", key="view_more_button", type="primary", use_container_width=True):
            toggle_cards()
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