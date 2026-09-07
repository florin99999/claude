# -*- coding: utf-8 -*-
import importlib
v2 = importlib.import_module('build_v2'); V=v2.V2
css=v2.recolor(open('../airvora-ds/_shared.css',encoding='utf-8').read())
def sw(hexc, name, token, use, border=False, h=140):
    b=' border: 1px solid %s; box-sizing: border-box;' % V['border'] if border else ''
    return f'''<div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="height: {h}px; background: {hexc};{b}"></div>
        <div class="label"><span class="mono" style="color: {V['primary']};">{name}</span><span class="spec">{hexc} · {token}</span><span class="spec">{use}</span></div>
      </div>'''
def combo(bg, dot, eyeb_c, title_c, text_c, label, title, text, border=False):
    b=' border: 1px solid %s; box-sizing: border-box;' % V['border'] if border else ''
    return f'''<div style="background: {bg};{b} padding: 30px 20px; display: flex; flex-direction: column; gap: 10px; min-height: 200px;">
        <div class="mono" style="display: flex; align-items: center; gap: 10px; color: {eyeb_c};"><span style="width: 8px; height: 8px; background: {dot}; flex: none;"></span><span>{label}</span></div>
        <h5 style="color: {title_c};">{title}</h5>
        <p style="color: {text_c};">{text}</p>
      </div>'''
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>'
def b(text, st): return f'<a class="btn" href="#" style="{st}"><span>{text}</span>{ARROW}</a>'
def eb(t): return f'<div class="eyebrow mono"><span class="eyebrow-dot"></span><span>{t}</span></div>'
body=f'''
<div class="sheet">
  <div style="display: flex; flex-direction: column; gap: 30px;">
    {eb('Aerconduct · Design system v2 · Culori')}
    <h1 style="max-width: 900px;">Paleta v2, în jurul brandului</h1>
    <p style="max-width: 570px;">Aceleași roluri de culoare ca în tema Airvora, construite în jurul roșului și albastrului din logo. Tipografia, spațierea și componentele rămân cele din v1.</p>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px; padding-top: 30px; border-top: 1px solid {V['border']};">
      <div class="label"><span class="spec">Sursă</span><span class="name">Roșu și albastru din logo</span></div>
      <div class="label"><span class="spec">Ton</span><span class="name">Rece, tehnic, contrast puternic</span></div>
      <div class="label"><span class="spec">Regulă</span><span class="name">Roșu doar pentru ofertă, albastru pentru accent</span></div>
      <div class="label"><span class="spec">Planșe</span><span class="name">Homepage v2 desktop + mobil</span></div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-head">
      {eb('01 · Culorile brandului')}
      <h2>Două culori din logo</h2>
      <p style="max-width: 570px;">Roșul apare rar și cu un singur sens: cererea de ofertă (butonul din header, butonul principal din hero, trimiterea formularului). Albastrul preia rolul accentului din temă: etichete și cifre pe fundal închis, blocuri, footer în varianta deschisă.</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px;">
      <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 10px;">
        {sw(V['red'],'Roșu brand','--color-red','Butoanele de cerere de ofertă',h=180)}
        {sw(V['red_dark'],'Roșu închis','--color-red-dark','Hover pe butoanele roșii',h=180)}
        {sw(V['red_tint'],'Roșu deschis','--color-red-tint','Fundal pentru mesaje de eroare sau stare',h=180)}
      </div>
      <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 10px;">
        {sw(V['accent'],'Albastru brand','--color-accent','Etichete pe închis, cifre, blocuri, hartă',h=180)}
        {sw(V['blue_dark'],'Albastru închis','--color-blue-dark','Hover pe linkuri, iconițe pe deschis',h=180)}
        {sw(V['blue_tint'],'Albastru deschis','--color-blue-tint','Footer, tag-uri, fundal secundar',h=180)}
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-head">
      {eb('02 · Paleta completă')}
      <h2>Rolurile din temă, în culorile noi</h2>
      <p style="max-width: 570px;">Fiecare culoare din tema Airvora are un echivalent unu-la-unu, ca homepage-ul să poată fi trecut de pe v1 pe v2 fără să se schimbe layout-ul.</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px;">
      {sw(V['primary'],'Primary','--color-primary · v1 #241F21','Titluri, butoane secundare, fundal CTA și proces')}
      {sw(V['secondary'],'Secondary','--color-secondary · v1 #062D2B','Secțiuni închise: De ce Aerconduct')}
      {sw(V['text'],'Text','--color-text · v1 #5E5A5C','Paragrafe, linkuri')}
      {sw(V['accent'],'Accent','--color-accent · v1 #F6F36F','Etichete pe închis, cifre, blocuri')}
      {sw(V['surface'],'Surface','--color-surface · v1 #F2EFE9','Fundalul paginii, text pe închis',border=True)}
      {sw(V['surface2'],'Surface 2','--color-surface-2 · v1 #ECE6DF','Carduri, benzi alternative')}
      {sw(V['border'],'Border','--color-border · v1 #D8D4CF','Linii, separatoare')}
      {sw(V['surface3'],'Surface 3','--color-surface-3 · v1 #DFDACE','Hover pe carduri, blocuri secundare')}
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px; padding-top: 10px;">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="height: 60px; background: {V['secondary']}; display: flex; align-items: center; padding: 0 20px;"><div style="width: 100%; height: 1px; background: rgba(243, 245, 247, 0.125);"></div></div>
        <div class="label"><span class="spec">Surface 12% · rgba(243,245,247,.125)</span><span class="spec">Separator pe fundal închis</span></div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="height: 60px; background: {V['surface']}; border: 1px solid {V['border']}; box-sizing: border-box; display: flex; align-items: center; padding: 0 20px;"><div style="width: 100%; height: 1px; background: rgba(12, 26, 43, 0.125);"></div></div>
        <div class="label"><span class="spec">Primary 12% · rgba(12,26,43,.125)</span><span class="spec">Separator subtil pe deschis</span></div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="height: 60px; background: rgba(12, 26, 43, 0.31);"></div>
        <div class="label"><span class="spec">Primary 31% · rgba(12,26,43,.31)</span><span class="spec">Overlay pe fotografii</span></div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="height: 60px; background: {V['white']}; border: 1px solid {V['border']}; box-sizing: border-box;"></div>
        <div class="label"><span class="spec">White · #FFFFFF</span><span class="spec">Text pe butoanele roșii</span></div>
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-head">
      {eb('03 · Combinații de fundal')}
      <h2>Cum se așază culorile</h2>
      <p style="max-width: 570px;">Ca în temă: pe deschis, marcajul și textul etichetei sunt navy; pe închis, sunt albastru brand. Roșul nu apare în etichete sau în titluri.</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px;">
      {combo(V['surface'], V['primary'], V['primary'], V['primary'], V['text'], 'Deschis', 'Titlu pe fundal deschis', 'Text în gri rece, titluri în navy.', border=True)}
      {combo(V['surface2'], V['primary'], V['primary'], V['primary'], V['text'], 'Card', 'Titlu pe card', 'Aceleași culori de text ca pe deschis.')}
      {combo(V['secondary'], V['accent'], V['accent'], V['surface'], V['border'], 'Închis', 'Titlu pe albastru închis', 'Eticheta în albastru brand, text în border.')}
      {combo(V['blue_tint'], V['primary'], V['primary'], V['primary'], V['text'], 'Footer', 'Titlu pe albastru deschis', 'Fundalul footer-ului, text în gri rece.')}
      {combo(V['primary'], V['accent'], V['accent'], V['surface'], V['border'], 'Navy', 'Titlu pe navy', 'Linkuri în border, hover în surface.')}
    </div>
  </div>

  <div class="sec">
    <div class="sec-head">
      {eb('04 · Butoane și cifre')}
      <h2>Roșu doar pentru ofertă</h2>
      <p style="max-width: 570px;">Butonul roșu apare exclusiv la cererea de ofertă. Celelalte butoane urmează tema: navy pe deschis, deschis sau contur pe închis. Cifrele mari sunt albastre.</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px;">
      <div style="background: {V['surface']}; border: 1px solid {V['border']}; box-sizing: border-box; padding: 30px; display: flex; flex-direction: column; gap: 20px;">
        <div class="spec">Pe fundal deschis</div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          {b('Cere ofertă', f"background: {V['red']}; color: {V['white']}; padding: 14px 18px; border: 0;")}
          {b('Cere ofertă', f"background: {V['red_dark']}; color: {V['white']}; padding: 14px 18px; border: 0;")}
          <span class="spec">Ofertă · hover: roșu închis</span>
        </div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          {b('Toate serviciile', f"background: {V['primary']}; color: {V['surface']}; padding: 14px 18px; border: 0;")}
          {b('Toate serviciile', f"background: {V['text']}; color: {V['surface']}; padding: 14px 18px; border: 0;")}
          <span class="spec">Primar · hover: fundal Text</span>
        </div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          {b('Află mai mult', f"background: transparent; color: {V['primary']}; padding: 0; border: 0;")}
          {b('Află mai mult', f"background: transparent; color: {V['blue_dark']}; padding: 0; border: 0;")}
          <span class="spec">Link · hover: albastru închis</span>
        </div>
      </div>
      <div style="background: {V['secondary']}; padding: 30px; display: flex; flex-direction: column; gap: 20px;">
        <div class="spec" style="color: {V['border']};">Pe fundal închis</div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          {b('Despre echipă', f"background: {V['surface']}; color: {V['primary']}; padding: 14px 18px; border: 0;")}
          {b('Despre echipă', f"background: {V['accent']}; color: {V['primary']}; padding: 14px 18px; border: 0;")}
          <span class="spec" style="color: {V['border']};">Deschis · hover: fundal albastru</span>
        </div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          {b('Vezi serviciile', f"background: transparent; color: {V['accent']}; padding: 13px 17px; border: 1px solid rgba(243, 245, 247, 0.19);")}
          {b('Vezi serviciile', f"background: {V['accent']}; color: {V['primary']}; padding: 13px 17px; border: 1px solid {V['accent']};")}
          <span class="spec" style="color: {V['border']};">Contur · hover: fundal albastru</span>
        </div>
        <div style="display: flex; gap: 30px; align-items: flex-end; flex-wrap: wrap; padding-top: 10px;">
          <div style="font-size: 90px; line-height: 1; letter-spacing: -3px; color: {V['accent']};">48<span style="font-size: 50px; letter-spacing: -2px;">h</span></div>
          <div class="mono" style="display: flex; align-items: center; gap: 10px; color: {V['accent']}; padding-bottom: 14px;"><span style="width: 8px; height: 8px; background: {V['accent']}; flex: none;"></span><span>Etichetă pe închis</span></div>
        </div>
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-head">
      {eb('05 · Token-uri')}
      <h2>Variabile CSS</h2>
    </div>
    <div style="background: {V['primary']}; padding: 30px; font-family: 'Chivo Mono', Menlo, Consolas, monospace; font-size: 12px; line-height: 1.7; color: {V['surface']}; white-space: pre; overflow-x: auto;">:root {{
  --color-primary:   {V['primary']};   --color-secondary: {V['secondary']};
  --color-text:      {V['text']};   --color-accent:    {V['accent']};
  --color-surface:   {V['surface']};   --color-surface-2: {V['surface2']};
  --color-border:    {V['border']};   --color-surface-3: {V['surface3']};
  --color-red:       {V['red']};   --color-red-dark:  {V['red_dark']};   --color-red-tint:  {V['red_tint']};
  --color-blue-dark: {V['blue_dark']};   --color-blue-tint: {V['blue_tint']};   --color-white:     {V['white']};
  --color-surface-a12: rgba(243, 245, 247, 0.125);   --color-primary-a12: rgba(12, 26, 43, 0.125);
  --color-primary-a31: rgba(12, 26, 43, 0.31);        --color-black-a19:   rgba(0, 0, 0, 0.19);
}}</div>
  </div>
</div>
'''
doc='<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500&family=Chivo+Mono:wght@400;500&display=swap">\n  <style>\n'+css+'  </style>\n</helmet>\n'+body+'</x-dc>\n</body>\n</html>\n'
open('V2Culori.dc.html','w',encoding='utf-8').write(doc); print('palette ok')
