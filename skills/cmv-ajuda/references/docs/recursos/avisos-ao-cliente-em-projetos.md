# Avisos ao Cliente em Projetos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/avisos-ao-cliente-em-projetos
- **Categoria:** Recursos
- **Menu:** Projetos › Avisos ao Cliente em Projetos

---

🧩 Seu cliente pergunta toda semana em que pé está o projeto dele? Com os **avisos ao cliente**, a plataforma envia uma mensagem ao cliente do projeto quando o projeto entra numa situação, como **Em andamento** ou **Concluído**, sem ninguém da equipe precisar lembrar de escrever.

A gestão escolhe as situações que avisam e escreve a mensagem de cada uma, com o nome do cliente, o do projeto, o da situação, o do responsável e o prazo trocados sozinhos. A configuração dos avisos ao cliente é uma só para a empresa e vale para todos os projetos.

Ideal para:

☑️ **Cliente informado:** Avisa o começo e a entrega do trabalho no momento em que o projeto muda de situação.

☑️ **Menos cobrança:** Responde ao "como está o meu projeto?" antes de o cliente perguntar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Projetos**.
>
> ➡️ Clique em **Avisos ao cliente**.
>
> ➡️ Ligue as situações que devem avisar e escreva a **Mensagem** de cada uma.
>
> ➡️ Clique em **Salvar**.

## Como configurar os avisos ao cliente

Acesse o menu **Projetos  ›  Avisos ao cliente**

A janela abre com o título *Avisos ao cliente por situação*, e cada linha dela é uma situação dos projetos.

🔘 **Enviar pela conexão:** a Conexão por onde o aviso é enviado. Só as conexões ativas aparecem na lista. Vazio, o aviso segue pela conversa do cliente: a que está aberta, a última, ou a Conexão padrão.

🔘 **Avisar quando entrar em "…":** a opção de cada situação, como *Avisar quando entrar em "Em andamento"*. Ligada, a situação ganha o campo **Mensagem** e, na empresa com conexão oficial, a opção **Usar um modelo aprovado da API oficial**.

🔘 **Mensagem:** o texto que o cliente recebe quando o projeto entra naquela situação, com até 2.000 caracteres. O campo vem com um texto sugerido, que pode ser trocado: `{{ms}}, {{cliente}}! Seu projeto {{projeto}} agora está na situação {{situacao}}.`

🔘 **Usar um modelo aprovado da API oficial:** troca o texto por um modelo já aprovado. Na conexão oficial, fora da janela de 24 horas, a mensagem só é enviada por modelo aprovado; na conexão por QR Code, vale o texto da **Mensagem**.

Clique em **Salvar**. A tela confirma *"Avisos salvos."*

⚠️ Com uma situação ligada e a **Mensagem** dela em branco, o **Salvar** fica desativado.

## As variáveis da mensagem do aviso

A **Mensagem** do aviso troca as variáveis pelos dados do projeto na hora do envio. A própria janela lista essas variáveis na linha **Variáveis do projeto**, logo abaixo de **Enviar pela conexão**. Cada variável vai entre chaves duplas:

➡️ `{{projeto}}`: o nome do projeto.

➡️ `{{situacao}}`: o nome da situação em que o projeto entrou, como *Em andamento*.

➡️ `{{cliente}}`: o nome do cliente do projeto.

➡️ `{{responsavel}}`: o nome do responsável pelo projeto.

➡️ `{{prazo}}`: o prazo do projeto, como *30/11/2026*.

Valem também as variáveis da conversa, como `{{ms}}`, que vira a saudação do horário (*Bom dia*, *Boa tarde*…), e `{{firstName}}`, o primeiro nome do contato. Um exemplo de mensagem:

```
{{ms}}, {{firstName}}! O projeto {{projeto}} entrou em {{situacao}}, com prazo {{prazo}}.
```

O cliente recebe algo como *"Bom dia, Ana! O projeto Reforma do Escritório entrou em Em andamento, com prazo 30/11/2026."*

## Quando o aviso ao cliente é enviado

➡️ Quando o projeto entra numa situação com o aviso ligado — por exemplo, ao arrastar o card do projeto para a coluna da situação, no quadro por situação.

➡️ Mover o projeto para a situação em que ele já está não envia o aviso de novo.

➡️ Situação sem o aviso ligado não envia nada.

➡️ Se o projeto passa para outra situação e depois volta, o cliente recebe o aviso outra vez.

➡️ O aviso chega na conversa do cliente e não mexe no atendimento: o que estava em **Aguardando** continua em **Aguardando**.

➡️ Cliente sem telefone cadastrado não recebe o aviso, e nenhum atendimento novo é aberto: a conversa dele ganha uma nota interna dizendo que o aviso daquela situação não foi enviado e pedindo o cadastro do telefone do contato.

## Quem configura os avisos ao cliente

Os avisos ao cliente são da gestão: administrador e supervisor veem o botão **Avisos ao cliente** e salvam a configuração. O atendente não tem o botão.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Movi o projeto para a mesma situação. O cliente recebe o aviso de novo?** Não. O aviso só é enviado quando o projeto entra na situação. Se o projeto passa para outra situação e depois volta, o cliente recebe o aviso outra vez.
>
> **Por onde o aviso ao cliente do projeto é enviado?** Pela Conexão escolhida em **Enviar pela conexão**. Com o campo vazio, pela conversa do cliente: a que está aberta, a última, ou a Conexão padrão.
>
> **O cliente do projeto não tem telefone cadastrado. O aviso ao cliente é enviado?** Não, porque o aviso não tem por onde chegar. A plataforma não abre atendimento novo: a conversa do cliente ganha uma nota interna dizendo que o aviso não foi enviado. Cadastre o telefone do contato para ele receber os próximos avisos.
>
> **O Salvar dos Avisos ao cliente não libera. Por quê?** Alguma situação está ligada com a **Mensagem** em branco. Escreva o texto ou desligue a situação.
>
> **Posso usar o nome do cliente na mensagem do aviso do projeto?** Sim. `{{cliente}}` traz o nome do cliente do projeto, e `{{firstName}}`, o primeiro nome do contato.
>
> **O atendente não encontra o botão Avisos ao cliente nos Projetos.** É da gestão: só administrador e supervisor configuram os avisos ao cliente.
