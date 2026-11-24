# Criação de Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/webhook-admin-criacao-de-empresa
- **Categoria:** APIs
- **Menu:** Webhooks Administrativos › Criação de Empresa

---

🧩 Este aviso chega toda vez que uma empresa nova é cadastrada na plataforma, venha o cadastro de você ou da própria pessoa pela tela de registro. É o gancho para colocar o cliente novo no seu CRM, no seu financeiro ou numa esteira de boas-vindas sem ninguém digitar nada.

Para receber, o endereço precisa estar cadastrado no campo **Webhook de Eventos [Conexões]**, no menu **Configurações  ›  Plataforma**, seção **Configurações Globais**.

## O que vem no aviso

```json
{
  "event": "new_company",
  "company": {
    "document": "",
    "id": 91,
    "name": "teste webhook empresa",
    "phone": "5511999999999",
    "namecomplete": "teste webhook",
    "pais": "BR",
    "indicator": null,
    "email": "teste@webhook.empresa",
    "status": true,
    "planId": 2,
    "dueDate": "2027-05-16T20:21:05.000Z",
    "recurrence": "MENSAL",
    "importar": false,
    "typebotName": "",
    "typebotUrl": "",
    "iframeUser": "",
    "iframeUserUrl": "",
    "iframeAdmin": "",
    "iframeAdminUrl": "",
    "blockGroups": false,
    "updatedAt": "2027-05-10T20:21:34.740Z",
    "createdAt": "2027-05-10T20:21:34.740Z",
    "schedules": [],
    "lastLogin": null,
    "paymentMethod": "",
    "messageCount": "",
    "keystorage": "postgres",
    "apiUsada": "postgres",
    "iframeUserUrlB": "",
    "iframeUserB": ""
  }
}
```

O aviso traz o cadastro inteiro da empresa. Os campos que costumam interessar a quem integra:

◽ `event` — vem sempre como `new_company`. É por ele que o seu sistema distingue este aviso do de alteração de conexão, já que os dois chegam no mesmo endereço.

◽ `company.id` — o identificador da empresa na plataforma. É a chave para amarrar o cadastro dela do seu lado.

◽ `company.name` — o nome da empresa, o mesmo que aparece no card.

◽ `company.email` e `company.phone` — o contato do cadastro. O telefone é o que recebe os lembretes de cobrança por WhatsApp, quando ativados.

◽ `company.namecomplete` — o nome da pessoa responsável.

◽ `company.document` — o CPF ou CNPJ, quando informado. Vem vazio se o cadastro não pediu.

◽ `company.indicator` — quem indicou a empresa, quando houve indicação. É o campo para medir programa de indicação.

◽ `company.planId` — o plano com que a empresa nasceu.

◽ `company.dueDate` e `company.recurrence` — o primeiro vencimento e a periodicidade da cobrança.

◽ `company.status` — se a empresa já nasce com acesso liberado.

Os demais campos são configurações internas da empresa recém-criada e costumam vir vazias num cadastro novo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como separo este aviso do de alteração de conexão, se os dois chegam na mesma URL?** Pelo campo `event`: aqui ele vem como `new_company`, e no aviso de conexão ele traz um código numérico junto de um `status`.
>
> **O aviso chega quando eu cadastro a empresa, ou só quando ela se cadastra sozinha?** Nos dois casos — o gatilho é a criação do cadastro, não o caminho por onde ele entrou.
