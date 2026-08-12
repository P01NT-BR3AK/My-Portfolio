// static/js/main.js
// Small progressive-enhancement touches — no framework needed for
// a showcase site like this.

document.addEventListener("DOMContentLoaded", () => {
  // Prevent the placeholder contact form from actually submitting
  // anywhere until a real backend endpoint is wired up.
  const form = document.querySelector(".contact-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const btn = form.querySelector("button[type='submit']");
      const original = btn.textContent;
      btn.textContent = "wire me up first ->";
      setTimeout(() => { btn.textContent = original; }, 1800);
    });
  }
});
