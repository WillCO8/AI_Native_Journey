console.log("✅ rock-paper-scissors.js has loaded");

const modeSelect = document.getElementById("rps-mode");
const buttons = Array.from(document.querySelectorAll("#rps-game-area button"));
const resultDiv = document.getElementById("rps-result");
const modeOptions = {
  classic: ["Rock", "Paper", "Scissors"],
  fun: ["The Rock", "Toilet Paper", "Edward Scissorhands"],
  custom: ["🪓", "💣", "🧨"]
};

function updateButtonLabels(mode) {
  const labels = modeOptions[mode];
  buttons.forEach((button, index) => {
    button.textContent = labels[index];
  });
}

modeSelect.addEventListener("change", () => {
  updateButtonLabels(modeSelect.value);
});

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const playerChoice = button.textContent;
    const options = modeOptions[modeSelect.value];
    const computerChoice = options[Math.floor(Math.random() * 3)];
    resultDiv.textContent = `You chose ${playerChoice}. Computer chose ${computerChoice}.`;
  });
});

// Initialize on load
updateButtonLabels(modeSelect.value);