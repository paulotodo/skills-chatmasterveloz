# Habilitar Webhook Administrativo

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/habilitar-webhook-administrativo
- **Categoria:** APIs
- **Menu:** Webhooks Administrativos › Habilitar Webhook Administrativo

---

🧩 O Webhook Administrativo é ligado num campo só, e a mesma URL recebe os dois eventos — alteração de conexão e criação de empresa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Plataforma**, seção **Configurações Globais**.
>
> ➡️ Preencha o campo **Webhook de Eventos [Conexões]** com o endereço que vai receber os avisos.
>
> ➡️ Esse endereço precisa aceitar **POST** com corpo em JSON.
>
> ⚠️ **Endereço preenchido e fora do ar pode interromper a plataforma inteira.** Enquanto houver URL nesse campo, todo evento tenta a entrega — e um destino que não responde afeta todas as empresas, não só a que gerou o evento. Se o seu receptor for sair do ar, **esvazie o campo antes**.

## Como testar sem esperar um evento

Reiniciar as conexões provoca o evento de alteração de status, que é o caminho mais rápido de conferir se o seu receptor está recebendo.

➡️ Acesse o menu **Conexões** e use **Reiniciar Conexões**.

➡️ O seu endereço deve receber um aviso para cada conexão reiniciada.

Se não chegar nada, o problema está no receptor ou no endereço digitado — a plataforma não guarda os avisos que não conseguiu entregar.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso usar um endereço diferente para cada evento?** Não. O campo é um só, e os dois tipos de aviso vão para ele. A separação é feita do seu lado, pelo conteúdo que chega.
>
> **O aviso é reenviado se o meu sistema estiver fora do ar na hora?** Não conte com isso. Trate cada aviso como entrega única e registre o que receber.
