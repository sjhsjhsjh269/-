document.getElementById('send-btn').addEventListener('click', async () => {
    const inputElement = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const userInput = inputElement.value.trim();
    
    if (userInput === '') return;

    // Display user input
    chatBox.innerHTML += `<div>User: ${userInput}</div>`;
    inputElement.value = '';

    try {
        // Call the server to get a response from the AI
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: userInput }),
        });
        const data = await response.json();
        
        // Display AI response
        chatBox.innerHTML += `<div>AI: ${data.output}</div>`;
    } catch (error) {
        console.error('Error:', error);
        chatBox.innerHTML += `<div>AI: Sorry, something went wrong.</div>`;
    }

    // Scroll to the bottom of the chat
    chatBox.scrollTop = chatBox.scrollHeight;
});
