# Adicionar WhatsApp QRCode

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/adicionar-whatsapp-qrcode
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Adicionar WhatsApp QRCode

---

🧩 Conectar por QR Code é ligar a plataforma a um número que vive num celular, do mesmo jeito que o WhatsApp Web: o aparelho lê um código e, a partir daí, as conversas passam pela plataforma. O celular continua funcionando normalmente.

É o caminho mais rápido de todos. Em poucos minutos o número da empresa já está atendendo pela plataforma, sem cadastro na Meta, sem custo por mensagem e sem esperar aprovação de ninguém.

Ideal para:

☑️ **Começar hoje:** O número que já existe entra na plataforma sem nenhum processo externo.

☑️ **Número secundário:** Um setor que atende pouco, um telefone de apoio, um teste antes de decidir.

☑️ **Sem custo por mensagem:** O envio não passa pela Meta e não entra em nenhuma fatura.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões**, abra **Ações** e escolha **Adicionar WhatsApp**.
>
> ➡️ Preencha o **Nome** e, na aba **Setores & Tempos**, marque um Setor. Salve.
>
> ➡️ No card, clique em **Ver QR Code** e leia com o celular do número: no WhatsApp, **Aparelhos conectados** e **Conectar um aparelho**.
>
> ➡️ O card muda para **Conectado**. Pronto.

## As formas de ligar o número

🔘 **Ver QR Code:** o caminho comum. O código muda de tempos em tempos; se expirar, o card gera outro.

🔘 **Obter Código:** em vez de ler o QR, a plataforma mostra um código numérico para digitar no celular, em **Aparelhos conectados**, opção **Conectar com número de telefone**. Serve quando a câmera não ajuda.

🔘 **Passkey:** outra forma de autenticar a sessão, sem QR.

🔘 **Importar Sessão:** traz uma sessão já exportada, sem ler o código de novo.

## O cadastro, aba por aba

São cinco abas. Só a primeira precisa estar preenchida para criar a conexão; as outras podem esperar, editando depois.

### ⚡ Geral

🔘 **Nome:** como esta conexão aparece nas listas e nos relatórios. Se você tem mais de um número, use o **papel** dele — Vendas, Suporte, Financeiro — em vez do número em si.

🔘 **Padrão:** marca esta conexão como a que a plataforma usa quando precisa escolher um canal sem indicação. Só uma fica assim por vez.

🔘 **Bloquear ECHO:** evita que a mesma mensagem chegue duplicada ao atendimento.

🔘 **Bloquear Grupos:** impede que conversa de grupo vire atendimento.

🔘 **Novo ticket ao reabrir** e **Novo ticket ao transferir:** decidem se a conversa continua no mesmo atendimento ou se abre um novo. Com um atendimento novo, o histórico anterior **não vai junto** — cada atendimento passa a valer por si.

🔘 **Arquivo de Capa:** imagem enviada ao cliente no começo da conversa.

### ⚡ Mensagens

São os textos automáticos que saem por esta conexão. Todos são opcionais, e cada um dispara num momento diferente.

🔘 **Mensagem de saudação:** quando a conversa começa.

🔘 **Mensagem de conclusão:** quando o atendimento é encerrado com mensagem de encerramento.

🔘 **Mensagem de fora de expediente:** quando o cliente escreve fora do horário.

🔘 **Mensagem de avaliação:** o convite para o cliente avaliar o atendimento.

🔘 **Mensagem de encerramento após inatividade:** o aviso enviado quando a plataforma fecha a conversa por falta de resposta.

⚠️ A saudação da Conexão e a saudação do Setor **somam**: se as duas estiverem preenchidas, o cliente recebe as duas. Preencha uma ou outra, conforme onde a conversa entra.

⚠️ A mensagem de fora de expediente só dispara se o expediente estiver configurado. Escrever o texto aqui não liga o controle de horário sozinho.

### ⚡ Setores & Tempos

🔘 **Setores:** para onde as conversas desta conexão vão. **É o campo mais importante do cadastro.** Sem Setor, o atendimento entra e não aparece para ninguém.

🔘 **Após** e **Mover:** transferem para outro Setor o cliente que ficou esperando tempo demais. O **Após** vai até quarenta minutos.

🔘 **Inatividade** e **Inatividade Sem Setor:** encerram sozinhos o atendimento em que o cliente parou de responder. Contam de cinco em cinco minutos até seiscentos, e depois passam a dias, até dez.

📌 Os dois pares têm artigo próprio, com as regras completas de quando cada um dispara. Procure por mover após e por encerrar por inatividade.

### ⚡ Integrações

🔘 **Token:** a senha que **você define** para acionar esta conexão pelas APIs. Só preencha se for usar integração; para o atendimento do dia a dia não é necessário. Trate como senha: quem tem o token envia mensagens pela sua conexão.

🔘 **Webhook Principal** e **Webhook Secundário:** endereços que recebem uma notificação a cada evento desta conexão.

🔘 **Ignorar Números:** lista de números que não devem virar atendimento.

🔘 **iFrame Externo - Integração / Contato:** endereço de um sistema seu que aparece dentro do painel do contato.

🔘 **Abrir o painel do contato ao abrir o ticket:** deixa o painel já aberto quando o atendente entra na conversa.

🔘 **Confirmação de Leitura:** define se a plataforma marca as mensagens do cliente como lidas.

🔘 **Prefixo VOIP:** o que é acrescentado antes do número nas chamadas por voz.

⚠️ O campo **Token de Voz para Chamadas pelo WhatsApp** é de uma integração que não existe mais. **Deixe em branco.**

⚠️ Mudar a **Confirmação de Leitura** não derruba a conexão sozinha, mas a mudança só passa a valer depois de você **reconectar o número à mão**. Salvar não basta.

### ⚡ Proxy

Faz a sessão desta conexão sair por um servidor intermediário, em vez de sair direto.

🔘 **Endereço do Proxy:** no formato `https://proxy.exemplo.com:443` ou `socks5://proxy.exemplo.com:1080`.

🔘 **Usuário do Proxy** e **Senha do Proxy:** deixe em branco se o proxy não exigir autenticação.

⚠️ A mudança só vale depois de reconectar a sessão.

## O que o card oferece depois de conectado

🔘 **IP** e **Cluster:** por onde a sessão desta conexão está saindo.

🔘 **Diagnosticar Proxy:** testa o proxy **desta conexão**, o que foi preenchido na aba acima. Abre um painel com o estado, a latência, o IP resolvido, o protocolo, o host e a porta.

🔘 **Rotacionar IP:** troca o endereço de saída da sessão. A plataforma avisa qual era e qual passou a ser.

🔘 **Perfil do número:** ajusta o que o cliente vê ao abrir seu contato no WhatsApp — a foto, o nome exibido e o recado, com a opção de apagar o recado depois de um tempo. A foto é cortada em quadrado. Só aparece com a conexão **conectada**.

🔘 **Ver Eventos:** o histórico do que aconteceu com a sessão.

🔘 **Reiniciar esta conexão** e **Configurar SIP:** manutenção da sessão e telefonia.

🔘 **Pausar conexão:** interrompe o tráfego sem desconectar. O que fazer com isso está no artigo da visão geral de Conexões.

⚠️ **Sem proxy configurado, o diagnóstico mostra "Falha".** Não é defeito: repare na linha **Configurado**, que dirá **Não**. É o estado normal de quem nunca preencheu a aba, e a conexão funciona assim.

## Quando a conexão cai

O card volta para **Desconectado** ou **QR Code**. Três botões resolvem:

🔘 **Reconectar:** tenta retomar a sessão que existia.

🔘 **Novo QR:** gera um código novo para ler outra vez.

🔘 **Excluir Sessão:** apaga a sessão e começa do zero. Use quando os dois anteriores não resolvem.

⚠️ O celular precisa ter internet e o WhatsApp aberto de vez em quando. Aparelho desligado por muito tempo derruba a sessão, e a conexão volta a pedir o código.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O QR Code não aparece.** Aguarde o card carregar e clique em **Ver QR Code** de novo. Se a conexão está em **Desconectado**, use **Novo QR**.
>
> **Li o código e o card continua em QR Code.** O código expirou antes de terminar. Gere outro e leia com o celular já na tela de **Conectar um aparelho**.
>
> **Perco as conversas se a conexão cair?** Não. O histórico fica na plataforma. Ao reconectar, o atendimento continua de onde parou.
>
> **Posso ler o mesmo QR em dois celulares?** Não. A conexão é de um número. Para outro número, crie outra conexão.
>
> **O celular precisa ficar ligado?** Sim, com internet. É ele que mantém a sessão de pé.
>
> **Onde vinculo o Setor depois de criar a conexão?** No card, no lápis de editar, aba **Setores & Tempos**.
>
> **O diagnóstico de proxy deu Falha e eu não uso proxy. Tem problema?** Não. Sem proxy preenchido é isso que aparece. A linha **Configurado** dirá **Não**, e é essa que importa.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Criar a conexão sem marcar Setor:** o cliente manda mensagem, o atendimento entra e não aparece para a equipe. **Solução:** edite a conexão, aba **Setores & Tempos**, e marque ao menos um.
>
> **Ler o QR com o celular errado:** a conexão fica com o número de quem leu. **Solução:** **Desconectar**, **Excluir Sessão** e ler com o aparelho certo.
>
> **Desconectar pelo celular:** em **Aparelhos conectados**, tocar em **Desconectar** derruba a plataforma junto. **Solução:** deixe o aparelho listado; para interromper, use **Desconectar** no card.
>
> **Preencher a saudação da Conexão e a do Setor:** o cliente recebe as duas, uma atrás da outra. **Solução:** escolha em qual dos dois lugares a saudação vai ficar.
>
> **Trocar a Confirmação de Leitura e achar que já valeu:** o campo salva, mas o comportamento só muda depois de reconectar o número. **Solução:** reconecte logo após salvar.
