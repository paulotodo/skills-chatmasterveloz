# Avisos da Meta na Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/avisos-da-meta-na-conexao
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Avisos da Meta na Conexão

---

🧩 Quando algo acontece com o seu número do lado da Meta, a Conexão de API Oficial mostra **uma faixa de aviso no próprio card**, na tela de Conexões. É a forma de você descobrir que a conta foi restrita, que o app perdeu permissão ou que o número mudou de aparelho, sem precisar entrar no painel da Meta para investigar.

A faixa traz numa linha só o que aconteceu, por que aconteceu e quem provocou. Ela aparece sozinha e some quando a situação se resolve.

Ideal para:

☑️ **Diagnóstico rápido:** Saber se o problema é da plataforma ou da conta na Meta, sem abrir chamado às cegas.

☑️ **Reação antes do cliente reclamar:** Uma restrição na conta aparece no card antes de virar mensagem que não chega.

☑️ **Histórico do número:** Entender por que a Conexão caiu, e se foi alguém que mexeu ou o próprio sistema.

## As três severidades

A cor da faixa diz o tamanho do problema, e a lista de cada cor é fixa.

🔴 **Erro** — a Conexão está comprometida e alguém precisa agir:

◽ Parceiro removido

◽ App desautorizado pelo cliente

◽ Conta desconectada

◽ Conta excluída

◽ Violação de política

◽ Restrição na conta

◽ Conta desabilitada

◽ Token expirado no envio

◽ App da Meta sem permissão necessária

🟡 **Aviso** — algo está fora do lugar, mas não parou tudo:

◽ Conta não inscrita nos webhooks, e por isso não recebe mensagens

◽ ID da conta divergente do que a Meta reconhece

◽ Reconectando, por troca de aparelho

🔵 **Informativo** — aconteceu algo e você só precisa saber:

◽ Conta verificada

◽ Atualização de revisão

◽ Reconectada automaticamente

◽ Parceiro vinculado

◽ Permissões concedidas

## O motivo, quando a conta desconecta

Quando o aviso é de desconexão, a faixa acrescenta o **porquê**:

◽ Número de telefone alterado

◽ WhatsApp registrado em outro aparelho

◽ Número registrado no WhatsApp comum

◽ Dispositivo principal inativo

◽ Dispositivo companion inativo

E diz ainda quem provocou: **pelo usuário** ou **pelo sistema**.

## O que fazer com cada tipo

🔘 **Restrição, violação ou conta desabilitada.** É decisão da Meta sobre o comportamento do número. A plataforma não desfaz isso. O caminho é o painel da Meta, e o artigo de número bloqueado nesta mesma seção explica como contestar.

🔘 **Token expirado ou app sem permissão.** A autorização entre a sua conta na Meta e a plataforma caiu ou ficou incompleta. Use o **Reconectar** no card, pelo mesmo caminho que foi usado no cadastro.

🔘 **Conta não inscrita nos webhooks.** O número está de pé, mas as mensagens chegam numa fila que ninguém lê. É o caso em que o atendimento simplesmente para de aparecer, sem a Conexão parecer caída.

🔘 **ID divergente.** O número mudou na Meta e não é mais o mesmo que está aqui. Reconectar misturaria histórico de dois números diferentes, então esse caso pede revisão manual.

🔘 **Reconectando por troca de aparelho.** É transitório, e costuma se resolver sozinho.

⚠️ **A faixa só existe quando há evento.** Conexão saudável não mostra nada, e a ausência de aviso é boa notícia, não falta de informação.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A faixa apareceu e sumiu sozinha. Perdi alguma coisa?** Não necessariamente. Avisos transitórios, como a troca de aparelho, somem quando a situação se normaliza.
>
> **Meu número continua conectado, mas a faixa diz que não recebo mensagens. Como assim?** É o caso da conta sem inscrição nos webhooks: a Conexão está de pé, mas o que chega não é entregue à plataforma. O card da Conexão oficial tem um botão que pergunta à Meta e refaz a inscrição.
>
> **A faixa diz violação de política. A plataforma pode reverter?** Não. A decisão é da Meta e se contesta no painel dela.
>
> **O que significa "app desautorizado pelo cliente"?** Alguém com acesso à conta da Meta removeu a autorização que permite à plataforma enviar pelo número. É preciso autorizar de novo.
>
> **Onde vejo isso tudo?** No menu **Conexões**, no card da Conexão de API Oficial.
