# Meta

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/meta
- **Categoria:** Trilhas
- **Menu:** Meta

---

🧩 A **Meta** é a empresa que controla as três redes por onde os seus clientes atendem: **Facebook**, **Instagram** e **WhatsApp**. Ela já se chamou Facebook Inc. e mudou de nome justamente para representar o ecossistema inteiro.

Entender como a Meta se organiza é o que separa uma integração que funciona de um número bloqueado. A nossa plataforma gerencia o atendimento, mas **a infraestrutura de envio é dela** — e são as regras dela que valem.

☑️ **Entendimento:** compreender por que certas regras existem.

☑️ **Conformidade:** seguir as políticas da Meta é o que ajuda a evitar o bloqueio do número do seu cliente.

☑️ **Hierarquia:** a nossa plataforma é a ferramenta que gerencia o atendimento; a infraestrutura de envio pertence à Meta.

## As peças do ecossistema

◽ **Portfólio Empresarial (BM):** a sede virtual da empresa dentro da Meta. É onde a empresa é verificada e onde ficam os ativos — Páginas, contas e aplicativos.

◽ **Aplicativo:** o software registrado na Meta que conversa com as APIs dela. É ele que faz aparecer o seu nome e o seu logotipo na janela de login do cliente.

◽ **Conta do WhatsApp Business (WABA):** a conta que guarda os números de WhatsApp Oficial do seu cliente.

O caminho é sempre nessa ordem: a empresa vira uma **BM**, a BM ganha um **Aplicativo**, e é o Aplicativo que conecta as contas dos seus clientes.

## As políticas comerciais

A Meta é rígida para proteger o usuário final de spam e de golpes, e proíbe a venda de certos itens — armas, drogas e jogos de azar, entre outros. Quem descumpre perde o número, e o volume de atendimento não protege ninguém.

## Os dois caminhos para oferecer a API Oficial

◽ **Integração Nativa (recomendada):** o cliente conecta pelo login do Facebook dentro da nossa plataforma, sem intermediário. Menor latência e custo mais competitivo.

◽ **Integração NotificameHub:** o setup é feito numa conta no NotificameHub, que intermedeia a conexão.

Priorize a **Nativa** para clientes novos. Por ser construção interna da nossa plataforma, ela deixa você com o controle do preço de venda e da marca, e o cliente não precisa criar conta em site externo. Deixe o **NotificameHub** para clientes antigos ou para cenários em que a integração externa seja exigida.

## O caminho desta trilha

⚡ **API Oficial Nativa** — os dois modelos de conexão: começar rápido com a estrutura de outra empresa, ou com a sua marca na tela de login.

⚡ **Portfólio Empresarial (BM)** — criar a sede da sua empresa na Meta e verificá-la.

⚡ **Tech Provider** — criar o seu aplicativo e pedir a Verificação de Acesso.

⚡ **Análise do App do WhatsApp** — as permissões, os textos e os vídeos que a Meta exige.

⚡ **Análise do App do Facebook** — o mesmo processo, para o Messenger.

⚡ **Análise do App do Instagram** — o mesmo processo, para o Direct.

⚡ **Publicar o App e Ligar na Plataforma** — o que fazer depois da aprovação: publicar o aplicativo e trazer as chaves para cá.

⚡ **Qualidade e Limite de Envio do Número** — quantos contatos novos por dia, como o limite sobe e o que derruba a nota do número.

⚡ **Bloqueio WhatsApp** — o que fazer quando um número é bloqueado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso passar por tudo isso para vender API Oficial?** Não. Dá para começar a vender hoje, no modelo mais simples, e cuidar da verificação e do aplicativo próprio depois — é o primeiro artigo desta trilha que explica a diferença.
>
> **O cliente final percebe a diferença no chat?** Não. Para quem recebe a mensagem é tudo WhatsApp Oficial; o que muda é como a mensagem trafega nos bastidores.
>
> **Posso ter clientes usando Nativa e outros usando Hub?** Sim. O sistema é híbrido: o Cliente A pode rodar na Nativa e o Cliente B via NotificameHub, ao mesmo tempo.
>
> **Os recursos como botões e listas funcionam nos dois caminhos?** Sim. As duas integrações suportam os recursos avançados da API Oficial do WhatsApp.
