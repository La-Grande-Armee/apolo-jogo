# Checklist de Qualidade — APOLO (adaptado do game-design-docs)

Use este checklist antes de commitar alterações no jogo APOLO.

## Conceito e promessa

- [ ] O conceito do jogo cabe em uma frase: "Quem, onde, o que escolhe, o que sente"
- [ ] A promessa ao jogador está clara (não é apenas "fazer um jogo popular")
- [ ] Fatos, hipóteses e decisões estão separados

## Coarlulo (core loop)

- [ ] O coarlulo conecta início ao fim sem interrupções
- [ ] Há escolha significativa dentro do loop (qual NPC visitar primeiro, qual resposta)
- [ ] Há trade-off nas escolhas
- [ ] Tempo por loop é razoável (2–4 minutos por NPC)

## Sistemas e UX

- [ ] Cada sistema tem mapeamento: regra → desafio/escolha → UX gerada
- [ ] Sistemas desnecessários para o MVP foram removidos
- [ ] Recursos têm entrada e saída definidas

## Ciclo do jogo

- [ ] Entrada definida (criar personagem, entrar no prédio)
- [ ] Término definido (12/12 descobertas, missão final com Alice, crachá)
- [ ] Duração estimada: 15–25 minutos

## MVP

- [ ] Personagem personalizável (nome, pele, cabelo, roupa, acessório)
- [ ] 3 andares com 12 NPCs + mentora Alice
- [ ] Diálogos + quiz por NPC
- [ ] Caderno com progresso X/12
- [ ] Missão final com Alice (3 perguntas)
- [ ] Crachá de conclusão para baixar em PNG
- [ ] Progresso salvo em localStorage (versão apolo-v3)
- [ ] Exportar/importar progresso em JSON

## Não está no MVP (não adicionar agora)

- [ ] Sala da turma multijogador (PeerJS) — opcional, experimental
- [ ] Minigames completos
- [ ] Fases 2–5
- [ ] Login de usuário / salvamento em nuvem

## Qualidade de código

- [ ] Todos os 12 NPCs existem em content.js
- [ ] Todos os 4 mapas existem em maps.js
- [ ] Todos os arquivos .js passam em `node --check`
- [ ] Testes `node --test apolo/tests/*.test.js` passam
- [ ] Script de validação `apolo/scripts/validate_apolo.py` roda sem erros

## Segurança

- [ ] Nenhuma chave de API, senha ou token adicionado ao repositório
- [ ] Nomes de jogadores tratados como texto puro (sem HTML)
- [ ] Progresso limitado a 16 KiB
