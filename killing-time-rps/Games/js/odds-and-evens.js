console.log("🎯 Odds and Evens - Best of 3 (Gods vs Demons + Custom)");

const oeMode = document.getElementById("oe-mode");
const oeResult = document.getElementById("oe-result");

const oeOddBtn = document.getElementById("oe-choose-odd");
const oeEvenBtn = document.getElementById("oe-choose-even");

const oeCustomInputs = document.getElementById("oe-custom-inputs");
const oeCustomOdd = document.getElementById("oe-custom-odd");
const oeCustomEven = document.getElementById("oe-custom-even");
const oeApplyBtn = document.getElementById("oe-apply-custom");

let oeLabels = {
  classic: ["Odd", "Even"],
  fun: ["Gods", "Demons"],
  custom: ["Odd", "Even"]
};

let oePlayerScore = 0;
let oeComputerScore = 0;
let oeGameOver = false;
let currentLabels = oeLabels.classic;

function updateOEButtonLabels() {
  const [oddLabel, evenLabel] = currentLabels;
  oeOddBtn.textContent = oddLabel;
  oeEvenBtn.textContent = evenLabel;
}

function resetOESimpleGame() {
  oePlayerScore = 0;
  oeComputerScore = 0;
  oeGameOver = false;

  const mode = oeMode.value;
  if (mode === "classic") {
    currentLabels = oeLabels.classic;
    oeCustomInputs.style.display = "none";
  } else if (mode === "fun") {
    currentLabels = oeLabels.fun;
    oeCustomInputs.style.display = "none";
  } else {
    currentLabels = oeLabels.custom;
    oeCustomInputs.style.display = "block";
  }

  updateOEButtonLabels();

  oeResult.innerHTML = "Choose Odd or Even to begin (first to 2 wins).";
}

function playSimpleOERound(playerGuess) {
  if (oeGameOver) return;

  const playerNum = Math.floor(Math.random() * 5) + 1;
  const computerNum = Math.floor(Math.random() * 5) + 1;
  const total = playerNum + computerNum;
  const sumIsEven = total % 2 === 0;
  const actual = sumIsEven ? "even" : "odd";

  const [oddLabel, evenLabel] = currentLabels;
  const guessLabel = playerGuess === "odd" ? oddLabel : evenLabel;
  const actualLabel = sumIsEven ? evenLabel : oddLabel;

  let resultText = `
    You chose <strong>${guessLabel}</strong><br>
    You rolled ${playerNum}, computer rolled ${computerNum}<br>
    Total: ${total} → <strong>${actualLabel}</strong><br>
  `;

  if (playerGuess === actual) {
    oePlayerScore++;
    resultText += "✅ You win this round!";
  } else {
    oeComputerScore++;
    resultText += "❌ Computer wins this round!";
  }

  resultText += `<br>Score — You: ${oePlayerScore} | Computer: ${oeComputerScore}`;

  if (oePlayerScore === 2 || oeComputerScore === 2) {
    oeGameOver = true;
    resultText += `<br><strong>${oePlayerScore === 2 ? "🎉 You" : "🤖 Computer"} win the game!</strong><br><button id="oe-restart">Play Again</button>`;
  }

  oeResult.innerHTML = resultText;

  if (oeGameOver) {
    document.getElementById("oe-restart").addEventListener("click", resetOESimpleGame);
  }
}

// Button handlers
oeOddBtn.addEventListener("click", () => playSimpleOERound("odd"));
oeEvenBtn.addEventListener("click", () => playSimpleOERound("even"));

// Mode switch logic
oeMode.addEventListener("change", resetOESimpleGame);

// Apply custom labels
oeApplyBtn.addEventListener("click", () => {
  const odd = oeCustomOdd.value.trim() || "Odd";
  const even = oeCustomEven.value.trim() || "Even";
  oeLabels.custom = [odd, even];
  currentLabels = oeLabels.custom;
  updateOEButtonLabels(); // 👈 this was missing!
  oeResult.innerHTML = "Custom labels applied. Choose to play!";
});

// Init
resetOESimpleGame();