#!/usr/bin/env bash
# gen.sh — harness de UMA janela de GPU para N cenas.
# Roda no Oráculo:  ./gen.sh cenas.tsv [--only prefixo]
#
# Por que existe: cada chamada solta ao qwen-image.sh para e religa o llama-cpp
# (o modelo de chat ocupa ~25 GB da VRAM). Gerar 16 cenas assim = 16 ciclos.
# Aqui o ciclo acontece uma vez: para no começo, gera tudo, religa no fim —
# sempre com trap, inclusive se for interrompido.
#
# A referência de personagem vem por variável de ambiente:
#   REF=/mnt/Volatil/sdcpp/ref/jogador-quarto.png ./gen.sh cenas-cap1.tsv
set -uo pipefail

ROOT=/mnt/Volatil/sdcpp
REF="${REF:-$ROOT/ref/personagem-noir.png}"
MAN=${1:?uso: ./gen.sh cenas.tsv [--only prefixo]}
ONLY=""
if [ "${2:-}" = "--only" ]; then ONLY="${3:-}"; fi

# Negativo base: vale para toda cena do curso.
NEG_BASE="text, letters, words, writing, caption, speech bubble, watermark, signature, logo, extra fingers, deformed hands"

n_ok=0; n_fail=0

midclt call app.stop llama-cpp >/dev/null 2>&1
trap 'echo "[gen] religando llama-cpp..."; midclt call app.start llama-cpp >/dev/null 2>&1' EXIT INT TERM

while IFS=$'\t' read -r name model w h seed ref prompt extra_neg; do
  case "$name" in ''|\#*) continue ;; esac
  if [ -n "$ONLY" ]; then
    case "$name" in "$ONLY"*) ;; *) continue ;; esac
  fi

  neg="$NEG_BASE"
  [ -n "${extra_neg:-}" ] && neg="$neg, $extra_neg"

  args=(--model "$model" -W "$w" -H "$h" --seed "$seed" --no-cycle -o "$name" -n "$neg")
  if [ "${ref:-n}" = "y" ]; then
    args+=(-r "$REF")
  fi

  echo "[gen] >>> $name  ($model ${w}x${h} seed=$seed ref=${ref:-n})"
  if "$ROOT/qwen-image.sh" "$prompt" "${args[@]}"; then
    n_ok=$((n_ok+1))
  else
    n_fail=$((n_fail+1)); echo "[gen] !!! FALHOU: $name" >&2
  fi
done < "$MAN"

echo "[gen] fim: ok=$n_ok falhas=$n_fail"
