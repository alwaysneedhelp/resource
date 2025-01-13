// cards.js

document.getElementById('membersBtn').addEventListener('click', function() {
  const popup = document.getElementById('cardPopup');
  popup.style.display = 'flex'; // Show the popup
});

// Close functionality when clicking outside the popup
document.getElementById('cardPopup').addEventListener('click', function(event) {
  if (event.target === this) {
      this.style.display = 'none'; // Hide the popup when clicking outside
  }
});