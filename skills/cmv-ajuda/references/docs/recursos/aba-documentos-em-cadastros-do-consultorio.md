# Aba Documentos em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-documentos-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Documentos em Cadastros do Consultório

---

🧩 A aba **Documentos** guarda os modelos dos documentos que o profissional emite: atestado, declaração de comparecimento, encaminhamento, relatório e outros. O modelo leva variáveis, que a plataforma troca pelos dados do paciente, do profissional e da consulta na hora de emitir.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Documentos**.
>
> ➡️ Clique em **Novo modelo**, escolha o **Tipo** e preencha **Nome do modelo**, **Título** e **Texto**.
>
> ➡️ Clique nas variáveis para colocá-las no texto e clique em **Salvar modelo**.

## Os campos

🔘 **Tipo:** **Atestado**, **Declaração de comparecimento**, **Encaminhamento**, **Relatório**, **Declaração** ou **Outro**.

🔘 **Nome do modelo:** como o modelo aparece para o profissional na hora de emitir.

🔘 **Título:** o título impresso no documento, como *ATESTADO*.

🔘 **Texto:** o corpo do documento, com as variáveis. Clicar numa variável coloca ela onde o cursor está.

🔘 **Disponível para emitir:** desmarcado, o modelo fica na lista como **Inativo** e não aparece para o profissional emitir.

O **Salvar modelo** só libera com **Nome do modelo**, **Título** e **Texto** preenchidos.

## As variáveis  
- `{{paciente}}` — o nome do paciente; o nome social, quando houver;
- `{{cpf}}` e `{{nascimento}}` — o CPF e a data de nascimento do paciente;
- `{{data}}` e `{{hora}}` — a data e a hora da emissão;
- `{{empresa}}` — o nome da clínica;
- `{{profissional}}`, `{{registro}}` e `{{especialidade}}` — o nome do profissional, o registro no conselho (como *CRM 12345/PR*) e as especialidades dele;
- `{{consulta_data}}`, `{{consulta_inicio}}` e `{{consulta_fim}}` — a data e as horas da consulta escolhida na emissão.

⚠️ Escreva só as variáveis da lista. Uma variável com outro nome não é trocada: ela aparece no documento exatamente como foi escrita, com as chaves.

## A lista

A aba mostra os modelos com o tipo e o nome, e o selo **Inativo** nos que estão desligados. O documento emitido não muda quando o modelo é editado depois: nas palavras da tela, *"o documento emitido não pode ser editado, só cancelado."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O modelo não aparece para o profissional emitir.** Confira se **Disponível para emitir** está marcado no modelo. Desmarcado, ele fica como **Inativo**.
>
> **A variável apareceu no documento com as chaves, sem o dado.** O nome da variável não é um dos da lista. Abra o modelo e troque pela variável certa, clicando nela no editor.
>
> **A receita também é um modelo de documento?** Não. A receita tem tela própria, no prontuário do paciente, com os medicamentos um a um.
