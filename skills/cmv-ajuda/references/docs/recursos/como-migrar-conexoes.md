# Como Migrar Conexões

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/como-migrar-conexoes
- **Categoria:** Recursos
- **Menu:** Conexões › Como Migrar Conexões

---

🧩 Todo atendimento nasce preso a duas coisas: o **Contato** e a **Conexão** por onde a conversa entrou. Se a Conexão for excluída, os atendimentos dela ficam órfãos — e o histórico daquele cliente se parte em dois. A **migração** existe para evitar isso: ela leva os atendimentos da Conexão antiga para a nova, junto com o que depende dela.

Na conexão de WhatsApp por QR Code há um caminho mais curto: o **Clonar conexão** cria a conexão nova, leva os atendimentos e apaga a antiga numa ação só.

Ideal para:

☑️ **Histórico inteiro:** O cliente continua com uma conversa só, em vez de começar do zero na Conexão nova.

☑️ **Troca de tecnologia:** O número muda de jeito de conectar sem a operação perder o que já foi conversado.

☑️ **Conserto de engano:** A Conexão foi excluída sem querer e os atendimentos precisam de destino.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões** e adicione a nova conexão, **sem conectar ainda**.
>
> ➡️ Em **Ações**, escolha **Migrar Tickets para Outra Conexão**, marque origem e destino, escolha o que vai junto e confirme.
>
> ➡️ Confira, na própria janela, o resultado de cada parte.
>
> ➡️ Na nova conexão, marque o Setor e conecte. Depois, **Reiniciar Conexões**.

## O passo a passo

![Modal de migração de tickets entre conexões, com os campos Conexão de Origem e Conexão de Destino](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6abc0b43a0d82.png)  
1. **Adicione a nova conexão, mas não conecte.** Ela nasce desconectada, e assim deve ficar até a migração terminar.
2. **Desconecte a conexão antiga** pelo botão **Desconectar** do card. Anote suas configurações para copiar para a nova.
3. Abra **Ações** e escolha **Migrar Tickets para Outra Conexão**. O modal se chama **Migrar Tickets entre Conexões**.
4. Em **Conexão de Origem**, marque a antiga, que entrega os atendimentos.
5. Em **Conexão de Destino**, marque a nova, que recebe.
6. Em *Escolha o que vai junto*, deixe marcado o que deve ir para a nova conexão. O que ficar desmarcado continua na conexão antiga.
7. Clique em **Confirmar Migração** e confira o resultado, que aparece na própria janela.
8. Na nova conexão, marque o Setor na aba **Setores & Tempos** e configure as informações copiadas da conexão antiga. Após, conecte o número.
9. Em **Ações**, clique em **Reiniciar Conexões**.

## O que vai junto com os atendimentos

Os atendimentos sempre vão para a Conexão de destino. O resto você escolhe: a janela **Migrar Tickets entre Conexões** traz, em *Escolha o que vai junto (desmarcado, fica na conexão antiga)*, uma caixa para cada parte, todas marcadas quando a janela abre.

🔘 **Registros dos atendimentos:** os registros que acompanham os atendimentos da Conexão antiga.

🔘 **Agendamentos que ainda vão sair:** os agendamentos que ainda não foram enviados.

🔘 **Campanhas que não terminaram.**

🔘 **Conexão padrão e acesso dos usuários:** quem tinha a Conexão antiga como padrão passa a ter a nova, e quem tinha acesso à Conexão antiga ganha o acesso à nova e **continua com o da antiga**. A migração soma o acesso, não troca.

🔘 **Loja do Cardápio Digital** da Conexão antiga.

🔘 **Gatilhos de Webhook do FlowBuilder** que iniciam o fluxo pela Conexão antiga: passam a usar a nova.

Com todas as caixas desmarcadas, a migração leva só os atendimentos.

⚠️ A Conexão de origem e a Conexão de destino precisam ser diferentes. Com a mesma conexão nos dois campos, a janela avisa *"Escolha conexões diferentes: a de origem e a de destino são a mesma."* e não migra nada.

## O resultado da migração

Depois de **Confirmar Migração**, a tela avisa *"Tickets migrados com sucesso!"*, e a janela continua aberta com o **Resultado da Migração**, parte por parte:

🔘 **Total**, **Migrados**, **Ignorados** e **Falhas:** a contagem dos atendimentos.

🔘 **Também foram para a nova conexão:** quantos **Agendamentos**, **Campanhas**, **Usuários com a conexão padrão**, **Usuários com acesso**, **Loja do Cardápio Digital**, **Gatilhos de Webhook** e **Registros dos atendimentos** foram levados.

## Clonar a conexão de WhatsApp por QR Code

Na conexão de WhatsApp por QR Code, o card tem o botão **Clonar conexão**. Ele faz a troca numa ação só: nasce uma conexão nova com todas as configurações da atual, e o sistema faz o resto sozinho. A janela **Clonar a conexão** descreve cada passo antes de confirmar:

➡️ Copia as mensagens, os Setores, os horários, os webhooks, o proxy e as integrações para a conexão nova.

➡️ Passa para ela os atendimentos, os agendamentos que ainda vão sair, as campanhas que não terminaram, a conexão padrão e o acesso dos usuários, o Cardápio Digital e os gatilhos de webhook.

➡️ Apaga a conexão atual. A nova fica com o mesmo nome e o mesmo token da API, e as integrações continuam funcionando.

➡️ A conexão nova começa desconectada: no fim, leia o QR Code com o celular do número.

⚠️ **A conexão atual é apagada, e não dá para desfazer.** A janela avisa isso antes do **CLONAR**; o **CANCELAR** fecha sem mudar nada.

Depois do **CLONAR**, a janela mostra *"Pronto: … foi clonada."*, a contagem do que passou para a conexão nova e o botão **LER O QR CODE**, para conectar o número ali mesmo.

## Se a troca for do jeito de conectar

Quando a mudança é na tecnologia da conexão de WhatsApp, e não só no número, **fale com a nossa equipe antes**.

⚠️ **Antes de excluir a conexão antiga, confira na nova se os atendimentos chegaram.** A exclusão não tem volta, e o aviso que a plataforma mostra na hora é claro: excluir uma conexão impede continuar qualquer conversa iniciada por ela.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que não posso simplesmente excluir a antiga e criar outra?** Porque o atendimento é preso à Conexão. Sem migrar, os que existiam ficam sem destino, e o mesmo cliente passa a ter uma conversa nova, separada de tudo que já tinha sido dito.
>
> **Excluí a conexão antiga antes de migrar. E agora?** Os atendimentos ficaram órfãos. Realize a migração dos tickets para a nova conexão: a conexão excluída continua na lista de **Conexão de Origem**. O histórico dos contatos não se perde.
>
> **Posso migrar entre canais diferentes?** Não. As listas de **Conexão de Origem** e **Conexão de Destino** trazem só conexões de WhatsApp: a migração é de WhatsApp para WhatsApp.
>
> **Posso escolher o que vai junto na migração de conexões?** Pode. Em *Escolha o que vai junto*, a janela **Migrar Tickets entre Conexões** traz uma caixa para cada parte, todas marcadas: desmarque o que deve ficar na conexão antiga. Os atendimentos vão sempre.
>
> **Depois de migrar, quem tinha acesso à conexão antiga perde esse acesso?** Não. Com **Conexão padrão e acesso dos usuários** marcado, o usuário ganha o acesso à conexão nova e continua com o da antiga.
>
> **Quero manter os agendamentos na conexão antiga. Dá?** Dá. Na migração, desmarque **Agendamentos que ainda vão sair**: eles ficam na conexão antiga, e o resto que estiver marcado vai para a nova.
>
> **Clonar a conexão ou migrar os tickets?** O **Clonar conexão**, só no WhatsApp por QR Code, cria a conexão nova com as mesmas configurações, o mesmo nome e o mesmo token da API, leva tudo e apaga a antiga numa ação só. A migração leva os atendimentos para uma conexão que você já criou, deixa escolher o que vai junto e não apaga a antiga.
>
> **Preciso migrar toda vez que a conexão cai e pede o código de novo?** Não. Queda de sessão não é troca de conexão: é a mesma conexão esperando ser reconectada, e o histórico continua no lugar.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Clicar na lixeira em vez de Desconectar:** apaga a conexão de origem e, com ela, o caminho de volta dos atendimentos. **Solução:** desconecte, migre, confira, e só então exclua.
>
> **Conectar a nova antes de migrar:** as duas ficam ativas ao mesmo tempo e as mensagens do cliente passam a entrar na conexão errada no meio do processo. **Solução:** crie a nova desconectada e só leia o código depois de confirmar a migração.
>
> **Excluir a antiga sem conferir:** se a migração não levou tudo, não há como recuperar. **Solução:** abra a nova conexão e veja os atendimentos lá antes de apagar qualquer coisa.
>
> **Selecione as conexões antes de prosseguir:** a janela avisa isso quando as conexões não foram escolhidas. **Solução:** marque a **Conexão de Origem** e a **Conexão de Destino** antes de clicar em **Confirmar Migração**.
>
> **Escolha conexões diferentes: a de origem e a de destino são a mesma:** a janela avisa isso quando a mesma conexão foi escolhida nos dois campos, e nada é migrado. **Solução:** em **Conexão de Destino**, marque a nova conexão.
