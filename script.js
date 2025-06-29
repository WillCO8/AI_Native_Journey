// ===== ROCK PAPER SCISSORS =====
let rpsOptions = {
  classic: ["rock", "paper", "scissors"],
  fun: ["The Rock", "Toilet Paper", "Edward Scissorhands"],
  custom: []
};

document.getElementById("rps-mode").addEventListener("change", function () {
  const mode = this.value;
  document.getElementById("custom-inputs").style.display = mode === "custom" ? "block" : "none";
  createRPSButtons(mode === "custom" ? rpsOptions.custom : rpsOptions[mode]);
});

document.getElementById("apply-custom").addEventListener("click", function () {
  rpsOptions.custom = [
    document.getElementById("custom1").value,
    document.getElementById("custom2").value,
    document.getElementById("custom3").value
  ];
  createRPSButtons(rpsOptions.custom);
});

let rpsScore = { player: 0, computer: 0 };

function createRPSButtons(options) {
  const area = document.getElementById("rps-game-area");
  area.innerHTML = "";
  options.forEach(option => {
    const btn = document.createElement("button");
    btn.textContent = option;
    btn.onclick = () => playRPS(option, options);
    area.appendChild(btn);
  });
}

function playRPS(playerChoice, options) {
  const computerChoice = options[Math.floor(Math.random() * options.length)];
  let result = "";

  if (playerChoice === computerChoice) {
    result = "It's a tie!";
  } else if (
    (playerChoice === options[0] && computerChoice === options[2]) ||
    (playerChoice === options[1] && computerChoice === options[0]) ||
    (playerChoice === options[2] && computerChoice === options[1])
  ) {
    rpsScore.player++;
    result = `You win this round! ${playerChoice} beats ${computerChoice}`;
  } else {
    rpsScore.computer++;
    result = `Computer wins this round! ${computerChoice} beats ${playerChoice}`;
  }

  if (rpsScore.player === 2) {
    result += " — 🎉 You won best of 3!";
    rpsScore = { player: 0, computer: 0 };
  } else if (rpsScore.computer === 2) {
    result += " — 😞 Computer won best of 3.";
    rpsScore = { player: 0, computer: 0 };
  }

  document.getElementById("rps-result").textContent = result;
}

// ===== ODDS AND EVENS =====
let oeScore = { player: 0, computer: 0 };

document.getElementById("oe-mode").addEventListener("change", function () {
  const mode = this.value;
  document.getElementById("oe-custom-inputs").style.display = mode === "custom" ? "block" : "none";
});

document.getElementById("oe-apply-custom").addEventListener("click", function () {
  document.getElementById("oe-choose-odd").textContent = document.getElementById("oe-custom-odd").value || "Odd";
  document.getElementById("oe-choose-even").textContent = document.getElementById("oe-custom-even").value || "Even";
});

["oe-choose-odd", "oe-choose-even"].forEach(id => {
  document.getElementById(id).addEventListener("click", function () {
    const mode = document.getElementById("oe-mode").value;
    const playerChoice = this.textContent;
    const computerNumber = Math.floor(Math.random() * 10) + 1;
    const total = computerNumber + 1;
    const isEven = total % 2 === 0;
    const result = (isEven && playerChoice.toLowerCase().includes("even")) ||
                   (!isEven && playerChoice.toLowerCase().includes("odd")) ?
      "You win this round!" : "Computer wins this round!";

    if (result.includes("You")) oeScore.player++;
    else oeScore.computer++;

    let summary = `${result} (Computer chose ${computerNumber})`;

    if (oeScore.player === 2) {
      summary += " — 🎉 You won best of 3!";
      oeScore = { player: 0, computer: 0 };
    } else if (oeScore.computer === 2) {
      summary += " — 😞 Computer won best of 3.";
      oeScore = { player: 0, computer: 0 };
    }

    document.getElementById("oe-result").textContent = summary;
  });
});

// ===== COIN FLIP =====
let cfScore = { player: 0, computer: 0 };

document.getElementById("cf-mode").addEventListener("change", function () {
  const mode = this.value;
  document.getElementById("cf-custom-inputs").style.display = mode === "custom" ? "block" : "none";
  document.getElementById("cf-fun-options").style.display = mode === "fun" ? "block" : "none";
});

document.getElementById("cf-apply-custom").addEventListener("click", function () {
  const option1 = document.getElementById("cf-custom-heads").value || "Option 1";
  const option2 = document.getElementById("cf-custom-tails").value || "Option 2";
  flipCoin(option1, option2);
});

document.getElementById("cf-flip-btn").addEventListener("click", function () {
  const mode = document.getElementById("cf-mode").value;
  let option1 = "Heads", option2 = "Tails";

  if (mode === "fun") {
    const rivalry = document.getElementById("cf-fun-select").value;
    if (rivalry === "2pac-biggie") {
      option1 = "2Pac"; option2 = "Biggie";
    } else if (rivalry === "kendrick-drake") {
      option1 = "Kendrick"; option2 = "Drake";
    } else if (rivalry === "jim-nas") {
      option1 = "Jim Jones"; option2 = "Nas";
    }
  } else if (mode === "custom") {
    option1 = document.getElementById("cf-custom-heads").value || "Option 1";
    option2 = document.getElementById("cf-custom-tails").value || "Option 2";
  }

  flipCoin(option1, option2);
});

function flipCoin(option1, option2) {
  const result = Math.random() < 0.5 ? option1 : option2;
  result.includes(option1) ? cfScore.player++ : cfScore.computer++;

  let text = `${result} wins this round!`;

  if (cfScore.player === 2) {
    text += " — 🎉 You won best of 3!";
    cfScore = { player: 0, computer: 0 };
  } else if (cfScore.computer === 2) {
    text += " — 😞 Computer won best of 3.";
    cfScore = { player: 0, computer: 0 };
  }

  document.getElementById("cf-result").textContent = text;
}
