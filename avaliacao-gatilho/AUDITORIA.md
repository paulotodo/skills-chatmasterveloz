# Auditoria independente dos pedidos de teste

Os 180 pedidos de `otimizacao/` e `validacao/` foram escritos por quem otimizou as descrições. Um agente que não participou leu os 12 arquivos, as seis `SKILL.md` e a documentação, sem ver os resultados, e procurou rótulos errados, rótulos discutíveis, pedidos irreais, lacunas e repetições entre os dois conjuntos. Os números (#) são a posição do pedido no arquivo.

## Contagem

| Categoria | Quantos de 180 |
|---|---|
| Rótulo errado | 0 |
| Rótulo discutível | 10 (7 fortes, 3 leves) |
| Pedido irreal | 5 |

## Rótulos discutíveis (duas skills seriam defensáveis)

| Arquivo | Pedido | Por que é discutível |
|---|---|---|
| `validacao/cmv-flowbuilder` #1 | "o robô do chat master veloz fica repetindo o menu toda hora…" | Forte. Pode ser o menu de Setores da conexão (opção Repetições do Bot), que é da `cmv-ajuda`. |
| `validacao/cmv-flowbuilder` #3 | "…cliente que mandar mensagem de madrugada receba aviso de fora do horário e caia num menu de manhã" | Forte. O aviso de fora do horário é configuração do Setor (`cmv-ajuda`) e o texto é da `cmv-mensagens`. |
| `otimizacao/cmv-flowbuilder` #3 | "quero mandar uma mensagem automática 1 dia depois pra quem pediu orçamento e sumiu…" | Forte. Também cabe em Agendamento (`cmv-mensagens`); nada no pedido fala de fluxo. |
| `otimizacao/cmv-api` #4 | "onde pego o token pra usar a API…? e qual a diferença entre token da empresa e token da conexão?" | Forte. A `cmv-api` e a `cmv-ajuda` reivindicam por escrito. |
| `otimizacao/cmv-mensagens` #6 e `validacao/cmv-mensagens` #6 | "qual variável eu uso pra colocar o primeiro nome…" (aciona) e "como envio a resposta rápida pelo atalho…" (não aciona) | Forte. Duas dúvidas de uso sem redação, com rótulos opostos. |
| `otimizacao/cmv-painel-css-js` #10 | "personalizar o visual do chat externo…" | Forte. O Chat Externo tem seção Aparência nativa; o caso análogo do Web Chat foi rotulado como `cmv-ajuda`. |
| `otimizacao/cmv-ajuda` #5 | "o que mudou no sistema essa semana? apareceu um menu novo 'Assistente de IA'…" | Leve. Carrega também um sinal da `cmv-agente-ia`. |
| `otimizacao/cmv-flowbuilder` #6 | "…quem comentar 'eu quero' no meu post do instagram receba o link no direct" | Leve. Existe o artigo "Automação Eu Quero" na ajuda. |
| `otimizacao/cmv-mensagens` #16 | "cria um template de mensagem no gerenciador do WhatsApp da Meta…, eu uso a Zenvia" | Leve. A descrição da `cmv-mensagens` não exclui outras plataformas. |

## Pedidos irreais

- `otimizacao/cmv-flowbuilder` #2 e #8 e `validacao/cmv-flowbuilder` #2: prometem um arquivo ("segue o json", "olha esse json") que não acompanha o pedido. O modelo pode só pedir o arquivo, e isso mede outra coisa que não a descrição.
- `otimizacao/cmv-ajuda` #15: o final "usando css personalizado" deixa o negativo óbvio.
- `otimizacao/cmv-api` #17: "sem plataforma no meio" é frase de quem escreve o rótulo.

## Padrões que atravessam os arquivos

- **Nome do produto sempre presente.** 88 dos 90 positivos citam "chat master veloz", CMV ou chatmasterveloz. Nada testa a promessa "mesmo sem o nome do produto" da `cmv-ajuda` e da `cmv-mensagens`.
- **Negativos fáceis.** Os negativos usam a palavra exata da skill irmã ("monta um fluxo no flowbuilder…" aparece 8 vezes). Palavras ambíguas como "robô" e "menu automático" nunca aparecem como negativo.
- **Repetição entre otimização e validação.** Os negativos de validação repetem os moldes dos de otimização em todas as skills. Os positivos de validação são novos em ajuda, api, agente-ia e flowbuilder, e parcialmente repetidos em painel-css-js (3 de 5) e mensagens (2 de 5).

## Lacunas de cobertura (as mais importantes por skill)

- **cmv-ajuda:** pedido sem o nome do produto; "onde fica" de recurso cuja produção é de uma irmã (onde colar o prompt, onde cadastrar o token); PDV, Instagram, Web Chat, Ligações e E-mails.
- **cmv-api:** agendar mensagem, botões, criar ou encerrar ticket por código; canais que não são WhatsApp; pedido totalmente leigo.
- **cmv-flowbuilder:** fluxo salvo que não dispara e boas-vindas em dobro; escolha de gatilho; pedido misto "fluxo com menu e IA no final".
- **cmv-agente-ia:** onde colar a chave da OpenAI; Análise de Atendimento e menu Assistente de IA; como testar o prompt antes de ligar.
- **cmv-mensagens:** pedido sem citar o CMV nem o tipo de mensagem; ausência, encerramento e pesquisa de satisfação; janela de 24h.
- **cmv-painel-css-js:** token ou chamada de API dentro do JS do painel; trocar textos e estilizar janelas; "onde mudo a cor principal do sistema?" como negativo.

O conjunto `independentes/` (60 pedidos escritos por outro agente, que não viu estes pedidos nem as descrições) cobre parte dessas lacunas: tem pedidos sem o nome do produto, com abreviações e com contexto de negócio.
