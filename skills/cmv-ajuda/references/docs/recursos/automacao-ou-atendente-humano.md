# Automação ou Atendente Humano

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/automacao-ou-atendente-humano
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Automação ou Atendente Humano

---

🧩 Decidir entre **bot** (automação) e **atendente humano** é uma das escolhas mais importantes da sua operação. Cada um tem velocidade, custo e cenários onde brilha. Misturar os dois com inteligência é o que faz a sua operação escalar sem perder qualidade.

☑️ **Custo controlado:** automação escala sem precisar contratar; sua equipe humana fica focada nos casos que realmente exigem gente.

☑️ **Velocidade no Aguardando:** bot responde em segundos, 24h por dia.

☑️ **Equipe focada no que importa:** repetição vai pra automação. Casos sensíveis e relacionamento ficam pra sua equipe.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Bots respondem sozinhos. Atendentes humanos resolvem o que é complexo. O segredo é o **mix certo** dos dois.➡️ O cliente **não sabe** se é automação — o sistema não revela nada, segue sua programação. ### 📘 Como Bot e Humano se relacionam em um Ticket
>
> O cliente manda mensagem → o ticket entra em 🟡 **Aguardando**. Cenário ideal para o bot atender enquanto o ticket não tem atendente humano atribuído.
>
> Veja o que pode acontecer:
> - **Bot resolver sozinho:** encerra o ticket no fim do fluxo. Vai direto pra 🔴 **Encerrado** sem passar por humano.
> - **Bot transferir para um humano:** quando precisa, passa o ticket pra um atendente. O ticket vira 🟢 **Atendendo**.
> - **Humano resolver:** e encerrar o atendimento manualmente, voltando o ticket para 🔴 **Encerrado**
> - **Humano devolver à fila:** o ticket volta pra 🟡 **Aguardando**.

### **As ferramentas de automação**

A sua plataforma pode ter uma ou mais ferramentas de automação disponíveis, dependendo do seu plano e do que você decidiu habilitar. Em geral, elas se dividem em três famílias:  
- **Automações por fluxo visual** — você desenha o caminho que o bot vai seguir, com perguntas, condições e ações. Boas para processos previsíveis (menu, FAQ, agendamento).
- **Automações por IA generativa** — o bot conversa abertamente, baseado em contexto e conhecimento que você forneceu. Boas para perguntas variadas onde menu não cabe.
- **Automações via integração externa** — você conecta sistemas de terceiros (n8n, Webhook, plataformas externas) que respondem ao cliente.

### **Cenários típicos de atendimentos**

🤖 **Só bot, ponta a ponta** ▫️ O bot resolve do início ao fim. Seu cliente não fala com um humano.

Atendimento padronizado, com respostas previsíveis.

Exemplos:  
- 2ª via de boleto
- Status de pedido / código de rastreio
- Agendamento (clínica, salão, oficina)
- FAQ — horário, endereço, prazo, política de troca
- Suporte nível 1 (problemas comuns com receita pronta)

🤖+👤 **Bot triagem → humano resolve (URA conversacional) ▫️** Sua equipe recebe o ticket já com contexto coletado pelo bot.

Bot inicia entendendo o que o cliente quer e encaminha.

Exemplos:  
- "Qual setor? 1 — Vendas, 2 — Suporte, 3 — Financeiro" → transfere pra fila certa.
- "Em qual produto você tem dúvida?" → transfere pro especialista.
- "Já é nosso cliente? Me passa seu CPF." → identifica e direciona.

🤖✨ **IA generativa atendendo direto** ▫️A IA responde conforme conhecimento de sua base de dados e transfere pra humano quando identifica que está fora do escopo dela.

Casos onde a pergunta varia demais pra caber em menus.

Exemplos:  
- Vendas consultivas (cliente pergunta sobre produto de mil formas diferentes)
- FAQ aberto (qualquer dúvida sobre o serviço)
- Suporte de primeiro nível em produto técnico
- Pré-qualificação de lead

👤 **Só humano, sem bot na frente** ▫️ Vai direto pra fila do humano certo. Bot nem aparece.

Cenários onde tentar bot é arriscado:  
- Cobrança, negociação de dívida
- Reclamação grave, atendimento sensível
- Vendas de alto valor (carro, imóvel, B2B grande)
- Atendimento VIP (cliente premium não fica em fila)
- Casos jurídicos

🤖+👤 **Híbrido por horário** ▫️ Um bloco de condição de horário logo no início — se está dentro do expediente, segue um caminho; se está fora, segue outro.  
- Em **horário comercial:** sua equipe atende, bot só pra triagem ou overflow.
- **Fora de horário:** bot 100%, registra demanda e responde no possível. Casos que precisam de humano ficam na fila pro próximo dia.

🔗 **Automações em cadeia**

Cenário avançado: uma automação chama outra. Ex.: bot por fluxo visual coleta os dados iniciais e, ao identificar que o cliente quer falar de um tema aberto, transfere o ticket pra outra automação baseada em IA. Ou vice-versa: IA conversa, e quando identifica intenção específica, dispara um fluxo estruturado pra finalizar (ex.: agendar, gerar boleto).

É uma estratégia poderosa pra operações maduras, mas exige planejamento — cada salto entre automações é um ponto onde o cliente pode "perder o fio" se não for bem desenhado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso usar mais de um tipo de bot na mesma operação?** Pode. Você pode ter um bot na fila Vendas, outro na fila Suporte, outro só na fila VIP. Cada fila escolhe a ferramenta que faz mais sentido pra ela.
>
> **Posso encadear automações (uma chama a outra)?** Pode. É estratégia avançada — funciona bem quando o caminho está bem desenhado.
>
> **Quanto custa rodar automação?** Depende da ferramenta. As que rodam dentro do sistema, em geral, não têm custo extra. As que usam IA generativa cobram por **tokens** consumidos.
>
> **Preciso de bot pra operar?** Não. Você pode rodar 100% humano. Bot é otimização.
>
> **Posso "esconder" do meu cliente que ele está falando com um bot?** Pode. O sistema não revela nada. A percepção depende só de como você escreveu o fluxo. Tem operações que escondem; outras deixam óbvio. É decisão sua.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Achar que bot resolve tudo.** Caso sensível (cobrança, reclamação, venda alto valor) com bot mal configurado vira cliente furioso. *Forma certa:* mapeia cenário — bot pra repetitivo e previsível, humano pra complexo e sensível.
>
> **Esquecer da transição entre bot e humano.** Bot que não "sabe" transferir quando trava deixa o cliente perdido.

#### 💡 Sugestões de Ouro  
- **Comece pequeno com bot.** 2 ou 3 perguntas frequentes já resolvem 70% do volume. Não tente cobrir 100% das interações no primeiro mês.
- **Mede o que o bot resolve vs o que ele transfere.** Se o bot tá transferindo mais de 60% dos atendimentos pra humano, ele só tá atrasando o cliente. Algo precisa mudar — ou o fluxo, ou a expectativa.
