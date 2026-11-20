# Webhook de Projetos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-de-projetos
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook de Projetos

---

🧩 Quer que o seu sistema saiba na hora que um projeto nasceu, que uma tarefa mudou ou que um modelo foi alterado? O **Webhook de Projetos** avisa o seu sistema a cada evento dos projetos, das etapas, das tarefas e dos modelos de projeto.

O **Webhook de Projetos** cobre só os projetos. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e desça até a seção **Projetos**.
>
> ➡️ Preencha o endereço do seu sistema no campo **Webhook de Projetos**.

## Onde ligar o Webhook de Projetos

🔘 **Webhook de Projetos (recebe os eventos dos projetos, colunas, tarefas e modelos):** o endereço que recebe todos os eventos de projetos da empresa. Em branco, nada é enviado. O botão **Salvar**, ao lado do campo, grava o endereço, e a tela avisa *"Webhook de Projetos salvo."*

O endereço precisa começar com http:// ou https://, sem espaços, e não pode apontar para a rede interna.

## Os eventos do Webhook de Projetos

Tudo chega no mesmo endereço. Os eventos enviados são estes:                          

| Evento | O que aconteceu |
|---|---|
| `projeto-criado` · `projeto-alterado` · `projeto-removido` | um projeto nasceu, mudou ou foi apagado |
| `etapa-criada` · `etapa-alterada` · `etapa-removida` | uma etapa (coluna do quadro do projeto) foi criada, mudou ou foi apagada |
| `tarefa-criada` · `tarefa-alterada` · `tarefa-removida` | uma tarefa de projeto foi criada, mudou ou foi apagada |
| `modelo-criado` · `modelo-alterado` · `modelo-removido` | um modelo de projeto foi criado, mudou ou foi apagado |

## O que chega em cada aviso

Cada aviso chega por **POST**, em JSON:

🔘 `acao`: o evento, como `tarefa-alterada`.

🔘 `companyId`, `origem`, `enviadoEm`, com a hora do envio, e `backendURL`, o endereço da plataforma.

🔘 O que mudou: `projeto`, `etapa`, `tarefa` ou `modelo`, conforme o evento. O `projeto-criado` traz também as `etapas`, as `tarefas` e a `equipe` do projeto; a `tarefa-alterada` traz em `antes` o projeto, a etapa e a situação de antes da mudança; o `projeto-removido` traz em `tarefasSoltas` quantas tarefas ficaram sem projeto.

A tarefa concluída chega como `tarefa-alterada`, com o `status` em `completed`; reaberta, o `status` volta a `pending`.

Exemplo de `tarefa-alterada`, com a tarefa chegando à etapa que fecha a tarefa:

```json
{
  "acao": "tarefa-alterada",
  "companyId": 2,
  "tarefa": {
    "id": 32,
    "title": "Instalar o equipamento",
    "description": "",
    "status": "completed",
    "priority": "medium",
    "dueDate": "2026-11-20T12:00:00.000Z",
    "assignedTo": 16,
    "responsaveis": [16],
    "createdBy": 11,
    "projetoId": 14,
    "etapaId": 51,
    "checklist": []
  },
  "antes": { "projetoId": 14, "etapaId": 48, "status": "pending" },
  "origem": "painel",
  "enviadoEm": "2026-11-05T09:21:12.346Z",
  "backendURL": "https://api.exemplo.com.br"
}
```

## Como saber que o aviso veio daqui

Todo aviso do **Webhook de Projetos** traz o cabeçalho `X-Projetos-Evento`, com o evento, e vai assinado com o **Token da Empresa** no cabeçalho `X-Assinatura-Projetos`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook de Projetos avisa as mensagens dos clientes?** Não. O **Webhook de Projetos** cobre só os eventos dos projetos. As mensagens dos clientes são avisadas pelos webhooks da Conexão e do Setor.
>
> **O Webhook de Projetos avisa quando um modelo de projeto muda?** Sim. Criar, alterar e apagar um modelo de projeto enviam `modelo-criado`, `modelo-alterado` e `modelo-removido`.
>
> **Como sei pelo webhook que uma tarefa de projeto foi concluída?** Chega a `tarefa-alterada` com o `status` em `completed`, e o `antes` mostra a etapa e a situação de antes.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Webhook de Projetos inválido:** ao salvar, a tela avisa *"Webhook de Projetos inválido: use um endereço http:// ou https://, sem espaços, fora da rede interna."* **Solução:** use o endereço público do seu sistema, começando com http:// ou https://, sem espaço no meio.
