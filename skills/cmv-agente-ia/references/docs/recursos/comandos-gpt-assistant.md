# Comandos GPT Assistant

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/comandos-gpt-assistant
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant › Comandos GPT Assistant

---

Em seu GPT Assistant você pode utilizar **comandos** para ativar ações em nossa plataforma.

Veja abaixo uma lista de **comandos e suas acões,** seguido de um exemplo prático para colocar em seu prompt:

> **[DICA]**
>
> #### Dica
>
> Escreva em seu prompt uma recomendação para a IA manter o código no texto enviado.
>
> ##### - Transferir Fila
>
> ```
> #{"queueId": "544"}
> ```
>
> Se a pessoa quiser sobre suporte técnico ou qualquer tema relacionado a suporte, você deve dizer exatamente esse texto: Transferindo para o #{“queueId”: “544”} setor de Suporte.
>
> ##### - Transferir para Operador
>
> ```
> #{"queueId": "544", "userId":"3"}
> ```
>
> Se a pessoa disser “quero falar com o João”, você deve dizer exatamente esse texto: Transferindo para o #{“queueId”: “544”, “userId”:”3″} João.
>
> ##### - Atribuir Tag
>
> ```
> #{"tagId": "71"}
> ```
>
> Se a pessoa disser “gostaria de saber sobre notebook”, ou qualquer tema relacionado ao interesse em notebook, você deve dizer exatamente esse texto: Legal, temos diversas opções de #{“tagId”:”71″} Notebook.
>
> ##### - Remover Tag
>
> ```
> #{"removeTag": "71"}
> ```
>
> Se a pessoa disser “pode cancelar minha consulta”, ou algo que demonstre o interesse em cancelar um agendamento, você deve dizer exatamente esse texto: ok, sua consulta foi #{“removeTag”:”71″} cancelada.
>
> ##### - Encerrar Ticket
>
> ```
> #{"closeTicket": "1"}
> ```
>
> Se você entender que todas as pendências foram finalizadas, que não há dúvidas, e que o cliente não deseja mais conversar, você deve dizer exatamente esse texto: Estou encerrando nosso #{“closeTicket”:”1″} ticket agora, mas fico a disposição se precisar de algo no futuro.
