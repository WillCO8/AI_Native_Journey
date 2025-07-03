document.getElementById("thought-form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const entry = document.getElementById("thought").value.trim();

  if (!entry) {
    document.getElementById("confirmation").textContent = "Please enter something before submitting.";
    return;
  }

  try {
    await fetch("https://script.google.com/macros/s/AKfycbz7YlfY76B8QOIqunKQv2VXKN1D48DbzqHZeYdYdL0Oxv3FZVom06VfHgYJUvwvgH0n/exec", {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `entry=${encodeURIComponent(entry)}`
    });

    document.getElementById("confirmation").textContent = "Thought submitted successfully!";
    document.getElementById("thought-form").reset();

  } catch (error) {
    console.error("Submission failed", error);
    document.getElementById("confirmation").textContent = "Something went wrong. Please try again.";
  }
});
