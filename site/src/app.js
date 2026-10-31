document.documentElement.lang = "pt-BR";
/* === Configuração === */
const LEAD_ENDPOINT = ""; // Site definitivo: URL do serviço de e-mail/CRM que recebe {nome, telefone, email, criadoEm}.
const CLIENT_PHONE = "(225) 572-4195";

/* Depoimentos: a seção só aparece com pelo menos 1 depoimento real.
   Exemplos de formato, mantidos comentados até o cliente fornecer:
   // { texto: "[PENDENTE: coletar com o cliente]", nome: "[PENDENTE]", fazenda: "[PENDENTE]", regiao: "[PENDENTE]" },
   // { texto: "[PENDENTE: coletar com o cliente]", nome: "[PENDENTE]", fazenda: "[PENDENTE]", regiao: "[PENDENTE]" },
   // { texto: "[PENDENTE: coletar com o cliente]", nome: "[PENDENTE]", fazenda: "[PENDENTE]", regiao: "[PENDENTE]" },
*/
const DEPOIMENTOS = [];

/* === Eventos (prontos para GA4 / Meta Pixel no site definitivo) === */
window.dataLayer = window.dataLayer || [];
function track(name, params){ try{ window.dataLayer.push(Object.assign({event:name}, params||{})); document.dispatchEvent(new CustomEvent("yote:"+name,{detail:params||{}})); }catch(e){} }
document.addEventListener("click", e => {
  const a = e.target.closest("[data-track]"); if (a) track(a.dataset.track, {local: a.dataset.where || ""});
});

document.documentElement.classList.add("js");

/* Menu */
const burger = document.querySelector(".burger"), nav = document.getElementById("menu");
if (burger) {
  burger.addEventListener("click", () => { const o = nav.classList.toggle("open"); burger.setAttribute("aria-expanded", o); burger.setAttribute("aria-label", o ? "Fechar menu" : "Abrir menu"); });
  nav.addEventListener("click", e => { if (e.target.closest("a")) { nav.classList.remove("open"); burger.setAttribute("aria-expanded","false"); } });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); burger.setAttribute("aria-expanded","false"); burger.focus(); } });
}

/* Copiar */
document.querySelectorAll(".copy").forEach(b => b.addEventListener("click", () => {
  const v = b.dataset.copy, done = () => { const t = b.textContent; b.textContent = "Copiado"; setTimeout(() => b.textContent = t, 1600); };
  const fallback = () => { const el = b.parentElement.querySelector(".val"); const r = document.createRange(); r.selectNodeContents(el); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Selecionado, use Ctrl+C"; setTimeout(() => b.textContent = "Copiar", 2200); };
  try { navigator.clipboard.writeText(v).then(done, fallback); } catch(e){ fallback(); }
}));

/* FAQ */
document.querySelectorAll(".faq button").forEach(btn => btn.addEventListener("click", () => {
  const open = btn.getAttribute("aria-expanded") === "true";
  btn.setAttribute("aria-expanded", !open);
  document.getElementById(btn.getAttribute("aria-controls")).classList.toggle("open", !open);
}));

/* Depoimentos */
document.querySelectorAll("[data-depoimentos]").forEach(sec => {
  const reais = DEPOIMENTOS.filter(d => d && d.texto && !/PENDENTE/.test(d.texto + d.nome));
  if (!reais.length) { sec.hidden = true; return; }
  const box = sec.querySelector(".quotes"), max = +sec.dataset.depoimentos || 3;
  reais.slice(0, max).forEach(d => {
    const f = document.createElement("figure"); f.className = "quote";
    const q = document.createElement("blockquote"); q.textContent = "“" + d.texto + "”";
    const c = document.createElement("cite"); c.textContent = d.nome;
    const s = document.createElement("span"); s.textContent = d.fazenda + " · " + d.regiao; c.append(s);
    f.append(q, c); box.append(f);
  });
  sec.hidden = false;
});

/* Entrada das seções: visível por padrão, desliza só quando entra na tela */
if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.remove("pre"); io.unobserve(en.target); } }), {threshold:.12});
  document.querySelectorAll(".reveal").forEach(el => { const r = el.getBoundingClientRect(); if (r.top > innerHeight) { el.classList.add("pre"); io.observe(el); } });
}

/* Contador nos números (só valores confirmados) */
document.querySelectorAll("[data-count]").forEach(el => {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) return;
  const end = +el.dataset.count, start = +el.dataset.from || 0, suf = el.dataset.suffix || "";
  const io = new IntersectionObserver(([en]) => { if (!en.isIntersecting) return; io.disconnect();
    const t0 = performance.now(); const step = t => { const p = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - p, 3); el.textContent = Math.round(start + (end - start) * e) + suf; if (p < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); });
  io.observe(el);
});

/* === Formulário === */
let dbPromise = null;
function getDb(){ if (!dbPromise) dbPromise = (window.claude && window.claude.use ? window.claude.use("db") : Promise.resolve(null)).catch(() => null); return dbPromise; }
getDb();

function maskPhone(v){ const d = v.replace(/\D/g, "").slice(0, 10); if (d.length < 4) return d.length ? "(" + d : ""; if (d.length < 7) return "(" + d.slice(0,3) + ") " + d.slice(3); return "(" + d.slice(0,3) + ") " + d.slice(3,6) + "-" + d.slice(6); }

document.querySelectorAll("form.lead-form").forEach(form => {
  const tel = form.querySelector("[name=telefone]");
  tel.addEventListener("input", () => { tel.value = maskPhone(tel.value); });
  const status = form.querySelector(".status"), btn = form.querySelector("button[type=submit]");
  const rules = {
    nome: v => v.trim().length >= 2 ? "" : "Escreva seu nome, com pelo menos 2 letras.",
    telefone: v => v.replace(/\D/g, "").length === 10 ? "" : "Digite o telefone com DDD, no formato (000) 000-0000.",
    email: v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? "" : "Confira o e-mail. Ele precisa ter @ e um domínio, como nome@fazenda.com."
  };
  const check = name => { const inp = form.elements[name], msg = rules[name](inp.value), err = form.querySelector("#" + inp.id + "-err"); err.textContent = msg; inp.setAttribute("aria-invalid", msg ? "true" : "false"); return !msg; };
  Object.keys(rules).forEach(n => form.elements[n].addEventListener("blur", () => { if (form.elements[n].value) check(n); }));

  form.addEventListener("submit", async e => {
    e.preventDefault();
    const ok = Object.keys(rules).map(check).every(Boolean);
    if (!ok) { form.querySelector("[aria-invalid=true]").focus(); return; }
    if (form.elements.empresa_site.value) return; // honeypot
    const lead = { nome: form.elements.nome.value.trim(), telefone: form.elements.telefone.value, email: form.elements.email.value.trim(), pagina: document.body.dataset.page, criadoEm: new Date().toISOString() };
    btn.setAttribute("aria-busy", "true"); btn.textContent = "Enviando…"; status.hidden = true;
    let mode = "demo";
    try {
      if (LEAD_ENDPOINT) {
        const r = await fetch(LEAD_ENDPOINT, { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(lead) });
        if (!r.ok) throw new Error("http " + r.status); mode = "sent";
      } else {
        const db = await getDb();
        if (db) { await db.collection("leads").add(lead); mode = "sent"; }
      }
      status.className = "status ok";
      status.innerHTML = mode === "sent" ? "Recebemos seu pedido. O Caio entra em contato em breve." : "Tudo certo com os dados.<small>Formulário de demonstração, nenhum dado foi enviado.</small>";
      if (mode === "sent") { track("lead_enviado", {pagina: lead.pagina}); form.reset(); }
    } catch (err) {
      status.className = "status bad";
      status.innerHTML = "";
      status.append("Não conseguimos enviar agora. Tente de novo em instantes ou ligue para " + CLIENT_PHONE + ".");
    }
    status.hidden = false; status.focus();
    btn.removeAttribute("aria-busy"); btn.textContent = "Solicitar demonstração";
  });
});
