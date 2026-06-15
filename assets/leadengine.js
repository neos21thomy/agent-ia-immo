/* ============================================================
   LeadEngine AI — Comportements partagés (V3)
   Inclure sur chaque page : <script src="assets/leadengine.js" defer></script>
   Gère : ambiance (halo + grain), barre de progression, nav + burger,
   révélations au scroll, compteurs animés. Respecte prefers-reduced-motion.
   ============================================================ */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const body = document.body;

  const mk = (cls) => { const d = document.createElement('div'); d.className = cls; d.setAttribute('aria-hidden', 'true'); return d; };
  if (!document.querySelector('.le-aura')) body.prepend(mk('le-aura'));
  if (!reduced && !document.querySelector('.le-grain')) body.prepend(mk('le-grain'));
  if (!document.querySelector('.le-progress')) {
    const p = mk('le-progress'); p.appendChild(document.createElement('i')); body.appendChild(p);
  }
  const progBar = document.querySelector('.le-progress > i');
  if (!document.querySelector('.le-bg-dots')) body.prepend(mk('le-bg-dots'));
  if (!reduced && !document.querySelector('.le-orbs')) {
    const orbs = mk('le-orbs');
    orbs.innerHTML = '<div class="le-orb a" data-par="0.10"></div><div class="le-orb b" data-par="0.05"></div><div class="le-orb c" data-par="0.14"></div><div class="le-orb d" data-par="0.08"></div>';
    body.prepend(orbs);
  }

  const nav = document.getElementById('nav') || document.querySelector('nav.le-nav');
  const onScroll = () => {
    if (nav) nav.classList.toggle('scrolled', scrollY > 40);
    if (progBar) {
      const h = document.documentElement.scrollHeight - innerHeight;
      progBar.style.transform = 'scaleX(' + (h > 0 ? Math.min(scrollY / h, 1) : 0) + ')';
    }
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const burger = document.getElementById('navBurger');
  const links = document.getElementById('navLinks');
  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open);
    });
    links.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => {
      links.classList.remove('open'); burger.classList.remove('open');
    }));
  }

  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      reveals.forEach((el) => el.classList.add('visible'));
    } else {
      const obs = new IntersectionObserver((entries) => entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
      }), { threshold: .12 });
      reveals.forEach((el, i) => { el.style.transitionDelay = (i % 3) * 90 + 'ms'; obs.observe(el); });
      setTimeout(() => reveals.forEach((el) => el.classList.add('visible')), 2200);
    }
  }

  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const run = (el) => {
      const target = +el.dataset.count, suffix = el.dataset.suffix || '';
      if (reduced) { el.textContent = target + suffix; return; }
      const t0 = performance.now(), dur = 1400;
      const step = (now) => {
        const p = Math.min((now - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    if (!('IntersectionObserver' in window)) counters.forEach(run);
    else {
      const cObs = new IntersectionObserver((entries) => entries.forEach((e) => {
        if (e.isIntersecting) { cObs.unobserve(e.target); run(e.target); }
      }), { threshold: .6 });
      counters.forEach((el) => cObs.observe(el));
    }
  }

  // Parallax doux (orbes + tout [data-par]) + inclinaison 3D des cartes .tilt
  if (!reduced) {
    const par = Array.from(document.querySelectorAll('[data-par]'));
    if (par.length) {
      let ticking = false;
      const upd = () => { const y = scrollY; par.forEach((el) => { el.style.transform = 'translate3d(0,' + (y * +el.dataset.par * -1).toFixed(1) + 'px,0)'; }); ticking = false; };
      addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(upd); ticking = true; } }, { passive: true });
      upd();
    }
    if (matchMedia('(pointer: fine)').matches) {
      document.querySelectorAll('.tilt').forEach((c) => {
        c.addEventListener('mousemove', (e) => {
          const r = c.getBoundingClientRect();
          c.style.setProperty('--rx', (((e.clientX - r.left) / r.width - .5) * 6).toFixed(2) + 'deg');
          c.style.setProperty('--ry', ((-((e.clientY - r.top) / r.height - .5)) * 6).toFixed(2) + 'deg');
        });
        c.addEventListener('mouseleave', () => { c.style.setProperty('--rx', '0deg'); c.style.setProperty('--ry', '0deg'); });
      });
    }

    // Passage immersif : le hero s'efface et s'élève quand on entre dans la section suivante
    const hero = document.querySelector('.hero');
    if (hero) {
      let hticking = false;
      const onHero = () => {
        const h = hero.offsetHeight || innerHeight;
        const p = Math.min(Math.max(scrollY / h, 0), 1);
        hero.style.opacity = String(1 - p * 0.85);
        hero.style.transform = 'translateY(' + (p * 42).toFixed(1) + 'px)';
        hticking = false;
      };
      addEventListener('scroll', () => { if (!hticking) { requestAnimationFrame(onHero); hticking = true; } }, { passive: true });
      onHero();
    }
  }
})();
