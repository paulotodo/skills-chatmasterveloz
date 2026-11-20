# Aba Integrações em Setores & Chatbot

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-integracoes-em-setores-e-chatbot
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Aba Integrações em Setores & Chatbot

---

🧩 A aba **Integrações** é onde o Setor passa a conversa para um serviço de fora — uma plataforma de inteligência artificial ou de fluxos de conversa. Em vez de responder com um fluxo montado aqui dentro, o Setor entrega o atendimento a um serviço externo que você já usa.

É a alternativa para quem já tem um assistente pronto em outra ferramenta e não quer refazer o trabalho. O Setor continua sendo a porta de entrada; o que muda é quem conversa do outro lado.

#### O que você encontra aqui

⚡ **Um bloco por plataforma.** Cada integração disponível aparece separada, com os próprios campos — normalmente o endereço do serviço e uma chave de acesso gerada lá.

⚡ **Um bloco de Configurações Gerais.** Tempos de espera e mensagens padrão que valem para as integrações: **Expiração do Fluxo (segundos)**, **Tempo de Delay (ms)** e **Mensagem de Encerramento** (*Mensagem enviada ao encerrar o atendimento*).

⚡ **Só o que o seu plano inclui.** Esta aba não é igual em toda plataforma: cada integração é liberada separadamente, e sem a liberação no plano a aba nem aparece no cadastro do Setor. Se você não encontra a que procura, ela não faz parte do seu plano — fale com quem administra a sua conta.

⚡ **Nada obrigatório.** A maioria dos Setores nunca precisa desta aba. Ela existe para quem já mantém um assistente fora daqui.

## Como ligar uma integração

Acesse o menu **Setores & Chatbot  ›  editar o Setor  ›  aba Integrações**.

🔘 Localize o bloco da plataforma que você usa e preencha os campos dela. Cada uma pede coisas diferentes: algumas querem só endereço e chave, outras pedem também nome do fluxo ou mensagens.

🔘 As informações vêm da plataforma externa, não daqui. Você as gera lá dentro e cola aqui.

🔘 Clique em **SALVAR INTEGRAÇÕES**, no fim da aba, ou em **Salvar**, no rodapé da janela. Os dois gravam o Setor com a integração e fecham a janela. A partir daí, quem chega neste Setor conversa com o serviço externo.

⚠️ Preencher os campos não basta: o **ChatBot Externo**, na aba Geral, é o interruptor que autoriza a integração a atender. Com ele desligado, a configuração fica gravada e parada.

> **[ATENCAO]**
>
> #### Atenção
>
> Um Setor tem **um** atendimento automático de cada vez. Se este Setor já usa um fluxo ou um assistente configurado na aba Geral, ligar também uma integração externa coloca dois motores no mesmo lugar — e fica difícil prever qual responde. Escolha um por Setor.

## Próximo Passo

🧭 Conferir se o **ChatBot Externo** está ligado, no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Geral**.

🧭 Mandar uma mensagem de teste pela Conexão que aponta para este Setor e acompanhar se a resposta vem da plataforma externa.

🧭 Garantir que exista um caminho para atendimento humano. Toda automação precisa saber a hora de entregar a conversa para uma pessoa.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Não encontro a aba Integrações no cadastro do Setor. Por quê?** A aba depende do plano: sem a liberação das integrações externas, o cadastro do Setor mostra as outras abas e esta fica de fora — fale com quem administra a sua conta.
>
> **Preenchi os campos e o assistente externo não responde.** Confira o **ChatBot Externo**, na aba Geral. Ele é o interruptor que autoriza a integração a atender — sem ele ligado, a configuração fica gravada e inativa.
>
> **Onde consigo a URL e a chave?** Na própria plataforma externa, não aqui. Cada serviço tem o lugar dele para gerar a chave de acesso; esta aba só guarda o que você já criou lá.
>
> **Posso usar uma integração externa e um fluxo ao mesmo tempo?** A tela não impede, mas não é recomendado: dois motores de automação no mesmo Setor disputam a mesma conversa. Se você quer os dois, use Setores diferentes.
>
> **Preciso preencher esta aba?** Não. A maioria dos Setores funciona sem ela. Ela existe para quem já mantém um assistente em outra ferramenta.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Preencher a integração e esquecer o ChatBot Externo:** os campos ficam salvos, a tela não reclama, e o cliente continua sem resposta automática. **Solução:** ligue o **ChatBot Externo** na aba Geral do mesmo Setor.
>
> **Colar a chave com espaço no começo ou no fim:** a cópia da plataforma externa costuma trazer espaço junto, e a conexão falha sem mensagem clara. **Solução:** cole e confira o começo e o fim do campo.
>
> **Ligar a integração num Setor que já tem fluxo:** os dois disputam a conversa e o comportamento fica imprevisível. **Solução:** um motor por Setor.
>
> **Integração sem saída para pessoa:** o cliente pede para falar com alguém e o serviço externo não tem como entregar a conversa. **Solução:** desenhe na plataforma externa um caminho que devolva o atendimento para um Setor com atendentes.
