# Mustaches

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mustaches
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Mustaches

---

🧩 **Os Mustaches** (apelido na área de programação para as chaves duplas `{{ }}`) são as **variáveis dinâmicas do sistema**. Eles funcionam como "espaços reservados" dentro de um texto. Em vez de escrever uma mensagem engessada, você insere um código e o sistema o substitui automaticamente por uma informação real e personalizada no momento do envio.

☑️ **Personalização:** Chame o cliente pelo nome em todas as mensagens automáticas, gerando proximidade.

☑️ **Escalabilidade:** Escreva uma única mensagem de saudação que serve para milhares de clientes diferentes.

☑️ **Profissionalismo:** Gere números de protocolo e informe horários exatos sem precisar digitar nada manualmente.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Digite sempre duas chaves abertas `{{`, seguidas do nome do código exato e de duas chaves fechadas `}}`.
>
> ➡️ O sistema lerá esse código e enviará a informação traduzida para o cliente.

## Como os Mustaches funcionam

De uma forma bem simples, ao utilizar um `{{mustache}}` em algum local que permite texto, o sistema irá substituir por sua variável correspondente.

Por exemplo, ao utilizar **`{{firstName}}`** em suas mensagens, ela será substituída pelo "**primeiro nome real do lead**" cadastrado no sistema.

`{{ms}}`, `{{firstName}}`. Tudo bem? Antes de começar, anote o seu protocolo `{{protocol}}`. Meu nome é `{{user}}`. Como posso ajudar?

**Será substituído por algo do tipo:** Boa tarde, Júlia. Tudo bem? Antes de começar, anote o seu protocolo #161672176 Meu nome é Rodolfo. Como posso ajudar?

Veja abaixo uma lista oficial de **mustaches** para você utilizar em suas mensagens e automações.

#### Mustaches de Conversa (lead, atendente, ticket)

##### - ID do contato

```
{{contact_id}}
```

##### - Nome do contato

```
{{name}}
```

##### - Primeiro nome do contato

```
{{firstName}}
```

##### - Número de telefone do contato

```
{{number}}
```

##### - Nome da fila / setor / departamento

```
{{queue}}
```

##### - Campo extra 1 do setor

```
{{queue_extra1}}
```

##### - Campo extra 2 do setor

```
{{queue_extra2}}
```

##### - Nome do atendente desse ticket

```
{{user}}
```

##### - Campo extra 1 do atendente

```
{{user_extra1}}
```

##### - Campo extra 2 do atendente

```
{{user_extra2}}
```

##### - Número do ticket do contato

```
{{ticket_id}}
```

##### - Número de protocolo atribuído e rastreável

```
{{protocol}}
```

##### - Número de protocolo aleatório

```
{{protocol_random}}
```

##### - Nome da conexão

```
{{connection}}
```

##### - Nome da empresa

```
{{name_company}}
```

#### Mustaches de Texto e Tempo

##### - Saudação (Bom dia, boa tarde, boa noite, boa madrugada)

```
{{ms}}
```

##### - Data e Hora completo

```
{{data_hora}}
```

##### - Data

```
{{date}}
```

##### - Hora

```
{{hour}}
```

##### - Quebra de linha

```
{{breakline}}
```

#### Mustache de Conexão e API (avançado)

##### - Domínio da API (URL do Backend sem https://)

```
{{backendURL}}
```

##### - Token da Conexão

```
{{connection_token}}
```

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso inventar o meu próprio Mustache? (ex: `{{cidade_do_cliente}}`)** Não. O sistema reconhece apenas os comandos oficiais listados acima. Se você digitar um mustache que não existe, o sistema enviará o texto literalmente com as chaves para o cliente.
>
> **O `{{firstName}}` funciona se o cliente não tiver cadastro?** Se o cliente for novo e não tiver nome salvo na sua agenda de Contatos, o sistema tentará usar o nome público que o próprio cliente configurou no perfil do WhatsApp dele.
>
> **Onde preencho o Campo extra 1 do atendente e o Campo extra 1 do setor?** Na aba **Geral** de cada cadastro: o do atendente no menu **Equipe  ›  editar o usuário**, e o do setor no menu **Setores & Chatbot**, editando o Setor. Cada cadastro tem dois campos extras, e as variáveis `{{user_extra1}}`, `{{user_extra2}}`, `{{queue_extra1}}` e `{{queue_extra2}}` trazem o que estiver preenchido neles.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Errar letras maiúsculas e minúsculas (Case Sensitive):** O usuário digita `{{firstname}}` (tudo minúsculo). O sistema não vai reconhecer o código, pois o correto é `{{firstName}}` (com o "N" maiúsculo). Copie e cole da lista acima para não errar.
>
> **Colocar espaços dentro das chaves:** Digitar `{{ ms }}` ou `{ {name} }`. Qualquer espaço extra quebra a leitura da variável pelo robô. O texto deve estar colado nas chaves.
>
> **Esquecer as chaves:** Digitar apenas a palavra protocol no meio do texto. O cliente vai receber literalmente a palavra "protocol" em vez do número do ticket. Sempre envolva a palavra com `{{` e `}}`.
