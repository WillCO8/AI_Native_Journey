document.getElementById("thoughtForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const thought = document.getElementById("thought").value.trim();
  const category = document.getElementById("category").value;

  if (thought) {
    fetch("https://script.google.com/macros/s/AKfycbz3YwVCW9RATT60Jp5niAK6P1-PlLEIYEPpu7ZoU03RvjKPWT_QHE2g27YQAWhvR694/exec", {
      method: "POST",
      body: JSON.stringify({ thought, category }),
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then(response => response.text())
    .then(result => {
      alert("Submission successful!");
      document.getElementById("thought").value = ""; // Clear the text area
    })
    .catch(error => {
      alert("Submission failed.");
      console.error("Error:", error);
    });
  } else {
    alert("Please enter something before submitting.");
  }
});
