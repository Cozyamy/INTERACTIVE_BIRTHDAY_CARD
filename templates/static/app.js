const wishForm = document.getElementById('wish-form');
const senderNameInput = document.getElementById('sender-name');
const wishMessageInput = document.getElementById('wish-message');

// Function to handle form submission
wishForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const sender_name = senderNameInput.value.trim();
    const message = wishMessageInput.value.trim();
    if (sender_name && message) {
        const response = await fetch('/wishes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sender_name, message })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        senderNameInput.value = '';
        wishMessageInput.value = '';

        window.location.href = '../wishes_page';
    }
});