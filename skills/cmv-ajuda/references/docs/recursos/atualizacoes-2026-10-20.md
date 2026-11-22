# 20/10/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-20
- **Categoria:** Recursos
- **Menu:** Atualizações › Outubro 2026 › 20/10/2026

---

🧩 Atualizações de 20 de outubro de 2026.

#### Novidades

⚡️ **Marcar como não lido:** no Atendimento, o ícone ao lado de **Resolver**, no topo do atendimento, marca a conversa como não lida para você voltar a ela depois.

⚡️ **Bloco Retornar último atendimento:** no FlowBuilder Nativo, devolve o cliente ao Setor, ao atendente e à situação do atendimento anterior.

⚡️ **Condição Protocolo fechado:** ainda no FlowBuilder Nativo, verifica se o último atendimento do contato foi encerrado há menos ou há mais de um tempo.

⚡️ **Variável Último protocolo:** cita o atendimento anterior nas mensagens.

#### Melhorias

☑️ **Status Desativado no rodízio:** tira o participante da roda sem mexer no status dele na plataforma.

☑️ **Relatório do rodízio:** os fluxos apagados ficam escondidos, com o botão **Ver apagados**.

☑️ **Dono das tags:** a tag criada por administrador ou supervisor já nasce valendo para a equipe toda, e o dono pode ser escolhido depois.

☑️ **Mesmos nomes no FlowBuilder Nativo:** janelas, tipos da Condição e canais com os mesmos nomes em toda parte.

☑️ **Quem atendeu** aparece na aba **Fechados** e na busca avançada.

☑️ **Assistente de IA:** as respostas vêm com o nome do assistente e um selo.

☑️ **Dashboard:** os números contam só os atendimentos reais.

#### Correções

◽ A automação de etiqueta não reabre mais atendimento encerrado.

◽ Importar contatos ignora status desconhecido, e nenhum atendimento some das abas.

◽ A conversa que tinha ficado escondida e recebe mensagem volta para o Aguardando.

◽ O Relatório de vendas do CRM mostra as perdas, filtra por produto e usa valores em reais.

◽ Mais estabilidade nos horários de movimento, e volta automática para o login quando a sessão termina em outra aba.

◽ No aplicativo do celular, a mensagem do Chat Externo volta a ser entregue.

## Marcar como não lido

No menu **Chats**, abra o atendimento: no topo, o ícone à esquerda de **Resolver** é o **Marcar como não lido**. Um clique marca a conversa como não lida na lista, para você voltar a ela depois.

🔘 **Nada é enviado ao cliente:** marcar como não lido não manda mensagem e não muda a situação do atendimento, que continua com o mesmo atendente.

🔘 **O mesmo ícone desfaz:** com a conversa não lida, o ícone passa a ser **Marcar como lido**.

![image.png](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ad8bad46df1e.png)

## Bloco Retornar último atendimento

O bloco **Retornar último atendimento** devolve o cliente para onde ele estava no atendimento anterior: o mesmo Setor, o mesmo atendente e a mesma situação.

➡️ Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Retornar último atendimento**.

🔘 **Sem nada para preencher:** o bloco não abre janela; o clique na paleta já o coloca no desenho.

🔘 **Sem protocolo anterior:** é a saída do bloco Retornar último atendimento para quem nunca foi atendido. Ligue essa saída ao caminho de sempre, como o menu.

![image.png](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ad8bb4112ab1.png)

## Condição Protocolo fechado

No bloco **Condição**, o tipo **Protocolo fechado** verifica se o último atendimento encerrado do contato, fora o atual, foi encerrado **há menos de** ou **há mais de** um tempo, em minutos, horas ou dias. Sem atendimento anterior, a condição Protocolo fechado é falsa.

☑️ **Para que serve:** reconhecer quem voltou logo depois de encerrar e, junto com o bloco Retornar último atendimento, levar essa pessoa de volta a quem já estava atendendo.

## Status Desativado no rodízio

No menu **Rodízios**, ao editar um rodízio, cada participante tem o campo **Status**: **Online**, **Indiferente** ou **Desativado**.

🔘 **Desativado:** tira o participante da roda sem mexer no status dele na plataforma.

🔘 **Relatório do rodízio:** os fluxos apagados ficam escondidos; o botão **Ver apagados** mostra os fluxos apagados.

![image.png](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ad8bbb31cc73.png)

## Dono das tags

A tag criada por administrador ou supervisor já nasce valendo para a equipe toda. Para dar um dono a uma ou mais tags:

➡️ Acesse o menu **Tags  ›  Atribuir dono** e marque as tags.

➡️ Clique em **Definir dono** e, na janela **Atribuir dono às tags**, escolha a pessoa no campo **Dono**.

➡️ Para a tag ficar pública, escolha **Ninguém (tag pública)**: sem dono, a tag fica visível para todos os operadores. Depois, clique em **Aplicar**.

## Mesmos nomes no FlowBuilder Nativo

O FlowBuilder Nativo passou a usar os mesmos nomes em toda parte:

🔘 **Janelas:** dizem **Adicionar bloco** ou **Editar bloco**, seguido do nome do bloco, como **Editar bloco: Condição**.

🔘 **Tipos da Condição:** **Resposta da Pergunta** e **Status do Atendimento**.

🔘 **Canais:** aparecem como **WhatsApp QRCode** e **WhatsApp Oficial**, os mesmos nomes da tela de Conexões.

#### O que você precisa fazer

Nada exige ação: tudo continua funcionando como antes.

➡️ Para tirar alguém do rodízio, acesse o menu **Rodízios  ›  editar o rodízio** e troque o **Status** do participante para **Desativado**.

➡️ Para escolher o dono das tags, acesse o menu **Tags  ›  Atribuir dono**
