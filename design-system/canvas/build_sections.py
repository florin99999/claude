# -*- coding: utf-8 -*-
import math
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>'
def ico(paths, size=25, color='#F6F36F', sw=1.5):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex: none;">{paths}</svg>'
def eyebrow(text, dark):
    c='#F2EFE9' if dark else '#241F21'; d='#F6F36F' if dark else '#241F21'
    return f'<div class="mono" style="display: flex; align-items: center; gap: 10px; color: {c};"><span style="width: 9px; height: 9px; background: {d}; flex: none;"></span><span>{text}</span></div>'
def h2(text, dark, desktop, extra=''):
    c='#F2EFE9' if dark else '#241F21'
    sz='font-size: 50px; letter-spacing: -2px;' if desktop else 'font-size: 32px; letter-spacing: -1.2px;'
    return f'<h2 style="color: {c}; {sz} font-weight: 400; line-height: 1.1; margin: 0; text-wrap: pretty; {extra}">{text}</h2>'
def btn(text, href, kind='primary', extra=''):
    st={'primary':'background: #241F21; color: #F2EFE9; padding: 14px 18px; border: 0;',
        'light':'background: #F2EFE9; color: #241F21; padding: 14px 18px; border: 0;',
        'accent':'background: #F6F36F; color: #241F21; padding: 14px 18px; border: 0;',
        'outline':'background: transparent; color: #F6F36F; padding: 13px 17px; border: 1px solid rgba(242, 239, 233, 0.19);',
        'link':'background: transparent; color: #241F21; padding: 0; border: 0;',
        'linkdark':'background: transparent; color: #F6F36F; padding: 0; border: 0;'}[kind]
    return f'<a class="btn" href="{href}" style="{st} {extra}"><span>{text}</span>{ARROW}</a>'
def sq(text, dark, size=15):
    d='#F6F36F' if dark else '#241F21'; c='#F2EFE9' if dark else '#241F21'
    return f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 8px; height: 8px; background: {d}; flex: none;"></span><span style="color: {c}; font-size: {size}px;">{text}</span></div>'
def img(src, alt, extra=''):
    return f'<img src="{src}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; {extra}">'

# ---------------- SECTIUNEA 2 ----------------
DIFF=[
 ('<path d="M3 7l9-4 9 4-9 4-9-4z"></path><path d="M3 12l9 4 9-4"></path><path d="M3 17l9 4 9-4"></path>',
  'Specializați în tubulatură ALP / P3ductal',
  'Una dintre puținele echipe din România cu experiență consistentă pe panouri preizolate. Confecție în atelier sau pe șantier, îmbinări cu profile de aluminiu.'),
 ('<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"></path><circle cx="12" cy="10" r="2.5"></circle>',
  'Singura echipă specializată din Moldova',
  'Sediul în Neamț înseamnă mobilizare în aceeași zi în Iași, Bacău, Suceava, Roman și Piatra Neamț, fără costuri de deplasare din București.'),
 ('<circle cx="12" cy="12" r="9"></circle><path d="M8 12l3 3 5-6"></path>',
  'Execuție conform standardelor',
  'Tubulatură realizată și montată conform EN 12237, EN 1507 și EN 12101-7 pentru desfumare, cu documentație de conformitate la predare.'),
 ('<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7"></path><path d="M17.5 14a6.5 6.5 0 0 1 4 6"></path>',
  'Capacitate de subcontractare',
  'Echipe de montaj disponibile pentru antreprenori generali, pe lucrări de la [X] ml în sus. Ofertă în 48 de ore de la primirea planului.'),
]
def about(desktop):
    pad='100px 20px' if desktop else '70px 10px'
    grid='repeat(4, minmax(0, 1fr))' if desktop else 'repeat(1, minmax(0, 1fr))'
    items=''.join(f'''
        <div style="display: flex; flex-direction: column; gap: 20px;">
          {ico(p)}
          <h3 style="color: #F2EFE9; font-size: 21px; font-weight: 500; line-height: 1.3; letter-spacing: -0.8px; margin: 0;">{t}</h3>
          <p style="color: #D8D4CF;">{d}</p>
        </div>''' for p,t,d in DIFF)
    photo=(f'<div style="width: 300px; min-height: 500px; flex: none; position: relative; overflow: hidden;">{img("despre-foto.jpg","Confecție tubulatură în atelier")}</div>' if desktop else
           f'<div style="width: 100%; min-height: 400px; position: relative; overflow: hidden;">{img("despre-foto.jpg","Confecție tubulatură în atelier","object-position: center 35%;")}</div>')
    return f'''
  <!-- SECTIUNEA 2: De ce Aerconduct (layout "About" din tema) -->
  <section style="background: #062D2B; padding: {pad}; display: flex; flex-direction: {'row' if desktop else 'column'}; justify-content: space-between; flex-wrap: wrap; gap: 50px 0;">
    <div style="{'width: 1000px; flex: none;' if desktop else 'width: 100%;'} display: flex; flex-direction: column; gap: 20px;">
      {eyebrow('De ce Aerconduct', True)}
      {h2('Un singur partener pentru toată tubulatura de pe șantier', True, desktop, 'max-width: 750px;')}
      <p style="color: #D8D4CF; max-width: 570px;">Lucrăm cu antreprenori generali, firme de instalații și beneficiari direcți. Preluăm planul HVAC, verificăm traseele, confecționăm și montăm – fără să trebuiască să coordonezi trei furnizori.</p>
      <div style="display: grid; grid-template-columns: {grid}; gap: {'50px' if desktop else '30px'}; margin: 20px 0 40px 0;">{items}
      </div>
      <div>{btn('Despre echipă','/despre/','light')}</div>
    </div>
    {photo}
  </section>'''

# ---------------- SECTIUNEA 3 ----------------
SERV=[
 ('alp','Tubulatură preizolată ALP / P3ductal','Soluție ușoară, izolată și igienică pentru spitale, birouri, HoReCa. Confecție la dimensiune, montaj rapid.','/servicii/montaj-tubulatura-alp/',
  '<rect x="3" y="5" width="18" height="14"></rect><path d="M3 9h18"></path><path d="M3 15h18"></path>'),
 ('zincata','Tubulatură rectangulară din tablă zincată','Trasee principale pentru hale și clădiri comerciale, cu flanșe și garnituri pentru clasa de etanșeitate cerută.','/servicii/tubulatura-rectangulara-zincata/',
  '<path d="M3 8h13v8H3z"></path><path d="M16 8l5-3v14l-5-3"></path>'),
 ('spiro','Tubulatură circulară Spiro','Diametre 100–1250 mm, fitinguri și racorduri, montaj aparent sau mascat.','/servicii/tubulatura-spiro/',
  '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4"></circle><path d="M3 12h5"></path><path d="M16 12h5"></path>'),
 ('inox','Tubulatură inox','Pentru industria alimentară, farma și bucătării profesionale, unde igiena și rezistența la coroziune sunt obligatorii.','/servicii/tubulatura-inox/',
  '<path d="M12 3l7 4v10l-7 4-7-4V7z"></path><path d="M12 11l7-4"></path><path d="M12 11L5 7"></path><path d="M12 11v10"></path>'),
 ('desfumare','Desfumare și antifoc','Tubulatură rezistentă la foc E600 120, clapete antifoc, ventilație parcări conform cerințelor ISU.','/servicii/tubulatura-desfumare/',
  '<path d="M12 21c-4 0-7-3-7-7 0-3 2-5 3-7 0 2 1 3 2 3 0-4 2-6 4-7 0 3 5 5 5 11 0 4-3 7-7 7z"></path>'),
 ('izolare','Izolare și cladding','Izolație termică și fonică a tubulaturii, protecție exterioară pentru trasee montate afară.','/servicii/izolare-tubulatura/',
  '<rect x="3" y="7" width="18" height="10" rx="5"></rect><path d="M7 7v10"></path><path d="M17 7v10"></path>'),
]
def services(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    grid='repeat(3, minmax(0, 1fr))' if desktop else 'repeat(1, minmax(0, 1fr))'
    title='font-size: 36px; letter-spacing: -1.2px;' if desktop else 'font-size: 30px; letter-spacing: -1px;'
    cards=''.join(f'''
      <div style="background: #ECE6DF; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <div style="position: relative; min-height: {'300px' if desktop else '280px'}; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            {img('serv-'+k+'.jpg','')}
            <div style="position: absolute; inset: 0; background: #241F21; opacity: 0.3;"></div>
            {ico(p, 72, '#F2EFE9', 1.1)}
          </div>
          <h3 style="color: #241F21; {title} font-weight: 400; line-height: 1.2; margin: 0; text-wrap: pretty;">{t}</h3>
          <p style="margin: 0 0 10px 0;">{d}</p>
        </div>
        {btn('Detalii serviciu', u, 'link')}
      </div>''' for k,t,d,u,p in SERV)
    return f'''
  <!-- SECTIUNEA 3: Servicii (layout "Our Services" din tema) -->
  <section style="background: #F2EFE9; padding: {pad}; display: flex; flex-direction: column; align-items: center; gap: 20px;">
    {eyebrow('Servicii', False)}
    {h2('Servicii de execuție și montaj tubulatură de ventilație', False, desktop, 'max-width: 750px; text-align: center;')}
    <p style="max-width: 570px; text-align: center; margin: 0 0 {'50px' if desktop else '20px'} 0;">Acoperim toate tipurile de tubulatură dintr-un proiect HVAC – de la distribuția principală la piesele speciale și izolație.</p>
    <div style="width: 100%; display: grid; grid-template-columns: {grid}; gap: {'20px' if desktop else '10px'};">{cards}
    </div>
    <div style="margin-top: 20px;">{btn('Toate serviciile','/servicii/','primary')}</div>
  </section>'''

# ---------------- SECTIUNEA 4: PROCES ----------------
STEPS=[('01','Trimiți planul','Primim planul HVAC (DWG/PDF) sau facem releveu la fața locului.'),
       ('02','Verificăm și ofertăm','Analizăm traseele, semnalăm conflictele cu structura sau alte instalații și trimitem oferta în 48 de ore.'),
       ('03','Confecționăm și montăm','Piesele se fac în atelier sau pe șantier; echipa montează pe grafic, coordonat cu ceilalți subcontractori.'),
       ('04','Predăm cu documentație','Verificare vizuală, teste de etanșeitate la cerere, declarații de conformitate și fotografii de execuție.')]
def process(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    grid='repeat(2, minmax(0, 1fr))' if desktop else 'repeat(1, minmax(0, 1fr))'
    num='font-size: 90px; letter-spacing: -3px; word-spacing: 8px;' if desktop else 'font-size: 68px; letter-spacing: -2px;'
    steps=''.join(f'''
      <div style="display: flex; flex-direction: {'row' if desktop else 'column'}; justify-content: space-between; border: 1px solid rgba(242, 239, 233, 0.125); background: #241F21;">
        <div style="{'width: 320px; flex: none;' if desktop else ''} padding: 20px; display: flex; align-items: center;"><div style="{num} line-height: 1; color: #F2EFE9;">Pas {n}</div></div>
        <div style="flex: 1; padding: 20px; display: flex; flex-direction: column; justify-content: center; gap: 10px;">
          <h3 style="color: #F2EFE9; font-size: {'28px' if desktop else '23px'}; font-weight: 400; line-height: 1.2; letter-spacing: -1.2px; margin: 0;">{t}</h3>
          <p style="color: #D8D4CF;">{d}</p>
        </div>
      </div>''' for n,t,d in STEPS)
    return f'''
  <!-- SECTIUNEA 4: Cum lucram (layout "Our Streamlined Process" din tema) -->
  <section style="background: #241F21; padding: {pad}; display: flex; flex-direction: column; align-items: flex-start; gap: 20px;">
    {eyebrow('Cum lucrăm', True)}
    {h2('De la plan la punere în funcțiune, în 4 pași', True, desktop, 'max-width: 550px; margin-bottom: ' + ('50px' if desktop else '20px') + ';')}
    <div style="width: 100%; display: grid; grid-template-columns: {grid}; gap: {'20px' if desktop else '10px'};">{steps}
    </div>
    <div style="margin-top: 20px;">{btn('Începe cu o cerere de ofertă','/cerere-oferta/','light')}</div>
  </section>'''

# ---------------- SECTIUNEA 5: INDUSTRII ----------------
IND=[('serv-modificari.jpg','Hale de producție și depozite','Trasee lungi, tubulatură zincată și textilă, exhaustare la utilaje.','/industrii/hale-productie/'),
     ('serv-alp.jpg','Spitale și clinici','Tubulatură ALP igienică, lavabilă, cu izolație integrată.','/industrii/spitale-clinici/'),
     ('serv-inox.jpg','Restaurante și bucătării profesionale','Hote, tubulatură inox, evacuare grăsimi.','/industrii/restaurante/'),
     ('serv-spiro.jpg','Clădiri de birouri','Tubulatură mascată, atenuare zgomot, finisaj curat.','/industrii/cladiri-birouri/'),
     ('ind-scoli.jpg','Școli și instituții publice','Execuție în licitații publice, documentație completă.','/industrii/institutii-publice/'),
     ('serv-desfumare.jpg','Parcări subterane','Desfumare și ventilație conform normativelor.','/industrii/parcari-subterane/')]
def industries(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    grid='repeat(3, minmax(0, 1fr))' if desktop else 'repeat(1, minmax(0, 1fr))'
    cards=''.join(f'''
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <div style="position: relative; min-height: {'280px' if desktop else '240px'}; overflow: hidden;">{img(src,'')}</div>
        <h3 style="color: #241F21; font-size: 28px; font-weight: 400; line-height: 1.2; letter-spacing: -1.2px; margin: 10px 0 0 0; text-wrap: pretty;">{t}</h3>
        <p style="margin: 0 0 10px 0;">{d}</p>
        {btn('Vezi soluțiile', u, 'link')}
      </div>''' for src,t,d,u in IND)
    return f'''
  <!-- SECTIUNEA 5: Industrii (layout "Resources / blog cards" din tema) -->
  <section style="background: #ECE6DF; padding: {pad}; display: flex; flex-direction: column; align-items: center; gap: 20px;">
    {eyebrow('Industrii', False)}
    {h2('Soluții de ventilație pentru fiecare tip de clădire', False, desktop, 'max-width: 750px; text-align: center;')}
    <p style="max-width: 750px; text-align: center; margin: 0 0 {'50px' if desktop else '20px'} 0;">Cerințele diferă: o hală are nevoie de debite mari, un spital de igienă, un restaurant de rezistență la grăsimi și temperatură.</p>
    <div style="width: 100%; display: grid; grid-template-columns: {grid}; gap: {'20px' if desktop else '30px'};">{cards}
    </div>
    <div style="margin-top: 20px;">{btn('Toate industriile','/industrii/','primary')}</div>
  </section>'''

# ---------------- SECTIUNEA 6: PROIECTE ----------------
PROJ=[('serv-zincata.jpg','[Hală producție, Roman, Neamț]','Distribuție principală zincată și ramificații ALP pentru o hală nouă de producție.',[('[1.200]','ml tubulatură zincată + ALP'),('[6]','săptămâni de execuție'),('[Nume / anonim]','antreprenor general')]),
      ('serv-igienizare.jpg','[Clinică privată, Iași]','Tubulatură ALP igienică pentru săli de tratament și zone de așteptare.',[('[800]','ml tubulatură ALP'),('[4]','săptămâni de execuție'),('[Beneficiar direct]','client')]),
      ('serv-izolare.jpg','[Restaurant, Bacău]','Evacuare grăsimi din inox și tubulatură zincată izolată pe terasă.',[('[350]','ml inox + zincată'),('[3]','săptămâni de execuție'),('[Nume / anonim]','firmă de instalații')])]
def projects(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    rows=''
    for i,(src,t,d,data) in enumerate(PROJ,1):
        counters=''.join(f'''
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="font-size: 28px; line-height: 1.2; letter-spacing: -1.2px; color: #F6F36F;">{v}</div>
            <p style="color: #F2EFE9;">{l}</p>
          </div>''' for v,l in data)
        rows+=f'''
      <div style="position: relative; min-height: {'600px' if desktop else '640px'}; display: flex; flex-direction: {'row' if desktop else 'column'}; justify-content: space-between; align-items: flex-end; gap: 20px; padding: 20px; margin-bottom: 10px; overflow: hidden;">
        {img(src,'')}
        <div style="position: absolute; inset: 0; background-image: linear-gradient(140deg, rgba(36, 31, 33, 0.125) 0%, #241F21 100%); opacity: 0.7;"></div>
        <div style="position: relative; {'width: 500px; flex: none;' if desktop else 'width: 100%;'} min-height: 220px; box-sizing: border-box; background: #ECE6DF; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div class="mono" style="color: #5E5A5C;">Proiect 0{i}</div>
            <h3 style="color: #241F21; font-size: {'28px' if desktop else '23px'}; font-weight: 400; line-height: 1.2; letter-spacing: -1.2px; margin: 0;">{t}</h3>
            <p>{d}</p>
          </div>
          {btn('Vezi studiul de caz','/proiecte/','link')}
        </div>
        <div style="position: relative; {'width: 380px; flex: none;' if desktop else 'width: 100%;'} display: grid; grid-template-columns: repeat({'1' if desktop else '1'}, minmax(0, 1fr)); gap: 20px; padding: {'0 0 10px 0' if desktop else '0'};">{counters}
        </div>
      </div>'''
    return f'''
  <!-- SECTIUNEA 6: Proiecte (layout "Our Projects" din tema) -->
  <section style="background: #F2EFE9; padding: {pad}; display: flex; flex-direction: column; align-items: center; gap: 20px;">
    {eyebrow('Proiecte', False)}
    {h2('Proiecte executate', False, desktop, 'max-width: 700px; text-align: center;')}
    <p style="max-width: 570px; text-align: center; margin: 0 0 {'50px' if desktop else '20px'} 0;">Fiecare proiect din portofoliu are date reale: locație, tip de tubulatură, metri liniari, termen.</p>
    <div style="width: 100%; display: flex; flex-direction: column;">{rows}
    </div>
    <div style="margin-top: 30px;">{btn('Vezi toate proiectele','/proiecte/','primary')}</div>
  </section>'''

# ---------------- SECTIUNEA 7: PARTENERI ----------------
PART=[('Ofertă pe ml sau pe proiect','Preț transparent, calculat pe metru liniar sau pe întregul pachet de tubulatură.'),
      ('Echipe de [X] montatori','Formații complete, dimensionate după graficul tău de execuție.'),
      ('Autoutilitare și scule proprii','Venim echipați: transport, scule, consumabile și utilaje de ridicat.'),
      ('Asigurare RC profesională [dacă există]','Acoperire pentru lucrările executate pe șantierul tău.')]
def partners(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    items=''
    for i,(t,d) in enumerate(PART):
        items+=f'''
        <div style="display: flex; gap: 20px; align-items: flex-start; padding: 20px 0;{' border-top: 1px solid rgba(238, 238, 238, 0.19);' if i else ''}">
          {ico('<circle cx="12" cy="12" r="9"></circle><path d="M8 12l3 3 5-6"></path>')}
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <h3 style="color: #F2EFE9; font-size: 21px; font-weight: 500; line-height: 1.3; letter-spacing: -0.8px; margin: 0;">{t}</h3>
            <p style="color: #D8D4CF;">{d}</p>
          </div>
        </div>'''
    return f'''
  <!-- SECTIUNEA 7: Pentru antreprenori (layout "Why Choose Us" din tema) -->
  <section style="position: relative; padding: {pad}; display: flex; flex-direction: {'row' if desktop else 'column'}; gap: {'40px' if desktop else '30px'}; align-items: flex-end; overflow: hidden;">
    {img('parteneri-bg.jpg','')}
    <div style="position: absolute; inset: 0; background-image: linear-gradient(180deg, rgba(36, 31, 33, 0.31) 0%, #241F21 100%);"></div>
    <div style="position: relative; {'width: 50%;' if desktop else 'width: 100%;'} display: flex; flex-direction: column; gap: 20px;">
      {eyebrow('Pentru antreprenori și firme de instalații', True)}
      {h2('Ai nevoie de o echipă de montaj tubulatură pe șantierul tău?', True, desktop, 'max-width: 700px;')}
      <p style="color: #D8D4CF; max-width: 570px;">Lucrăm ca subcontractor pentru antreprenori generali și firme de instalații care au proiectul, dar nu au echipa. Preluăm partea de tubulatură integral – material, confecție, montaj, documentație – și ne integrăm în graficul tău de execuție. Disponibili pentru lucrări în toată țara, cu mobilizare rapidă în Moldova.</p>
      <div style="margin-top: 10px;">{btn('Discută cu noi despre proiectul tău','/parteneri/','light')}</div>
    </div>
    <div style="position: relative; {'width: 50%;' if desktop else 'width: 100%;'} display: flex; flex-direction: column;">{items}
    </div>
  </section>'''

# ---------------- SECTIUNEA 8: ZONE ----------------
def map_svg(width):
    pts=[(20.26,46.13),(20.7,46.6),(21.1,46.9),(21.5,47.4),(22.0,47.8),(22.2,48.0),(22.9,47.95),(23.5,48.0),(24.0,47.95),(24.6,47.95),(25.0,47.75),(25.4,47.9),(26.0,47.95),(26.3,48.2),(26.6,48.27),(27.0,48.0),(27.3,47.6),(27.7,47.2),(28.1,46.7),(28.2,46.2),(28.1,45.6),(28.2,45.45),(28.8,45.3),(29.3,45.4),(29.7,45.2),(29.6,44.8),(28.9,44.4),(28.6,43.9),(28.6,43.75),(28.0,43.8),(27.5,44.0),(27.0,44.1),(26.5,44.05),(25.8,43.7),(25.4,43.62),(24.6,43.7),(23.8,43.8),(23.2,43.8),(22.7,44.2),(22.4,44.5),(22.7,44.6),(22.2,44.5),(21.6,44.8),(21.4,45.2),(21.0,45.3),(20.8,45.7),(20.7,46.0)]
    k=width/9.8; ky=k*1.42
    def P(lon,lat): return (round((lon-20.15)*k,1), round((48.4-lat)*ky,1))
    path=' '.join(('M' if i==0 else 'L')+f'{x},{y}' for i,(x,y) in enumerate(P(a,b) for a,b in pts))+' Z'
    cities=[('Tămășeni',26.93,46.95,True),('Piatra Neamț',26.37,46.93,False),('Iași',27.6,47.16,False),('Bacău',26.9,46.57,False),('Suceava',26.25,47.65,False),('Botoșani',26.67,47.75,False),('Vaslui',27.73,46.64,False),('Galați',28.05,45.44,False),('București',26.1,44.43,False)]
    h=round((48.4-43.5)*ky)
    out=[f'<svg viewBox="0 0 {width} {h}" width="{width}" height="{h}" style="display: block; max-width: 100%; height: auto;" role="img" aria-label="Harta României cu zonele deservite">',
         f'<path d="{path}" fill="#062D2B" stroke="#F2EFE9" stroke-width="1"></path>']
    # Moldova region highlight: rough polygon east of Carpathians
    mold=[(26.0,48.2),(26.6,48.27),(27.0,48.0),(27.3,47.6),(27.7,47.2),(28.1,46.7),(28.2,46.2),(28.1,45.6),(28.2,45.45),(27.6,45.4),(27.0,45.5),(26.4,45.9),(26.0,46.4),(25.9,47.0),(25.6,47.6),(25.4,47.9),(26.0,47.95)]
    mp=' '.join(('M' if i==0 else 'L')+f'{x},{y}' for i,(x,y) in enumerate(P(a,b) for a,b in mold))+' Z'
    out.append(f'<path d="{mp}" fill="#F6F36F" fill-opacity="0.22" stroke="#F6F36F" stroke-width="1"></path>')
    for name,lon,lat,hq in cities:
        x,y=P(lon,lat)
        if hq:
            out.append(f'<rect x="{x-6}" y="{y-6}" width="12" height="12" fill="#F6F36F"></rect><text x="{x+10}" y="{y-8}" font-family="Chivo Mono, Menlo, monospace" font-size="11" font-weight="500" fill="#F6F36F">{name.upper()} · SEDIU</text>')
        else:
            dx,dy=(8,4)
            if name in ('Suceava','Piatra Neamț','București'): dx=-8
            anchor='end' if dx<0 else 'start'
            out.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#F2EFE9"></circle><text x="{x+dx}" y="{y+dy}" text-anchor="{anchor}" font-family="Chivo Mono, Menlo, monospace" font-size="11" font-weight="500" fill="#F2EFE9">{name.upper()}</text>')
    out.append('</svg>')
    return '\n'.join(out)
ZONE=['Piatra Neamț','Roman','Iași','Bacău','Suceava','Botoșani','Vaslui','Galați','București','[alte orașe]']
def zones(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    links=''.join(f'<a href="/zone/{z.lower().replace(" ","-").replace("ț","t").replace("ș","s").replace("[","").replace("]","")}/" style="display: flex; align-items: center; gap: 10px; color: #241F21;"><span style="width: 8px; height: 8px; background: #241F21; flex: none;"></span><span>{z}</span></a>' for z in ZONE)
    return f'''
  <!-- SECTIUNEA 8: Zone deservite (doua coloane: text + harta simpla) -->
  <section style="background: #ECE6DF; padding: {pad}; display: flex; flex-direction: {'row' if desktop else 'column'}; gap: {'60px' if desktop else '30px'}; align-items: center;">
    <div style="{'width: 50%;' if desktop else 'width: 100%;'} display: flex; flex-direction: column; gap: 20px;">
      {eyebrow('Zone deservite', False)}
      {h2('Montaj tubulatură de ventilație în Moldova și în toată România', False, desktop, 'max-width: 600px;')}
      <p style="max-width: 570px;">Suntem în comuna Tămășeni, județul Neamț, la sub o oră de Iași, Bacău și Roman. Executăm lucrări curent în Neamț, Iași, Bacău, Suceava, Botoșani, Vaslui și Galați, și ne deplasăm pentru proiecte în orice județ.</p>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 30px; margin-top: 10px; max-width: 480px;">{links}</div>
    </div>
    <div style="{'width: 50%;' if desktop else 'width: 100%;'} background: #241F21; padding: {'40px' if desktop else '20px'}; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px;">
      {map_svg(600 if desktop else 330)}
      <div class="mono" style="display: flex; gap: 20px; flex-wrap: wrap; color: #D8D4CF;"><span style="display: flex; align-items: center; gap: 8px;"><span style="width: 10px; height: 10px; background: #F6F36F; opacity: 0.5;"></span>Mobilizare în aceeași zi</span><span style="display: flex; align-items: center; gap: 8px;"><span style="width: 10px; height: 10px; background: #062D2B; border: 1px solid #F2EFE9;"></span>Deplasare la cerere</span></div>
    </div>
  </section>'''

# ---------------- SECTIUNEA 9: FAQ ----------------
FAQ=[('Ce tip de tubulatură e potrivit pentru proiectul meu?','Depinde de destinație: zincată pentru hale și trasee mari, ALP pentru spații unde contează igiena și izolația, inox pentru alimentar și bucătării, rezistentă la foc pentru desfumare. Îți recomandăm soluția după ce vedem planul.'),
     ('Cât costă tubulatura de ventilație?','Prețul se calculează pe metru liniar sau pe metru pătrat de tablă/panou și depinde de secțiune, material, clasa de etanșeitate și complexitatea traseului. Trimite planul și primești ofertă detaliată în 48 de ore. <a href="/ghid-preturi/" style="color: #241F21; text-decoration: underline;">Vezi și ghidul nostru de prețuri.</a>'),
     ('Lucrați și în afara Moldovei?','Da, executăm lucrări în toată țara. Pentru proiecte din Moldova mobilizarea este în aceeași zi.'),
     ('Puteți lucra ca subcontractor?','Da, este cel mai frecvent mod în care lucrăm cu antreprenorii generali și firmele de instalații.'),
     ('Oferiți și materialul, sau doar manopera?','Ambele variante: putem livra la pachet material + montaj sau doar montaj pe materialul tău.'),
     ('Faceți teste de etanșeitate?','Da, la cerere, cu raport de măsurători conform clasei de etanșeitate din proiect.')]
def faq(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    rows=''
    for i,(q,a) in enumerate(FAQ):
        open_=(i==0)
        icon=('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5E5A5C" stroke-width="2" stroke-linecap="round" style="flex: none;"><path d="M5 12h14"></path></svg>' if open_ else
              '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#5E5A5C" stroke-width="2" stroke-linecap="round" style="flex: none;"><path d="M12 5v14"></path><path d="M5 12h14"></path></svg>')
        body=f'<p style="max-width: {"50%" if desktop else "100%"}; padding: 0 30px 30px 0;">{a}</p>' if open_ else ''
        rows+=f'''
      <div style="border-bottom: 1px solid #D8D4CF; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 40px; padding: {'12px 0 22px 0' if open_ else '22px 0'};">
          <h3 style="color: #241F21; font-size: {'21px' if desktop else '19px'}; font-weight: 500; line-height: 1.3; letter-spacing: -0.8px; margin: 0;">{q}</h3>
          {icon}
        </div>{body}
      </div>'''
    return f'''
  <!-- SECTIUNEA 9: FAQ (layout "Answers to Common Questions" din tema) -->
  <section style="background: #F2EFE9; padding: {pad}; display: flex; flex-direction: column; gap: 20px;">
    {eyebrow('Întrebări frecvente', False)}
    {h2('Întrebări frecvente', False, desktop, 'max-width: 550px; margin-bottom: ' + ('50px' if desktop else '20px') + ';')}
    <div style="display: flex; flex-direction: column;">{rows}
    </div>
  </section>'''

# ---------------- SECTIUNEA 10: CTA + FORMULAR ----------------
def field(label, ph, kind='input', dark=False):
    box='background: #F2EFE9; border: 1px solid #D8D4CF; padding: 14px 16px; color: #5E5A5C; box-sizing: border-box; width: 100%;'
    if kind=='select':
        inner=f'<div style="{box} display: flex; justify-content: space-between; align-items: center;"><span>{ph}</span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"></path></svg></div>'
    elif kind=='file':
        inner=f'<div style="{box} border-style: dashed; display: flex; align-items: center; gap: 10px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 16V4"></path><path d="M7 9l5-5 5 5"></path><path d="M4 20h16"></path></svg><span>{ph}</span></div>'
    elif kind=='textarea':
        inner=f'<div style="{box} min-height: 110px;">{ph}</div>'
    else:
        inner=f'<div style="{box}">{ph}</div>'
    return f'<div style="display: flex; flex-direction: column; gap: 8px;"><span class="mono" style="color: #241F21;">{label}</span>{inner}</div>'
def cta(desktop):
    pad='100px 30px' if desktop else '70px 10px'
    g2='repeat(2, minmax(0, 1fr))' if desktop else 'repeat(1, minmax(0, 1fr))'
    return f'''
  <!-- SECTIUNEA 10: CTA final + formular (layout "Ready to get started" din tema, cu formularul din pagina Consultation) -->
  <section style="background-image: linear-gradient(180deg, #ECE6DF 0%, #F2EFE9 100%); padding: 0 10px 10px 10px;">
    <div style="background: #241F21; background-image: radial-gradient(ellipse at 100% 0%, rgba(6, 45, 43, 0.7) 0%, rgba(36, 31, 33, 0) 55%); padding: {pad}; display: flex; flex-direction: {'row' if desktop else 'column'}; gap: {'60px' if desktop else '30px'}; align-items: flex-start;">
      <div style="{'width: 45%;' if desktop else 'width: 100%;'} display: flex; flex-direction: column; gap: 20px;">
        {eyebrow('Cere ofertă', True)}
        {h2('Trimite planul, primești oferta în 48 de ore', True, desktop, 'max-width: 600px;')}
        <p style="color: #D8D4CF; max-width: 500px;">Atașează planul HVAC sau descrie-ne proiectul: tip clădire, suprafață, termen. Revenim cu ofertă detaliată și recomandarea tehnică potrivită.</p>
        <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 20px; padding-top: 30px; border-top: 1px solid rgba(242, 239, 233, 0.125);">
          <div class="mono" style="color: #F6F36F;">Sau direct</div>
          <a href="tel:+40765887236" style="display: flex; align-items: center; gap: 12px; color: #F2EFE9; font-size: 21px; letter-spacing: -0.8px;">{ico('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.9 2z"></path>', 22, '#F6F36F')}+40 765 887 236</a>
          <a href="https://wa.me/40765887236" style="display: flex; align-items: center; gap: 12px; color: #F2EFE9;">{ico('<path d="M20 11.5a8 8 0 0 1-11.8 7L4 20l1.6-4A8 8 0 1 1 20 11.5z"></path><path d="M9.5 9.5c0 3 2 5 5 5l1-1.5-2-1-1 1a4 4 0 0 1-2-2l1-1-1-2z"></path>', 22, '#F6F36F')}WhatsApp</a>
          <a href="mailto:office@aerconduct.ro" style="display: flex; align-items: center; gap: 12px; color: #F2EFE9;">{ico('<rect x="3" y="5" width="18" height="14"></rect><path d="M3 7l9 6 9-6"></path>', 22, '#F6F36F')}office@aerconduct.ro</a>
        </div>
      </div>
      <div style="{'width: 55%;' if desktop else 'width: 100%;'} box-sizing: border-box; background: #ECE6DF; padding: {'40px' if desktop else '20px'}; display: flex; flex-direction: column; gap: 20px;">
        <div style="display: grid; grid-template-columns: {g2}; gap: 10px;">
          {field('Nume','Numele tău')}
          {field('Companie','Firma')}
          {field('Telefon','+40 7')}
          {field('Email','adresa@firma.ro')}
          {field('Județ','Neamț')}
          {field('Tip proiect','Hală industrială','select')}
        </div>
        {field('Plan HVAC','Atașează planul (DWG, PDF, până la 20 MB)','file')}
        {field('Mesaj','Tip clădire, suprafață, termen, orice detaliu util','textarea')}
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap;">
          <span class="spec" style="font-family: 'Chivo Mono', Menlo, monospace; font-size: 11px; color: #5E5A5C;">Răspundem în maximum 48 de ore lucrătoare.</span>
          {btn('Trimite cererea de ofertă','/cerere-oferta/','primary')}
        </div>
      </div>
    </div>
  </section>'''

# ---------------- FOOTER ----------------
def footer(desktop):
    pad='100px 30px 30px 30px' if desktop else '70px 10px 20px 10px'
    def col(title, links):
        ls=''.join(f'<a href="{h}" style="color: #5E5A5C;">{t}</a>' for t,h in links)
        return f'<div style="display: flex; flex-direction: column; gap: 20px;"><h3 style="color: #241F21; font-size: 17px; font-weight: 500; line-height: 1.3; letter-spacing: -0.6px; margin: 0;">{title}</h3><div style="display: flex; flex-direction: column; gap: 10px;">{ls}</div></div>'
    serv=[(t,u) for k,t,d,u,p in SERV]+[('Modificări instalații existente','/servicii/modificari-instalatii-ventilatie/'),('Igienizare și mentenanță','/servicii/igienizare-tubulatura/')]
    ind=[(t,u) for s,t,d,u in IND]
    zone=[(z,'/zone/') for z in ZONE[:8]]
    social='<div style="display: flex; gap: 10px;">'+''.join(f'<a href="#" aria-label="{n}" style="width: 40px; height: 40px; border: 1px solid #241F21; border-radius: 500px; display: flex; align-items: center; justify-content: center; color: #241F21;">{ico(p,18,"#241F21",1.8)}</a>' for n,p in [('Facebook','<path d="M14 8h3V4h-3c-2.8 0-5 2.2-5 5v2H6v4h3v9h4v-9h3l1-4h-4V9c0-.6.4-1 1-1z"></path>'),('LinkedIn','<path d="M4 9h4v12H4z"></path><circle cx="6" cy="5" r="2"></circle><path d="M11 21v-7a3 3 0 0 1 6 0v7"></path><path d="M11 9h4"></path>'),('WhatsApp','<path d="M20 11.5a8 8 0 0 1-11.8 7L4 20l1.6-4A8 8 0 1 1 20 11.5z"></path>')])+'</div>'
    grid='grid-template-columns: 340px repeat(3, minmax(0, 1fr));' if desktop else 'grid-template-columns: repeat(1, minmax(0, 1fr));'
    return f'''
  <!-- FOOTER (layout footer din tema, pe fundal accent) -->
  <footer style="background: #F6F36F; padding: {pad}; display: flex; flex-direction: column; gap: {'60px' if desktop else '40px'};">
    <div style="display: grid; {grid} gap: {'40px' if desktop else '40px'};">
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <img src="logo-dark.png" alt="Aerconduct" style="width: {'200px' if desktop else '170px'}; height: auto; display: block;">
        <p style="color: #241F21; max-width: 280px;">Execuție și montaj tubulatură de ventilație industrială și comercială. Echipă proprie, deplasare în toată țara.</p>
        <div class="mono" style="color: #5E5A5C; display: flex; flex-direction: column; gap: 4px; text-transform: none;"><span>[Denumire firmă SRL]</span><span>CUI [__________] · Reg. Com. [__________]</span><span>Comuna Tămășeni, județul Neamț</span></div>
      </div>
      {col('Servicii', serv)}
      <div style="display: flex; flex-direction: column; gap: 40px;">{col('Industrii', ind)}{col('Zone', zone)}</div>
      <div style="display: flex; flex-direction: column; gap: 40px;">
        {col('Contact', [('+40 765 887 236','tel:+40765887236'),('office@aerconduct.ro','mailto:office@aerconduct.ro'),('Profil Google Business','#')])}
        {col('Program', [('Luni – Vineri: 08:00 – 17:00','#'),('Sâmbătă – Duminică: închis','#')])}
        {social}
      </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; padding-top: 20px; border-top: 1px solid rgba(36, 31, 33, 0.19);">
      <div class="mono" style="display: flex; gap: 20px; flex-wrap: wrap;"><a href="/termeni/" style="color: #241F21;">Termeni</a><a href="/confidentialitate/" style="color: #241F21;">Confidențialitate</a><a href="/cookies/" style="color: #241F21;">Cookies</a></div>
      <span class="mono" style="color: #241F21;">© 2026 Aerconduct</span>
    </div>
  </footer>'''

for fn, desk in (('_main_body.html', True), ('_mobil_body.html', False)):
    s=open(fn,encoding='utf-8').read().rstrip()
    assert s.endswith('</div>')
    cut=s.find('\n  <!-- SECTIUNEA 2')
    if cut!=-1: s=s[:cut].rstrip()+'\n</div>'
    parts=[f(desk) for f in (about,services,process,industries,projects,partners,zones,faq,cta,footer)]
    s=s[:-6].rstrip()+''.join(parts)+'\n</div>\n'
    open(fn,'w',encoding='utf-8').write(s)
print('ok')
