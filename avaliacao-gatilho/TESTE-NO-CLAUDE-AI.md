# Teste manual no claude.ai

O acionamento das skills foi medido por script no Claude Code. No claude.ai (site e aplicativo) não existe forma documentada de medir por script, então este teste é feito à mão. Leva uns 20 minutos.

## O que a documentação oficial garante e o que não garante

Conferido em 19/11/2026 na Central de Ajuda (`support.claude.com`, artigo "What are skills?") e na documentação de Agent Skills (`platform.claude.com`).

| Ponto | O que está documentado | Situação das seis skills |
|---|---|---|
| Arquivo de envio | "Upload a ZIP file containing your skill folder". O formato `.skill` não é citado. | `dist/<skill>.zip`, gerado por `python3 montar.py --zip` |
| Pasta dentro do zip | O nome da pasta precisa ser igual ao `name` da skill | Conferido nos seis pacotes |
| `name` | Até 64 caracteres, minúsculas, números e hífens; sem "anthropic" nem "claude" | Conferido |
| `description` | Até 1.024 caracteres, sem tags XML | A maior tem 1.009 caracteres (1.024 bytes) |
| Tamanho | 30 MB descompactados (regra da API; o claude.ai não publica limite próprio) | O maior pacote tem 2,7 MB descompactado |
| Quantidade de arquivos | Não documentado. Visto nos envios de 21/11/2026: "Zip contains too many files (maximum 200)" e, com os artigos num zip interno, "Zip cannot contain nested zip files" | `cmv-ajuda` (519 artigos) e `cmv-api` (380) passam do limite: o `montar.py` põe os artigos delas num arquivo de texto só, `references/docs.json`, e o `SKILL.md` do pacote ganha a nota que manda extraí-los. Os pacotes ficam com 4 e 5 arquivos |
| Pré-requisito | Execução de código ligada | Ver passo 1 |
| Critério de acionamento | A `description` é comparada com o pedido, como no Claude Code | Não há garantia de comportamento idêntico |

Não documentado, e por isso só o teste responde: o que o claude.ai faz com uma descrição perto do limite, e se o acionamento é igual ao do Claude Code. No Claude Code, com os dois pacotes instalados como o claude.ai os recebe, Haiku e Sonnet abriram os artigos e responderam com a fonte certa (uma execução por modelo e por skill, repetida em 22/11 com o `docs.json`; os artigos extraídos saíram idênticos aos originais).

Visto em 22/11/2026, nos 14 pedidos (uma conversa nova por pedido, Fable 5.2, esforço Médio, sem projeto, enviados pelo navegador): 14 de 14 com a skill esperada, nenhuma nos pedidos 13 e 14. Nos pedidos 1 a 4 o claude.ai extraiu os artigos do `docs.json` e citou a fonte; no 5 rodou o `validar_fluxo.py` e no 11 o `conferir_seletores.py`. Ressalvas: a memória do claude.ai da conta estava ligada e pode ter ajudado nos pedidos que não citam o CMV; os pedidos 10 a 13 foram digitados sem os acentos por falha da automação.

Também em 22/11/2026, conjunto reduzido de seis pedidos (1, 2, 3, 5, 11 e 13) com os outros modelos, texto com os acentos certos:

| Modelo | Skill esperada | Observações |
|---|---|---|
| Haiku 5.5 | 6 de 6 | Extraiu os artigos e citou a fonte nos pedidos 1, 2 e 3. No 5, validador rodou (estrutura sem erros, 5 valores a trocar), mas a resposta citou o caminho interno do arquivo. No 11, pintou só a barra do topo e os botões dela, sem tratar os botões principais |
| Sonnet 5.5 | 6 de 6 | Citou a fonte nos pedidos 1, 2 e 3 (no 3, com o título do artigo alterado). No 5, gerou o arquivo e leu uma memória da conta antes; não foi aberto o passo do validador. No 11, tratou barra e botões como a skill ensina |

A memória do claude.ai interferiu: uma resposta do Sonnet citou a "revenda", dado fictício de outro pedido de teste. Para repetir o teste sem esse efeito, desligar a memória ou usar conversa temporária.

## Passo 1: instalar

1. Em **Settings › Capabilities**, ligue **Code execution and file creation**. Em planos Team e Enterprise, quem liga é o dono da organização.
2. Em **Customize › Skills**, clique em **+**, depois **Create skill** e **Upload a skill**.
3. Envie os seis arquivos de `dist/`, um por vez: `cmv-ajuda.zip`, `cmv-api.zip`, `cmv-flowbuilder.zip`, `cmv-agente-ia.zip`, `cmv-mensagens.zip`, `cmv-painel-css-js.zip`.
4. Anote na tabela abaixo se algum envio foi recusado e a mensagem exata.
5. Nas instruções do projeto (ou nas preferências do perfil), cole o texto de contexto que está no README, na seção "Diga ao Claude que você usa o Chat Master Veloz". No Claude Code ele levou o Haiku de 81 para 83 acertos em 84 e fez a skill de API ser carregada num pedido que não cita o produto. Se quiser medir o efeito no claude.ai, faça os pedidos pares do passo 2 uma vez sem o texto e uma vez com ele.

| Pacote | Aceito? | Mensagem, se recusado |
|---|---|---|
| cmv-ajuda.zip | Recusado duas vezes em 21/11 (522 arquivos; depois, zip interno). Aceito em 22/11 com os artigos em `docs.json` | "Zip contains too many files (maximum 200)"; "Zip cannot contain nested zip files" |
| cmv-api.zip | Recusado duas vezes em 21/11 (384 arquivos; depois, zip interno). Aceito em 22/11 com os artigos em `docs.json` | "Zip contains too many files (maximum 200)"; "Zip cannot contain nested zip files" |
| cmv-flowbuilder.zip | Aceito em 21/11 | |
| cmv-agente-ia.zip | Aceito em 21/11 | |
| cmv-mensagens.zip | Aceito em 21/11 | |
| cmv-painel-css-js.zip | Aceito em 21/11 | |

## Passo 2: 14 pedidos

Abra uma **conversa nova para cada pedido**, cole o texto e veja qual skill o Claude usou. Abra os passos que a resposta mostra e procure o nome da skill; não conferi como o claude.ai exibe isso hoje, então, se não ficar claro, pergunte no fim da conversa "qual skill você carregou para responder?". Em cada skill há um pedido que cita o produto e um que não cita; o segundo é o caso difícil.

| # | Pedido | Deve usar | Usou |
|---|---|---|---|
| 1 | No Chat Master Veloz, consigo colocar a logo e a cor do meu restaurante no Cardápio Digital? Onde fica essa configuração? | cmv-ajuda | cmv-ajuda (22/11, Fable 5.2; fonte: Cardápio Digital) |
| 2 | desde ontem um monte de conversa ficou com fundo vermelho na lista de atendimentos e cliente reclamando que não recebe resposta. o que é isso e como resolve?? | cmv-ajuda | cmv-ajuda (22/11, Fable 5.2; fontes: Conexão desconectada e mais duas) |
| 3 | Já tenho o template lembrete_consulta aprovado na Meta. Preciso do curl pra enviar ele pelo CMV preenchendo o nome do paciente e o horário nas variáveis. | cmv-api | cmv-api (22/11, Fable 5.2; fonte: API Oficial Mensagem Template) |
| 4 | quando o pedido é marcado como entregue no nosso sistema eu queria encerrar o ticket do cliente sozinho, sem o atendente ter que clicar em Resolver. dá pra fazer isso por requisição? em php de preferência | cmv-api | cmv-api (22/11, Fable 5.2; fontes: API Encerrar Ticket e API Listar Tickets do Contato) |
| 5 | Me gera o arquivo pra importar no Chat Master Veloz: fluxo de uma escola de idiomas com menu Matrícula, Financeiro e Secretaria, e quem escrever fora do horário recebe aviso de que respondemos no próximo dia útil. | cmv-flowbuilder | cmv-flowbuilder (22/11; arquivo gerado, validador rodou: estrutura sem erros, 7 valores a trocar) |
| 6 | importei o fluxo ontem, salvei, ele aparece na lista do FlowBuilder Nativo, mas quando mando mensagem de teste não acontece nada, a conversa cai direto em Aguardando sem resposta. o que falta? | cmv-flowbuilder | cmv-flowbuilder (22/11) |
| 7 | No Chat Master Veloz, o GPT Assistant consegue responder dentro de um grupo de WhatsApp? Queria que ele só falasse quando alguém chamasse por um comando. | cmv-agente-ia | cmv-agente-ia (22/11) |
| 8 | a ia do atendimento tá inventando preço de procedimento que não existe e às vezes responde textão enorme. a tabela de valores tá certinha no prompt lá em Prompts OPEN.AI, temperatura em 1. onde eu mexo? | cmv-agente-ia | cmv-agente-ia (22/11) |
| 9 | Vou fazer minha primeira campanha no CMV pra avisar que a loja mudou de endereço. Escreve as variações do texto e a mensagem de descadastramento? É conexão por QR Code. | cmv-mensagens | cmv-mensagens (22/11) |
| 10 | preciso de uma msg pra mandar pros pais avisando q a rematrícula vence dia 10 e quem não renovar perde a vaga. escola infantil, uns 180 responsáveis, número conectado por qr code | cmv-mensagens | cmv-mensagens (22/11; pedido chegou sem acentos) |
| 11 | O painel do Chat Master Veloz vem todo no verde padrão. Preciso deixar a barra de cima e os botões em azul marinho (#0b1f3a), que é a cor da minha revenda, também no tema escuro. | cmv-painel-css-js | cmv-painel-css-js (22/11; pedido chegou sem acentos; conferidor rodou: 0 problemas, 0 avisos) |
| 12 | quero reordenar o menu lateral: Tickets, Contatos e CRM lá em cima e o resto embaixo. tem como sem pedir pro suporte? | cmv-painel-css-js | cmv-painel-css-js (22/11; pedido chegou sem acentos) |
| 13 | meu fluxo no manychat parou de responder comentário no instagram desde ontem. o gatilho por palavra-chave tá ativo e a conta tá conectada. o que pode ser? | nenhuma | nenhuma (22/11; pedido chegou sem acentos) |
| 14 | preciso de um css pra esconder o rodapé do tema Astra no meu site em wordpress e trocar a cor do botão do formulário de contato pra laranja | nenhuma | nenhuma (22/11) |

## Passo 3: uma tarefa completa

O acionamento é metade do caminho. Peça uma entrega de verdade em duas skills que rodam script e veja se o claude.ai executa:

- **cmv-flowbuilder:** repita o pedido 5 e confira se o arquivo `.json` é gerado e validado pelo script da skill (a resposta deve dizer que a validação passou).
- **cmv-painel-css-js:** repita o pedido 11 e confira se o CSS vem conferido contra o catálogo de seletores.

Se o script não rodar, anote o erro: pode ser acesso à rede ou ambiente de execução diferente do Claude Code.

## Como ler o resultado

- **Envio recusado:** me mande a mensagem exata; o pacote é ajustado.
- **Pedido com o nome do produto que não usou a skill:** problema sério, a descrição precisa ser revista para o claude.ai.
- **Pedido sem o nome do produto que não usou a skill:** é o ponto fraco conhecido nos modelos menores. Anote qual modelo estava selecionado na conversa.
- **Pedidos 13 ou 14 usando alguma skill:** acionamento indevido; anote qual.
