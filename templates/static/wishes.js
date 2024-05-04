let currentWishIndex = 0;
let wishes = [];

// Function to fetch wishes from server
async function fetchWishes() {
    const response = await fetch('/wishes');
    wishes = await response.json();
    displayWish();
}

// Function to display wishes
function displayWish() {
    if (wishes.length > 0) {
        const wish = wishes[currentWishIndex];
        const namePlaceholder = document.getElementById('name-placeholder');
        const wishPlaceholder = document.getElementById('wish-placeholder');
        namePlaceholder.textContent = wish.sender_name;
        wishPlaceholder.textContent = wish.message;
    }
}

// Fetch wishes when the page loads
fetchWishes();

// Function to Loop through the wish on click of the "Next" button
document.getElementById('next-wish').addEventListener('click', () => {
    currentWishIndex = (currentWishIndex + 1) % wishes.length;
    displayWish();
});