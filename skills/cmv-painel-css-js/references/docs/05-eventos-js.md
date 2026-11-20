<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.141.0 -->

# Eventos que o JS pode ouvir

Formato: um título `###` por **Evento** (2 itens), com os campos Onde · Quando · `detail` abaixo.

### `sip:state`

- **Onde:** `window`
- **Quando:** a cada mudança do ramal ou da chamada (o mesmo instante em que o `<body>` muda)
- **detail:** `registration` · `call` · `direction` (`inbound` · `outbound` · `null`) · `muted` · `onHold` · `number` · `ticketId`

### `atendimentos:buscado`

- **Onde:** `window`
- **Quando:** quando a busca da Pesquisar termina — a do botão Buscar e a de cada página, com a tabela nova já na tela (a exportação para CSV não dispara)
- **detail:** `pagina` · `total` (o total do filtro) · `quantidade` (quantos vieram nesta página) · `erro` (`true` quando a busca falhou)

```js
window.addEventListener("sip:state", e => console.log(e.detail.call, e.detail.number));
window.addEventListener("atendimentos:buscado", e => console.log(e.detail.total, e.detail.erro));
```

Sem ele, o JS personalizado dependia de um MutationObserver vigiando a janela da chamada.
