# Design system Airvora

Sistem de design extras din tema [Airvora – Commercial HVAC Services Elementor Template Kit](https://themeforest.net/item/airvora-commercial-hvac-services-elementor-template-kit/64601576)
(autor askproject), analizând stilurile globale ale kitului din demo-ul live (`elementor-kit-16`).
Este baza pentru noul homepage Aerconduct.

- **Canvasul unic** (design system + homepage, editabil): https://claude.ai/code/artifact/a27d6697-2dcf-40d5-b029-892ec8612769
- **Token-uri CSS**: [`airvora-tokens.css`](airvora-tokens.css)
- **Sursele planșelor**: [`canvas/`](canvas/) (`Main.dc.html` = homepage desktop, `Mobil.dc.html` = homepage mobil, `Fundamente.dc.html`, `Componente.dc.html`)

## Rezumat

| Categorie | Valori |
|---|---|
| Culori | Primary `#241F21` · Secondary `#062D2B` · Text `#5E5A5C` · Accent `#F6F36F` · Surface `#F2EFE9` · Surface 2 `#ECE6DF` · Border `#D8D4CF` · Surface 3 `#DFDACE` |
| Fonturi | Plus Jakarta Sans (titluri și text, grosime 400; H5/H6 la 500) · Chivo Mono 500 majuscule (etichete, butoane, meniu) |
| Titluri | Display 90 · H1 67 · H2 50 · H3 36 · H4 28 · H5 21 · H6 17 · Body 15 · Label 12 (px, desktop); tracking negativ pe toate titlurile |
| Spațiere | 10 · 20 · 30 · 70 · 100 px; container 1200 px cu margini de 20 px |
| Forme | Colțuri 0 pe carduri/imagini/câmpuri; 5 px pe butoane; 100 px tag-uri; 500 px avataruri; fără umbre |
| Butoane | Chivo Mono 12 px, padding 14×18 (header 12×14, mic 10×12), săgeată 14 px la 10 px, tranziție 0.4 s |
| Breakpoints | desktop > 1024 px · tabletă 768–1024 px · mobil < 768 px |

## Notă de licență

Culorile, fonturile și proporțiile nu sunt protejate, dar imaginile demo și layout-ul exact al paginilor din kit sunt
opera autorului. Pentru un homepage „identic” cu demo-ul este nevoie de licența kitului de pe ThemeForest;
altfel, construim un layout propriu pe acest sistem de design.

## Homepage (în lucru)

Toate planșele stau în același canvas, alături de design system.

- **Etapa 1 – header + hero + bară de încredere**: `canvas/Main.dc.html` (desktop 1440) și `canvas/Mobil.dc.html` (mobil 390).
  Cifrele din bara de încredere sunt de exemplu, de înlocuit cu cele reale.
- **Etapa 2 – „De ce Aerconduct”** pe layout-ul „About” din temă (verde închis, text + grilă de 4 diferențiatori + fotografie de 300 px).
- **Etapa 3 – „Servicii”** pe layout-ul „Our Services” din temă (titlu centrat, carduri bej cu fotografie, titlu, text, link), pe 4 coloane pentru cele 8 servicii.
