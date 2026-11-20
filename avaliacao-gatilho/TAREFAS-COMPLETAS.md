# Avaliação de tarefas completas (19 a 24/11/2026)

O roteamento mede se a skill certa é carregada. Esta avaliação mede o passo seguinte: se a resposta entregue está correta. Cada tarefa rodou no Haiku 5.5 e no Sonnet 5.5, com as seis skills instaladas como cópias reais (`ferramenta/ponta_a_ponta.py`). Um agente avaliador independente conferiu cada resposta contra os artigos de `references/docs/`, rodou os validadores das skills nos arquivos e no código entregue e separou defeito da skill de defeito do modelo.

## Resultado das cinco rodadas

| Rodada | Pedidos | Aprovadas | Com ressalvas | Reprovadas |
|---|---|---|---|---|
| 1 | `roteamento/tarefas-completas.json`, skills de antes | 8 | 4 | 0 |
| 2 | os mesmos pedidos, depois das correções | 7 | 5 | 0 |
| 3 | `roteamento/tarefas-completas-2.json` (pedidos novos), depois de mais ajustes | 7 | 5 | 0 |
| 4 | 24 respostas: os pedidos da rodada 3 de novo e `roteamento/tarefas-completas-3.json` (tipos novos) | 10 | 14 | 0 |
| 5 | 13 respostas, só as tarefas das skills corrigidas depois da rodada 4 | 6 | 6 | 1 |

Em todas as rodadas a skill certa foi carregada nas 12 execuções, todos os validadores passaram (fluxo, seletores de CSS, prompt) e nenhuma resposta violou os limites de segurança (token só em variável de ambiente, nenhum segredo em JS, nenhum preço).

A contagem quase não mudou, mas o tipo de ressalva mudou. Na rodada 1 havia erros de conteúdo: oferta de pôr horário dentro do arquivo de fluxo, pré-requisito do Horário de Expediente omitido, "responda SAIR" no descadastramento, CSS que mudava mais do que o pedido, caminho de arquivo interno no lugar do comando de teste. Esses sumiram. As ressalvas das rodadas 2 e 3 são menores e quase todas do Haiku. É uma execução por célula, então diferenças pequenas entre rodadas podem ser acaso.

A rodada 4 cobriu tipos de tarefa que ainda não tinham sido avaliados: dúvida de permissão por setor, webhook para o n8n, depuração de um fluxo exportado com defeito plantado (`roteamento/arquivos/fluxo-com-saida-solta.json`), prompt de IA criado do zero, respostas rápidas e aviso por JavaScript. Os dois modelos acharam o defeito plantado e a causa certa. Das 14 ressalvas, a maioria é leve; as que tinham efeito para o usuário e apareceram nos dois modelos viraram correção nas skills (lista abaixo). Depois dessas correções houve só uma conferência por script em quatro tarefas, sem nova avaliação por leitura.

A rodada 5 confirmou as correções da rodada 4 (etapa de perguntas da IA, maiúsculas nas respostas rápidas, depuração sem reimportar) e não viu piora causada por elas. A reprovada foi o Haiku no pedido de encerrar ticket por API: ele não carregou a skill, tratou a pasta das skills como arquivos do projeto e deixou um marcador de token escrito no código. O texto de contexto do README foi refeito por causa disso; com ele, a skill foi carregada nas 3 execuções desse pedido.

Depois da sincronização com a documentação de 20/11/2026, as 12 tarefas dos conjuntos 2 e 3 rodaram de novo em Haiku e Sonnet, com o texto de contexto novo, e foram conferidas só por script: skill certa carregada em 24 de 24, validador de fluxo e conferidor de seletores sem erro. Não houve avaliação por leitura depois da sincronização.

## O que foi corrigido nas skills

Nenhuma descrição (o texto que decide o acionamento) foi tocada.

- **cmv-flowbuilder:** o gerador imprime o bloco "CONFIGURAR NA EMPRESA" quando o fluxo tem Horário de Expediente (o horário não vai no arquivo; a aba Horários depende do Gerenciamento Por Setor; ligar isso vale para todos os Setores). Menu com aviso de fora do horário passou a ser entrega direta, sem rodada de confirmação. O arquivo é gravado na pasta de trabalho, a resposta começa pela linha do arquivo e a fonte vai com título e link.
- **cmv-mensagens:** a regra "PARAR, não SAIR" subiu para as armadilhas, a ficha de campanha e o exemplo; as fichas trazem o link de cada artigo; a tabela ficou opcional para campanha com variações longas; aviso de que a linha "Menu" do artigo é o caminho na Central de Ajuda, não no painel.
- **cmv-api:** o comando do teste de status é entregue pronto; as opções de tempo limite e de status vão em todo cURL; todo ID de exemplo vem com a chamada que o obtém; a pergunta sobre a conexão inclui Oficial direta ou pelo Hub; o mapa ganhou o caminho do telefone do contato até o `ticketId`.
- **cmv-ajuda:** os comandos de leitura trazem a linha com o link; o artigo de suporte é citado com o link por extenso; antes de dizer "não está documentado", abrir todos os artigos que o mapa aponta.
- **cmv-painel-css-js:** a receita de cores separa o núcleo do pedido do que é opcional; a receita da barra manda dizer que o catálogo não informa o tema; não escrever o caminho de menu da Cor Principal.
- **cmv-agente-ia:** no plano de testes, a entrega são as mensagens do cliente escritas uma a uma, não a tabela de cenários.
- **Em todas:** caminho de arquivo da skill não vai na resposta; vai o título do artigo e o link.

Depois da rodada 4:

- **cmv-agente-ia:** "cria o prompt" só com o ramo e o objetivo volta a ser a etapa de perguntas (os dois modelos pulavam direto para um rascunho de mais de 120 linhas cheio de marcadores); a resposta não abre com relato de processo; o plano de testes fecha com as fontes.
- **cmv-api:** como um sistema acha o `ticketId` sem ninguém olhar a tela (o `chamadoId` do webhook ou a API Listar Tickets do Contato) subiu do mapa para o `SKILL.md`; receber webhook não pede API Externa.
- **cmv-mensagens:** em resposta rápida, o que muda a cada cliente vai em MAIÚSCULAS para o atendente trocar ao enviar, não entre colchetes; "opção de saída no texto do template" passou a ser dita como recomendação da skill, não como frase de artigo.
- **cmv-flowbuilder:** a depuração de um fluxo exportado ganhou ordem fixa: rodar o validador, apontar o bloco pelo nome, corrigir no fluxo que já está no painel (não reimportar) e fechar com a fonte.
- **cmv-painel-css-js:** o arquivo de conferência é temporário e não é citado; a fonte é citada pelo título da parte do catálogo, não pelo nome do arquivo.

## O que ainda aparece

- **Dedução dita como fato.** Apareceu nas três rodadas, nos dois modelos (por exemplo "encerrar por API é o mesmo que clicar em Resolver"). As skills têm a regra; os modelos menores nem sempre a seguem.
- **Haiku pula itens do molde.** No FlowBuilder, deixou de dizer como o fluxo entra no ar e pulou o **Resumo do fluxo** numa das execuções; em mensagens, contrariou a ficha sobre onde aparece o motivo de um template reprovado.
- **Sonnet lê pouco.** Em ajuda, concluiu que a Central não explicava uma terceira causa depois de abrir um artigo só.
- **Respostas longas** no plano de testes da IA (mais de 100 linhas), porque o roteiro é a entrega.
- **Haiku sem a linha de contexto.** Nestas tarefas as skills são instaladas como cópias, sem o gancho do plugin. No pedido de encerrar ticket, que não cita o produto, o Haiku respondeu duas vezes sem carregar a skill: o código saiu certo, mas sem fonte, sem o teste de status e sem os pré-requisitos. É o mesmo ponto fraco medido no roteamento, e a linha de contexto do README é a correção.

## O que só um teste na plataforma responde

- Se os arquivos `.json` gerados importam e se as saídas do bloco Horário de Expediente são mesmo "dentro" e "fora" na ordem que a skill presume (a skill avisa que o formato é observado, não oficial).
- A ordem certa entre preencher a aba Horários de cada Setor e ligar o Gerenciamento Por Setor: os artigos se contradizem.
- Como a opção **Abrir Tickets Fora do Expediente?** convive com um fluxo ligado a um Setor fechado: a documentação não diz.
- O efeito visual do CSS no painel e se as chamadas de API são aceitas como estão.

## Como repetir

```bash
cd avaliacao-gatilho/ferramenta
python3 ponta_a_ponta.py --modelo claude-haiku-5-5 --tarefas ../roteamento/tarefas-completas-2.json --saida /tmp/tarefas
```

Cada pasta de saída traz `resposta.md`, `resumo.json` (pedido, ferramentas usadas, arquivos criados) e os arquivos gerados. A nota é dada por leitura contra os artigos; os validadores das skills (`validar_fluxo.py`, `conferir_seletores.py`, `conferir_prompt.py`) conferem a parte mecânica.
