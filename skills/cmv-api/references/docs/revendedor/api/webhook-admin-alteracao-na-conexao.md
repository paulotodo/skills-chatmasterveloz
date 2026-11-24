# Alteração na Conexão

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/webhook-admin-alteracao-na-conexao
- **Categoria:** APIs
- **Menu:** Webhooks Administrativos › Alteração na Conexão

---

🧩 Este aviso chega toda vez que uma conexão de qualquer empresa muda de status. É com ele que se monta o monitoramento: saber que um número caiu no momento em que cai, sem ninguém olhando a lista de conexões.

Para receber, o endereço precisa estar cadastrado no campo **Webhook de Eventos [Conexões]**, no menu **Configurações  ›  Plataforma**, seção **Configurações Globais**.

## Os status possíveis

◽ **connected** — a conexão está no ar.

◽ **disconnected** — a conexão caiu. É o status que vem acompanhado de um código explicando o motivo.

◽ **pending** — a conexão está em processo de subir.

◽ **qrcode** — a conexão está esperando a leitura do QR Code.

## Os códigos do status disconnected

O campo `event` diz por que a conexão caiu:

◽ `401` — dispositivo desconectado (logado em outro dispositivo).

◽ `402` — banido temporariamente.

◽ `403` — banido permanentemente.

◽ `408` — conexão expirada ou perdida.

◽ `411` — desalinhamento de multi-dispositivos.

◽ `428` — conexão fechada.

◽ `440` — conexão substituída por outra.

◽ `500` — sessão corrompida.

◽ `515` — necessário reiniciar.

⚠️ Os códigos `402` e `403` são os que exigem ação sua, não do cliente: o número foi banido pelo WhatsApp, e reconectar não resolve.

## O que vem no aviso

```json
{
  "headers": {
    "host": "go.dominio.com.br",
    "content-length": "88",
    "content-type": "application/json",
    "x-forwarded-for": "203.0.113.42",
    "x-forwarded-host": "go.dominio.com.br",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https",
    "x-forwarded-server": "traefik_traefik.1",
    "x-real-ip": "203.0.113.42",
    "accept-encoding": "gzip"
  },
  "params": {},
  "query": {},
  "body": {
    "whatsappId": 22,
    "companyId": 12,
    "event": "200",
    "status": "connected",
    "channel": "whatsapp",
    "company": {
      "id": 2,
      "name": "Minha Empresa"
    },
    "backendURL": "https://backend.dominio.com.br"
  },
  "webhookUrl": "https://go.dominio.com.br/webhookadmin",
  "executionMode": "production"
}
```

O que interessa está em `body` — o resto é o envelope que a ferramenta de automação acrescenta ao registrar a chamada.

◽ `whatsappId` — o identificador da conexão que mudou de status. É por ele que o seu sistema sabe de qual número se trata.

◽ `companyId` — o identificador da empresa dona da conexão.

◽ `event` — o código do evento. No status **disconnected** ele traz um dos motivos da lista acima; no exemplo, o status é **connected** e o código é `200`.

◽ `status` — o novo status da conexão, entre os quatro possíveis.

◽ `channel` — o canal da conexão.

◽ `company` — o identificador e o nome da empresa, repetidos por conveniência para quem monta alerta legível.

◽ `backendURL` — o endereço do backend da instância que disparou o aviso. Útil para quem administra mais de uma.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Recebo um aviso por conexão ou um por empresa?** Um por conexão. Uma empresa com cinco números gera cinco avisos quando as cinco reiniciam.
>
> **O código 200 está na lista de motivos?** Não. A lista cobre o status **disconnected**; `200` é o que aparece quando a conexão sobe.
