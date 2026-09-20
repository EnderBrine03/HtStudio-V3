document.getElementById("btn").addEventListener("click", () => {
  document.getElementById("out").textContent =
    "JS çalışıyor · " + new Date().toLocaleTimeString("tr-TR");
});
