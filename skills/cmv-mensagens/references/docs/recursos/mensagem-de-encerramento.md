# Mensagem de Encerramento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mensagem-de-encerramento
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Mensagem de Encerramento

---

🧩 **A Mensagem de Encerramento** é uma resposta automática disparada no exato momento em que o atendente finaliza o ticket (conversa) com o cliente. Ela funciona como um "tchau" oficial, garantindo que o cliente saiba que o atendimento foi concluído com sucesso.

☑️ **Padronização:** Garante que todos os clientes recebam a mesma despedida cordial, mantendo a qualidade e o tom de voz da sua empresa, independentemente de qual atendente prestou o suporte.

☑️ **Agilidade:** O atendente não precisa perder tempo digitando "Obrigado por entrar em contato, qualquer dúvida estamos à disposição" dezenas de vezes por dia. Um clique resolve tudo.

☑️ **Experiência do Cliente:** Transmite profissionalismo e finaliza o ciclo de comunicação de forma educada e clara.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ A mensagem padrão da **conexão** é configurada em Conexões Editar Mensagens Mensagem de Conclusão
>
> ➡️ A mensagem pessoal do **atendente** é configurada em Perfil Mensagem de Despedida
>
> ➡️ A mensagem do **Perfil do atendente tem prioridade** e substitui a da Conexão, mas só funciona se a mensagem da Conexão também estiver preenchida.
>
> ➡️ Na tela de chat, ao fechar um ticket, clique na opção **“Resolver Com Mensagem de Encerramento”**.

## Como configurar a Mensagem de Encerramento

O sistema possui duas camadas para essa mensagem: uma global (para a conexão) e uma individual (para cada atendente).

### 💬 Na Conexão

Esta é a mensagem de encerramento base. Ela é enviada para todos os clientes, a menos que o atendente crie uma mensagem própria.

- em → Conexões > Editar > Mensagens > Mensagem de Conclusão

🔘 **Mensagem de Conclusão:** Digite o texto padrão de encerramento da empresa.  
- *Exemplo:* "Agradecemos o seu contato! Seu atendimento foi encerrado. Caso precise de algo mais, basta nos chamar novamente."

### 💬 No Perfil

Se um atendente quiser ter uma despedida própria, ele pode criar uma mensagem individual.

- em → Perfil > Mensagem de Despedida

🔘 **Mensagem de Despedida:** Digite o texto personalizado do usuário.  
- *Exemplo:* "Aqui é o João, foi um prazer te atender hoje! Estou encerrando este chamado. Um excelente dia para você!"

> **[ATENCAO]**
>
> #### Atenção
>
> A mensagem do **Perfil do atendente tem prioridade** e substitui a da Conexão, mas só funciona se a mensagem da Conexão também estiver preenchida.

## Como utilizar a Mensagem de Encerramento

Na tela de chat, ao clicar para finalizar o atendimento, o sistema perguntará como você deseja encerrar:  
- **"Resolver Sem Mensagem de Encerramento"**: O ticket é fechado silenciosamente (útil para mensagens de spam ou conversas que não exigem despedida).
- **"Resolver Com Mensagem de Encerramento"**: O sistema fecha o ticket e dispara automaticamente a mensagem configurada (escolha sempre esta opção para um atendimento formal).

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Eu preenchi as duas mensagens (Conexão e Perfil). Qual será enviada ao cliente?** O sistema sempre dará **prioridade à mensagem do Perfil**. Se o atendente "João" tem uma mensagem configurada no Perfil dele, o cliente receberá o texto do João, ignorando o texto geral da Conexão.
>
> **Posso usar apenas a mensagem do Perfil e apagar a da Conexão?** Não! Para que a mensagem do Perfil funcione, o campo "Mensagem de Conclusão" lá na Conexão **precisa** estar preenchido. A conexão precisa ter uma mensagem base para liberar a funcionalidade.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Deixar a mensagem da Conexão vazia e preencher só a do Perfil:** O atendente cria uma mensagem no próprio perfil, atende o cliente, clica em "Resolver Com Mensagem", mas o cliente não recebe nada. Isso acontece porque o administrador esqueceu de preencher o texto base no menu Conexões.
>
> **Clicar no botão errado por pressa:** O atendente clica instintivamente em "Resolver *Sem* Mensagem" para fechar o chat rápido.
>
> **Colocar perguntas na Mensagem de Encerramento:** Escrever textos como "Seu chamado foi encerrado, ficou alguma dúvida?". Se o cliente responder "Sim", o bot abrirá um *novo ticket* imediatamente, gerando retrabalho. A mensagem de encerramento deve ser uma afirmação final, sem instigar o cliente a continuar a conversa.
