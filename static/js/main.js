// static/js/main.js
// Small progressive-enhancement touches — no framework needed for
// a showcase site like this.

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".contact-form");
  const successMsg = document.getElementById("contact-success");

  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const btn = form.querySelector("button[type='submit']");
      const originalText = btn.textContent;
      btn.disabled = true;
      btn.textContent = "sending...";

      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
        });

        if (response.ok) {
          form.hidden = true;
          if (successMsg) successMsg.hidden = false;
        } else {
          btn.textContent = "something went wrong — try again";
          btn.disabled = false;
        }
      } catch (err) {
        btn.textContent = "something went wrong — try again";
        btn.disabled = false;
      } finally {
        setTimeout(() => {
          if (!form.hidden) btn.textContent = originalText;
        }, 3000);
      }
    });
  }
});
