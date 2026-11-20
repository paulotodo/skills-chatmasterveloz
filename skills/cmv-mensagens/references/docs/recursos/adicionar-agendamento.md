# Adicionar Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/adicionar-agendamento
- **Categoria:** Recursos
- **Menu:** Agendamentos › Adicionar Agendamento

---

🧩 **Adicionar um Agendamento** permite que você programe o envio automático de mensagens para o futuro. Seja um retorno pontual para amanhã à tarde (Simples) ou uma cobrança que deve ser enviada todo dia 10 (Recorrente), o sistema assume o trabalho de lembrar e disparar a mensagem por você.

☑️ **Produtividade:** Automatize cobranças, lembretes e follow-ups em ciclos contínuos.

☑️ **Anotações Internas:** Crie lembretes silenciosos que apenas a sua equipe consegue ler dentro do ticket.

☑️ **Multimídia:** Você pode agendar não apenas textos, mas também enviar arquivos e documentos anexados.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Agendamentos** e clique no botão **+ Nova Agendamento** no canto superior direito.
>
> ➡️ Ou dentro da conversa do cliente, clique no botão superior de **Agendamento** (o contato já virá preenchido).

## Como adicionar um Agendamento

Você pode iniciar um agendamento de duas formas:  
1. Através do menu → Agendamentos > + Nova Agendamento
2. Ou diretamente em um Chat, na área de Ações do Ticket no canto superior, enquanto atende um cliente (o que agiliza o processo, pois o nome dele já vem selecionado).

![Chat - Adicionar Agendamento](https://clihelper.chatmasterveloz.com/docs-imagem/29263-agendamento-chat-adicionar.jpg) ![Adicionar um Agendamento](https://clihelper.chatmasterveloz.com/docs-imagem/29263-agendamento-adicionar.jpg)⚡ **Informação do Contato**

🔘 **Contato:** Busque o cliente digitando pelo menos 3 letras. (Se usou o atalho do chat, pule esta etapa).

⚡ **Conexão e Fila**

🔘 **Conexão:** Selecione qual conexão enviará a mensagem.

🔘 **Fila:** (Opcional) Vincule a mensagem a um departamento específico. **Funciona apenas** se escolher Abrir Ticket.

#### API Oficial

Se a conexão escolhida no passo anterior for uma **API Oficial (Cloud)**, as regras de envio mudam:

◽ O sistema exibirá um campo extra para escolha de **Mensagem Template**.

◽ Você **obrigatoriamente** precisa selecionar um Template aprovado para enviar ao cliente.

◽ A caixa de texto será preenchida com o nome do Template. Mesmo que você apague e digite outro texto ali, o sistema irá ignorar a sua edição e **sobrescrever** com o texto original do Template na hora do envio.

⚠️ Atenção:

◽ Mensagens de texto comum e anexos comuns **não** são enviadas pela API Oficial de forma agendada, mesmo que a janela de 24 horas do cliente esteja aberta. A única exceção para usar texto livre na API Oficial é se o agendamento for configurado apenas para “Criar Anotação” (nossa Comunicação Interna – Whisper).

⚡ **Mensagem e Arquivo**

🔘 **Mensagem:** Digite o texto da mensagem.

🔲 **Anexar Arquivo:** Use o ícone de clipe no final da tela para adicionar um arquivo.

⚡ **Data e Horário**

🔘 **Data e Horário do Envio:** Escolha o dia e o minuto exato do primeiro (ou único) disparo.

⚡ **Configurações Avançadas**

🔘 **Abrir Ticket:** Defina se a mensagem será enviada de forma silenciosa (Não) ou se o sistema deve abrir a tela de chat para o seu atendente (Sim).

🔘 **Criar Anotação:** Se você marcar "Sim", a mensagem digitada no campo principal NÃO será enviada ao cliente. Ela se transformará em uma **mensagem interna** no ticket, que somente o seu atendente poderá ver. Excelente para deixar instruções (ex: "Ligar para este cliente hoje e oferecer o upgrade").

🔘 **Repetir a cada:** Se for um envio único (Simples), deixe como "Não Repetir".

Se for uma rotina (Recorrente), escolha a frequência (ex: a cada 1 dia, a cada 7 dias, etc).

Porém, se você precisa que seja enviada a mensagem em um dia fixo no mês: selecione a opção **Todo dia...** (e então selecione o dia no campo **Repetir todo dia**).

🔘 **Repetir todo dia:** Selecione o **dia do mês** que deve ser repetido essa mensagem. (Atenção: para usar esse campo, selecione **Todo dia...** no campo anterior **Repetir a cada**).

Você pode também optar por enviar a cada **Ano** a partir da data selecionada de envio.

🔘 **Quantas vezes repetir:** Se ativou a repetição, defina se ela vai acontecer um número fixo de vezes (ex: 12 parcelas) ou se será "Ilimitado" (para sempre).

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso agendar uma mensagem para um número que não está salvo nos Contatos?** Não. Para garantir a segurança e evitar envios acidentais, o destinatário precisa estar previamente cadastrado na sua base de Contatos do sistema para aparecer na busca.
>
> **Se eu marcar "Não" em Abrir Ticket, eu perco a conversa?** Não perde! A mensagem será enviada e ficará registrada no histórico do cliente. Se ele responder, o fluxo normal acontece: ele volta para a fila e aguarda atendimento.
>
> **Posso usar o "Criar Anotação" para um disparo recorrente?** Sim! Você pode programar o sistema para gerar uma anotação interna no ticket do cliente todo dia 01, lembrando o seu vendedor de conferir o status da conta daquele cliente, sem que o cliente saiba.
>
> **A API Oficial cobra pelos agendamentos de Template?** Depende da categoria do Template. Se for um template de Marketing, haverá o custo padrão da Meta. Porém, se for um template de Utilidade (Utility) e a janela de 24 horas daquele cliente estiver aberta (porque ele conversou com você recentemente), a Meta não cobrará por esse disparo de Utilidade!

> **[ERROS]**
>
> #### Erros Comuns
>
> **Configurar a data inicial errada:** Querer que a cobrança saia todo dia 05, mas configurar a "Data e Horário do Envio" inicial para o dia 20. O sistema vai obedecer a data inicial e começará a repetir a cada mês no dia 20, e não no dia 05.
>
> **Editar o texto do Template da API Oficial:** O usuário seleciona o Template de cobrança, vê o código na caixa de texto e resolve apagar para escrever "Oi, segue seu boleto". Na hora agendada, o WhatsApp ignora a edição manual e dispara o Template original.
>
> **Enviar mensagem de texto livre pela API Oficial:** O usuário não seleciona nenhum Template, digita um texto comum e agenda. O envio falhará, pois a API Oficial exige o uso de Templates para disparos programados.
