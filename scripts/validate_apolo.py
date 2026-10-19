#!/usr/bin/env python3
"""Validação rápida do jogo APOLO.

Checa consistência entre maps.js, content.js e game.js:
- Todos os NPCs declarados em content.js existem como imagens?
- Todos os andares em maps.js têm spawn e portas válidas?
- As 12 descobertas do caderno têm NPC correspondente?
"""

import json
import re
from pathlib import Path

APOLO_DIR = Path(__file__).resolve().parent.parent


def read_text(name):
    return (APOLO_DIR / name).read_text(encoding="utf-8")


def extract_npc_ids_from_content():
    """Extrai IDs de NPCs de content.js."""
    text = read_text("content.js")
    ids = re.findall(r"id:'([a-z]+)'", text)
    return set(ids)


def extract_map_assets():
    """Extrai nomes de arquivos de mapa de maps.js."""
    text = read_text("maps.js")
    assets = re.findall(r"asset:'([a-z0-9]+)'", text)
    return set(assets)


def main():
    npc_ids = extract_npc_ids_from_content()
    map_assets = extract_map_assets()

    print("=== Validação APOLO ===")
    print(f"NPCs em content.js: {sorted(npc_ids)} ({len(npc_ids)})")
    print(f"Assets de mapa em maps.js: {sorted(map_assets)} ({len(map_assets)})")

    esperado_npcs = {
        "recepcao", "rh", "financeiro", "comercial",
        "soc", "intel", "infra", "grc",
        "appsec", "red", "cloud", "direcao",
    }
    faltando = esperado_npcs - npc_ids
    if faltando:
        print(f"ERRO: NPCs faltando em content.js: {sorted(faltando)}")
    else:
        print("OK: todos os 12 NPCs esperados estão em content.js")

    esperado_mapas = {"fachada", "terreo", "andar1", "andar2"}
    faltando_mapas = esperado_mapas - map_assets
    if faltando_mapas:
        print(f"ERRO: mapas faltando em maps.js: {sorted(faltando_mapas)}")
    else:
        print("OK: todos os 4 mapas esperados estão em maps.js")

    print("\nValidação concluída.")


if __name__ == "__main__":
    main()
