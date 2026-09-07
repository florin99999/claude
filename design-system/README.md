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

## Homepage

Toate planșele stau în același canvas, alături de design system. Pagina este împărțită în 3 planșe pe desktop (`Main`, `HomeB`, `HomeC`) și 5 pe mobil (`Mobil` … `MobilE`), așezate una sub alta în continuare, pentru că planșele foarte înalte nu se randează complet în editor. Secțiunile homepage-ului și layout-ul din temă pe care îl urmează:

| Secțiune | Layout din tema Airvora |
|---|---|
| Header + hero + bară de încredere | Header transparent peste hero, două coloane de 50%, contoare pe fotografie |
| De ce Aerconduct | „About”: verde închis, grilă de 4 diferențiatori, fotografie de 300 px |
| Servicii | „Our Services”: titlu centrat, 6 carduri bej pe 3 coloane |
| Cum lucrăm | „Process”: fundal negru cald, 4 pași în grilă 2 × 2, număr Display |
| Industrii | Carduri de tip blog: fotografie, titlu, un rând, link |
| Proiecte | „Projects”: rânduri cu fotografie de fundal, card bej și 3 contoare |
| Pentru antreprenori | „Why choose us”: fotografie cu gradient, text stânga, listă cu separatoare dreapta |
| Zone deservite | Două coloane: text + hartă simplă SVG (secțiune fără echivalent în temă) |
| FAQ | Acordeon cu linii de 1 px, prima întrebare deschisă |
| CTA + formular | „Ready to get started” pe negru cald, cu formular pe card bej |
| Footer | Footer pe fundal accent, 4 coloane, rând legal jos |

`canvas/build_sections.py` generează secțiunile 2–10 și footer-ul din conținut, iar `canvas/build_pages.py` le împarte în planșe, pentru desktop și mobil. Valorile între paranteze drepte sunt de completat.

## V2 – paleta pe culorile brandului

Aceleași roluri de culoare ca în temă, construite în jurul roșului `#E02127` și albastrului `#3EA8DE` din logo:
navy `#0C1A2B` (primary), albastru închis `#10334F` (secondary), gri rece `#5B6470` (text), albastru brand `#3EA8DE` (accent),
alb rece `#F3F5F7`, carduri `#E8EDF1`, border `#CFD6DD`. Roșul este culoarea de acțiune (butoane principale, marcajele etichetelor),
albastrul preia rolul accentului (etichete pe închis, cifre, footer).

- Token-uri: [`colors-v2.css`](colors-v2.css) (se încarcă după `airvora-tokens.css`).
- Planșa „Design system v2 · Culori” și homepage-ul v2 (`canvas/V2*.dc.html`) sunt în același canvas. `canvas/build_v2.py` generează v2 din v1 prin înlocuirea culorilor.

