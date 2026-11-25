# Web Chat

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/web-chat
- **Categoria:** Recursos
- **Menu:** Conexões › Web Chat

---

🧩 O **Web Chat** coloca um chat dentro do seu site, e as conversas caem na mesma tela de atendimento dos outros canais. Instalar é colar um bloco de código no site; o resto é configuração aqui.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/22970-webchat-site.jpg) ![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/22970-chat-webchat.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões**, abra **Ações** e escolha **Adicionar WebChat**.
>
> ➡️ Preencha o **Nome da Conexão**, o **Nome do Widget** e marque um Setor. Salve.
>
> ➡️ Edite a conexão de novo e abra a aba **Código Embed**. Copie o código e cole no site, antes da tag `</body>`.

## Aba Geral

🔘 **Nome da Conexão:** o nome interno, para a lista e os relatórios.

🔘 **Nome do Widget:** o que o visitante lê no cabeçalho do chat.

🔘 **Setores:** para onde as conversas vão. Sem Setor, ninguém vê.

🔘 **Habilitar som de notificação:** o aviso sonoro do lado do visitante.

🔘 **Novo ticket ao reabrir** e **Novo ticket ao transferir:** o mesmo comportamento das outras conexões.

🔘 **Abrir ticket automaticamente ao visitar:** nas palavras da tela, *quando desligado, um ticket só é aberto quando o visitante enviar a primeira mensagem; a presença no mapa de visitantes continua funcionando normalmente*.

🔘 **Abrir o widget automaticamente após (segundos):** nas palavras da tela, *0 = desligado; maior que 0, o widget abre sozinho após o tempo definido*.

🔘 **Usar horário de atendimento:** nas palavras da tela, *fora deste horário, o WebChat mostra que a empresa está offline e quando volta, e continua recebendo mensagens*. Ligado, você define o horário de cada dia da semana; dia sem horário fica offline.

🔘 **Idioma:** o idioma dos textos do chat.

🔘 **Campos do formulário inicial:** **Nome**, **E-mail** e **Telefone**, cada um com a opção **Obrigatório**. Nas palavras da tela: *defina quais campos o visitante deve preencher antes de iniciar a conversa*.

## Aba Aparência

🔘 **Foto, nome e frase do topo:** nas palavras da tela, *a foto, o nome e a frase que aparecem no topo do WebChat*.

◽ **Enviar foto:** JPG, PNG ou WEBP. A foto é recortada em quadrado e salva na hora.

◽ **Nome no topo:** em branco, usa o nome da empresa.

◽ **Frase abaixo do nome:** em branco, mostra "online" ou o nome do cliente.

🔘 **Cor Primária** e **Cor Secundária:** as cores do chat, para combinar com o site.

🔘 **Texto do Placeholder:** a frase dentro da caixa de digitação.

🔘 **Exibir Avatar**, **Habilitar Emojis** e **Habilitar Upload de Arquivos:** ligam ou desligam esses recursos no chat do site.

## Aba Mensagens

🔘 **Mensagem de Boas-vindas:** nas palavras da tela, *exibida como primeira mensagem assim que o widget é carregado*.

## Aba Integrações

🔘 **URL de Webhook** e **URL de Webhook Secundário:** endereços que recebem os eventos do WebChat, como as mensagens recebidas. O secundário recebe os mesmos eventos, para uma integração paralela.

🔘 **Token de Autenticação:** enviado no cabeçalho das chamadas aos webhooks, para o seu sistema confirmar de onde vieram.

🔘 **Bloquear bots e crawlers:** ligado, as visitas de buscadores, monitores e robôs de raspagem conhecidos são descartadas — não geram contato nem atendimento e não aparecem no mapa de visitantes.

## Aba Código Embed

Só aparece com conteúdo **depois de salvar** a conexão: no cadastro novo, a aba fica desabilitada. Ao editar, ela mostra um bloco de código com o identificador da sua conexão e o endereço da plataforma, e o botão **Copiar código**. Nas palavras da tela: *copie o código abaixo e cole antes da tag `</body>` do seu site*.

⚠️ O código identifica a sua conexão. Quem tem o código consegue abrir chats na sua operação; não publique fora do seu site.

## Botões e menu do fluxo no Web Chat

Quando o Setor da conexão roda um fluxo do **FlowBuilder Nativo**, o bloco **Botões** e o **Menu em Lista** chegam clicáveis no chat do site: o visitante toca na opção em vez de digitar, e o fluxo segue na hora. No **Menu em Lista**, o botão da lista abre as opções dentro do chat.

Só a última mensagem com opções aceita o toque: as opções das mensagens anteriores ficam desativadas no chat do site, e o toque numa delas é recusado.

Com **Abrir ticket automaticamente ao visitar** ligado, o fluxo começa quando o visitante abre a página, antes de ele escrever.

Os avisos *Visitante acessou o site* e *Visitante preencheu o formulário* aparecem no atendimento como **mensagem interna** e não respondem o fluxo: o bloco que espera um toque continua esperando o visitante.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A aba Código Embed está cinza.** A conexão ainda não foi salva. Salve, edite de novo e a aba abre.
>
> **De onde vêm os visitantes que aparecem antes de escrever?** De **Abrir ticket automaticamente ao visitar**. Desligue para só abrir atendimento na primeira mensagem. O mapa fica no menu **Visitantes ao Vivo**.
>
> **O chat abre sozinho no site.** É **Abrir o widget automaticamente após**. Coloque **0**.
>
> **O visitante do Web Chat pode tocar nos botões do fluxo?** Pode. O bloco **Botões** e o **Menu em Lista** chegam clicáveis no chat do site, e o fluxo segue na hora. Só a última mensagem com opções aceita o toque.
>
> **Posso pedir só o nome?** Sim. Em **Campos do formulário inicial**, deixe só **Nome** marcado.
>
> **O chat do site aparece como offline.** Pode ser o **Usar horário de atendimento**: fora do horário definido, o chat mostra que a empresa está offline e quando volta, mas continua recebendo as mensagens.
