<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-29.930.0 -->

# Eventos que o JS pode ouvir

| Evento | Onde | Quando | `detail` |
|---|---|---|---|
| `sip:state` | `window` | a cada mudança do ramal ou da chamada (o mesmo instante em que o `<body>` muda) | `registration` · `call` · `direction` (`inbound` · `outbound` · `null`) · `muted` · `onHold` · `number` · `ticketId` |

```js
window.addEventListener("sip:state", e => console.log(e.detail.call, e.detail.number));
```

Sem ele, o JS personalizado dependia de um MutationObserver vigiando a janela da chamada.
