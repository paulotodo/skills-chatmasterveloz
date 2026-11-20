# Aba Profissionais em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-profissionais-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Profissionais em Cadastros do Consultório

---

🧩 A aba **Profissionais** diz quem atende no consultório: o usuário da plataforma, o registro dele no conselho da profissão e os horários em que a agenda oferece consulta com ele.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Profissionais**.
>
> ➡️ Clique em **Adicionar profissional** e escolha o **Usuário**.
>
> ➡️ Preencha **Conselho**, **Número no conselho** e **UF**, os dias e os horários de atendimento, e clique em **Salvar**.

## Os campos

🔘 **Usuário:** a pessoa da equipe que atende. Quem já é profissional não aparece na lista. Sem usuário disponível, crie a pessoa no menu **Equipe**.

🔘 **Conselho:** o conselho da profissão — **CRM**, **CRO**, **CRP**, **CREFITO**, **CRN**, **COREN**, **CRFa**, **CREF**, **CRBM**, **CRF**, **CRMV** ou **Outro**.

🔘 **Número no conselho:** até 20 caracteres, só letras, números, ponto, hífen e barra.

🔘 **UF:** o estado do registro.

🔘 **RQE:** o registro de especialidade, se houver.

🔘 **Especialidades:** separadas por vírgula, até 10, cada uma com até 60 caracteres. Elas entram nos documentos que o profissional emite.

🔘 **Ativo:** desmarcado, o profissional sai das novas consultas e continua no histórico.

🔘 **Aceita marcação pela API (atendente de IA):** desmarcado, a integração da clínica não marca consulta com este profissional; a marcação fica com a recepção.

O **Salvar** só libera com **Usuário**, **Número no conselho** e **UF** preenchidos.

## O horário de atendimento

São os horários em que a agenda oferece consultas com o profissional, dia a dia da semana, com **Hora Inicial** e **Hora Final**. O botão **Adicionar outro intervalo de trabalho** cria mais uma faixa no mesmo dia, como manhã e tarde.

🔘 **Dia preenchido:** a agenda sugere os horários livres dentro das faixas. Marcar fora delas pede **Encaixe**.

🔘 **Dia em branco:** sem limite de horário, e a agenda não sugere horário: a recepção digita a hora.

🔘 **00:00 às 00:00:** folga. O profissional não atende naquele dia.

⚠️ Uma faixa que termina antes de começar, ou duas faixas que se cruzam no mesmo dia, impedem o salvamento: *"O expediente tem dois horários que se cruzam no mesmo dia. Ajuste as faixas para não se sobreporem."*

## Os convênios que atende

O bloco **Convênios que atende** tem uma caixinha para cada convênio cadastrado na aba **Convênios**. Marque os convênios pelos quais o profissional atende. Sem convênio cadastrado, o bloco avisa *"Nenhum convênio cadastrado. Cadastre os convênios na aba Convênios para escolher aqui quais este profissional atende."*

🔘 **Horário próprio para este convênio:** aparece ao marcar o convênio. Marcado, abre uma grade só para aquele convênio, que já vem copiada do horário de atendimento do profissional: deixe nela os dias e as faixas em que ele atende pelo convênio. O horário de atendimento do profissional não muda.

Nas palavras da tela, *"Sem horário próprio, o convênio segue o horário de atendimento acima; com ele, a agenda oferece só os dias e horários do convênio."*

## A lista

A aba mostra cada profissional com **Usuário**, **Registro** (o conselho, o número e a UF, como *CRM 12345/PR*), **RQE**, **Especialidades** e **Situação**, e os botões **Editar profissional** e **Remover profissional**.

Remover pede confirmação: *"O usuário continua no sistema; só deixa de atender no consultório."* Profissional com consultas na agenda ou com registros no prontuário não é removido: desative o cadastro.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O usuário que eu quero não aparece no campo Usuário.** Ou ele já é profissional, ou ainda não existe na equipe. Confira a lista da aba **Profissionais** e o menu **Equipe**.
>
> **O botão Salvar do profissional não habilita.** Faltam **Usuário**, **Número no conselho** ou **UF**, ou o número tem um caractere que não vale, como espaço ou asterisco.
>
> **O profissional atende de manhã e à tarde. Como cadastro o horário de almoço?** Use **Adicionar outro intervalo de trabalho** no dia: uma faixa para a manhã e outra para a tarde. O intervalo entre elas fica fora da agenda.
>
> **O profissional não atende aos sábados.** Preencha o sábado com **00:00** às **00:00**. Deixar o dia em branco é o contrário: libera qualquer horário.
>
> **O profissional atende por um convênio só às quartas de manhã. Como cadastro?** Em **Convênios que atende**, marque o convênio e **Horário próprio para este convênio**, e deixe nessa grade só a quarta, com a faixa da manhã: para esse convênio, a agenda passa a oferecer só esse horário. O horário de atendimento dele continua o mesmo.
