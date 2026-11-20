# Avaliação pela IA

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/avaliacao-pela-ia
- **Categoria:** Recursos
- **Menu:** Avaliação pela IA

---

🧩 Você sabe como a sua equipe está atendendo, ou só descobre quando o cliente reclama? Ler conversa por conversa não cabe na rotina de quem gerencia, e o atendente fica sem saber o que fez bem e o que precisa melhorar.

A **Avaliação pela IA** lê os atendimentos encerrados nos horários que a empresa escolhe, dá uma nota de 0 a 10 e aponta o que melhorar. A gestão acompanha o resultado num relatório, e cada atendente recebe uma aula curta, com um exemplo real. Nada disso é enviado ao cliente.

Ideal para:

☑️ **Retorno à equipe:** Entrega a cada atendente o que continuar fazendo, o que evitar e como responder melhor.

☑️ **Visão da gestão:** Reúne a nota média, o índice e os números por atendente e por Setor num relatório só.

☑️ **Atendimentos que pedem atenção:** Separa as notas baixas na faixa **Detratores**, com acesso direto à conversa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e ligue **Avaliar os atendimentos pela IA**. Só o administrador tem essa opção.
>
> ➡️ Em **Horários das rodadas**, informe de 1 a 4 horários e clique em **Salvar**.
>
> ➡️ Depois da rodada, acesse o menu **Avaliação pela IA** para ver o **Relatório** e as **Aulas**.

## Como ligar a Avaliação pela IA

Acesse o menu **Configurações  ›  Opções**. O bloco **Avaliação dos atendimentos pela IA** aparece só para o administrador:

🔘 **Avaliar os atendimentos pela IA:** liga a avaliação. A opção é gravada na hora, sem precisar de **Salvar**, e a tela confirma com *"Avaliação pela IA salva."*

🔘 **Horários das rodadas:** de 1 a 4 horários, separados por vírgula, por exemplo `12:00, 23:00`. Nesses horários, a IA da empresa dá a nota aos atendimentos encerrados, aponta o que melhorar e escreve uma aula curta para cada atendente.

🔘 **Webhook da avaliação:** o endereço de outro sistema que recebe os eventos da avaliação. A tela lista três: `atendimento-avaliado`, `avaliacao-falhou` e `aula-gerada`. O endereço precisa começar com `http://` ou `https://`, sem espaços, e não pode apontar para a rede interna.

🔘 **Salvar:** grava os horários e o webhook.

🔘 **Avaliar agora:** começa uma rodada sem esperar o horário, com o aviso *"A avaliação começou. Os resultados aparecem no relatório em alguns minutos."* O botão fica desativado enquanto **Avaliar os atendimentos pela IA** estiver desligado.

## Quem vê o quê na Avaliação pela IA                                    

| Perfil | Menu **Avaliação pela IA** | O que abre | Bloco no menu **Configurações › Opções** |
|---|---|---|---|
| Administrador | Sim | **Relatório** e **Aulas**, com **Exportar CSV** | Sim |
| Supervisor | Sim | **Relatório** e **Aulas**, com **Exportar CSV** | Não |
| Atendente | Sim | **Minhas aulas** | Não |
| Atendente com acesso limitado | Não | Sem o item no menu | Não |

## O Relatório da Avaliação pela IA

Acesse o menu **Avaliação pela IA**, aba **Relatório**. A tela abre nos últimos 30 dias:

🔘 **Filtros:** **De**, **Até**, **Atendente**, **Setor** e **Faixa da nota**. O período aceita no máximo um ano.

🔘 **Nota média** e **Atendimentos avaliados:** a média das notas e a quantidade de atendimentos avaliados no que está filtrado.

🔘 **Faixas da nota:** **Promotores (9-10)**, **Neutros (7-8)** e **Detratores (0-6)**, com a quantidade de atendimentos em cada faixa.

🔘 **Índice (estilo NPS):** a parcela de promotores menos a de detratores, de -100 a 100. Com 1 promotor e 6 detratores em 7 atendimentos, o índice é -71.

🔘 **Distribuição das notas** e **Evolução por dia:** os gráficos de quantos atendimentos receberam cada nota, de 0 a 10, e de como a média andou a cada dia.

🔘 **Por atendente** e **Por Setor:** as tabelas com **Nome**, **Média**, **Atendimentos** e **Índice**.

🔘 **Atendimentos avaliados:** a lista com **Encerrado em**, **Contato**, **Atendente**, **Setor**, **Nota** e **Pontos de atenção**. O botão **Abrir conversa** leva à conversa encerrada daquele atendimento.

## Como exportar o CSV da Avaliação pela IA

Na aba **Relatório**, clique em **Exportar CSV**. O arquivo traz os atendimentos do período filtrado, com as colunas separadas por ponto e vírgula: **Encerrado em**, **Protocolo**, **Contato**, **Atendente**, **Setor**, **Nota**, **Pontos de atenção**, **Pontos fortes**, **Próximo passo** e **Resumo**.

Quando há mais de um ponto na mesma célula, eles vêm separados por `|`.

## As aulas da Avaliação pela IA

Depois das rodadas, cada atendente ganha uma aula feita a partir dos atendimentos dele. O administrador e o supervisor veem as aulas na aba **Aulas**, com filtro por **Atendente**. O atendente vê só as dele, na aba **Minhas aulas**.

Cada aula traz:

🔘 **Identificação:** o título, o atendente, quantos atendimentos entraram, a média e o período.

🔘 **Continue fazendo:** o que o atendente já faz bem.

🔘 **Evite:** o que deixar de fazer.

🔘 **Um exemplo real:** **A situação**, **Como foi** e **Como fica melhor**.

🔘 **Marcar como vista:** registra a leitura, que passa a aparecer como *"Vista por"*, com o nome e a data. O supervisor enxerga quem já viu.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A Avaliação pela IA envia alguma mensagem ao cliente?** Não. A nota, o relatório e as aulas ficam dentro da plataforma: o cliente não recebe nada, e a conversa encerrada continua como estava.
>
> **A Avaliação pela IA é a mesma coisa que a pesquisa de avaliação enviada ao cliente?** Não. Na pesquisa, quem dá a nota é o cliente. Na **Avaliação pela IA**, quem dá a nota é a IA, lendo o atendimento encerrado.
>
> **O atendente vê a própria nota na Avaliação pela IA?** O atendente não abre o **Relatório**. Ele vê as próprias aulas na aba **Minhas aulas**, cada uma com a média do período dela.
>
> **O supervisor pode mudar os Horários das rodadas da Avaliação pela IA?** Não. O bloco **Avaliação dos atendimentos pela IA**, no menu **Configurações  ›  Opções**, aparece só para o administrador.
>
> **O botão Avaliar agora avalia um atendimento escolhido?** Não. A tela não pede atendimento nenhum: **Avaliar agora** começa a rodada da empresa.
>
> **Um mesmo ticket pode ter mais de uma nota na Avaliação pela IA?** Pode. A avaliação é por protocolo: um ticket com dois protocolos avaliados tem duas notas, uma para cada protocolo.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A tela mostra "A avaliação pela IA não faz parte do seu plano.":** a página não mostra o relatório nem as aulas. **Solução:** peça a liberação da **Avaliação pela IA** no plano da empresa.
>
> **O Relatório mostra "Nenhum atendimento avaliado no período.":** o período ou o filtro escolhido não tem nenhuma avaliação. **Solução:** amplie **De** e **Até**, volte **Faixa da nota** para **Todas** e confira se **Avaliar os atendimentos pela IA** está ligado no menu **Configurações  ›  Opções**.
>
> **O campo Horários das rodadas mostra "Use de 1 a 4 horários no formato HH:MM":** o **Salvar** fica desativado. **Solução:** informe de 1 a 4 horários, separados por vírgula, como `12:00, 23:00`. O campo não aceita ficar vazio.
>
> **O Relatório mostra "Confira o período do relatório":** a data inicial passou da final, ou o período tem mais de um ano, e os números continuam os da busca anterior. **Solução:** corrija **De** e **Até**.
