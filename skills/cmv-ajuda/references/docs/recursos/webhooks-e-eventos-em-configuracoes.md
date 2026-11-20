# Webhooks e Eventos em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhooks-e-eventos-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Webhooks e Eventos em Configurações

---

🧩 A seção **Webhooks | Eventos** junta três coisas diferentes: a versão do CRM que a empresa usa, o token que permite incorporar um atendimento em outro sistema, e os endereços que recebem eventos da plataforma.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e localize **Webhooks | Eventos**.
>
> ➡️ É aqui — e não em Configurações de Sistema — que fica a **Versão do CRM**.

## Os campos, na ordem da tela

🔘 **Versão do CRM:** escolhe qual CRM a empresa usa — **v1 — funil único** ou **v2 — múltiplos funis**. Trocar não move dado nenhum: cada versão tem as suas próprias tabelas, e dá para voltar. A versão nova abre vazia, e a tela de Funis tem um botão para importar o conteúdo da anterior.

🔘 **Token de Validação (incorporar atendimento):** com um token preenchido, a tela de um atendimento pode ser incorporada em outro sistema por iframe, no endereço `/embed/ticket/{id}?token=SEU_TOKEN&userId=ID_DO_OPERADOR`. No lugar de `{id}` vai o número do ticket, e no lugar de `ID_DO_OPERADOR`, o **ID** que aparece no card da pessoa, no menu **Equipe**.

**GERAR:** cria um token novo e já grava, sem botão de salvar. **O token anterior para de funcionar na hora**, e todo link montado com ele passa a ser recusado. Com o campo vazio, o recurso fica desligado.

⚠️ **Trate o Token de Validação como senha:** ele dá acesso às conversas da empresa.

🔘 **Eventos de Mensagens Internas**, **Eventos de Usuários**, **Eventos de TAG** e **Eventos de CRM:** os endereços que recebem, por webhook, os eventos de cada tipo.

⚠️ A troca de **Versão do CRM** vale para a empresa inteira e é imediata. Numa conta com CRM em uso, a equipe abre o menu e encontra o quadro vazio até a importação — combine antes de trocar.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Onde troco o CRM para a versão de múltiplos funis?** Aqui, em **Versão do CRM**. Depois disso o menu CRM ganha **Funis** e o quadro passa a se chamar **Board**.
>
> **Trocar de versão apaga o que já existe?** Não. Cada versão guarda os dados separadamente, e voltar para a anterior devolve o funil como estava.
