# Mover após (Aguardando)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mover-apos
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Mover após (Aguardando)

---

🧩 **O recurso "Mover Após"** é uma regra de segurança para quem ficou parado no robô. Ele funciona como um cronômetro: se o cliente não escolher um **Setor** no menu, ou parar num bloco do fluxo esperando uma resposta, e o tempo definido passar, o sistema transfere a conversa para o **Setor** escolhido, onde a equipe continua o atendimento.

☑️ **Resgate Humano:** Direciona um ticket que travou no meio de uma automação direto para um setor de "Transbordo" ou "Recepção", onde um atendente real possa dar continuidade.

☑️ **Menu sem resposta:** Leva para um Setor o cliente que recebeu o menu de Setores e não escolheu nenhum, em vez de deixar a conversa sem Setor.

☑️ **Experiência do Cliente:** Mostra agilidade, garantindo que a conversa sempre avance para um setor disponível em vez de ficar no limbo do atendimento.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**.
>
> ➡️ Escolha o tempo em **Após** e o Setor de destino em **Mover**.

## Como configurar o Mover por Inatividade

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**

Abaixo do campo Setores, configure os campos:

🔘 **Após (Tempo de Espera):** quanto tempo o cliente pode ficar parado no robô antes de ser transferido. A lista vai de 2 a 40 minutos; **DESABILITADO** desliga o **Mover Após**.

🔘 **Mover (Setor de Destino):** Selecione para qual Setor esse cliente será transferido quando o cronômetro zerar.  
- *Sugestão:* Crie um setor chamado "Triagem" ou "Transbordo" e selecione-o aqui. Assim, todos os clientes que pararam no robô serão transferidos para um lugar centralizado para a equipe de recepção assumir.

![Campos Após e Mover na aba Setores & Tempos da Conexão](https://clihelper.chatmasterveloz.com/docs-imagem/24789-mover-inatividade.jpg)

⚠️ Ao ligar o **Mover Após**, as conversas que já estavam paradas no robô há mais tempo que o **Após** são transferidas logo em seguida, e cada cliente recebe a **Mensagem de Encaminhamento**.

## Quem o Mover Após transfere

O cronômetro do **Mover Após** vale enquanto o cliente está com o robô:

➡️ **Sem Setor:** o cliente recebeu o menu de Setores e não escolheu nenhum.

➡️ **Parado no fluxo:** o cliente está num bloco do fluxo esperando uma resposta, como **Pergunta** e **Botões**. Passado o tempo, o atendimento vai para o Setor de destino mesmo com o fluxo aberto.

A conversa que já entrou num Setor e está em **Aguardando**, esperando um atendente, **não** é transferida pelo **Mover Após**: ela fica nesse Setor até alguém assumir.

O bloco **Pergunta** pode ficar de fora: ele tem a opção **Mover de setor por inatividade**. Desligada, o atendimento fica naquela pergunta até o cliente voltar, sem o cronômetro — para as perguntas em que a demora é esperada. Só o bloco **Pergunta** tem essa opção.

Ao ser transferido pelo **Mover Após**, o cliente recebe a **Mensagem de Encaminhamento**, do menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**. A **Mensagem de saudação** do Setor de destino não é enviada nessa transferência.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Mover Após transfere a conversa que já está em Aguardando num Setor?** Não. O **Mover Após** só transfere quem ainda está com o robô: sem Setor escolhido ou parado num bloco do fluxo. A conversa que já entrou num Setor espera ali até um atendente assumir.
>
> **O Mover Após afeta os clientes que eu já estou atendendo?** Não. Ele só transfere quem ainda está com o robô; a conversa que um atendente aceitou (status *Atendendo*) fica com ele.
>
> **O que acontece se eu deixar o Após em DESABILITADO?** O **Mover Após** fica desligado: o cliente que parar no robô continua ali até responder ou até alguém assumir a conversa.
>
> **Qual a diferença entre o "Mover Após" e a "Inatividade"?** O **Mover Após** transfere para outro Setor quem parou no robô, sem Setor ou num bloco do fluxo. O "Encerrar por Inatividade" atua na coluna "Atendendo" (quando o atendente já assumiu a conversa).
>
> **O fluxo estava esperando uma resposta e o atendimento mudou de Setor sozinho. Por quê?** Foi o **Mover Após**: ele conta também com o cliente parado num bloco do fluxo. Se naquela pergunta a espera é esperada, desligue **Mover de setor por inatividade** no próprio bloco **Pergunta**.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Definir um tempo muito curto:** Colocar o campo "Após" com 2 ou 3 minutos. O cliente recebe o menu do robô, para para ler as opções e, antes mesmo de conseguir digitar o número desejado, o sistema tira ele do robô e joga para o setor humano.
>
> **Mover para um setor sem atendentes:** Configurar a regra perfeitamente, mas apontar o destino ("Mover") para um setor que não tem nenhum usuário vinculado a ele. O ticket será transferido, mas continuará parado na aba "Aguardando" do novo Setor, pois ninguém tem acesso para puxá-lo.
>
> **Contar com a saudação do Setor de destino:** o cliente transferido pelo **Mover Após** não recebe a **Mensagem de saudação** do Setor de destino, e sim a **Mensagem de Encaminhamento**. **Solução:** ajuste o texto da **Mensagem de Encaminhamento** no menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**, para que ele sirva a qualquer transferência.
