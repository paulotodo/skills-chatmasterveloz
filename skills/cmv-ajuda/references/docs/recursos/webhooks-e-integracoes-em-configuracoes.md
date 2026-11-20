# Webhooks e integrações em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhooks-e-integracoes-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações › Webhooks e integrações em Configurações

---

🧩 A seção **Webhooks e integrações** guarda os endereços que recebem, por webhook, os avisos do que acontece na empresa. Cada campo recebe um tipo de evento, e alguns só aparecem quando o recurso correspondente está disponível no seu plano.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Webhooks e integrações**.
>
> ➡️ Cole, no campo do tipo de evento que interessa, o endereço do seu sistema que vai receber os avisos.
>
> ➡️ Nos campos que têm o botão **SALVAR** logo abaixo, clique nele para gravar o endereço.

## Os campos, na ordem da tela

🔘 **Eventos de Mensagens Internas**, **Eventos de Usuários**, **Eventos de TAG** e **Eventos de CRM:** os endereços que recebem, por webhook, os eventos de cada tipo.

🔘 **Webhook do PDV (recebe os eventos de pedidos, pagamentos, caixa e estoque):** se disponível no seu plano, o endereço que recebe os eventos do PDV. Nas palavras da tela: *"Deixe em branco para não enviar. O aviso vai assinado com o token da empresa (cabeçalho X-Assinatura-Pdv)."* Grave o endereço no botão **SALVAR**, logo abaixo. Embaixo do botão, a linha **Eventos enviados** lista o nome de cada evento que o endereço recebe, a começar por `pedido-criado`, `pedido-alterado` e `pedido-confirmado`.

🔘 **Webhook de Projetos (recebe os eventos dos projetos, colunas, tarefas e modelos):** se disponível no seu plano, o endereço que recebe os eventos dos projetos. Nas palavras da tela: *"Deixe em branco para não enviar. O aviso vai assinado com o token da empresa (cabeçalho X-Assinatura-Projetos)."* Grave o endereço no botão **SALVAR**, logo abaixo. Embaixo do botão, a tela lista: *"Eventos enviados: projeto-criado, projeto-alterado, projeto-removido, etapa-criada, etapa-alterada, etapa-removida, tarefa-criada, tarefa-alterada, tarefa-removida, tarefa-restaurada, modelo-criado, modelo-alterado, modelo-removido, anexo-adicionado, anexo-removido, comentario-criado, comentario-removido, aviso-ao-cliente-enviado, aviso-ao-cliente-nao-enviado."*

🔘 **Webhook de e-mail (recebe o e-mail que chega e o que sai pelas contas da empresa):** se disponível no seu plano, o endereço que recebe os eventos dos e-mails das contas da empresa. Nas palavras da tela: *"Deixe em branco para não enviar. Só avisa o e-mail recebido com até 48 horas (a caixa antiga não dispara a automação). O aviso vai assinado com o token da empresa (cabeçalho X-Assinatura-Email)."* Grave o endereço no botão **SALVAR**, logo abaixo. Embaixo do botão, a tela lista: *"Eventos enviados: email-recebido, email-enviado, email-excluido, email-arquivado, email-lido, email-nao-lido."*

🔘 **Webhook da avaliação:** se disponível no seu plano, o endereço que recebe os avisos da avaliação dos atendimentos pela IA. Nas palavras da tela: *"Recebe: atendimento-avaliado, avaliacao-falhou, aula-gerada, alerta-da-avaliacao"*. Grave o endereço no botão **SALVAR**, logo abaixo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Os avisos do Webhook do PDV, do Webhook de Projetos e do Webhook de e-mail chegam assinados?** Sim. Pela própria tela, eles vão assinados com o token da empresa, cada um no seu cabeçalho: `X-Assinatura-Pdv`, `X-Assinatura-Projetos` e `X-Assinatura-Email`.
>
> **Onde fica o Token de Validação, que incorpora a tela de um atendimento em outro sistema?** Na mesma aba, seção **Segurança**: menu **Configurações  ›  Opções  ›  Integrações e segurança**.
