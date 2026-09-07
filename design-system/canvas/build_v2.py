# -*- coding: utf-8 -*-
import re, os
# ---------- Paleta v2 (roluri identice cu tema, culori in jurul brandului) ----------
V2 = {
 'primary':   '#0C1A2B',  # navy aproape negru (titluri, butoane secundare, fundal CTA)
 'secondary': '#10334F',  # albastru inchis (sectiuni inchise)
 'text':      '#5B6470',  # gri rece
 'accent':    '#3EA8DE',  # albastru brand (etichete pe inchis, cifre, blocuri, footer)
 'surface':   '#F3F5F7',  # alb rece
 'surface2':  '#E8EDF1',  # carduri
 'border':    '#CFD6DD',
 'surface3':  '#DDE4EA',
 'red':       '#E02127',  # rosu brand (CTA principal, marcaje)
 'red_dark':  '#B8151B',
 'red_tint':  '#FBE3E4',
 'blue_dark': '#1E7FB3',
 'blue_tint': '#D6ECF8',
 'white':     '#FFFFFF',
}
MAP = [
 ('#241F21', V2['primary']), ('#062D2B', V2['secondary']), ('#5E5A5C', V2['text']), ('#F6F36F', V2['accent']),
 ('#F2EFE9', V2['surface']), ('#ECE6DF', V2['surface2']), ('#D8D4CF', V2['border']), ('#DFDACE', V2['surface3']),
 ('rgba(242, 239, 233,', 'rgba(243, 245, 247,'), ('rgba(36, 31, 33,', 'rgba(12, 26, 43,'), ('rgba(6, 45, 43,', 'rgba(16, 51, 79,'),
]
def recolor(s):
    for a,b in MAP: s = s.replace(a,b)
    # rosul doar pe CTA-urile de oferta: header, hero, "Incepe cu o cerere de oferta", trimiterea formularului
    s = s.replace('.nav a.active { color: %s; }' % V2['accent'],
                  '.nav a.active { color: %s; }\n    .btn-light[href="/cerere-oferta/"] { background: %s; color: %s; }\n    .btn-light[href="/cerere-oferta/"]:hover { background: %s; color: %s; }' % (V2['accent'], V2['red'], V2['white'], V2['red_dark'], V2['white']))
    s = s.replace('href="/cerere-oferta/" style="background: %s; color: %s; padding: 14px 18px; border: 0; "' % (V2['surface'], V2['primary']),
                  'href="/cerere-oferta/" style="background: %s; color: %s; padding: 14px 18px; border: 0; "' % (V2['red'], V2['white']))
    s = s.replace('style="background: %s; color: %s; padding: 14px 18px; border: 0; "><span>Trimite cererea de ofertă</span>' % (V2['primary'], V2['surface']),
                  'style="background: %s; color: %s; padding: 14px 18px; border: 0; "><span>Trimite cererea de ofertă</span>' % (V2['red'], V2['white']))
    # footer pe albastru deschis, mai putin dominant
    s = s.replace('<footer style="background: %s;' % V2['accent'], '<footer style="background: %s;' % V2['blue_tint'])
    return s
SRC = ['Main','HomeB','HomeC','Mobil','MobilB','MobilC','MobilD','MobilE']
DST = ['V2Home','V2HomeB','V2HomeC','V2Mobil','V2MobilB','V2MobilC','V2MobilD','V2MobilE']
for a,b in zip(SRC,DST):
    s = open(a+'.dc.html', encoding='utf-8').read()
    open(b+'.dc.html','w',encoding='utf-8').write(recolor(s))
    print('wrote', b)
