# Editar Empresa em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-editar-empresa
- **Categoria:** Recursos
- **Menu:** Configurações › Empresas em Configurações › Editar Empresa em Configurações

---

🧩 **Editar Empresa** é o modal que abre ao clicar no nome de uma empresa, no card dela. Tudo que é sobre essa empresa — plano, vencimento, limites de voz, bloqueios, aparência própria e integrações.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Empresas** e clique no nome da empresa, no card dela.
>
> ➡️ Percorra as abas **Informações Básicas**, **Configurações**, **Avançado** e **Integrações**.
>
> ➡️ Na aba **Integrações**, a seção **Chave da OpenAI** tem botão próprio: escolha a opção (com a chave da plataforma, cole a chave em **Chave da plataforma para esta empresa**) e clique em **SALVAR CHAVE**.
>
> ➡️ Clique em **Salvar Alterações**. **Cancelar** descarta tudo que foi mexido nas quatro abas.

## ⚡Aba Informações Básicas

◽ **Dados da Empresa**

🔘 **Nome da Empresa:** obrigatório. É o nome do card e da saudação no topo da plataforma.

🔘 **Nome Completo:** o nome do responsável.

🔘 **E-mail:** obrigatório. O contato da empresa.

🔘 **Telefone** e **País:** o telefone recebe os lembretes de cobrança por WhatsApp, quando ativados.

🔘 **Indicador:** quem indicou a empresa — o mesmo dado do **Código de Indicação** do cadastro.

## ⚡Aba Configurações

◽ **Plano e Status**

🔘 **Plano:** obrigatório. Define limites e o que a empresa pode usar.

🔘 **Status:** a situação da conta dessa empresa.

🔘 **Próximo Vencimento**: data do próximo vencimento.

🔘 **Recorrência:** quando a próxima fatura vence e com que frequência (Mensal, Trimestral, Semestral ou Anual).

◽ **Tarifador de Voz**

🔘 **Franquia de minutos (mês):** nas palavras da tela, *"Minutos de saída inclusos por mês. 0 bloqueia as ligações quando o plano tem tarifador."*

🔘 **Preço por minuto:** *"Tarifa única, cobrada 60/60 sobre o tempo atendido. 0 mede sem cobrar."*

Os dois campos alimentam o card **Consumo de Voz**.

◽ **Permissões e Bloqueios**

🔘 **Pode Acessar?:** a permissão de login.

🔘 **Campanhas Habilitadas:** ligado, a empresa usa Campanhas — desde que o plano esteja habilitado.

🔘 **Bloquear Grupos:** ligado, mensagens de grupo não viram atendimento nesta empresa.

🔘 **Confirmação de Leitura:** ligado, o cliente vê o visto azul quando a mensagem é lida. (Atenção, sobrecarrega a plataforma)

🔘 **Importar Conversas:** ligado, ao conectar um número as conversas existentes no aparelho são importadas. (Funcionalidade instável)

🔘 **Modo Híbrido para API Oficial:** ligado, a conexão oficial trabalha em modo híbrido com uma não oficial do mesmo número.

🔘 **Modo Alternativo (Chat Externo por Link):** ligado, a empresa pode atender por link externo, fora da tela padrão.

🔘 **Concatenador de Mensagens:** concatena mensagens manuais antes de enviar. A configuração acontece dentro de cada Conexão.

◽ **Customização Visual (CSS/JS)**

🔘 **Usar a customização geral (CSS e JS):** ligado, a empresa usa o CSS e o JS do card **Cores**. Desligado, nas palavras da tela, *"esta empresa fica com o layout padrão: sem o CSS geral do painel e sem o JS geral. Não afeta as telas de login e cadastro, que são gerais."* Ao entrar, a aba recarrega uma vez para o código geral sair de verdade.

🔘 **CSS desta empresa:** a aparência só desta empresa, depois do login, *"somando ao CSS geral (quando ligado)"*. Em empate de especificidade, vence o CSS da empresa; para vencer regras do tema, pode precisar de `!important`.

🔘 **JS desta empresa:** o comportamento só desta empresa, depois do login, *"além do JS geral"*. Passa a valer no próximo carregamento da página.

🔘 **CSS do Chat Externo (Modo Alternativo):** vale só na página de chat que o cliente final abre pelo link. Como aquela página tem marcação própria, use nela as âncoras `custom-css-chat-*`.

## ⚡Aba Avançado

◽ **Configurações Técnicas**

🔘 **KeyStorage:** o identificador de armazenamento da empresa. PostgreSQL

🔘 **API Não Oficial:** qual biblioteca a empresa usa nas conexões de WhatsApp não oficial.

🔘 **Ambiente:** o ambiente da empresa.

🔘 **Usar Proxy?** e **Proxy String (se personalizado):** se as conexões da empresa passam por um proxy, e qual.

## ⚡Aba Integrações

◽ **Chave da OpenAI**

Nas palavras da tela: *"Escolha se esta empresa usa a chave própria (cadastrada por ela nas Integrações) ou a chave da plataforma. A chave da plataforma nunca aparece para a empresa."*

🔘 **Chave própria do cliente:** a inteligência artificial desta empresa usa a chave da OpenAI que ela cadastra no menu **Integrações**, no card **OPEN.AI**.

🔘 **Chave da plataforma (subsidiada):** a inteligência artificial desta empresa usa a chave salva nesta seção, no lugar da dela.

🔘 **Chave da plataforma para esta empresa:** aparece ao marcar **Chave da plataforma (subsidiada)**. É um campo de senha, de até 300 caracteres, para a chave da OpenAI que esta empresa vai usar. Sem chave salva, a tela mostra *"Nenhuma chave salva ainda."*; com chave salva, *"Chave salva, terminada em …. Preencha só para trocar."*, com o final da chave no lugar das reticências.

🔘 **SALVAR CHAVE:** o botão da seção **Chave da OpenAI**, separado do **Salvar Alterações** da janela. Escolha a opção, cole a chave quando for a da plataforma e clique nele: o aviso *"Chave da OpenAI salva."* confirma. Sem chave colada, a tela recusa com *"Para usar a chave da plataforma, cadastre a chave primeiro."*; com uma chave fora do formato da OpenAI, com *"A chave da OpenAI não parece válida. Confira e cole de novo."* Nas duas recusas, nada muda. Fechada a janela em **Cancelar** sem o **SALVAR CHAVE**, a escolha volta à que estava.

🔘 **TIRAR A CHAVE DA PLATAFORMA:** aparece quando há chave salva. Apaga a chave da plataforma desta empresa e a devolve à **Chave própria do cliente**.

⚠️ O **SALVAR CHAVE** aceita uma chave no formato da OpenAI mesmo que ela não funcione. Com uma chave assim salva, a IA que responde no Setor fica calada e as gravações das chamadas ficam sem transcrição, até a chave ser trocada ou tirada.

Com a chave da plataforma salva, a empresa vê no card **OPEN.AI** do menu **Integrações** o aviso *"A inteligência artificial desta conta usa a chave da plataforma. Não é preciso cadastrar uma chave aqui."* no lugar do campo **Token OpenAI**; **Model OpenAI** e **Idioma OpenAI** continuam no card. A chave que a empresa já tinha cadastrado fica guardada e volta a valer quando a chave da plataforma é tirada.

A chave da plataforma vale para a IA que responde no Setor (os prompts), a análise e o resumo do atendimento, o Copiloto de mensagens, a transcrição de áudio pedida pelo atendente e a IA nas gravações das chamadas. O saldo de **Tokens de IA** do Copiloto continua descontando com ela.

Ao criar uma empresa, a seção mostra *"Crie a empresa primeiro; a chave da OpenAI é definida ao editá-la."*: a chave se escolhe depois, editando a empresa.

◽ **TypeBot**

🔘 **TypeBot Nome** e **TypeBot URL:** o Typebot desta empresa.

◽ **IFrames**

🔘 **Iframe User** e **Iframe User URL**, até o **Iframe User 7**: o nome e o endereço de até sete páginas externas abertas dentro da plataforma para os usuários, supervisores e administradores da empresa.

🔘 **Iframe Admin** e **Iframe Admin URL**, até o **Iframe Admin 6**: até seis páginas, somente para acesso de administradores.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Mudei o plano e a empresa continua sem o recurso.** Quem já estava com a plataforma aberta precisa recarregar a página. E confira se o recurso está habilitado no plano, no menu **Configurações  ›  Planos**.
>
> **Bloqueei o acesso e o administrador ainda está dentro.** A sessão aberta termina quando ele recarregar ou sair. **Pode Acessar?** em **Não** impede login novo.
>
> **A empresa quer o próprio logotipo.** Logotipo é da instância, no card **Logotipos / Ícones**. Por empresa, o que existe é **CSS desta empresa** — dá para trocar cores e esconder elementos.
