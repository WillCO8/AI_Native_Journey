console.log("✊ Rock Paper Scissors Loaded");

const rpsMode = document.getElementById("rps-mode");
const rpsGameArea = document.getElementById("rps-game-area");
const rpsResult = document.getElementById("rps-result");
const customInputsDiv = document.getElementById("custom-inputs");

const custom1Input = document.getElementById("custom1") || document.createElement("input");
const custom2Input = document.getElementById("custom2") || document.createElement("input");
const custom3Input = document.getElementById("custom3") || document.createElement("input");
const applyCustomBtn = document.getElementById("apply-custom") || document.createElement("button");

let rpsChoices = ["Rock", "Paper", "Scissors"];
let rpsPlayerScore = 0;
let rpsComputerScore = 0;
let rpsGameOver = false;

function getComputerChoice() {
  return rpsChoices[Math.floor(Math.random() * rpsChoices.length)];
}

function determineWinner(player, computer) {
  const index = rpsChoices.indexOf(player);
  const winAgainst = rpsChoices[(index + 1) % rpsChoices.length];
  if (player === computer) return "tie";
  if (computer === winAgainst) return "lose";
  return "win";
}

function playRPS(playerChoice) {
  if (rpsGameOver) return;

  const computerChoice = getComputerChoice();
  const result = determineWinner(playerChoice, computerChoice);

  let resultText = `You chose <strong>${playerChoice}</strong><br>`;
  resultText += `Computer chose <strong>${computerChoice}</strong><br>`;

  if (result === "tie") {
    resultText += "It's a tie!";
  } else if (result === "win") {
    rpsPlayerScore++;
    resultText += "✅ You win this round!";
  } else {
    rpsComputerScore++;
    resultText += "❌ Computer wins this round!";
  }

  resultText += `<br>Score — You: ${rpsPlayerScore} | Computer: ${rpsComputerScore}`;

  if (rpsPlayerScore === 2 || rpsComputerScore === 2) {
    rpsGameOver = true;
    resultText += `<br><strong>${rpsPlayerScore === 2 ? "🎉 You win the game!" : "🤖 Computer wins the game!"}</strong><br><button id="rps-restart">Play Again</button>`;
  }

  rpsResult.innerHTML = resultText;

  if (rpsGameOver) {
    document.getElementById("rps-restart").addEventListener("click", resetRPSGame);
  }
}

function updateRPSButtons() {
  rpsGameArea.innerHTML = "<p>Make your move:</p>";
  rpsChoices.forEach(choice => {
    const btn = document.createElement("button");
    btn.textContent = choice;
    btn.addEventListener("click", () => playRPS(choice));
    rpsGameArea.appendChild(btn);
  });
}

function resetRPSGame() {
  rpsPlayerScore = 0;
  rpsComputerScore = 0;
  rpsGameOver = false;

  const mode = rpsMode.value;
  if (mode === "classic") {
    rpsChoices = ["Rock", "Paper", "Scissors"];
    customInputsDiv.style.display = "none";
  } else if (mode === "fun") {
    rpsChoices = ["The Rock", "Toilet Paper", "Edward Scissorhands"];
    customInputsDiv.style.display = "none";
  } else {
    rpsChoices = ["Option 1", "Option 2", "Option 3"];
    customInputsDiv.style.display = "block";
  }

  updateRPSButtons();
  rpsResult.innerHTML = "Choose your move to begin!";
}

// Event Listeners
rpsMode.addEventListener("change", resetRPSGame);

applyCustomBtn.addEventListener("click", () => {
  const val1 = custom1Input.value.trim() || "Option 1";
  const val2 = custom2Input.value.trim() || "Option 2";
  const val3 = custom3Input.value.trim() || "Option 3";
  rpsChoices = [val1, val2, val3];
  updateRPSButtons();
  rpsResult.innerHTML = "Custom names applied! Let the game begin.";
});

// Init
resetRPSGame();