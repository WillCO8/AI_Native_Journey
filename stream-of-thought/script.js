document.getElementById("thought-form").addEventListener("submit", function(event) {
  event.preventDefault();
  
  const thought = document.getElementById("thought").value;
  console.log("Submitted thought:", thought);

  // You could connect this to Google Apps Script later
  alert("Thought submitted: " + thought);

  // Optionally, clear the form
  document.getElementById("thought-form").reset();
});