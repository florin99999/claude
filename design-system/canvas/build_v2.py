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
    # butonul principal (pe sectiuni inchise + header) devine rosu brand
    s = s.replace('.btn-light { background: %s; color: %s; padding: 14px 18px; border: 0; }' % (V2['surface'], V2['primary']),
                  '.btn-light { background: %s; color: %s; padding: 14px 18px; border: 0; }' % (V2['red'], V2['white']))
    s = s.replace('.btn-light:hover { background: %s; color: %s; }' % (V2['accent'], V2['primary']),
                  '.btn-light:hover { background: %s; color: %s; }' % (V2['red_dark'], V2['white']))
    s = s.replace("background: %s; color: %s; padding: 14px 18px; border: 0;'" % (V2['surface'], V2['primary']), "XX")
    # CTA-urile principale generate inline (btn('...','light')) -> rosu
    s = s.replace('style="background: %s; color: %s; padding: 14px 18px; border: 0; "' % (V2['surface'], V2['primary']),
                  'style="background: %s; color: %s; padding: 14px 18px; border: 0; "' % (V2['red'], V2['white']))
    # butonul de trimitere a formularului -> rosu
    s = s.replace('style="background: %s; color: %s; padding: 14px 18px; border: 0; "><span>Trimite cererea de ofertă</span>' % (V2['primary'], V2['surface']),
                  'style="background: %s; color: %s; padding: 14px 18px; border: 0; "><span>Trimite cererea de ofertă</span>' % (V2['red'], V2['white']))
    # marcajele patrate ale etichetelor -> rosu brand (pe deschis si pe inchis)
    s = s.replace('width: 8px; height: 8px; background: %s; flex: none;' % V2['accent'], 'width: 8px; height: 8px; background: %s; flex: none;' % V2['red'])
    s = s.replace('width: 9px; height: 9px; background: %s; flex: none;' % V2['accent'], 'width: 9px; height: 9px; background: %s; flex: none;' % V2['red'])
    s = s.replace('width: 9px; height: 9px; background: %s; flex: none;' % V2['primary'], 'width: 9px; height: 9px; background: %s; flex: none;' % V2['red'])
    # footer pe albastru brand: linkurile in navy pentru contrast
    if '<footer' in s:
        head, foot = s.split('<footer', 1)
        foot = foot.replace('color: %s;' % V2['text'], 'color: %s;' % V2['primary'])
        s = head + '<footer' + foot
    return s
SRC = ['Main','HomeB','HomeC','Mobil','MobilB','MobilC','MobilD','MobilE']
DST = ['V2Home','V2HomeB','V2HomeC','V2Mobil','V2MobilB','V2MobilC','V2MobilD','V2MobilE']
for a,b in zip(SRC,DST):
    s = open(a+'.dc.html', encoding='utf-8').read()
    open(b+'.dc.html','w',encoding='utf-8').write(recolor(s))
    print('wrote', b)
