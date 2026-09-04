/* Aerconduct – interacțiuni & scroll fin
   - Lenis pentru scroll inerțial (fallback: scroll nativ)
   - GSAP ScrollTrigger pentru reveal-uri, parallax hero, contoare
   - Fallback IntersectionObserver când GSAP nu e disponibil          */
(function () {
  'use strict';
  const doc = document.documentElement;
  doc.classList.remove('no-js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
  const hasLenis = typeof window.Lenis !== 'undefined';

  /* ---------- Scroll fin (Lenis) ---------- */
  let lenis = null;
  if (hasLenis && !reduce) {
    lenis = new Lenis({
      duration: 1.25,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
      wheelMultiplier: 0.95,
      touchMultiplier: 1.4,
      lerp: 0.09
    });
    if (hasGsap) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      const raf = (time) => { lenis.raf(time); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
  } else if (hasGsap) {
    gsap.registerPlugin(ScrollTrigger);
  }

  const scrollTo = (target, offset) => {
    if (lenis) { lenis.scrollTo(target, { offset: offset || 0, duration: 1.4 }); }
    else if (target && target.scrollIntoView) { target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }
  };

  /* ---------- Ancore interne ---------- */
  const navbar = document.getElementById('navbar');
  const navH = () => (navbar ? navbar.offsetHeight : 0);
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      closeNav();
      scrollTo(el, -navH() + 1);
      history.replaceState(null, '', id);
    });
  });

  /* ---------- Meniu mobil ---------- */
  const nav = document.getElementById('nav');
  const toggle = document.getElementById('navToggle');
  function closeNav() {
    if (!nav) return;
    nav.classList.remove('is-open');
    toggle && toggle.setAttribute('aria-expanded', 'false');
    lenis && lenis.start();
  }
  toggle && toggle.addEventListener('click', () => {
    const open = !nav.classList.contains('is-open');
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    if (lenis) open ? lenis.stop() : lenis.start();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeNav(); });

  /* ---------- Header compact / ascuns la scroll în jos ---------- */
  const progress = document.querySelector('.scroll-progress span');
  const toTop = document.getElementById('toTop');
  let lastY = 0;
  const onScroll = (y) => {
    if (navbar) {
      navbar.classList.toggle('is-compact', y > 60);
      navbar.classList.toggle('is-hidden', y > 400 && y > lastY + 4 && !nav.classList.contains('is-open'));
    }
    if (toTop) toTop.classList.toggle('is-visible', y > 600);
    if (progress) {
      const max = doc.scrollHeight - window.innerHeight;
      progress.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
    }
    lastY = y;
  };
  if (lenis) lenis.on('scroll', (e) => onScroll(e.scroll));
  else window.addEventListener('scroll', () => onScroll(window.scrollY), { passive: true });
  onScroll(window.scrollY);

  /* ---------- Link activ în meniu ---------- */
  const sections = [...document.querySelectorAll('main section[id]')];
  const navLinks = [...document.querySelectorAll('.nav a[href^="#"]')];
  if ('IntersectionObserver' in window && sections.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        navLinks.forEach((l) => l.classList.toggle('is-active', l.getAttribute('href') === '#' + en.target.id));
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach((s) => io.observe(s));
  }

  /* ---------- Contoare ---------- */
  const fmt = (n, el) => {
    const s = el.dataset.format === 'ro' ? Math.round(n).toLocaleString('ro-RO') : String(Math.round(n));
    return s + (el.dataset.suffix || '');
  };
  const runCounter = (el) => {
    if (el.dataset.done) return;
    el.dataset.done = '1';
    const target = parseFloat(el.dataset.count || '0');
    if (reduce || !hasGsap) { el.textContent = fmt(target, el); return; }
    const obj = { v: 0 };
    gsap.to(obj, { v: target, duration: 2, ease: 'power3.out', onUpdate: () => { el.textContent = fmt(obj.v, el); } });
  };

  /* ---------- Reveal-uri ---------- */
  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if (hasGsap && !reduce) {
    doc.classList.add('gsap');
    gsap.set(reveals, { autoAlpha: 0, y: 34 });
    // grupuri: stagger între copii
    document.querySelectorAll('[data-reveal-group]').forEach((group) => {
      const items = [...group.querySelectorAll(':scope > [data-reveal], :scope > * > [data-reveal]')].filter((el) => el.closest('[data-reveal-group]') === group);
      if (!items.length) return;
      gsap.to(items, {
        autoAlpha: 1, y: 0, duration: 1.1, ease: 'power3.out', stagger: 0.1,
        scrollTrigger: { trigger: group, start: 'top 85%', once: true },
        onStart: () => items.forEach((el) => el.querySelectorAll('[data-count]').forEach(runCounter))
      });
    });
    // singulare
    reveals.filter((el) => !el.closest('[data-reveal-group]')).forEach((el) => {
      gsap.to(el, {
        autoAlpha: 1, y: 0, duration: 1.1, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true },
        onStart: () => el.querySelectorAll('[data-count]').forEach(runCounter)
      });
    });
    // hero: intrare la încărcare
    const heroItems = document.querySelectorAll('.hero [data-reveal]');
    gsap.to(heroItems, { autoAlpha: 1, y: 0, duration: 1.2, ease: 'power3.out', stagger: 0.12, delay: 0.15, overwrite: true });
    // parallax hero
    const media = document.querySelector('[data-parallax]');
    if (media) {
      gsap.to(media, { yPercent: 18, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
      gsap.to('.hero__content', { yPercent: 12, autoAlpha: 0.15, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    }
    // imagini cu ușor parallax în secțiuni
    document.querySelectorAll('.why__photo img, .partners__media img').forEach((img) => {
      gsap.fromTo(img, { yPercent: -6 }, { yPercent: 6, ease: 'none', scrollTrigger: { trigger: img, start: 'top bottom', end: 'bottom top', scrub: true } });
    });
    window.addEventListener('load', () => ScrollTrigger.refresh());
  } else {
    // fallback fără GSAP
    const show = (el) => { el.classList.add('is-visible'); el.querySelectorAll('[data-count]').forEach(runCounter); };
    if ('IntersectionObserver' in window && !reduce) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((en, i) => {
          if (!en.isIntersecting) return;
          const el = en.target;
          const group = el.closest('[data-reveal-group]');
          const idx = group ? [...group.querySelectorAll('[data-reveal]')].indexOf(el) : 0;
          setTimeout(() => show(el), Math.min(idx, 8) * 90);
          io.unobserve(el);
        });
      }, { rootMargin: '0px 0px -10% 0px' });
      reveals.forEach((el) => io.observe(el));
    } else {
      reveals.forEach(show);
    }
  }

  /* ---------- FAQ: un singur item deschis ---------- */
  const faqItems = document.querySelectorAll('.faq__item');
  faqItems.forEach((d) => d.addEventListener('toggle', () => {
    if (d.open) faqItems.forEach((o) => { if (o !== d) o.open = false; });
    hasGsap && ScrollTrigger.refresh();
  }));

  /* ---------- Formular: validare minimă ---------- */
  const form = document.querySelector('.form');
  form && form.addEventListener('submit', (e) => {
    if (!form.checkValidity()) {
      e.preventDefault();
      form.reportValidity();
    }
  });

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
