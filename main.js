(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;

  // scroll reveal
  const io = new IntersectionObserver((es) => {
    es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  // hero reveals fire on load
  requestAnimationFrame(() => document.querySelectorAll('.hero .reveal').forEach((el) => el.classList.add('in')));

  // scroll progress + word-by-word statement
  const bar = document.getElementById('progress');
  const big = document.querySelector('.problem-big');
  const words = [];
  if (big) (function split(node) {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === 3) {
        const f = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach((t) => {
          if (!t.trim()) return f.append(t);
          const s = document.createElement('span'); s.className = 'w'; s.textContent = t; words.push(s); f.append(s);
        });
        n.replaceWith(f);
      } else split(n);
    });
  })(big);
  const paint = () => {
    bar.style.setProperty('--p', scrollY / (document.documentElement.scrollHeight - innerHeight));
    if (!big) return;
    const r = big.getBoundingClientRect();
    const k = Math.min(1, Math.max(0, (innerHeight * 0.9 - r.top) / (innerHeight * 0.4)));
    words.forEach((w, i) => w.classList.toggle('lit', i / words.length < k));
  };
  addEventListener('scroll', () => requestAnimationFrame(paint), { passive: true });
  paint();

  // feature <-> phone sync
  const items = [...document.querySelectorAll('.feature')];
  const shots = [...document.querySelectorAll('.shot')];
  const segBtns = [...document.querySelectorAll('.seg button')];
  const show = (key) => shots.forEach((s) => s.classList.toggle('on', s.dataset.key === key));
  const fio = new IntersectionObserver((es) => {
    es.forEach((e) => {
      if (!e.isIntersecting) return;
      items.forEach((i) => i.classList.toggle('is-active', i === e.target));
      const on = segBtns.find((b) => b.classList.contains('on'));
      show(e.target === items[0] ? (on ? on.dataset.view : 'map') : e.target.dataset.img);
    });
  }, { rootMargin: '-40% 0px -50% 0px' });
  items.forEach((i) => fio.observe(i));
  segBtns.forEach((b) => b.addEventListener('click', () => {
    segBtns.forEach((x) => x.classList.toggle('on', x === b));
    show(b.dataset.view);
  }));

  if (reduce || !fine) return;

  // magnetic buttons
  document.querySelectorAll('.magnetic').forEach((el) => {
    el.addEventListener('pointermove', (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * 0.18;
      const y = (e.clientY - r.top - r.height / 2) * 0.28;
      el.style.transform = `translate(${x}px,${y}px)`;
    });
    el.addEventListener('pointerleave', () => { el.style.transform = ''; });
  });

  // phone tilt
  document.querySelectorAll('[data-tilt]').forEach((el) => {
    const host = el.parentElement;
    host.addEventListener('pointermove', (e) => {
      const r = host.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      el.classList.add('live');
      el.style.setProperty('--ry', `${nx * 10}deg`);
      el.style.setProperty('--rx', `${-ny * 8}deg`);
    });
    host.addEventListener('pointerleave', () => {
      el.classList.remove('live');
      el.style.setProperty('--ry', '0deg');
      el.style.setProperty('--rx', '0deg');
    });
  });

  // spotlight on plan card
  const card = document.querySelector('.plan-card-in');
  if (card) card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    card.style.setProperty('--mx', `${e.clientX - r.left}px`);
    card.style.setProperty('--my', `${e.clientY - r.top}px`);
  });
})();

// demo form: validate, then open the mail client addressed to the team
(() => {
  const form = document.getElementById('demo-form');
  if (!form) return;
  const note = document.getElementById('form-note');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let ok = true;
    ['nome', 'tel', 'email'].forEach((id) => {
      const i = form.elements[id];
      const bad = !i.value.trim() || (id === 'email' && !i.validity.valid);
      i.setAttribute('aria-invalid', bad);
      if (bad && ok) { i.focus(); ok = false; }
    });
    if (!ok) return;
    const f = form.elements;
    const body = `Nome: ${f.nome.value}\nTelefone: ${f.tel.value}\nE-mail: ${f.email.value}`;
    note.textContent = 'Abrindo o seu e-mail com o pedido preenchido.';
    note.classList.add('ok');
    location.href = `mailto:support@yotefarmview.com?subject=${encodeURIComponent('Solicitar demonstração')}&body=${encodeURIComponent(body)}`;
  });
  form.addEventListener('input', (e) => e.target.removeAttribute('aria-invalid'));
})();

// mobile menu
(() => {
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (!btn || !menu) return;
  const set = (open) => {
    btn.setAttribute('aria-expanded', open);
    btn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    document.body.classList.toggle('menu-open', open);
    if (open) menu.hidden = false;
    menu.classList.toggle('open', open);
  };
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape') set(false); });
  matchMedia('(min-width: 901px)').addEventListener('change', (e) => { if (e.matches) set(false); });
})();
