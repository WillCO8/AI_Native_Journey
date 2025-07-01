document.getElementById("thought-form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const category = document.getElementById("category").value;
  const entry = document.getElementById("entry").value;

  if (!entry.trim()) {
    document.getElementById("confirmation").textContent = "Please enter something before submitting.";
    return;
  }

  const payload = {
    category: category,
    entry: entry,
  };

  try {
    const response = await fetch("https://script.google.com/macros/s/AKfycbz7YlfY76B8QOIqunKQv2VXKN1D48DbzqHZeYdYdL0Oxv3FZVom06VfHgYJUvwvgH0n/exec", {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    document.getElementById("confirmation").textContent = "Thought submitted successfully!";
    document.getElementById("thought-form").reset();
  } catch (error) {
    console.error("Submission failed", error);
    document.getElementById("confirmation").textContent = "Something went wrong. Please try again.";
  }
});
