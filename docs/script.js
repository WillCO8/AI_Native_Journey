<<<<<<< HEAD
document.getElementById("thought-form").addEventListener("submit", async function (e) {
=======
document.getElementById("thought-form").addEventListener("submit", async function(e) {
>>>>>>> bbeba3f2403e71c2db81f18d6d80ab85d623f691
  e.preventDefault();

  const entry = document.getElementById("thought").value.trim();

  if (!entry) {
    document.getElementById("confirmation").textContent = "Please enter something before submitting.";
    return;
  }

  try {
<<<<<<< HEAD
    await fetch("https://script.google.com/macros/s/AKfycbz7YlfY76B8QQIqunKQv2VXKN1D48DbzqHZeYdYdL00xv3FZVom60VfHgYJUvwgH0n/exec", {
=======
    await fetch("https://script.google.com/macros/s/AKfycbz7YlfY76B8QOIqunKQv2VXKN1D48DbzqHZeYdYdL0Oxv3FZVom06VfHgYJUvwvgH0n/exec", {
>>>>>>> bbeba3f2403e71c2db81f18d6d80ab85d623f691
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `entry=${encodeURIComponent(entry)}`
    });

    document.getElementById("confirmation").textContent = "Thought submitted successfully!";
    document.getElementById("thought-form").reset();
<<<<<<< HEAD
=======

>>>>>>> bbeba3f2403e71c2db81f18d6d80ab85d623f691
  } catch (error) {
    console.error("Submission failed", error);
    document.getElementById("confirmation").textContent = "Something went wrong. Please try again.";
  }
<<<<<<< HEAD
});
=======
});
>>>>>>> bbeba3f2403e71c2db81f18d6d80ab85d623f691
