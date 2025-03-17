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
        --primary-pink: #e42fbd;
        --bg-light: #f8f9fa;
        --card-border: rgba(174, 68, 213, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--primary-blue), var(--primary-purple));
    }
    
    /* Card styling */
    .study-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid var(--primary-purple);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom container styling */
    .stButton>button {
        background-color: var(--primary-blue);
        color: white;
    }
    
    .chat-container {
        border-radius: 10px;
        background: var(--bg-light);
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎯 Learning Assistant")
    st.markdown("---")
    
    # Navigation
    selected = st.radio(
        "Navigation",
        ["💭 Chat", "📈 Progress", "📚 Resources", "⚙️ Settings"]
    )

# Main layout with columns
col1, col2 = st.columns([2, 1])

# Main chat area
with col1:
    st.header("Chat with Your Learning Assistant")
    
    # Chat container
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        # Placeholder for chat messages
        st.empty()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Input area
    user_input = st.text_input("Ask me anything...", key="user_input")
    col1_1, col1_2 = st.columns([4, 1])
    with col1_2:
        st.button("Send", use_container_width=True)

# Study plan cards column
with col2:
    st.header("Today's Study Plan")
    
    # Example study cards (you can make this dynamic)
    study_cards = [
        {
            "title": "Arrays & Two Pointers",
            "time": "45 minutes",
            "description": "Learn how to efficiently solve problems using the two pointers technique.",
            "resources": [
                "📄 Two Pointers Technique - Article",
                "🎥 Visual Explanation of Two Pointers"
            ],
            "practice": [
                "🧩 LeetCode #1: Two Sum",
                "🧩 LeetCode #15: 3Sum"
            ]
        },
        # Add more cards as needed
    ]
    
    # Display cards
    for card in study_cards:
        st.markdown(f"""
        <div class="study-card">
            <h3>{card['title']}</h3>
            <p>⏱️ Estimated time: {card['time']}</p>
            <p>{card['description']}</p>
            <h4>Resources:</h4>
            <ul>
                {"".join(f"<li>{resource}</li>" for resource in card['resources'])}
            </ul>
            <h4>Practice Problems:</h4>
            <ul>
                {"".join(f"<li>{problem}</li>" for problem in card['practice'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)