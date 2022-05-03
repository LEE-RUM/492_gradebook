const allModals = document.querySelectorAll("[data-type='modal']");

allModals.forEach(modal => {
    const overlay = modal.querySelector(".overlay");
    overlay.addEventListener("click", (e) => {
        modal.classList.toggle("hide", true);
    })
})

const allModalsTogglers = document.querySelectorAll("[data-modal]");

allModalsTogglers.forEach(btn => {
    btn.addEventListener("click", (e) => {
        const modalQuery = btn.getAttribute("data-modal");
        const modal = document.querySelector(modalQuery);
        modal.classList.toggle("hide", false);
    });
})