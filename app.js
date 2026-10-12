const state = {
  data: null,
  pool: [],
  questions: [],
  currentIndex: 0,
  answeredCount: 0,
  correct: 0,
  wrong: [],
  answered: false,
};

const els = {
  totalCount: document.querySelector("#totalCount"),
  topicSelect: document.querySelector("#topicSelect"),
  wordTypeSelect: document.querySelector("#wordTypeSelect"),
  directionSelect: document.querySelector("#directionSelect"),
  countLabel: document.querySelector("#countLabel"),
  countInput: document.querySelector("#countInput"),
  startButton: document.querySelector("#startButton"),
  progressText: document.querySelector("#progressText"),
  scoreText: document.querySelector("#scoreText"),
  promptLabel: document.querySelector("#promptLabel"),
  promptText: document.querySelector("#promptText"),
  answerForm: document.querySelector("#answerForm"),
  answerInput: document.querySelector("#answerInput"),
  nextButton: document.querySelector("#nextButton"),
  feedback: document.querySelector("#feedback"),
  resultsSection: document.querySelector("#resultsSection"),
  resultSummary: document.querySelector("#resultSummary"),
  wrongList: document.querySelector("#wrongList"),
  retryWrongButton: document.querySelector("#retryWrongButton"),
};

function normalize(value) {
  return String(value).trim().toLowerCase().replace(/\s+/g, " ");
}

function shuffle(items) {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function option(value, label) {
  const el = document.createElement("option");
  el.value = value;
  el.textContent = label;
  return el;
}

function fillControls(data) {
  els.totalCount.textContent = data.total.toLocaleString("de-DE");

  els.topicSelect.append(option("Alle", `Alle Themen (${data.total})`));
  data.topics.forEach((topic) => {
    els.topicSelect.append(option(topic.name, `${topic.name} (${topic.counts.Gesamt})`));
  });

  els.wordTypeSelect.append(option("Alle", "Alle Wortarten"));
  data.wordTypes.forEach((wordType) => {
    const count = data.entries.filter((entry) => entry.wordType === wordType).length;
    els.wordTypeSelect.append(option(wordType, `${wordType} (${count})`));
  });

  updateCountHint();
}

function currentPool() {
  const topic = els.topicSelect.value;
  const wordType = els.wordTypeSelect.value;
  return state.data.entries.filter((entry) => {
    const topicMatches = topic === "Alle" || entry.topic === topic;
    const typeMatches = wordType === "Alle" || entry.wordType === wordType;
    return topicMatches && typeMatches;
  });
}

function updateCountHint() {
  if (!state.data) {
    return;
  }

  const available = currentPool().length;
  els.countLabel.textContent = `Anzahl (max. ${available})`;
  els.countInput.max = String(Math.max(available, 1));

  const currentValue = Number.parseInt(els.countInput.value, 10) || 1;
  if (available > 0 && currentValue > available) {
    els.countInput.value = String(available);
  }
}

function makeQuestion(entry) {
  const direction = els.directionSelect.value;
  if (direction === "de-en") {
    return {
      entry,
      promptLabel: "Deutsch",
      answerLabel: "English",
      prompt: entry.german,
      expected: entry.english,
    };
  }
  return {
    entry,
    promptLabel: "English",
    answerLabel: "Deutsch",
    prompt: entry.english,
    expected: entry.german,
  };
}

function updateStatus() {
  const total = state.questions.length;
  const current = Math.min(state.currentIndex + 1, total);
  els.progressText.textContent = total ? `${current} / ${total}` : "Bereit";
  els.scoreText.textContent = `${state.correct} / ${state.answeredCount}`;
}

function showCurrentQuestion() {
  if (state.currentIndex >= state.questions.length) {
    finishQuiz();
    return;
  }

  const question = state.questions[state.currentIndex];
  els.promptLabel.textContent = `${question.promptLabel} · ${question.entry.wordType} / ${question.entry.topic}`;
  els.promptText.textContent = question.prompt;
  els.answerInput.value = "";
  els.answerInput.placeholder = `${question.answerLabel} eingeben`;
  els.answerInput.disabled = false;
  els.nextButton.disabled = true;
  els.feedback.hidden = true;
  els.feedback.className = "feedback";
  state.answered = false;
  updateStatus();
  els.answerInput.focus();
}

function startQuiz(pool = null) {
  const selected = pool || currentPool();
  if (!selected.length) {
    els.promptText.textContent = "Keine Einträge für diese Auswahl gefunden.";
    return;
  }

  const requestedCount = Number.parseInt(els.countInput.value, 10) || 20;
  const count = Math.max(1, Math.min(requestedCount, selected.length));
  state.pool = selected;
  state.questions = shuffle(selected).slice(0, count).map(makeQuestion);
  state.currentIndex = 0;
  state.answeredCount = 0;
  state.correct = 0;
  state.wrong = [];
  state.answered = false;
  els.resultsSection.hidden = true;
  showCurrentQuestion();
}

function submitAnswer(event) {
  event.preventDefault();
  if (!state.questions.length) {
    startQuiz();
    return;
  }

  if (state.answered) {
    goToNextQuestion();
    return;
  }

  const question = state.questions[state.currentIndex];
  const given = els.answerInput.value;
  const isCorrect = normalize(given) === normalize(question.expected);

  if (isCorrect) {
    state.correct += 1;
    els.feedback.textContent = "Richtig.";
    els.feedback.className = "feedback ok";
  } else {
    state.wrong.push({ question, given });
    els.feedback.textContent = `Falsch. Richtig wäre: ${question.expected}`;
    els.feedback.className = "feedback wrong";
  }

  els.feedback.hidden = false;
  state.answered = true;
  state.answeredCount += 1;
  els.answerInput.disabled = true;
  els.nextButton.disabled = false;
  updateStatus();
  els.answerInput.value = "";
  els.answerInput.placeholder = "Weiter drücken";
}

function goToNextQuestion() {
  if (!state.answered) {
    return;
  }

  state.currentIndex += 1;
  showCurrentQuestion();
}

function finishQuiz() {
  const total = state.questions.length;
  const wrong = state.wrong.length;
  const percent = total ? Math.round((state.correct / total) * 100) : 0;

  els.progressText.textContent = "Fertig";
  els.scoreText.textContent = `${state.correct} / ${total}`;
  els.promptLabel.textContent = "Auswertung";
  els.promptText.textContent = `${percent}% richtig`;
  els.answerInput.disabled = true;
  els.nextButton.disabled = true;
  els.feedback.hidden = true;
  els.resultsSection.hidden = false;
  els.resultSummary.innerHTML = `
    <p><strong>${state.correct}</strong> richtig, <strong>${wrong}</strong> falsch, <strong>${total}</strong> gesamt.</p>
  `;
  els.wrongList.replaceChildren();

  state.wrong.forEach(({ question, given }) => {
    const item = document.createElement("li");
    item.innerHTML = `
      <strong>${question.prompt}</strong><br />
      <span>Richtig: ${question.expected}</span><br />
      <span class="small">Deine Antwort: ${given || "leer"} · ${question.entry.wordType} / ${question.entry.topic}</span>
    `;
    els.wrongList.append(item);
  });

  els.retryWrongButton.disabled = state.wrong.length === 0;
}

async function init() {
  const response = await fetch("dictionary.json");
  state.data = await response.json();
  fillControls(state.data);
  updateStatus();
}

els.startButton.addEventListener("click", () => startQuiz());
els.topicSelect.addEventListener("change", updateCountHint);
els.wordTypeSelect.addEventListener("change", updateCountHint);
els.answerForm.addEventListener("submit", submitAnswer);
els.nextButton.addEventListener("click", goToNextQuestion);
els.retryWrongButton.addEventListener("click", () => {
  const pool = state.wrong.map(({ question }) => question.entry);
  els.countInput.value = String(pool.length);
  startQuiz(pool);
});

init().catch((error) => {
  els.promptText.textContent = "Dictionary konnte nicht geladen werden.";
  els.feedback.hidden = false;
  els.feedback.className = "feedback wrong";
  els.feedback.textContent = error.message;
});
