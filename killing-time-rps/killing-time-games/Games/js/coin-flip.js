console.log("🪙 Coin Flip Game Loaded");

const cfMode = document.getElementById("cf-mode");
const cfFunSelect = document.getElementById("cf-fun-select");
const cfCustomInputs = document.getElementById("cf-custom-inputs");
const cfFunOptions = document.getElementById("cf-fun-options");

const cfCustomHeads = document.getElementById("cf-custom-heads");
const cfCustomTails = document.getElementById("cf-custom-tails");
const cfApplyCustom = document.getElementById("cf-apply-custom");

const cfFlipBtn = document.getElementById("cf-flip-btn");
const cfResult = document.getElementById("cf-result");

let cfLabels = {
  classic: ["Heads", "Tails"],
  fun: {
    "2pac-biggie": ["2Pac", "Biggie"],
    "kendrick-drake": ["Kendrick", "Drake"],
    "jim-nas": ["Jim Jones", "Nas"]
  },
  custom: ["Option 1", "Option 2"]
};

let cfCurrentLabels = cfLabels.classic;
let cfPlayerScore = 0;
let cfComputerScore = 0;
let cfGameOver = false;

function resetCFGame() {
  cfPlayerScore = 0;
  cfComputerScore = 0;
  cfGameOver = false;

  const mode = cfMode.value;

  if (mode === "classic") {
    cfFunOptions.style.display = "none";
    cfCustomInputs.style.display = "none";
    cfCurrentLabels = cfLabels.classic;
  } else if (mode === "fun") {
    cfFunOptions.style.display = "block";
    cfCustomInputs.style.display = "none";
    const rivalry = cfFunSelect.value;
    cfCurrentLabels = cfLabels.fun[rivalry];
  } else {
    cfFunOptions.style.display = "none";
    cfCustomInputs.style.display = "block";
    cfCurrentLabels = cfLabels.custom;
  }

  cfResult.innerHTML = `Click "Flip Coin" to begin (first to 2 wins).`;
}

function flipCoin() {
  if (cfGameOver) return;

  const result = Math.random() < 0.5 ? 0 : 1;
  const winner = cfCurrentLabels[result];

  if (result === 0) {
    cfPlayerScore++;
  } else {
    cfComputerScore++;
  }

  let resultText = `🪙 The coin landed on <strong>${winner}</strong><br>`;
  resultText += `Score — ${cfCurrentLabels[0]}: ${cfPlayerScore}, ${cfCurrentLabels[1]}: ${cfComputerScore}<br>`;

  if (cfPlayerScore === 2 || cfComputerScore === 2) {
    cfGameOver = true;
    resultText += `<strong>${cfPlayerScore === 2 ? `${cfCurrentLabels[0]} wins! 🏆` : `${cfCurrentLabels[1]} wins! 🏆`}</strong><br>`;
    resultText += `<button id="cf-restart">Play Again</button>`;
  }

  cfResult.innerHTML = resultText;

  if (cfGameOver) {
    document.getElementById("cf-restart").addEventListener("click", resetCFGame);
  }
}

cfMode.addEventListener("change", resetCFGame);
cfFunSelect.addEventListener("change", () => {
  if (cfMode.value === "fun") {
    const rivalry = cfFunSelect.value;
    cfCurrentLabels = cfLabels.fun[rivalry];
    resetCFGame();
  }
});

cfApplyCustom.addEventListener("click", () => {
  const h = cfCustomHeads.value.trim() || "Option 1";
  const t = cfCustomTails.value.trim() || "Option 2";
  cfLabels.custom = [h, t];
  cfCurrentLabels = cfLabels.custom;
  resetCFGame();
});

cfFlipBtn.addEventListener("click", flipCoin);

// Init
resetCFGame();