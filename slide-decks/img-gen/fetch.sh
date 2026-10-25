#!/usr/bin/env bash
# fetch.sh — traz as cenas geradas no Oráculo para img/ do repositório.
# Roda no agente (não no Oráculo). Usa o cenas.tsv para saber o que buscar.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="$HERE/../img"
OUT=/mnt/Volatil/sdcpp/out
n=0

while IFS=$'\t' read -r name _rest; do
  case "$name" in ''|\#*) continue ;; esac
  if scp -q "oraculo:$OUT/$name.png" "$DEST/$name.png" 2>/dev/null; then
    n=$((n+1))
    echo "ok   $name.png"
  else
    echo "falta $name.png"
  fi
done < "$HERE/cenas.tsv"

echo "--- $n arquivo(s) em $DEST"
