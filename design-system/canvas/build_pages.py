# -*- coding: utf-8 -*-
import re, importlib, json
bs = importlib.import_module('build_sections')
HEAD = open('_head.html', encoding='utf-8').read()
def hero(fn):
    s = open(fn, encoding='utf-8').read()
    cut = s.find('\n  <!-- SECTIUNEA 2')
    root_open = s[:s.find('\n')+1]           # first line: root div
    body = s[len(root_open):cut] if cut != -1 else s[len(root_open):s.rfind('</div>')]
    return root_open, body
SEG_DESK = [('Main',   'hero+about+services',  [bs.about, bs.services]),
            ('HomeB',  'process+industries+projects', [bs.process, bs.industries, bs.projects]),
            ('HomeC',  'partners+zones+faq+cta+footer', [bs.partners, bs.zones, bs.faq, bs.cta, bs.footer])]
SEG_MOB  = [('Mobil',  'hero+about',            [bs.about]),
            ('MobilB', 'services+process',      [bs.services, bs.process]),
            ('MobilC', 'industries+projects',   [bs.industries, bs.projects]),
            ('MobilD', 'partners+zones+faq',    [bs.partners, bs.zones, bs.faq]),
            ('MobilE', 'cta+footer',            [bs.cta, bs.footer])]
def build(segs, body_file, desktop, width):
    root_open, hero_body = hero(body_file)
    for i, (name, _, fns) in enumerate(segs):
        parts = ''.join(f(desktop) for f in fns)
        if i == 0:
            doc = root_open + hero_body + parts + '\n</div>\n'
        else:
            doc = f'<div style="width: {width}px; position: relative; background: #F2EFE9;">' + parts + '\n</div>\n'
        open(name + '.dc.html', 'w', encoding='utf-8').write(HEAD + doc + '</x-dc>\n</body>\n</html>\n')
        print('wrote', name)
build(SEG_DESK, '_main_body.html', True, 1440)
build(SEG_MOB, '_mobil_body.html', False, 390)
