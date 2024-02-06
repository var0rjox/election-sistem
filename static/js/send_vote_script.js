const btn_vote = document.getElementById("btn-vote");
const voteForm = document.getElementById("vote-form");

voteForm.addEventListener("submit", (e) => {
  votingFinished();
});

function getCheckedCandidate() {
  let radios = document.getElementsByName("selected_candidate");
  let selected_candidate = Array.from(radios).find((radio) => radio.checked);

  return { selected_candidate: selected_candidate?.dataset.candidateName };
}

function anyCandidateChecked() {
  const aceptButton = document.createElement("button");
  aceptButton.classList.add("btn", "btn-primary");
  aceptButton.setAttribute("data-bs-dismiss", "modal");
  aceptButton.setAttribute("type", "button");
  aceptButton.innerText = "Aceptar";

  const message = "Seleccione un candidato.";
  const { modal } = createModal(message, [aceptButton]);
  modal.show();
}

function confirmVote(selected_candidate) {
  const cancelButton = document.createElement("button");
  cancelButton.classList.add("btn", "btn-secondary");
  cancelButton.setAttribute("data-bs-dismiss", "modal");
  cancelButton.setAttribute("type", "button");
  cancelButton.innerText = "Cancelar";

  const submitButton = document.createElement("button");
  submitButton.classList.add("btn", "btn-primary");
  submitButton.setAttribute("data-bs-dismiss", "modal");
  submitButton.setAttribute("type", "submit");
  submitButton.innerText = "Enviar";

  const message = `¿Esta seguro de seleccionar a <b>${selected_candidate}</b> para votar?`;
  const { modal } = createModal(message, [cancelButton, submitButton]);
  modal.show();
}

function votingFinished() {
  const message = "Haz finalizado el proceso para emitir tu voto, Gracias";
  const { modal } = createModal(message, [], (closeButton = false));
  modal.show();
  setTimeout(() => {
    modal.hide();
  }, 5000);
}

function createModal(message, buttons, closeButton = true) {
  const bodyModal = document.getElementById("content-modal-body");
  const footerModal = document.getElementById("content-modal-footer");

  bodyModal.innerHTML = message;
  footerModal.innerHTML = "";
  buttons.forEach((button) => {
    footerModal.appendChild(button);
  });

  if (!closeButton) {
    document.getElementById("btn-close-modal").style.display = "none";
  }

  const containerModal = document.getElementById("modal_alert");
  const modal = new bootstrap.Modal(containerModal);
  return { modal };
}

btn_vote.addEventListener("click", () => {
  const { selected_candidate } = getCheckedCandidate();

  if (!selected_candidate) {
    anyCandidateChecked();
    return;
  } else {
    confirmVote(selected_candidate);
  }
});
