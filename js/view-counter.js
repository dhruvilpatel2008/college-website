document.addEventListener("DOMContentLoaded", () => {
  const counter = document.getElementById("view-counter");
  if (!counter) return;

  const namespace = "dhruvil-portfolio-2026"; // unique
  const key = "visits";

  fetch(`https://api.countapi.xyz/update/${namespace}/${key}?amount=1`)
    .then(res => res.json())
    .then(data => {
      counter.textContent = `👁️ Visitors: ${data.value}`;
    })
    .catch(err => {
      console.error("Counter error:", err);
      counter.textContent = "👁️ Visitors: 0";
    });
});
