# Descrição compacta: a entrada do `scripts/gerar_fluxo.py`

Para gerar o arquivo .json de um fluxo, não escreva o JSON da plataforma. Escreva uma **descrição compacta**: a lista dos blocos, cada um com um apelido, e a lista das ligações entre apelidos. O gerador cria os IDs, as posições, os campos de topo e as ligações no formato observado, e roda o validador no resultado.

```bash
python3 scripts/gerar_fluxo.py descricao.json fluxo.json           # gera e confere
python3 scripts/gerar_fluxo.py descricao.json fluxo.json --final   # quando os IDs de Setor e tag foram informados
python3 scripts/gerar_fluxo.py --teste                             # autoteste
```

Exemplo completo: `assets/descricao-exemplo.json` (é a descrição que gerou `assets/exemplo-minimo.json`).

O formato da descrição é desta skill, não da plataforma. O formato do arquivo gerado é o **observado em um arquivo exportado** (`references/formato-json.md`), não documentação oficial, e a importação de um arquivo gerado não foi testada por quem escreveu a skill.

## Estrutura

```json
{
  "blocos": [
    {"apelido": "boas_vindas", "tipo": "conteudo", "itens": ["Olá!", 2, "Como posso ajudar?"]},
    {"apelido": "menu", "tipo": "menu", "mensagem": "Escolha um assunto",
     "opcoes": [["Comprar", "Orçamentos e pedidos"], "Suporte"],
     "resposta_invalida": true, "sem_resposta_minutos": 30},
    {"apelido": "comercial", "tipo": "setor", "nome": "Comercial"},
    {"apelido": "fim", "tipo": "encerrar", "mensagem": "Até mais!"}
  ],
  "ligacoes": [
    ["inicio", "boas_vindas"],
    ["boas_vindas", "menu"],
    ["menu", 1, "comercial"],
    ["menu", 2, "comercial"],
    ["menu", "invalida", "boas_vindas"],
    ["menu", "sem_resposta", "fim"]
  ]
}
```

- `apelido`: um nome curto, sem repetição. Serve só para escrever as ligações; não vai para o arquivo. O apelido `inicio` já existe: é o bloco **Início**.
- `ligacoes`: `[origem, destino]` quando a origem tem uma saída só; `[origem, saída, destino]` quando tem mais de uma.

## Tipos de bloco

| `tipo` | Bloco no editor | Campos (os opcionais entre parênteses) | Saídas para usar em `ligacoes` |
|---|---|---|---|
| `conteudo` | Conteúdo | `itens`: lista em ordem de envio; texto é uma mensagem, número inteiro é um intervalo em segundos, de 1 a 120 | uma só |
| `menu` | Menu, no tipo Menu em Lista | `mensagem`, `opcoes` (cada uma um título, ou `[título, descrição]`), (`botao`, padrão "Ver opções"), (`cabecalho`), (`rodape`), (`resposta_invalida`: `true` liga o Caminho alternativo), (`sem_resposta_minutos`) | `1`, `2`… pelo número da opção; `invalida`; `sem_resposta` |
| `pergunta` | Pergunta | `mensagem` | uma só |
| `variavel` | Variável | `nome` (com ou sem os `%`) | uma só |
| `condicao` | Condição | `valor`, (`compara`: `resposta`, que é o padrão, ou `tags`) | `verdadeiro`, `falso` |
| `switch` | Switch (tags) | `regras`: lista de `{"nome": …, "tag_id": …}`, na ordem de prioridade | o `nome` de cada regra; `nenhuma` |
| `tag` | Tag | `nome`, (`id`) | uma só |
| `intervalo` | Intervalo | `segundos`, de 1 a 120 (com mais de 2 minutos o bloco ganha a saída **Janela expirada**, sem formato observado) | uma só |
| `msg_interna` | Msg Interna | `mensagem` | uma só |
| `codigo_js` | Execução de Código JS | `codigo` | uma só |
| `horario` | Horário de Expediente | `nome` do Setor que dá o horário, (`id`). Os dias e horas não vão no arquivo: o bloco lê a aba **Horários** desse Setor | `dentro`, `fora` |
| `setor` | Setor | `nome`, (`id`) | nenhuma |
| `encerrar` | Encerrar | (`mensagem`) | nenhuma |
| `marcador` | lugar reservado para um bloco sem formato observado | `instrucao`: o que pôr ali, como "substituir por Botões com o link …" | uma só |

Qualquer outro `tipo`, campo com nome diferente dos da tabela, apelido repetido ou saída que o bloco não tem: o gerador recusa a descrição, lista os problemas e não grava nada.

## O que o gerador decide por você

- **Menu sempre em Lista.** É o único tipo de menu com formato observado. Opção com até 20 caracteres, descrição até 72. Para **Menu em Texto** ou **Menu em Botões**, a pessoa importa e troca o **Tipo de Menu** no editor; as opções continuam (`references/docs/recursos/bloco-menu.md`).
- **Setor e tag sem `id` viram marcador.** O bloco sai com `sec` 0 e o nome `TROCAR: Setor Comercial` (ou `TROCAR: tag …`), e o validador lista em VALORES A TROCAR. Com `id` (número inteiro da conta), sai o ID e o nome. Regra de `switch` sem `tag_id` também vira valor a trocar.
- **`marcador` vira uma Msg Interna** com o texto `TROCAR NO EDITOR: <instrucao>`. Se alguém esquecer de trocar, é uma nota que só a equipe vê, e a conversa segue. Serve para os blocos que o artigo descreve com uma saída só (Botões, Template, Oportunidade, Contato, Enviar Localização, Link do Chat Externo). Para HTTP Request, Remover Tag, Webview e Carrossel de Produtos, o artigo não diz quantas saídas o bloco tem: o marcador guarda o lugar, mas avise que as saídas serão vistas no editor. Bloco com várias saídas sem formato observado não tem substituto: roteiro de montagem.
- **Condição só em dois modos.** `resposta` grava a combinação observada para **Resposta da Pergunta** com **Igual**; `tags` grava a observada para **Tag** com **Contém** (`valor` é a lista de nomes de tag separados por vírgula). O significado dessas combinações é hipótese, não confirmação (`references/formato-json.md`, seção 7).
- **Saídas com nome de hipótese.** `verdadeiro` e `falso` da Condição e `dentro` e `fora` do Horário de Expediente são gravados como as saídas `a` e `b` do arquivo. Que `a` seja Verdadeiro ou Dentro do Horário não foi confirmado.
- **Posição:** uma coluna por distância do Início. O botão **Organizar automaticamente** do editor rearruma, se a pessoa preferir.

## O que o gerador imprime

1. O relatório do validador: ERROS, AVISOS e VALORES A TROCAR. Código de saída diferente de zero quer dizer que há erro no fluxo (1) ou na descrição (2).
2. A lista **CONFERIR NO EDITOR**: os blocos gravados com valor de significado não confirmado (Condição, Horário de Expediente, Execução de Código JS, Switch) e as Perguntas, que não levam **Sem resposta**. Repasse essa lista à pessoa, em linguagem simples.
3. A lista **CONFIGURAR NA EMPRESA**, só quando o fluxo tem Horário de Expediente: o horário vem da aba **Horários** do Setor, que só aparece com o **Gerenciamento de Expediente** em **Gerenciamento Por Setor**, e ligar isso faz todos os Setores seguirem o horário já preenchido (`references/docs/recursos/bloco-horario-de-expediente.md`, `references/docs/recursos/aba-horarios-em-setores-e-chatbot.md`). Repasse também, e não ofereça arquivo "já com os horários".

## O que não cabe na descrição

Imagem, áudio, vídeo e arquivo no Conteúdo; **Sem resposta** e **Mover de setor por inatividade** na Pergunta; Condição de horário, dia, feriado, conexão, status, protocolo, anúncio e postagem; as outras comparações do Switch (tags); **Setor vinculado ao fluxo** no Horário de Expediente; Intervalo de mais de 2 minutos; e todos os blocos da seção 9 de `references/formato-json.md`. Para isso: `marcador`, instrução de completar no editor, ou roteiro de montagem.
