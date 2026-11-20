# Skills do Chat Master Veloz

Seis skills que ensinam o Claude a trabalhar com o Chat Master Veloz: tirar dúvidas de uso, integrar por API, montar fluxos de chatbot, escrever prompts de IA, redigir mensagens e personalizar o painel. Cada skill leva dentro dela a cópia da documentação oficial de que precisa, então funciona sozinha, sem internet e sem depender das outras.

| Skill | Para quê | Exemplo de pedido |
|---|---|---|
| `cmv-ajuda` | Como usar e configurar qualquer recurso do painel; dúvidas, erros, novidades | "Como cadastro uma atendente que só veja o setor Financeiro?" |
| `cmv-api` | Integrações por API e webhooks, com o código pronto | "Quero que minha loja mande um WhatsApp quando o pagamento for aprovado" |
| `cmv-flowbuilder` | Desenhar fluxos de chatbot: roteiro de montagem ou arquivo para importar | "Monta um fluxo de triagem com menu e horário de expediente" |
| `cmv-agente-ia` | Prompt e configuração do atendente de IA e dos outros recursos de IA | "Cria o prompt de uma atendente virtual para minha clínica" |
| `cmv-mensagens` | Respostas rápidas, templates da API Oficial, campanhas, agendamentos | "Escreve um template de cobrança que não seja reprovado" |
| `cmv-painel-css-js` | CSS e JS personalizados do painel | "Deixa o painel com as cores da minha marca" |

Não é preciso chamar a skill pelo nome: basta fazer o pedido, e o Claude escolhe a certa.

## Como instalar

**Claude Code, todas de uma vez (como plugin):**

```bash
claude --plugin-dir /caminho/para/skills-chatmasterveloz
```

**Claude Code, de forma permanente:** copie as pastas de `skills/` para `~/.claude/skills/` (valem em qualquer projeto) ou para `.claude/skills/` de um projeto.

```bash
cp -r skills/cmv-* ~/.claude/skills/
```

**claude.ai (aplicativo e site):** gere os pacotes com `python3 montar.py --zip` e envie cada arquivo `dist/<nome>.zip` em **Customize › Skills › + › Create skill › Upload a skill**. É preciso ter a execução de código ligada em **Settings › Capabilities**. O `dist/<nome>.skill` é o mesmo arquivo com outra extensão.

### Diga ao Claude que você usa o Chat Master Veloz

Nos modelos menores (Haiku e, às vezes, Sonnet), um pedido que não cita o nome da plataforma pode ser respondido sem carregar skill nenhuma. Uma linha de contexto resolve quase tudo: no teste cego, o Haiku foi de 78 para 83 acertos em 84 com ela, sem passar a acionar em pedidos sobre outras ferramentas.

- **Como plugin:** já vem pronto. O plugin tem um gancho de início de sessão (`hooks/hooks.json`) que entrega esta linha, guardada em `hooks/contexto.json`: "Esta empresa usa a plataforma Chat Master Veloz (CMV) para atender clientes pelo WhatsApp e outros canais."
- **Skills copiadas para `~/.claude/skills/` ou `.claude/skills/`:** ponha essa mesma linha no `CLAUDE.md` do projeto ou em `~/.claude/CLAUDE.md`.
- **claude.ai:** ponha a linha nas instruções do projeto ou nas suas preferências de perfil.

## Como atualizar quando a plataforma mudar

A documentação dentro de cada skill (`references/docs/`) é uma cópia das pastas `../docs-plataforma-chatmasterveloz/` e `../docs-css-chatmasterveloz/`. Para trazer a versão nova:

```bash
python3 ../docs-plataforma-chatmasterveloz/_gerar.py   # baixa a Central de Ajuda de novo
python3 ../docs-css-chatmasterveloz/_gerar.py          # baixa o catálogo de CSS de novo
python3 montar.py --zip                                # recopia para as skills e refaz os pacotes
```

O `montar.py` para com erro se um arquivo escrito à mão citar um artigo que deixou de existir (renomeado ou removido). Corrija a citação e rode de novo.

O que cada skill copia está em `skills/<nome>/fontes.txt`. Os arquivos escritos à mão (`SKILL.md`, `references/*.md`, `assets/`, `scripts/`) não são tocados pelo `montar.py`: depois de uma atualização grande da plataforma, vale reler os mapas e as receitas.

## Medição do acionamento

As descrições (o texto que faz o Claude escolher a skill) foram otimizadas e medidas com pedidos de teste, com as seis skills instaladas juntas e sem a configuração pessoal da máquina. Tudo fica em `avaliacao-gatilho/`.

**Medição atual: roteamento.** O `ferramenta/rotear.py` instala as seis skills de verdade e registra qual delas cada pedido carrega. Os pedidos estão em `roteamento/`: `desenvolvimento.json` (84, usados para ajustar as descrições) e `teste.json` (84, o teste cego, nunca usado para ajustar). Foram escritos por dois agentes separados e rotulados de novo por um terceiro, que concordou em 167 de 168. A maioria não cita o nome do produto. Resultado no teste cego, 3 repetições por pedido:

| Modelo | Descrições de 18/11 | Descrições de 19/11 (atuais) |
|---|---|---|
| Fable 5.2 | 84/84 | 84/84 |
| Opus 5.5 | 83/84 | 83/84 |
| Sonnet 5.5 | 81/84 | 82/84 |
| Haiku 5.5 | 74/84 | 78/84 |

Com a linha de contexto da seção "Diga ao Claude que você usa o Chat Master Veloz", o Haiku chega a 83/84 (instruções do projeto) e 82/84 (gancho do plugin); pelo plugin o Opus dá 84/84. Nos 240 pedidos das medições anteriores (`roteamento/antigos.json`), as descrições atuais dão 238 no Haiku e 239 no Opus.

Em nenhuma medição uma skill foi carregada em pedido sobre outra plataforma (12 de 12 em todos os modelos). O ponto fraco que resta é o Haiku responder direto, sem carregar skill, em parte dos pedidos que não citam o Chat Master Veloz; o número dele oscila uns 2 pedidos entre medições. As descrições anteriores e as novas estão em `descricoes/`, para comparar ou voltar atrás com `ferramenta/candidata.py <arquivo> --aplicar`.

```bash
cd avaliacao-gatilho/ferramenta
python3 rotear.py --modelo claude-haiku-5-5 --conjunto ../roteamento/teste.json
python3 candidata.py novas.json /tmp/candidata      # cópia das skills com descrições candidatas
python3 rotear.py --modelo claude-haiku-5-5 --conjunto ../roteamento/desenvolvimento.json --skills /tmp/candidata --sufixo=-candidata
```

Ao mudar uma descrição, ajuste pelo conjunto de desenvolvimento e só confira no teste cego no fim; depois rode também `roteamento/antigos.json` (os 240 pedidos das medições anteriores), que serve de conferência de regressão.

**Tarefas completas.** O acionamento é metade do caminho; o resultado de três rodadas de avaliação das respostas em Haiku e Sonnet, o que foi corrigido nas skills e o que ainda aparece estão em `avaliacao-gatilho/TAREFAS-COMPLETAS.md`. O `ferramenta/ponta_a_ponta.py` roda uma tarefa real por skill (`roteamento/tarefas-completas.json`) com as skills instaladas como cópias de verdade e guarda a resposta e os arquivos gerados, para alguém dar a nota contra a documentação. Opções do `rotear.py` além das mostradas acima: `--plugin` mede pelo caminho de instalação como plugin e `--contexto "texto"` simula as instruções do projeto.

**Para revisar os pedidos:** abra `avaliacao-gatilho/revisao-pedidos.html` no navegador. Ela lista os 168 pedidos com o resultado por modelo, começa pelos 22 em que a sua decisão é necessária e tem um campo para colar pedidos reais dos seus usuários. `AUDITORIA.md` traz o que uma auditoria independente achou nos conjuntos antigos.

**claude.ai:** não há como medir por script. O roteiro de teste manual está em `avaliacao-gatilho/TESTE-NO-CLAUDE-AI.md`.

**Medição anterior (18/11).** `otimizacao/`, `validacao/` e `independentes/` são os conjuntos da primeira otimização, medidos por skill com `ferramenta/medir.py` (cópias corrigidas dos scripts do skill-creator em `ferramenta/scripts/`); `REVISAO.md` mostra aqueles resultados. Esse medidor testa uma skill por vez com uma cópia temporária e, em paralelo, deixa várias cópias da mesma descrição visíveis, o que pode aumentar o acionamento; por isso o `rotear.py` é o medidor de referência.

## Limites

- As skills só afirmam o que a documentação diz. Imagens e vídeos da Central de Ajuda não foram transcritos, e preços e planos não são citados.
- O arquivo de fluxo que a `cmv-flowbuilder` gera segue o formato observado em um fluxo exportado, não um formato publicado pela plataforma: teste o fluxo importado antes de ligá-lo a uma conexão que atende clientes.
- As receitas de CSS foram conferidas contra o catálogo de seletores, não em um painel real.
