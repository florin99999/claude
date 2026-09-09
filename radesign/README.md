# Radesign – landing page „Design Interior Iași”

Pagină statică de prezentare (fără header/footer de website, fără linkuri externe), construită doar cu HTML, CSS și JavaScript minimal.

## Structură

| Fișier | Rol |
|---|---|
| `index.html` | pagina completă, HTML semantic (`header` / `main` / `section` / `footer`), meta SEO, Open Graph, JSON-LD `LocalBusiness` |
| `assets/css/style.css` | design system: variabile globale în `:root` (culori, fonturi, raze, container), clase reutilizabile (`.btn`, `.card`, `.chip`, `.grid`, `.cover`, `.field`), responsive (desktop / tabletă ≤1024px / mobil ≤640px) |
| `assets/js/main.js` | carusel (auto + săgeți), filtre galerie, lightbox (`<dialog>`), slider înainte/după |
| `assets/img/` | imagini generate cu Higgsfield (Nano Banana), logo, favicon |
| `assets/video/` | gol – aici pui `hero.mp4` (10–15 s, fără sunet); până atunci se afișează posterul `hero.jpg` |

Tokenii vizuali (Epilogue 600 / Inter Tight, auriu `#E8B237`, crem `#F5F1E6`, raze 10px / 40px, container 1300px) sunt cei de pe radesign.ro.

## Rulare locală

```bash
python3 -m http.server 8080
```

apoi deschide `http://localhost:8080/`.

## De completat înainte de publicare

- `link rel="canonical"` și URL-urile `og:` din `<head>` – pune URL-ul final al paginii.
- **Formular**: `action="#"` – conectează la endpoint-ul tău (PHP / Formspree / WordPress etc.).
- **Recenzii**: înlocuiește lista `.reviews` cu widget-ul Google Reviews; textele `[Nume Client]`, `[Data recenziei]`, `[NR]` sunt placeholder.
- **Galerie**: fiecare `figure` are `data-photos="..."` – lista imaginilor deschise în lightbox (5–10 poze/proiect). Categoriile de filtrare sunt în `data-cat`.
- **Imagini**: cele din `assets/img/` sunt generate AI; se înlocuiesc cu fotografiile reale din portofoliu păstrând numele fișierelor (`p-01.jpg` … `p-12.jpg`, `slide-1..3.jpg`, `before.jpg`, `after.jpg`, `hero.jpg`, `cta.jpg`).
