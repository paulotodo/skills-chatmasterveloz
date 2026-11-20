# Resumo automático do Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/resumo-automatico-do-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Resumo automático do Dashboard

---

🧩 Quem gerencia nem sempre abre o painel todo dia. O **Resumo automático** do Dashboard leva os números até essa pessoa: na hora escolhida, os indicadores principais, a comparação com o período anterior e os alertas abertos são enviados por e-mail, por WhatsApp ou pelos dois.

Nas palavras da tela: *"Os números são os mesmos do painel, com os filtros salvos aqui."* O resumo pode ser da empresa inteira ou só de um Setor, de uma pessoa ou de uma tag.

Ideal para:

☑️ **Gestão à distância:** o dono acompanha o atendimento pelo e-mail ou pelo WhatsApp, sem entrar no sistema.

☑️ **Rotina da semana:** o resumo semanal chega no mesmo dia e hora, pronto para a reunião da equipe.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique no botão **Resumo automático**, no topo da tela.
>
> ➡️ Marque **Enviar o resumo automaticamente**, escolha a frequência e a hora, informe os e-mails ou o WhatsApp e clique em **Salvar**.

## Os campos da janela Resumo automático

A janela se chama **Resumo automático do Dashboard**.

🔘 **Enviar o resumo automaticamente:** liga e desliga o envio na hora marcada. Desmarcada, a configuração continua guardada, mas nada é enviado sozinho.

🔘 **Frequência:** de quanto em quanto tempo o resumo é enviado, e de que período são os números:

➡️ **Diário:** *"O resumo de ontem, todo dia na hora escolhida."*

➡️ **Semanal:** *"Os 7 dias até ontem, no dia da semana escolhido."* O campo **Dia da semana** vai de segunda-feira a domingo.

➡️ **Mensal:** *"O mês passado, no dia do mês escolhido."* O campo **Dia do mês** vai do dia 1 ao 28.

🔘 **Hora:** a hora do envio.

🔘 **E-mails:** os endereços que recebem o resumo, até 10, separados por vírgula.

🔘 **WhatsApp (número):** o número que recebe o resumo, com 10 a 15 dígitos.

🔘 **Conexão:** por qual Conexão o resumo é enviado ao WhatsApp — **A conexão padrão** ou uma conexão escolhida da empresa.

Para ligar o envio, basta um destino: pelo menos um e-mail ou um número de WhatsApp.

### Os filtros do Resumo automático

Embaixo dos destinos, a janela diz de que parte da empresa são os números: *Sem filtros: a empresa inteira.* ou *Com 1 filtro(s) salvo(s).*

O botão **Usar os filtros que estão na tela agora** copia para o resumo o que está escolhido no Dashboard naquele momento: a conexão de **Filtrar por Conexão** e os **Setores**, **Atendentes** e **Tags** de **Filtros Avançados**. Para um resumo só do Setor Comercial, por exemplo, escolha o Setor nos **Filtros Avançados**, clique em **Aplicar Filtros**, abra o **Resumo automático**, clique no botão e salve.

Os filtros ficam guardados no resumo: trocar ou limpar os filtros da tela depois não muda o que o resumo envia.

## Salvar e Enviar agora

🔘 **Salvar:** grava a configuração, com o aviso *Resumo salvo.* Com **Enviar o resumo automaticamente** marcado, o resumo passa a ser enviado na frequência e na hora escolhidas.

🔘 **Enviar agora:** envia o resumo na hora, para conferir como ele chega. Ele usa o que está **na janela** naquele momento, mesmo antes de salvar.

Depois de um envio, a janela mostra quando foi e de que período — por exemplo, *Último envio: 17/11/2026, 09:08:23 (período 16/11/2026).* O resumo diário vai com o assunto *Resumo diário do atendimento —* seguido da data do dia resumido.

Quando parte do resumo não pôde ser enviada — por exemplo, o e-mail —, a tela avisa *O resumo não saiu inteiro. Veja o motivo na janela.*, e o motivo aparece logo embaixo do **Último envio**.

## O que chega no Resumo automático

No WhatsApp, o resumo chega numa mensagem só, com o título do período — por exemplo, *Resumo diário do atendimento — 16/11/2026*. Com filtro salvo, a linha logo abaixo do título diz de que parte da empresa são os números — por exemplo, *Setor: Atendimento*.

Em seguida, estes números:

➡️ **Atendimentos**, **Resolvidos** e **Taxa de resolução**.

➡️ **Primeira resposta (média)**, em minutos, e **Resolução (média)**, em horas.

➡️ **Conformidade SLA** e **Avaliação (NPS)**.

Cada número do Resumo automático vem com a comparação entre parênteses: o valor do período de mesma duração logo antes do resumido e a diferença, com uma seta — por exemplo, *Atendimentos: 36 (antes: 91; -55 ▼)*. Quando o número não mudou, a comparação diz *igual*: *Conformidade SLA: 100,0% (antes: 100,0%, igual)*.

Quando o período anterior não teve atendimento, os números chegam sem a comparação, e uma linha antes deles avisa *Período anterior: sem atendimentos.*

O número que não tem como ser calculado no período chega com um traço (*—*) no lugar do valor: sem atendimento resolvido, não há **Resolução (média)** nem **Conformidade SLA**; sem avaliação, não há **Avaliação (NPS)**. Quando o período não teve nenhum atendimento, a mensagem avisa *Sem atendimentos no período.* antes dos números, que chegam com 0 em **Atendimentos** e **Resolvidos** e com o traço nos demais.

Embaixo vem o bloco **Alertas abertos**, com cada alerta do momento e a quantidade — por exemplo, *SLA Próximo do Vencimento: 100 ticket(s) próximos de vencer o SLA* ou *Clientes Sem Resposta: 6 atendimento(s) com a última mensagem do cliente sem resposta há mais de 30 min*. Os números e os alertas seguem os filtros salvos no resumo. Sem alerta aberto, a mensagem termina com *Nenhum alerta aberto.*

## As mensagens da janela

🔘 *Para ligar, informe pelo menos um e-mail ou um número de WhatsApp.* — o envio automático está marcado sem nenhum destino.

🔘 *Um dos e-mails não é válido.* — um endereço da lista está escrito errado.

🔘 *Use até 10 e-mails.* — a lista passou de dez endereços.

🔘 *O número de WhatsApp precisa ter de 10 a 15 dígitos.* — o número está curto ou longo demais.

Essas mensagens aparecem na própria janela, e nada é gravado até a correção.

## Quem configura o Resumo automático

O botão **Resumo automático** é do administrador. O supervisor não tem o botão no Dashboard.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O resumo diário do Dashboard traz os números de hoje?** Não. O **Diário** envia o resumo de ontem, todo dia na hora escolhida. O **Semanal** envia os 7 dias até ontem, e o **Mensal**, o mês passado.
>
> **Dá para receber o Resumo automático do Dashboard só de um Setor?** Dá. Escolha o Setor em **Filtros Avançados**, clique em **Aplicar Filtros**, abra o **Resumo automático** e clique em **Usar os filtros que estão na tela agora** antes de salvar. A janela passa a mostrar quantos filtros estão salvos.
>
> **Cliquei em Enviar agora no Resumo automático sem salvar. O que foi enviado?** O que estava na janela naquele momento. Para que o envio na hora marcada use a mesma configuração, clique também em **Salvar**.
>
> **O resumo mensal do Dashboard pode ser enviado no dia 30?** Não. O **Dia do mês** vai do dia 1 ao 28.
>
> **Desmarquei Enviar o resumo automaticamente. Perdi a configuração do resumo?** Não. Os destinos, a frequência e os filtros continuam guardados; só o envio na hora marcada para.
>
> **O Resumo automático do Dashboard chegou com Sem atendimentos no período.** Confira os filtros salvos no resumo. Com um Setor salvo, os números e os alertas são só desse Setor, e um período em que ele não teve atendimento chega com *Sem atendimentos no período.* e os números em 0 ou com traço, embora a empresa tenha atendido. A janela mostra *Com 1 filtro(s) salvo(s).* quando há filtro, e a mensagem diz o filtro logo abaixo do título — *Setor: Atendimento*, por exemplo. Para a empresa inteira, limpe os filtros da tela, clique em **Usar os filtros que estão na tela agora** e salve.
>
> **O que quer dizer o traço (—) no Resumo automático do Dashboard?** Que o número não tem como ser calculado no período: sem atendimento resolvido, não há **Resolução (média)** nem **Conformidade SLA**, e sem avaliação, não há **Avaliação (NPS)**. O traço não é zero: *Resolvidos: 0* com *Atendimentos: 3* quer dizer que houve atendimentos e nenhum foi resolvido.
>
> **O supervisor pode configurar o Resumo automático do Dashboard?** Não. O botão **Resumo automático** aparece só para o administrador.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Resumo por e-mail que não chega:** a janela mostra o motivo *o e-mail da plataforma não está configurado (Configurações da Plataforma)*. O envio de e-mail do resumo depende de uma configuração da plataforma que não fica na empresa. **Solução:** peça a quem fornece a plataforma para configurar o envio de e-mails; enquanto isso, use o **WhatsApp (número)**.
>
> **Marcar a caixa e fechar a janela:** **Enviar o resumo automaticamente** marcada não grava nada sozinha. **Solução:** clique em **Salvar** e confira o aviso *Resumo salvo.*
