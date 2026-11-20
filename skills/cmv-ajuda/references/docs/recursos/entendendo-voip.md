# Entendendo VoIP

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/entendendo-voip
- **Categoria:** Recursos
- **Menu:** Ligações › Entendendo VoIP

---

🧩 **O VoIP (Voice over Internet Protocol, ou Voz sobre IP)** é a tecnologia utilizada para conversas de voz via internet.

Sendo possível, juntamente com um PABX digital, criar URAs, Ramais e Grupos. Vamos conhecer um pouco sobre esse universo.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ **VoIP:** A tecnologia base (A transmissão da voz pela internet).
>
> ➡️ **PABX Virtual:** O “cérebro” da operação (Gerencia ramais, filas e a URA).
>
> ➡️ **DID:** O seu número virtual (A porta de entrada do cliente).
>
> ➡️ **SIP:** O “idioma” (Protocolo que os aparelhos usam para se conectar).

## **O Dicionário da Telefonia em Nuvem**

Para entender como tudo se conecta, é preciso conhecer os quatro pilares da telefonia digital.

⚡ **1. O CÉREBRO: PABX EM NUVEM (Cloud PBX)**

Na telefonia antiga, o PABX era aquela caixa de metal cheia de fios pregada na parede da empresa que distribuía os ramais.

◽ O **PABX Virtual** faz exatamente a mesma coisa, mas é um software hospedado em servidores na internet.

◽ É nele que você cria a **URA** (Atendimento Automático: *"Pressione 1 para Vendas"*), configura filas de espera, grava ligações e define regras de horário de atendimento.

⚡ **2. O NÚMERO: DID (Direct Inward Dialing)**

O DID é o que chamamos de "Número Virtual".

◽ Para o seu cliente, ele é um número de telefone fixo ou móvel completamente normal.

◽ A diferença é que, quando o cliente liga para esse número, a chamada não vai para um poste da rua, ela viaja pela internet e "toca" diretamente no seu PABX em Nuvem.

⚡ **3. A LINGUAGEM E ROTA: SIP e TRONCO SIP**

SIP (Session Initiation Protocol) é a tecnologia que cria, gerencia e encerra a chamada de voz digital.

◽ **Protocolo SIP:** Pense nele como o idioma padrão da telefonia digital. É assim que o seu computador "fala" com o servidor.

◽ **Tronco SIP (SIP Trunk):** É a sua "linha telefônica" virtual. É o serviço contratado de uma operadora VoIP que conecta o seu PABX à rede mundial de telefonia, permitindo que você faça ligações para celulares e telefones normais, e não apenas pela internet.

⚡ **4. OS APARELHOS: SOFTPHONE vs TELEFONE IP**

Para fazer a ligação, você precisa de um "aparelho" na ponta, que serão os ramais dessa linha.

◽ **Softphone:** É um aplicativo instalado no seu computador ou celular (ex: Zoiper, MicroSIP, WebRTC). Você usa um fone de ouvido para falar, dispensando a necessidade de comprar aparelhos físicos.

◽ **Telefone IP:** É um telefone de mesa físico, mas em vez de se conectar na tomada de telefone antiga (RJ11), ele se conecta na sua rede de internet (cabo de rede RJ45 ou Wi-Fi).

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **Preciso de uma internet muito rápida para usar VoIP?** A velocidade (Megas) não é o mais importante, mas sim a **estabilidade** (Latência/Ping e Jitter). Uma chamada de voz consome pouquíssima banda (cerca de 100 kbps), mas se a sua internet oscilar ou perder pacotes, a voz ficará "robótica" ou com cortes.
>
> **Posso portar meu número fixo atual para o VoIP?** Sim! O processo de portabilidade numérica funciona da mesma forma. Você pode pegar seu número analógico da operadora tradicional e portá-lo para uma operadora VoIP, transformando-o em um número digital (DID). Mas você pode contratar números digitais também.
>
> **Posso usar meu número WhatsApp como VoIP na plataforma?** Sim, é possível utilizar ligações whatsapp no sistema.

> **[ERROS]**
>
> ## Erros Comuns
>
> **Usar Wi-Fi Instável no Atendimento:** Conectar o computador do atendente via Wi-Fi longe do roteador. Como o VoIP é sensível a oscilações, a voz pode picotar.
>
> *Solução:* Para quem atende chamadas o dia todo, o ideal é usar o computador conectado via **cabo de rede (Ethernet)**.
>
> **Ignorar a configuração "SIP ALG" no roteador:** A grande maioria dos roteadores de provedores de internet vem com uma função chamada "SIP ALG" ativada. Ironicamente, ela costuma bloquear ou corromper pacotes de voz.
>
> *Sintoma:* A ligação conecta, o tempo corre, mas você não ouve o cliente (ou vice-versa), ou a chamada cai em 30 segundos cravados. É preciso acessar o roteador e desativar o SIP ALG.
>
> **Esquecer a regra de discagem da Operadora:** Ao usar um Tronco SIP, o usuário tenta discar como se estivesse em uma linha analógica local (digitando apenas os 8 ou 9 dígitos). No VoIP, é quase sempre necessário enviar a chamada no formato completo (Ex: DDD + Número ou 0 + Operadora + DDD + Número), senão a ligação não completa.
