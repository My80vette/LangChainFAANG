// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const viewMoreTasks = document.getElementById('viewMoreTasks');
const hiddenTasks = document.getElementById('hiddenTasks');

// Event Listeners
sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

if (viewMoreTasks) {
    viewMoreTasks.addEventListener('click', toggleTasks);
}

// Message sending function
function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return;
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Clear input
    userInput.value = '';
    
    // Send to server and get response
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        // Add assistant response to chat
        addMessage(data.message, 'assistant');
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('Sorry, there was an error processing your request.', 'assistant');
    });
}

// Function to add a message to the chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    
    const icon = sender === 'user' ? 'fa-user' : 'fa-robot';
    
    messageDiv.innerHTML = `
        <div class="message-content">
            <i class="fas ${icon} message-icon"></i>
            <div class="message-text">${text}</div>
        </div>
        <div class="message-time">${time}</div>
    `;
    
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    // If the chat is getting too long, remove old messages
    const maxMessages = 50;
    const messages = chatMessages.querySelectorAll('.message');
    if (messages.length > maxMessages) {
        for (let i = 0; i < messages.length - maxMessages; i++) {
            chatMessages.removeChild(messages[i]);
        }
    }
}

// Toggle hidden tasks visibility
function toggleTasks() {
    if (hiddenTasks.style.display === 'block') {
        hiddenTasks.style.display = 'none';
        viewMoreTasks.textContent = `View Other Tasks (${hiddenTasks.childElementCount})`;
    } else {
        hiddenTasks.style.display = 'block';
        viewMoreTasks.textContent = 'Hide Tasks';
    }
} 