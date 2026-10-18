(function () {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  if (window.location.search.includes("sent=1")) {
    document.getElementById("form-success")?.classList.add("visible");
  }

  const toggle = document.querySelector(".menu-toggle");
  const menu = document.getElementById("site-menu");
  const label = toggle?.querySelector(".menu-toggle-label");

  function setMenuOpen(open) {
    if (!toggle || !menu) return;
    toggle.setAttribute("aria-expanded", String(open));
    menu.classList.toggle("is-open", open);
    menu.hidden = !open;
    document.body.classList.toggle("menu-open", open);
    if (label) label.textContent = open ? "Sulje valikko" : "Avaa valikko";
  }

  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      setMenuOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") setMenuOpen(false);
    });

    menu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setMenuOpen(false));
    });
  }

  const file = (window.location.pathname.split("/").pop() || "index.html").replace(
    /^$/,
    "index.html"
  );
  document.querySelectorAll('.site-menu a, .nav a[href$=".html"], .nav a[href^="index.html"]').forEach(
    (link) => {
      const href = (link.getAttribute("href") || "").split("#")[0];
      if (href === file || (file === "index.html" && (href === "" || href === "/" || href === "index.html"))) {
        link.setAttribute("aria-current", "page");
      }
    }
  );
})();
