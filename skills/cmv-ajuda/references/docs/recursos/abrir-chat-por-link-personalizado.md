# Abrir Chat por Link Personalizado

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/abrir-chat-por-link-personalizado
- **Categoria:** Recursos
- **Menu:** Chats / Tickets › Abrir Chat por Link Personalizado

---

🧩 O **link de atendimento Personalizado** é um endereço que já contém quem atende, em qual setor e por qual conexão, e entrega a conversa aberta na tela da plataforma.

![Link de Atendimento Personalizado](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ab3e86a0d6ca.png)

Serve para quem começa o atendimento **fora** da plataforma: um botão no sistema da empresa, uma lista de leads, um atalho salvo no navegador.

Ideal para:

☑️ **Botão no sistema da empresa:** Abre a conversa a partir de um sistema externo, sem que o operador procure o contato na lista.

☑️ **Escala de plantão:** Direciona o atendimento ao operador da vez, porque o atendente vai escrito dentro do link.

☑️ **Lead que ainda não é contato:** Cadastra o número no momento em que o link é aberto, sem nenhum passo anterior.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Equipe** e anote o número que aparece como **ID** no card do atendente.
>
> ➡️ Acesse o menu **Setores & Chatbot** e anote o número ao lado do nome do setor.
>
> ➡️ Acesse o menu **Conexões** e anote o número que aparece como **ID** no card da conexão.
>
> ➡️ Monte o endereço na ordem **/ atendente / setor / conexão / telefone**.
>
> ➡️ Abra o endereço no navegador, já conectado à plataforma.

## Como montar o link

Depois do endereço que você usa para entrar na plataforma vêm quatro informações, sempre nesta ordem:

```
https://{FRONTEND_URL}/ATENDENTE/SETOR/CONEXAO/TELEFONE
```

Com os números no lugar:

```
https://{FRONTEND_URL}/5/3/12/5511967296849
```

🔘 **Endereço da plataforma:** o começo do link, `{FRONTEND_URL}`, é o endereço em que você entra na plataforma. Se ele aparecer como `{FRONTEND_URL}`, troque pelo endereço que aparece na barra do navegador quando você está na plataforma.

🔘 **Atendente:** o número do Atendente. Está no menu **Equipe**, como **ID**, no card de cada pessoa. Não precisa ser você — o link pode apontar para outro operador, e o atendimento nasce no nome dele.

🔘 **Setor:** o número do setor em que o atendimento entra. Está no menu **Setores & Chatbot**, ao lado do nome, com **#** na frente.

🔘 **Conexão:** o número da conexão por onde a conversa fica. Está no menu **Conexões**, como **ID**, no card.

🔘 **Telefone:** o número do cliente com código do país e DDD. Parênteses, traços e espaços são ignorados, mas os dígitos precisam ser exatamente os do cadastro do contato.

⚠️ O link só abre para quem está conectado à plataforma. Quem clicar sem estar logado é direcionado para tela de entrada — **este não é um link para enviar ao cliente**.

## O que acontece ao abrir o link

🔘 **O contato não tem atendimento aberto:** a conversa abre no nome, no setor, e na conexão do link, já em atendimento — sem passar pelo chatbot nem pela espera.

🔘 **O contato já foi atendido antes:** a conversa anterior volta inteira, com todo o histórico. A tela anuncia um ticket novo, mas nada se perde.

🔘 **O número não está nos contatos:** o cadastro é criado na hora, com o próprio número no lugar do nome. Vale renomear depois.

🔘 **O contato está esperando no setor:** o atendimento sai da espera e passa para o seu nome, sem aviso na tela.

🔘 **O contato está com outro operador:** aparece **Contato em Atendimento**, com o nome de quem está atendendo e os botões **Visualizar Ticket** e **Voltar**. O atendimento não muda de mãos.

⚠️ Abrir o atendimento pelo link **não envia nada ao cliente** — nem saudação, nem aviso. A primeira mensagem é sempre sua.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso mandar esse link para o cliente?** Não. Ele funciona apenas para quem tem acesso à plataforma e está conectado; o cliente cairia na tela de entrada.
>
> **Preciso ser administrador para usar o link?** Não. Ele funciona para qualquer pessoa da equipe que consiga entrar na plataforma — atendente, supervisor ou administrador.
>
> **O link tira o atendimento de outro operador?** Não. Quando o contato já está com alguém, a tela mostra quem é e oferece apenas visualizar a conversa.
>
> **Dá para apontar o link para outro atendente?** Sim. O atendente é a primeira informação do endereço, e o atendimento nasce no nome dele mesmo que quem abriu o link seja outra pessoa. Isso não depende do seu perfil.
>
> **Serve para número que ainda não é contato?** Sim. O cadastro nasce junto com o atendimento, usando o número como nome.
>
> **O cliente recebe alguma mensagem quando abro o atendimento assim?** Não. A conversa abre vazia do lado dele; nada é enviado até você escrever.
>
> **A tela disse que criou um ticket novo, mas a conversa antiga está lá. Está errado?** Não. Quando já houve atendimento com aquele contato naquela conexão, o link reabre a mesma conversa — o aviso é só o texto da tela.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer o código do país:** sem o **55** na frente, o número não é reconhecido como o contato que já existe — nascem um contato repetido e um atendimento à parte. Use sempre código do país + DDD + número.
>
> **Sobrar o nono dígito:** em DDD acima de 30 o número tem oito dígitos. Acrescentar o nove cria outro contato, com a conversa separada da original.
>
> **Endereço incompleto:** faltando qualquer uma das quatro informações, a tela mostra **Parâmetros inválidos** e volta para os atendimentos em dois segundos.
>
> **Setor ou conexão que não existe mais:** o link devolve uma mensagem de erro técnica e não abre nada. Quando um link para de funcionar do nada, confira os números — setor apagado é a causa mais comum.
