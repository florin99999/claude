# Aerconduct – landing page

Landing page static pentru **aerconduct.ro**, redesenat după structura temei
[Steelnova (CaseThemes)](https://demo.casethemes.net/steelnova/), cu copy-ul și
secțiunile din brief.

## Structură

| Fișier | Rol |
|---|---|
| `index.html` | pagina completă (10 secțiuni + footer, schema `LocalBusiness` + `FAQPage`) |
| `assets/css/style.css` | design system: fonturi Kanit + Inter, paletă navy / albastru brand / roșu brand |
| `assets/js/main.js` | scroll fin (Lenis) + reveal-uri, parallax și contoare (GSAP ScrollTrigger), meniu mobil, FAQ |
| `assets/img/logo.svg`, `logo-white.svg` | logo recreat vectorial (variantă pe fundal deschis / închis) |
| `scripts/localize-images.sh` | descarcă imaginile generate cu Higgsfield în `assets/img/` și rescrie căile |

## Imagini

Cele 20 de fotografii au fost generate cu Higgsfield (Nano Banana 2) și sunt referite
momentan direct de pe CDN-ul Higgsfield. Pentru producție rulează:

```bash
bash scripts/localize-images.sh
```

Scriptul descarcă imaginile în `assets/img/`, le convertește în WebP dacă ai `cwebp`
instalat și actualizează `index.html`.

## Rulare locală

Orice server static merge, de exemplu:

```bash
python3 -m http.server 8080
```

apoi deschide `http://localhost:8080/`.

## De completat înainte de publicare

Elementele marcate cu clasa `.placeholder` (evidențiate cu roșu în pagină) și
comentariile `PLACEHOLDER` din `index.html`:

- cifrele din bara de încredere (`data-count`) și din badge-ul „ani de experiență”;
- pragul minim de metri liniari pentru subcontractare și numărul de montatori;
- datele celor 3 proiecte (locație, ml, termen, antreprenor);
- denumirea firmei, CUI, Reg. Com.;
- linkurile social media și profilul Google Business.
