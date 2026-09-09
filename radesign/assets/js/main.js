/* Radesign – interacțiuni minime: carusel, filtre galerie, lightbox, slider înainte/după. */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

/* Carusel */
const slides = $$('.slider__item');
let current = 0, timer;
const show = i => {
  current = (i + slides.length) % slides.length;
  slides.forEach((s, n) => s.classList.toggle('is-active', n === current));
  $('.slider__count').textContent = `${current + 1} / ${slides.length}`;
  clearInterval(timer);
  timer = setInterval(() => show(current + 1), 6000);
};
$$('.slider__nav [data-dir]').forEach(b => b.addEventListener('click', () => show(current + +b.dataset.dir)));
show(0);

/* Filtre galerie */
$$('.chip[data-filter]').forEach(chip => chip.addEventListener('click', () => {
  $$('.chip[data-filter]').forEach(c => c.classList.toggle('is-active', c === chip));
  const f = chip.dataset.filter;
  $$('.gallery__item').forEach(item => item.classList.toggle('is-hidden', f !== 'all' && !item.dataset.cat.split(' ').includes(f)));
}));

/* Lightbox */
const box = $('.lightbox'), boxImg = $('img', box);
let photos = [], idx = 0;
const showPhoto = i => { idx = (i + photos.length) % photos.length; boxImg.src = photos[idx]; };
$$('.gallery__item').forEach(item => item.addEventListener('click', () => {
  photos = item.dataset.photos.split(',');
  showPhoto(0);
  box.showModal();
}));
$$('[data-dir]', box).forEach(b => b.addEventListener('click', () => showPhoto(idx + +b.dataset.dir)));
$('.lightbox__close').addEventListener('click', () => box.close());
box.addEventListener('click', e => { if (e.target === box) box.close(); });

/* Înainte / după */
const compare = $('.compare');
$('input', compare).addEventListener('input', e => compare.style.setProperty('--pos', e.target.value + '%'));
