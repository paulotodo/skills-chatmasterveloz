# Mensagem de Aniversário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mensagem-de-aniversario
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Mensagem de Aniversário

---

🧩 **A Mensagem de Aniversário** é uma automação simples, mas extremamente poderosa, que envia uma mensagem de felicitações personalizada para o seu cliente exatamente no dia do aniversário dele, sempre às **10h da manhã**. É a forma perfeita de humanizar o seu atendimento e reativar clientes antigos sem gerar nenhum trabalho manual para a sua equipe.

☑️ **Fidelização:** Fortalece o relacionamento, mostrando que o cliente é lembrado, criando um forte vínculo emocional com a sua marca.

☑️ **Engajamento:** Reabre um canal de comunicação de forma natural e amigável.

☑️ **Aumento de Vendas:** É a oportunidade de ouro para enviar um "presente" (como um cupom de desconto exclusivo ou frete grátis), incentivando o cliente a fazer uma nova compra no mês de aniversário.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Preencha o **dia e o mês do aniversário** ao editar um contato.
>
> ➡️ Em **Configurações**, configure sua **Mensagem de Aniversário**.
>
> ➡️ A mensagem é enviada pela **Conexão definida como Padrão** no dia do aniversário do contato às **10h da manhã**.

## Como cadastrar o aniversário do Contato

Ao **Editar um Contato**, no campo **Aniversário**, escolha o **Dia** e o **Mês**. O **Ano** é opcional, e não é preciso informar horário.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/24913-contato-aniversario.jpg)

## Como configurar a mensagem de aniversário

Acesse o menu **Configurações  ›  Mensagem de Aniversário** para configurar uma mensagem personalizada, que será enviada às **10h da manhã** no **dia do aniversário** registrado no cadastro do Contato.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/24913-mensagem-aniversario.jpg)

## Definir a Conexão de Disparo

O sistema precisa saber qual das suas conexões será o "remetente" dessa mensagem automática.

No menu **Conexões  ›  Editar  ›  Geral**, defina a conexão desejada como **Padrão**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso mudar o horário de disparo (10h da manhã)?** Não. Atualmente, o gatilho interno do sistema é programado para disparar pontualmente às 10h da manhã. É um horário estratégico e comercialmente validado para não incomodar o cliente de madrugada.
>
> **O que acontece se eu não souber o ano em que o cliente nasceu?** Deixe o **Ano** em branco: ele é opcional no campo **Aniversário**. O disparo leva em consideração apenas o **Dia** e o **Mês** para enviar a mensagem anual.
>
> **Uso a API Oficial do WhatsApp (Cloud). A mensagem de aniversário vai chegar?** ⚠️ **Atenção a esta regra da Meta:** Se você usa a API Oficial, o disparo obedece à regra da janela de 24 horas. Se a janela estiver fechada, uma mensagem de texto comum será bloqueada pelo WhatsApp.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer de definir a Conexão Padrão:** O usuário configura o texto, cadastra as datas, mas não marca nenhuma conexão como "Padrão" no menu Conexões. Chega às 10h da manhã, o sistema tenta enviar a mensagem, não sabe qual conexão usar e o disparo falha.
>
> **Mensagem engessada e sem Call to Action (Chamada para Ação):** Escrever apenas "Feliz aniversário". O cliente vai ler, pensar "obrigado" e fechar o WhatsApp. Aproveite esse envio automático (que tem altíssima taxa de abertura) para engajar! Envie um link, ofereça um mimo ou faça uma pergunta.
>
> **Digitar a data no campo de "Anotações" do contato:** Anotar "aniversário dia 12/05" nas notas livres do cadastro do cliente. O robô não lê anotações em texto. A data obrigatoriamente precisa estar inserida no campo oficial chamado **Aniversário** para que o gatilho funcione.
