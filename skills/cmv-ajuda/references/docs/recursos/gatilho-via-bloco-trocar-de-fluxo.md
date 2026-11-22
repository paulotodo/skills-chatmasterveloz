# Gatilho via Bloco Trocar de Fluxo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-bloco-trocar-de-fluxo
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Pontos de Entrada (Gatilho) › Gatilho via Bloco Trocar de Fluxo

---

🧩 O **Gatilho via Bloco Trocar de Fluxo** é o ponto de entrada em que um fluxo passa o cliente para outro. Isso permite ligar fluxos diferentes, criando uma estrada por onde o cliente segue sem perceber que trocou de fluxo.

☑️ **Organização por assunto:** em vez de um fluxo gigante, fluxos menores, um para triagem, um para o financeiro, um para o suporte, ligados uns aos outros.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Ligue o fluxo de destino a um Setor, no cadastro do Setor.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo de origem e use o bloco **Trocar Fluxo** escolhendo esse Setor.

## Como configurar a troca de fluxo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Trocar Fluxo**

O bloco pede um Setor e inicia o fluxo ligado a ele. A lista mostra só os Setores que têm um fluxo ligado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual o comportamento padrão do bloco Trocar Fluxo?** Iniciar o fluxo ligado ao Setor escolhido. Para isso, o atendimento é levado ao **Aguardando**, caso não esteja, para a automação rodar.
>
> **O cliente percebe a troca de fluxo?** Não. Para o cliente, a conversa continua normalmente.
>
> **Posso criar um loop infinito trocando de fluxo?** Pode, e é perigoso. Se o fluxo A manda para o B e o B manda para o A sem nenhuma condição de parada, o cliente fica preso num laço de mensagens.
>
> **Por que o meu Setor não aparece no bloco Trocar Fluxo?** Porque esse Setor não tem um fluxo ligado a ele.
>
> **O Trocar Fluxo funciona igual ao bloco Setor?** Não. Os dois pedem um Setor, mas o bloco **Setor** deixa o atendimento parado esperando a equipe, mesmo que o Setor tenha fluxo. O **Trocar Fluxo** inicia o fluxo ligado ao Setor.
