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

**Claude Code, pelo marketplace (recomendado):** dentro de uma sessão do Claude Code, rode

```text
/plugin install chatmasterveloz --marketplace paulotodo/skills-chatmasterveloz
```

Em versão anterior à 2.1.275, são dois passos: `/plugin marketplace add paulotodo/skills-chatmasterveloz` e depois `/plugin install chatmasterveloz@chatmasterveloz`. As skills passam a valer em qualquer projeto. A documentação copiada nas skills é atualizada todo dia no repositório; para receber, rode `/plugin marketplace update chatmasterveloz` ou ligue a atualização automática desse marketplace em `/plugin`.

**Claude Code, a partir de uma cópia da pasta (sem instalar):**

```bash
claude --plugin-dir /caminho/para/skills-chatmasterveloz
```

**Claude Code, de forma permanente:** copie as pastas de `skills/` para `~/.claude/skills/` (valem em qualquer projeto) ou para `.claude/skills/` de um projeto. Se você já enviou os pacotes ao claude.ai e entra no Claude Code com a mesma conta, elas chegam sozinhas (aparecem em `/skills` sob "claude.ai sync") e a cópia é dispensável.

```bash
cp -r skills/cmv-* ~/.claude/skills/
```

**claude.ai (aplicativo e site):** gere os pacotes com `python3 montar.py --zip` e envie cada arquivo `dist/<nome>.zip` em **Customize › Skills › + › Create skill › Upload a skill**. É preciso ter a execução de código ligada em **Settings › Capabilities**. O `dist/<nome>.skill` é o mesmo arquivo com outra extensão. O claude.ai recusa pacote com mais de 200 arquivos e também recusa zip dentro do pacote; por isso, nos pacotes da `cmv-ajuda` e da `cmv-api` os artigos vão todos num arquivo de texto, `references/docs.json`, e o `SKILL.md` do pacote manda extraí-los antes de ler. A pasta `skills/` não muda.

### Diga ao Claude que você usa o Chat Master Veloz

Nos modelos menores (Haiku e, às vezes, Sonnet), um pedido que não cita o nome da plataforma pode ser respondido sem carregar skill nenhuma. Um parágrafo de contexto resolve a maior parte:

> Esta empresa usa a plataforma Chat Master Veloz (CMV) para atender clientes pelo WhatsApp e outros canais. Pedidos sobre atendimento, painel, tickets, fluxos, mensagens, IA ou integrações que não citem outra ferramenta são sobre o CMV: carregue com a ferramenta Skill a skill cmv-* que trata do assunto antes de responder, mesmo que o pedido não cite a plataforma. Pedido que cita outra ferramenta ou plataforma (ManyChat, Typebot, Zapier, Chatwoot, o aplicativo WhatsApp Business e semelhantes) não é do CMV: responda sem as skills cmv-*.

- **Como plugin:** já vem pronto. O plugin tem um gancho de início de sessão (`hooks/hooks.json`) que entrega esse texto, guardado em `hooks/contexto.json`.
- **Skills copiadas para `~/.claude/skills/` ou `.claude/skills/`:** ponha o texto no `CLAUDE.md` do projeto ou em `~/.claude/CLAUDE.md`.
- **claude.ai:** ponha o texto nas instruções do projeto ou nas suas preferências de perfil.

O que foi medido com esse texto e as descrições atuais (de 21/11), no Haiku: 83 de 84 no teste cego antigo e 35 de 36 no teste cego dos módulos novos, sem carregar skill em nenhum pedido sobre outra ferramenta (18 de 18). Sem contexto nenhum ele faz 81 e 34. Com as descrições de 19/11 e este texto, Sonnet e Opus tinham feito 83 e 84 de 84; não foram medidos de novo com o texto. Numa tarefa de API que não cita o produto, o Haiku passou a carregar a skill em 3 de 3 execuções (antes, nenhuma). O custo: no Haiku aumentam os casos em que ele carrega a skill certa e mais uma irmã junto. A versão sem a última frase (a exceção para outras ferramentas) não serve: com ela o Haiku passou a carregar skills em pedidos sobre ManyChat, Zapier e o aplicativo WhatsApp Business.

## Como atualizar quando a plataforma mudar

A documentação dentro de cada skill (`references/docs/`) é uma cópia das pastas `../docs-plataforma-chatmasterveloz/` e `../docs-css-chatmasterveloz/`.

**Automático.** O `atualizar.sh` baixa a Central de Ajuda e o catálogo de CSS, recopia para as skills, roda os autotestes, refaz os pacotes e registra tudo num commit. Ele está agendado no cron deste servidor para todo dia às 06:20 UTC (`crontab -l` mostra a linha; `crontab -e` muda o horário ou remove). O resultado de cada execução fica em `atualizacoes.log`:

- `sem mudanças na documentação`: nada a fazer.
- `ATUALIZADO: …`: entrou um commit com a lista dos artigos novos e removidos. Artigo novo pode pedir revisão dos mapas escritos à mão.
- `FALHOU: …`: nada mudou (as pastas de origem e as skills voltam ao estado anterior). O caso mais comum é um arquivo escrito à mão citar um artigo que saiu ou mudou de nome: corrija a citação, registre no git e rode `./atualizar.sh`.
- `PULADO: …`: havia alteração não registrada no git. Registre (`git commit`) ou desfaça, senão a atualização não roda.

**À mão**, se preferir:

```bash
python3 ../docs-plataforma-chatmasterveloz/_gerar.py   # baixa a Central de Ajuda de novo
python3 ../docs-css-chatmasterveloz/_gerar.py          # baixa o catálogo de CSS de novo
python3 montar.py --zip                                # recopia para as skills e refaz os pacotes
```

O `montar.py` para com erro se um arquivo escrito à mão citar um artigo que deixou de existir, seja como `references/docs/recursos/x.md`, `recursos/x.md` ou só `x.md`.

O que cada skill copia está em `skills/<nome>/fontes.txt`. Os arquivos escritos à mão (`SKILL.md`, `references/*.md`, `assets/`, `scripts/`) não são tocados pela atualização, e é neles que a plataforma pode envelhecer sem aviso: a atualização troca a cópia dos artigos, mas não reescreve um resumo que deixou de ser verdade. Depois de uma mudança grande (módulo novo, tela reorganizada), vale uma revisão. A de 20/11/2026 está descrita no histórico do git.

## Medição do acionamento

As descrições (o texto que faz o Claude escolher a skill) foram otimizadas e medidas com pedidos de teste, com as seis skills instaladas juntas e sem a configuração pessoal da máquina. Tudo fica em `avaliacao-gatilho/`.

**Medição atual: roteamento.** O `ferramenta/rotear.py` instala as seis skills de verdade e registra qual delas cada pedido carrega. Os pedidos estão em `roteamento/`: `desenvolvimento.json` (84, usados para ajustar as descrições) e `teste.json` (84, o teste cego). Foram escritos por dois agentes separados e rotulados de novo por um terceiro, que concordou em 167 de 168. A maioria não cita o nome do produto. Em 21/11 entraram `novos-desenvolvimento.json` e `novos-teste.json` (36 cada), sobre os módulos que a plataforma ganhou em 20/11 (Consultório, Reservas, Mail Marketing, Dashboard, Links de agendamento, Base de Conhecimento, Provedor de IA), escritos por um agente que não viu as descrições e rotulados às cegas por outro, que concordou no destino dos 72. Resultado nos testes cegos, 3 repetições por pedido:

| Modelo | Antigo (84): 18/11 | 19/11 | 21/11 (atuais) | Novo (36): 19/11 | 21/11 (atuais) |
|---|---|---|---|---|---|
| Fable 5.2 | 84 | 84 | 84 | não medido | 36 |
| Opus 5.5 | 83 | 83 | 83 | 35 | 36 |
| Sonnet 5.5 | 81 | 82 | 82 | 32 | 36 |
| Haiku 5.5 | 74 | 78 | 81 | 30 | 34 |

As descrições de 21/11 mudaram em quatro skills (`cmv-ajuda`, `cmv-api`, `cmv-agente-ia`, `cmv-mensagens`): passaram a citar os módulos novos, a `cmv-mensagens` passou a aceitar o e-mail que vai pelo Mail Marketing e a `cmv-agente-ia` ganhou a frase "quem tem esta skill usa o CMV", que as outras já tinham. Todas estão a até 5 bytes do limite de 1.024: incluir qualquer coisa pede cortar outra. Nos 240 pedidos das medições anteriores (`roteamento/antigos.json`) o Haiku fez 238 antes e 238 depois. Uma versão intermediária foi descartada porque fazia um erro técnico que aparece na tela ("Missing Body in Payload") cair na `cmv-api`; a versão final foi conferida no teste cego depois desse ajuste, então o teste cego antigo já não é totalmente cego e o novo foi usado duas vezes.

Em nenhuma medição uma skill foi carregada em pedido sobre outra plataforma (12 de 12 no conjunto antigo e 6 de 6 no novo, em todos os modelos medidos). O ponto fraco que resta é o Haiku responder direto, sem carregar skill, em parte dos pedidos que não citam o Chat Master Veloz (nos módulos novos, as dúvidas de uso da Avaliação pela IA); o número dele oscila uns 2 pedidos entre medições, e o texto de contexto da seção "Diga ao Claude que você usa o Chat Master Veloz" cobre boa parte disso. As descrições anteriores e as novas estão em `descricoes/`, para comparar ou voltar atrás com `ferramenta/candidata.py <arquivo> --aplicar`.

```bash
cd avaliacao-gatilho/ferramenta
python3 rotear.py --modelo claude-haiku-5-5 --conjunto ../roteamento/teste.json
python3 candidata.py novas.json /tmp/candidata      # cópia das skills com descrições candidatas
python3 rotear.py --modelo claude-haiku-5-5 --conjunto ../roteamento/desenvolvimento.json --skills /tmp/candidata --sufixo=-candidata
```

Ao mudar uma descrição, ajuste pelo conjunto de desenvolvimento e só confira no teste cego no fim; depois rode também `roteamento/antigos.json` (os 240 pedidos das medições anteriores), que serve de conferência de regressão.

**Tarefas completas.** O acionamento é metade do caminho; o resultado de oito rodadas de avaliação das respostas em Haiku e Sonnet, o que foi corrigido nas skills e o que ainda aparece estão em `avaliacao-gatilho/TAREFAS-COMPLETAS.md`. O `ferramenta/ponta_a_ponta.py` roda uma tarefa real por skill (`roteamento/tarefas-completas.json`) com as skills instaladas como cópias de verdade e guarda a resposta e os arquivos gerados, para alguém dar a nota contra a documentação. Opções do `rotear.py` além das mostradas acima: `--plugin` mede pelo caminho de instalação como plugin e `--contexto "texto"` simula as instruções do projeto.

**Para revisar os pedidos:** abra `avaliacao-gatilho/REVISAO-ROTEAMENTO.md` (gerado por `ferramenta/revisao_roteamento.py`). Os 168 pedidos vêm numerados, começando pelos que pedem decisão sua, e a resposta é pelo chat, com o número do pedido. `AUDITORIA.md` traz o que uma auditoria independente achou nos conjuntos antigos.

**claude.ai:** não há como medir por script. O roteiro de teste manual está em `avaliacao-gatilho/TESTE-NO-CLAUDE-AI.md`.

**Medição anterior (18/11).** `otimizacao/`, `validacao/` e `independentes/` são os conjuntos da primeira otimização, medidos por skill com `ferramenta/medir.py` (cópias corrigidas dos scripts do skill-creator em `ferramenta/scripts/`); `REVISAO.md` mostra aqueles resultados. Esse medidor testa uma skill por vez com uma cópia temporária e, em paralelo, deixa várias cópias da mesma descrição visíveis, o que pode aumentar o acionamento; por isso o `rotear.py` é o medidor de referência.

## Limites

- As skills só afirmam o que a documentação diz. Imagens e vídeos da Central de Ajuda não foram transcritos, e preços e planos não são citados.
- O arquivo de fluxo que a `cmv-flowbuilder` gera segue o formato observado em um fluxo exportado, não um formato publicado pela plataforma: teste o fluxo importado antes de ligá-lo a uma conexão que atende clientes. Em 22/11/2026 um arquivo gerado pelo `gerar_fluxo.py` (Início, Conteúdo, Horário de Expediente, Menu, Msg Interna, Setor e Encerrar; 17 blocos) foi importado no painel: o editor abriu os 17 blocos e as 17 ligações, o **Verificar** mostrou tudo conectado, o **Resumo do fluxo** bateu com a contagem do validador e a saída **Dentro do Horário** apareceu ligada ao caminho de dentro do expediente. No mesmo dia esse fluxo rodou numa conversa de verdade, ligado a um Setor de teste e a uma Conexão do WhatsApp por QR Code: saudação, Horário de Expediente pelas duas saídas (fechado no dia: Fora do Horário e passagem ao Setor; aberto: menu), Menu em lista, resposta inválida (aviso e menu de novo), escolha de uma opção, Msg Interna, passagem ao Setor e silêncio do robô na mensagem seguinte. Os blocos Setor importados com marcador abriram com o campo **Setor** vazio e foram preenchidos à mão. Numa segunda rodada, a saída **Sem resposta** do Menu (2 minutos) levou ao bloco Encerrar e a mensagem dele chegou cerca de 3 minutos depois do menu; a mensagem enviada 9 minutos depois do Encerrar, sem **SAIR** antes, não recomeçou o fluxo; depois do **SAIR**, recomeçou. Em 23/11/2026 o bloco **Enviar e-mail** entrou no gerador: o formato foi visto no editor (não num arquivo exportado), e um arquivo gerado com ele foi importado e abriu com as duas saídas ligadas e o **Enviar por** vazio; esse bloco não rodou numa conversa. Não foram testados: as outras duas opções do menu e os blocos fora dessa lista.
- As receitas de CSS foram conferidas contra o catálogo de seletores. Em 22/11/2026, 14 das 20 foram aplicadas num painel real sem salvar (regra injetada só na aba de teste, JS rodado só nela) e fizeram o efeito esperado: cor da marca no tema escuro (1), barra do topo (3), esconder e ordenar o menu (4 e 5), balões da conversa (6), cartão da lista (7), campo de digitação (9), janela comum e de confirmação (11), regra só na página de Contatos (12), Kanban e Quadro com a cor da etapa (14), os três trechos de JS (16, 17 e 18, estes dois com clique e evento simulados) e a Dashboard nova, com e sem Modo TV, e a legada (20). Os nomes usados nas receitas 8 e 13 existem na tela (barra de ações com `data-action`, cartão com `data-status` e `data-group`), mas a regra não foi aplicada. No mesmo dia, uma regra sem efeito visual foi salva no campo **CSS desta empresa**: depois de recarregar a página à mão ela estava em `<style id="custom-css-company">`, no `<head>`, depois do `custom-css-frontend`, e valia na página; apagada do campo, o elemento sumiu. Ainda em 22/11/2026, uma linha sem efeito visual foi salva no **JS desta empresa**: rodou uma vez depois de recarregar, em `<script id="custom-js-company">` no fim do `<body>`, e não rodou de novo ao trocar de tela; apagada do campo, ainda rodou no primeiro recarregamento e só sumiu no segundo. Na tela de login pública, aberta sem sessão, existiam o `#custom-css-login` e todas as classes da receita 10 (o link `cadastro` não aparecia nessa instalação), e uma regra sem efeito visual salva no **CSS pré-login** chegou a ela em `<style id="custom-css-frontend">`. Não foram testados: o visual da receita 10 aplicado, o JS pré-login e o pós-login, o CSS pós-login, as telas de cadastro e de recuperar a senha, o prefixo dos erros de JS no console, os fundos do tema escuro (2), o Chat Externo (19), o botão de modelo da receita 15 (não apareceu no atendimento aberto), o modo de nota interna do campo de digitação, o bloco de aniversariantes da Dashboard legada (não apareceu) e o evento `sip:state` emitido pela plataforma.
- O e-mail do Mail Marketing é redigido pela `cmv-mensagens` só quando vai por esse módulo; e-mail avulso (Gmail, Outlook, outra ferramenta) fica fora. A Central de Ajuda não informa tamanho máximo de assunto e de texto, em quais campos a variável funciona nem regras de consentimento: a skill manda conferir com **Enviar teste**.
- Na `cmv-agente-ia`, a Central de Ajuda não mostra a forma dos blocos de agenda e de oportunidade do GPT Assistant. A skill manda inseri-los pela janela **COMANDOS DA IA** e traz só a forma observada num painel em 21/11/2026, que não é oficial e pode mudar com a versão. O conferidor de prompt nunca acusa erro nesses blocos: avisa, e diz quando o bloco difere da forma observada. Foi testado com as duas seções reais inseridas pela janela (uma de agenda, uma de oportunidade), de uma conta só. Em 22/11/2026 a prévia da janela mostrou as variações (oportunidade sem produto, funil, etapa e Setor; agenda com e sem o cancelamento), e o conferidor as reconheceu sem erro. Em 22/11/2026 o comando de agenda rodou numa conversa de verdade: a IA marcou o compromisso (nota interna na conversa, e o cliente sem mensagem de confirmação depois do "sim") e, ao pedido do mesmo horário na mesma conversa, respondeu que estava ocupado e ofereceu o seguinte. Numa conversa nova, pedindo o mesmo horário já ocupado, a IA confirmou sem saber, o sistema recusou depois do "sim" (nota interna de aviso à equipe, nada marcado) e o cliente ficou sem mensagem (confirmado no WhatsApp de quem testou). Foi uma conversa de cada caso, com um prompt só de agenda. Em 23/11/2026 o cancelamento foi testado: a IA respondeu ao cliente que tinha cancelado, mas a tarefa continuou pendente e o evento continuou no Google Calendar (sem nota interna); a causa não foi determinada. No mesmo teste, a IA recusou duas vezes um horário ocupado por evento criado direto no Google Calendar sem tentar marcar, de modo que a recusa do sistema nesse caso segue sem teste.
- A reserva de mesa do PDV e o módulo Reservas têm APIs diferentes; a `cmv-api` separa os dois e pergunta quando o pedido não deixa claro, mas a documentação não traz o formato da resposta nem o código de erro de horário ocupado da reserva de mesa.

## Licença

Proprietária, do Chat Master Veloz: quem recebe pode usar, mas não redistribuir nem distribuir versões modificadas sem autorização. O texto está no arquivo `LICENSE` e vai dentro de cada pacote de `dist/` como `LICENSE.txt`.
