document.getElementById('send-btn').addEventListener('click', function () {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        appendMessage(userInput, 'user');
        document.getElementById('user-input').value = ''; // Clear the input field

        // Send the user input to the Flask backend (via the /ask route)
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput }),
        })
        .then(response => response.json())
        .then(data => {
            appendMessage(data.response, 'bot');
        })
        .catch(error => console.error('Error:', error));
    }
});

// Function to append message to chat log
function appendMessage(message, sender) {
    const chatLog = document.getElementById('chat-log');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(sender);
    messageElement.innerText = message;
    chatLog.appendChild(messageElement);

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Sample suggestions array
const suggestions = [
    "How do I set up a new source in Segment?",
    "How to integrate Segment with Salesforce?",
    "What does mParticle help with?",
    "Tell me about Lytics customer journey features",
    "How does Zeotap improve data security?"
];

// Show suggestions dynamically
document.getElementById('user-input').addEventListener('input', function (e) {
    const input = e.target.value.toLowerCase();
    const filteredSuggestions = suggestions.filter(suggestion => suggestion.toLowerCase().includes(input));
    
    const suggestionBox = document.getElementById('suggestions');
    suggestionBox.innerHTML = '';
    filteredSuggestions.forEach(suggestion => {
        const suggestionElement = document.createElement('div');
        suggestionElement.textContent = suggestion;
        suggestionElement.classList.add('suggestion-item');
        suggestionElement.onclick = () => {
            document.getElementById('user-input').value = suggestion;
            suggestionBox.innerHTML = '';
        };
        suggestionBox.appendChild(suggestionElement);
    });
});
