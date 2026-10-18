(function () {
  const PRICING = {
    base: 299,
    includedPages: 3,
    extraPage: 49,
    includedForms: 1,
    extraForm: 39,
    addons: {
      seo: { label: "SEO-perusoptimointi", price: 89 },
      gallery: { label: "Kuvagalleria", price: 59 },
      booking: { label: "Varaus- tai ajanvarauslomake", price: 69 },
      multilang: { label: "Kaksikielinen sivusto (FI + EN)", price: 149 },
      content: { label: "Sisällön kirjoitusapu (max 5 sivua)", price: 199 },
      analytics: { label: "Analytiikka ja evästebanneri", price: 49 },
    },
  };

  const fmt = new Intl.NumberFormat("fi-FI", {
    style: "currency",
    currency: "EUR",
    maximumFractionDigits: 0,
  });

  const form = document.getElementById("order-form");
  if (!form) return;

  const pagesInput = form.querySelector('[name="pages"]');
  const formsInput = form.querySelector('[name="contact_forms"]');
  const summaryLines = document.getElementById("summary-lines");
  const summaryTotal = document.getElementById("summary-total");
  const hiddenTotal = form.querySelector('[name="calculated_total"]');
  const hiddenSummary = form.querySelector('[name="order_summary"]');

  function calculate() {
    const pages = Math.max(1, parseInt(pagesInput.value, 10) || PRICING.includedPages);
    const forms = Math.max(0, parseInt(formsInput.value, 10) || 0);
    const extraPages = Math.max(0, pages - PRICING.includedPages);
    const extraForms = Math.max(0, forms - PRICING.includedForms);

    const lines = [
      { label: "Peruspaketti (3 sivua, 1 lomake)", amount: PRICING.base },
    ];

    if (extraPages > 0) {
      lines.push({
        label: `Lisäsivut (${extraPages} × ${PRICING.extraPage} €)`,
        amount: extraPages * PRICING.extraPage,
      });
    }

    if (extraForms > 0) {
      lines.push({
        label: `Lisälomakkeet (${extraForms} × ${PRICING.extraForm} €)`,
        amount: extraForms * PRICING.extraForm,
      });
    }

    const selectedAddons = [];
    form.querySelectorAll('input[name^="addon_"]:checked').forEach((el) => {
      const key = el.name.replace("addon_", "");
      const addon = PRICING.addons[key];
      if (addon) {
        lines.push({ label: addon.label, amount: addon.price });
        selectedAddons.push(addon.label);
      }
    });

    const total = lines.reduce((sum, line) => sum + line.amount, 0);

    summaryLines.innerHTML = lines
      .map(
        (line) =>
          `<li><span>${line.label}</span><span>${fmt.format(line.amount)}</span></li>`
      )
      .join("");

    summaryTotal.textContent = fmt.format(total);

    if (hiddenTotal) hiddenTotal.value = String(total);
    if (hiddenSummary) {
      hiddenSummary.value = [
        `Sivuja: ${pages}`,
        `Yhteydenottolomakkeita: ${forms}`,
        selectedAddons.length
          ? `Lisäpalvelut: ${selectedAddons.join(", ")}`
          : "Lisäpalvelut: ei valittu",
        `Yhteensä: ${fmt.format(total)} (alv 0 %)`,
      ].join("\n");
    }

    return total;
  }

  form.addEventListener("input", calculate);
  form.addEventListener("change", calculate);

  form.addEventListener("submit", function () {
    calculate();
  });

  document.querySelectorAll("[data-package]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const pkg = JSON.parse(btn.getAttribute("data-package"));
      if (pagesInput && pkg.pages) pagesInput.value = pkg.pages;
      if (formsInput && pkg.forms) formsInput.value = pkg.forms;
      form.querySelectorAll('input[name^="addon_"]').forEach((el) => {
        const key = el.name.replace("addon_", "");
        el.checked = Array.isArray(pkg.addons) && pkg.addons.includes(key);
      });
      if (pkg.industry && form.industry) form.industry.value = pkg.industry;
      calculate();
      document.getElementById("tilaa")?.scrollIntoView({ behavior: "smooth" });
    });
  });

  calculate();
})();

