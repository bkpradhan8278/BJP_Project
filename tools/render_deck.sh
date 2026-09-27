#!/usr/bin/env bash
# Renders the deck to PDF and per-slide PNGs (requires LibreOffice Impress + poppler-utils).
set -euo pipefail
cd "$(dirname "$0")/../deliverables"
soffice -env:UserInstallation=file:///tmp/lo_profile_deck --headless --convert-to pdf \
  Election_Intelligence_Command_Center_Executive_Deck.pptx >/dev/null 2>&1
mkdir -p slides && rm -f slides/slide-*.png
pdftoppm -png -r 90 Election_Intelligence_Command_Center_Executive_Deck.pdf slides/slide
ls slides | wc -l
