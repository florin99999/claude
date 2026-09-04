#!/usr/bin/env bash
# Descarcă imaginile generate (Higgsfield) în assets/img/ și rescrie index.html
# ca să le încarce local. Rulează din rădăcina proiectului:  bash scripts/localize-images.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/img
while read -r name url; do
  [ -z "$name" ] && continue
  out="assets/img/$name.png"
  if [ ! -s "$out" ]; then
    echo "↓ $name"
    curl -fsSL "$url" -o "$out"
  fi
  # conversie opțională în WebP dacă există cwebp (mai mic cu ~70%)
  if command -v cwebp >/dev/null 2>&1; then
    cwebp -quiet -q 80 "$out" -o "assets/img/$name.webp" && out="assets/img/$name.webp"
  fi
  sed -i.bak "s#$url#$out#g" index.html && rm -f index.html.bak
done < scripts/images.txt
echo "Gata. Imaginile sunt în assets/img/ și index.html a fost actualizat."
