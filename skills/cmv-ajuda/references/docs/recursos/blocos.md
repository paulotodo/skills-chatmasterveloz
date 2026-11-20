# Blocos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/blocos
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos

---

🧩 Cada etapa de um fluxo é um **bloco**: uma peça que faz uma coisa só, como enviar uma mensagem, esperar a resposta do cliente, guardar um dado, decidir o próximo passo ou entregar o atendimento a alguém.

O fluxo é a sequência desses blocos, ligados por linhas no editor. Adicionar, editar, ligar, duplicar e excluir funcionam do mesmo jeito em todos eles; o que muda de um bloco para outro é a janela de configuração e as saídas que ele tem.

## Os tipos de bloco

Cada artigo de bloco traz uma ou mais etiquetas, que dizem o tipo de trabalho que ele faz:

⚡ **Mensagem** — envia algo ao cliente: texto, mídia, botões, um menu ou um template.

⚡ **Dados** — trabalha nos bastidores: guarda respostas em variáveis, coloca ou tira tags, registra notas que só a equipe vê.

⚡ **Roteador** — decide por qual caminho o fluxo segue: pela resposta do cliente, pelas tags, pelo horário ou por sorteio.

⚡ **Integração** — conversa com outros sistemas, como APIs externas e plataformas de pagamento.

⚡ **Financeiro** — trata de cobranças.

⚡ **Atendimento** — entrega a conversa a um Setor, a um atendente ou a um robô.

⚡ **Finalização** — encerra o fluxo ou o atendimento, ou passa a conversa adiante de vez.

## Canais e saídas

Alguns blocos funcionam só em certos canais de conexão, porque dependem de recursos que só existem neles. O artigo de cada bloco diz onde ele funciona e o que acontece nos outros canais.

Cada bloco tem as saídas que o trabalho dele pede: uma só para seguir em frente, duas para um sim ou não, várias para cada caminho possível. Saída sem ligação é um ponto onde a conversa para.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Um bloco pode ter mais de uma etiqueta?** Pode. Um menu, por exemplo, envia as opções ao cliente e também decide o caminho pela escolha dele, por isso é **Mensagem** e **Roteador**.
>
> **O que acontece quando o cliente chega a uma saída de bloco sem ligação?** O fluxo para ali e o cliente fica sem resposta. Use o **Verificar**, na barra do editor, para achar esses pontos antes de salvar.
