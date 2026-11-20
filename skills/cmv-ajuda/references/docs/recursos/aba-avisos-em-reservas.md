# Aba Avisos em Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-avisos-em-reservas
- **Categoria:** Recursos
- **Menu:** Reservas › Aba Avisos em Reservas

---

🧩 A aba **Avisos** monta as mensagens automáticas ao cliente: a reserva confirmada, remarcada ou cancelada, os lembretes antes do horário e a vaga da lista de espera. Cada mensagem é enviada sozinha na conversa do cliente quando a reserva muda.

Todos os avisos começam desligados: ligue os que quiser e ajuste o texto.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Reservas** e abra a aba **Avisos**.
>
> ➡️ Escolha a conexão em **Enviar pela conexão**.
>
> ➡️ Ligue os avisos que quiser, ajuste o texto de cada um e clique em **Salvar**.

## Por onde os avisos são enviados

🔘 **Enviar pela conexão:** a **Conexão** por onde as mensagens vão. A opção **A conversa do cliente (ou a conexão padrão)** usa a conversa que o cliente já tem; as outras opções são as conexões da empresa.

O aviso vai para o telefone da reserva. Reserva sem telefone não recebe aviso.

## Os avisos da reserva

🔘 **Reserva confirmada:** enviado quando a reserva já nasce confirmada, pela agenda ou pela página.

🔘 **Pedido recebido:** enviado quando o cliente pede pela página e a equipe ainda vai confirmar.

🔘 **Confirmada pela equipe:** enviado quando a equipe confirma um pedido pendente.

🔘 **Reserva remarcada:** enviado quando o horário ou o recurso da reserva muda.

🔘 **Reserva cancelada:** enviado quando a reserva é cancelada, pela equipe ou pelo cliente. O motivo do cancelamento entra no texto pela variável `{{motivo}}`.

## Os lembretes

🔘 **Lembretes antes do horário:** até cinco lembretes por reserva confirmada. **Adicionar lembrete** cria um, com **Ligado** e **Quanto tempo antes**: 30 min, 1 h, 2 h, 3 h, 6 h, 12 h, 1 dia, 2 dias, 3 dias ou 7 dias. Nas palavras da tela: *"Quem reservar depois da hora do lembrete não o recebe."*

## A vaga na lista de espera

🔘 **Vaga na lista de espera:** quando um horário abre, por uma reserva cancelada ou remarcada, quem está na lista de espera daquele dia recebe esta mensagem, com os horários livres e o link da página. Ligada, a página de reservas também passa a oferecer a lista de espera quando o dia está lotado.

## As variáveis

O texto de cada aviso aceita variáveis, trocadas pelos dados da reserva na hora do envio:

◽ `{{cliente}}` — o nome do cliente.

◽ `{{servico}}` e `{{recurso}}` — a oferta e o recurso da reserva.

◽ `{{data}}`, `{{diaDaSemana}}`, `{{hora}}` e `{{horaFim}}` — o dia, o dia da semana, a hora do começo e a do fim.

◽ `{{dataSaida}}` e `{{noites}}` — a data de saída e o número de noites da diária.

◽ `{{pessoas}}` — quantas pessoas.

◽ `{{empresa}}` — o nome da empresa.

◽ `{{codigo}}` e `{{link}}` — o código da reserva e o link da **Minha reserva**.

◽ `{{motivo}}` — o motivo do cancelamento.

O aviso da vaga na lista de espera usa `{{cliente}}`, `{{servico}}`, `{{data}}`, `{{diaDaSemana}}`, `{{horarios}}` (os horários livres), `{{link}}` (o link da página) e `{{empresa}}` (o nome da empresa).

Para a diária, acrescente `{{dataSaida}}` e `{{noites}}` ao texto da **Reserva confirmada**, como `Saída: {{dataSaida}} · {{noites}} noite(s)`. Sem elas, o hóspede recebe só a data de entrada.

Ao salvar, a tela avisa *"Avisos salvos."*

## O que foi enviado

No detalhe de cada reserva, na **Agenda de reservas**, o bloco **Mensagens ao cliente** lista cada aviso com a data, a hora e a situação: **enviado**, ou **não enviado** com o motivo, como *"a reserva não tem telefone"*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Liguei os avisos e o cliente não recebeu nada.** Abra a reserva na **Agenda de reservas** e confira o bloco **Mensagens ao cliente**. Uma reserva sem telefone aparece como **não enviado (a reserva não tem telefone)**.
>
> **O hóspede da diária recebeu só a data de entrada.** Acrescente `{{dataSaida}}` e `{{noites}}` ao texto do aviso na aba **Avisos** e salve. As próximas mensagens já levam a saída e as noites.
>
> **Como a página passa a oferecer a lista de espera?** Ligue o aviso **Vaga na lista de espera** na aba **Avisos**. Ligado, a página oferece a lista quando o dia está lotado.
