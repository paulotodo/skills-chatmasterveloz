# Webhook do Funil

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-funil
- **Categoria:** Recursos
- **Menu:** CRM › Funis do CRM › Webhook do Funil

---

🧩 O webhook do funil avisa outro sistema da sua empresa a cada movimentação: oportunidade criada, mudou de etapa, foi ganha, foi perdida. É assim que um sistema externo — de faturamento, de implantação — fica sabendo da venda sem ninguém digitar nada duas vezes.

Cada aviso é enviado para o endereço configurado no funil, em POST, com os dados em JSON.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **CRM  ›  Funis** e clique em **Novo funil**, ou no ícone **Editar funil** de um funil que já existe.
>
> ➡️ Cole o endereço em **URL do webhook** e clique em **Salvar**.
>
> ➡️ Abra o **Editar funil** de novo e clique em **Gerar segredo**. Guarde o segredo.
>
> ➡️ Clique em **Enviar teste** e confira em **Últimas entregas**.

## Configurar o endereço

🔘 **URL do webhook:** o endereço que recebe os avisos. Vazio, o funil não envia nada.

⚠️ Os botões de segredo e de teste só aparecem depois que o funil é salvo — a tela avisa: *"Salve o funil para poder gerar segredo e testar."*

## Segredo e assinatura

🔘 **Gerar segredo:** cria uma senha que o seu sistema usa para conferir que o aviso veio mesmo da plataforma. Ela aparece **uma vez só** — *"Guarde agora: este segredo não será mostrado de novo."*

🔘 **Trocar segredo:** cria um segredo novo na hora, sem pedir confirmação. Daí em diante, as assinaturas usam o segredo novo — atualize o seu sistema.

Com o segredo gerado, cada aviso leva um cabeçalho de assinatura cujo valor começa com `sha256=`. É o HMAC-SHA256 do corpo recebido, calculado com o segredo como chave. O seu sistema refaz a conta e compara: se bater, o aviso é legítimo. Para ver o nome exato do cabeçalho, use **Enviar teste** e olhe o que chegou. Sem segredo, os avisos chegam sem assinatura.

## Os avisos enviados

O campo `evento` do JSON diz o que aconteceu:                                                                  

| Evento | Quando é enviado |
|---|---|
| `CREATED` | oportunidade criada |
| `LANE_CHANGED` | mudou de etapa — vem junto com os eventos de ganho, perda, devolução e reprovação na auditoria |
| `WON` | venda ganha |
| `LOST` | venda perdida |
| `REOPENED` | venda ganha ou perdida devolvida ao funil |
| `VALUE_CHANGED` | valor alterado |
| `OWNER_CHANGED` | responsável trocado |
| `ENCADEADA` | a venda abriu uma oportunidade em outro funil |
| `AUDIT_PENDING` | venda ganha num funil com auditoria — entrou na fila de conferência |
| `AUDIT_APPROVED` | venda aprovada na auditoria — passa a contar |
| `AUDIT_REJECTED` | venda reprovada na auditoria — volta para a etapa de antes |
| `DELETED` | oportunidade excluída: foi para **Excluídas** |
| `RESTORED` | oportunidade restaurada de **Excluídas** |
| `TESTE` | botão **Enviar teste** |

Em funil com **Exigir auditoria da venda**, a venda ganha manda `AUDIT_PENDING` junto com o `WON` e o `LANE_CHANGED`. Aprovada, ela manda só o `AUDIT_APPROVED`. Reprovada, manda `AUDIT_REJECTED` e o `LANE_CHANGED` da volta para a etapa.

**Excluir de vez** não envia aviso: o último que o seu sistema recebe daquela oportunidade é o `DELETED` de quando ela foi para **Excluídas**.

## O que vai em cada aviso

➡️ **evento** e **ocorridoEm**, a data e hora.

➡️ **funil**, com número e nome.

➡️ **oportunidade**: número, valor, status (`OPEN`, `WON` ou `LOST`), etapa, contato e responsável.

➡️ **de** e **para**: a etapa anterior e a nova. No `DELETED` só **de** vem preenchido, com a etapa em que a oportunidade estava; no `RESTORED`, só **para**, com a etapa em que ela voltou.

➡️ **valorAntes** e **valorDepois**.

➡️ **observacao** — no `ENCADEADA`, o funil e o número da oportunidade criada.

➡️ **autor**: quem fez a movimentação.

⚠️ O contato vai com nome, número e e-mail. Configure só endereços do seu próprio sistema.

O motivo da perda não vai no aviso.

## Testar e acompanhar

🔘 **Enviar teste:** manda um aviso `TESTE` e mostra se foi entregue. Usa a URL **salva** — trocou o endereço, salve antes de testar.

🔘 **Últimas entregas:** cada aviso com o evento, a situação (**entregue** ou **falhou**), o código de resposta do seu sistema e a hora. **Atualizar** recarrega a lista. A quantidade de falhas aparece ao lado do título **Webhook**, como *1 falha(s)*.

🔘 **Reenviar:** aparece nos avisos que falharam.

Quando a entrega falha, a plataforma tenta de novo sozinha: depois de 5 minutos, de 15 minutos e mais duas vezes de hora em hora — 5 tentativas no total, em pouco mais de duas horas. A linha mostra quantas já foram feitas.

⚠️ Depois da 5ª tentativa, a plataforma para, e a tela não avisa: a linha continua como **falhou**, com *5 tentativas*. Daí em diante, o aviso só chega pelo **Reenviar**.

⚠️ Trocou a URL? O **Reenviar** e as novas tentativas passam a usar o endereço novo. Os avisos que falharam antes ainda podem chegar: clique em **Reenviar** em cada um.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Excluir uma oportunidade avisa o meu sistema pelo Webhook do Funil?** Sim. Quando a oportunidade vai para **Excluídas**, o funil envia `DELETED`; quando ela é restaurada, `RESTORED`. O **Excluir de vez** não envia aviso.
>
> **Corrigi a URL. Os avisos que falharam antes se perdem?** Não. Clique em **Reenviar** em cada um: o reenvio vai para o endereço atual do funil.
>
> **Meu sistema ficou fora do ar por algumas horas. Os avisos chegam sozinhos?** Os que ainda estavam dentro das 5 tentativas chegam quando o sistema voltar. Os que já tinham esgotado as 5 — pouco mais de duas horas depois da primeira falha — só chegam se você clicar em **Reenviar** em **Últimas entregas**.
>
> **Não aparecem os botões Gerar segredo e Enviar teste.** A tela avisa: *"Salve o funil para poder gerar segredo e testar."*

> **[ERROS]**
>
> #### Erros Comuns
>
> **O teste não foi entregue:** o seu sistema respondeu com erro, e o código aparece na mensagem e em **Últimas entregas**. **Solução:** confira se o endereço está no ar e aceita POST com JSON.
>
> **O reenvio falhou:** o seu sistema voltou a responder com erro ao **Reenviar**. **Solução:** confira se o endereço está no ar e aceita POST com JSON, e clique em **Reenviar** de novo.
