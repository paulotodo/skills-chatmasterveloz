# Aba Integrações em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-integracoes-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Integrações em Cadastros do Consultório

---

🧩 A aba **Integrações** cria as chaves que deixam um sistema de fora mexer na agenda da clínica: o atendente de IA que marca consultas pela conversa, ou o sistema da própria clínica. Cada integração tem a sua chave, que faz só o que os escopos dela permitem e pode ser revogada sozinha.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Integrações**.
>
> ➡️ Escreva o **Nome da integração**, marque os **Escopos** e clique em **Criar chave**.
>
> ➡️ Copie a chave na janela que abre e guarde no sistema da integração.

## Os campos

🔘 **Nome da integração:** como *atendente-ia*. Ele aparece nas consultas marcadas por essa integração e nos avisos do webhook.

🔘 **Escopos:** o que a chave pode fazer.  
- **Atendente** — o que o paciente faz: ver os horários, marcar, achar, confirmar, cancelar e remarcar as consultas do contato da conversa;
- **Clínica** — tudo, sem pedir o contato: também falta, atendimento e encaixe. Para o sistema da própria clínica;
- **Pacientes** — ver, criar e ligar a ficha do paciente ao contato.

O **Criar chave** só libera com o nome e ao menos um escopo.

⚠️ A chave aparece uma vez só. Nas palavras da tela: *"Copie a chave agora: ela não aparece de novo. Guarde-a no sistema da integração, no cabeçalho Authorization: Bearer."*

## A lista de chaves

Cada chave aparece com o nome, os escopos, o começo da chave e o **Último uso** — **Nunca usada** enquanto ninguém a usou —, e o botão **Revogar**.

🔘 **Revogar:** pede confirmação — *"A integração que usa esta chave para de funcionar na hora. Não dá para desfazer: para voltar, crie uma chave nova."* A chave fica na lista como **Revogada em**, com a data.

## O que mais vale para a integração

➡️ O profissional e o serviço só aceitam marcação de fora com **Aceita marcação pela API (atendente de IA)** marcado nos cadastros deles.

➡️ A antecedência e os dias à frente da marcação de fora ficam na aba **Marcação**, e cada serviço pode ter a regra dele.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Perdi a chave da integração. Consigo ver de novo?** Não. A chave aparece uma vez só, na criação. Crie uma chave nova e revogue a antiga.
>
> **Qual escopo dou para o atendente de IA que marca consultas pela conversa?** **Atendente**: ele mexe só nas consultas do contato da conversa, como o próprio paciente faria. **Clínica** é para o sistema da própria clínica, sem a exigência do contato.
>
> **A integração parou de funcionar depois que revoguei a chave.** É o esperado: a chave revogada para na hora, e não há como desfazer. Crie outra chave para a integração.
