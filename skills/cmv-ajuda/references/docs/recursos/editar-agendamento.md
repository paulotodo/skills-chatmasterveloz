# Editar Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/editar-agendamento
- **Categoria:** Recursos
- **Menu:** Agendamentos › Editar Agendamento

---

🧩 **A Edição de Agendamento** garante que a sua automação acompanhe as mudanças do dia a dia. Se o cliente pediu para adiar um retorno ou se um contrato foi encerrado antes do previsto, você tem total controle para ajustar os textos, as datas ou interromper o ciclo de disparos imediatamente.

☑️ **Flexibilidade Total:** Altere horários e mensagens sem precisar excluir e criar tudo do zero.

☑️ **Gestão de Recorrência:** Ajuste o número de parcelas ou mude o dia fixo de cobrança com facilidade.

☑️ **Atalhos de Agilidade:** Edite agendamentos sem sair da conversa com o cliente através do chat.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Agendamentos**. Clique no nome ou ícone **lápis** (✏️) para Editar.
>
> ➡️ Ou dentro da conversa do cliente, clique no botão superior de **Agendamento** e após no nome para Editar.
>
> ➡️ Edite os **campos** desejados e clique no botão **Salvar**.

## Como editar um Agendamento

Você pode editar um agendamento, que ainda não foi enviado, de duas formas:  
1. Através do menu → Agendamentos > Editar
2. Ou diretamente em um Chat, na área de Ações do Ticket no canto superior, enquanto atende um cliente.

![Ticket - Resumo do Contato](https://clihelper.chatmasterveloz.com/docs-imagem/29353-resumo-do-contato.jpg)⚡ **Informação do Contato**

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
> **Posso editar um agendamento que já foi enviado?** Não. O sistema mantém o registro do que já foi enviado como um histórico imutável para sua segurança e auditoria. Se precisar enviar novamente com correções, você deve criar um novo agendamento.
>
> **O que acontece se eu excluir um agendamento recorrente na metade do caminho?** O sistema interrompe o ciclo imediatamente. Nenhuma das mensagens futuras programadas para aquele "pacote" de repetições será enviada.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer de conferir o horário ao editar:** Ao mudar a data de um agendamento de segunda para terça, certifique-se de conferir se o horário (ex: 10h00) ainda faz sentido para o cliente. O sistema mantém o horário anterior a menos que você o altere manualmente.
>
> **Excluir o agendamento em vez de apenas editar o texto:** Muitas vezes o usuário apaga o agendamento inteiro só para mudar uma palavra na mensagem. Use o botão de **Lápis (**✏️**)**; é muito mais rápido e mantém a organização do seu histórico de agendamentos pendentes.
