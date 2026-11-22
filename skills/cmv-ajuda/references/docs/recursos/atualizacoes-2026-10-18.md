# 18/10/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-18
- **Categoria:** Recursos
- **Menu:** Atualizações › Outubro 2026 › 18/10/2026

---

🧩 Atualizações de 18 de outubro de 2026.

#### Novidades

⚡️ **Saída Sem resposta:** no FlowBuilder Nativo, os blocos Pergunta, Menu, Botões, Avaliação, IA e Typebot ganham um tempo de espera e a saída Sem resposta, para quem parou de responder.

⚡️ **Rodízio por integração:** um sistema externo envia o atendimento e o rodízio cadastrado escolhe o operador, com a mesma regra dos fluxos. Pela integração também dá para listar os rodízios, com nome e situação, e redistribuir um atendimento que já tem responsável, sem duplicar a entrega.

⚡️ **Respostas Rápidas pela API:** crie e consulte respostas rápidas gerais, por Setor ou individuais, como na tela.

⚡️ **Fluxos pela API:** crie um fluxo completo em uma única chamada, inclusive a partir de um fluxo exportado.

⚡️ **Setores pela API:** crie Setores já com horários e mensagens, sem precisar enviar campos opcionais.

⚡️ **Usuários pela API:** edite um usuário mudando só o que precisa, sem perder as permissões configuradas.

## Saída Sem resposta

No bloco **Pergunta**, o campo **Sem resposta: seguir pela saída depois de (minutos)** define quanto tempo esperar. Com minutos, o bloco ganha a saída **Sem resposta**: ligue essa saída ao próximo passo de quem não responder nesse tempo, como um rodízio de outra equipe. Vazio ou 0 desliga.

🔘 **Conta da última mensagem:** o tempo da saída Sem resposta conta a partir da última mensagem do cliente, para que ninguém seja redirecionado enquanto ainda está conversando.

🔘 **Cancela sozinha:** a espera termina quando o atendimento é aceito, encerrado ou segue no fluxo.

🔘 **Nos outros blocos:** a mesma saída vale para Menu, Botões, Avaliação, IA e Typebot.

#### O que você precisa fazer

Nada exige ação: tudo continua funcionando como antes.

➡️ Para usar a saída Sem resposta, defina os minutos no campo **Sem resposta** do bloco Pergunta, no menu **FlowBuilder Nativo**.
