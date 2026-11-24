# Servidor de Mídia em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/servidor-de-midia-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Servidor de Mídia em Configurações

---

🧩 O card **Servidor de mídia** guarda o servidor que leva o áudio e o vídeo das chamadas: as da equipe, no **Chat Interno**, e a videochamada com o cliente, no atendimento. Vale para todas as empresas da instância, e cada empresa usa as chamadas que o plano dela libera.

A instância já vem com o servidor padrão do sistema. O card **Servidor de mídia** serve para usar um servidor próprio no lugar dele, se você quiser.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Servidor de mídia**.
>
> ➡️ Preencha **Endereço (wss://)**, **Chave (API key)** e **Segredo (API secret)** do seu servidor.
>
> ➡️ Clique em **Testar conexão** e depois em **Salvar**.

## Os campos

🔘 **Endereço (wss://):** o endereço do servidor de mídia, começando por `wss://`.

🔘 **Chave (API key)** e **Segredo (API secret):** as credenciais do servidor. O segredo salvo não volta a aparecer no campo: nas palavras da tela, *"Já existe um segredo guardado. Deixe em branco para mantê-lo."*

🔘 **Prefixo das salas (opcional):** nas palavras da tela, *"Separa as salas desta instalação quando o servidor é compartilhado."* Em branco, a tela mostra o prefixo que vale.

## Os botões

🔘 **Testar conexão:** confere endereço, chave e segredo. Com tudo certo, a resposta é *"O servidor de mídia respondeu: endereço, chave e segredo conferem."*

🔘 **Apagar e voltar ao servidor padrão:** aparece quando o servidor em uso é o salvo na tela. Pede confirmação e, apagado, volta a valer o servidor padrão do sistema.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso cadastrar um Servidor de mídia para as chamadas funcionarem?** Não. A instância já usa o servidor padrão do sistema. Cadastre um próprio no card **Servidor de mídia** só se quiser trocar.
>
> **Preciso cadastrar o Servidor de mídia em cada empresa?** Não. O **Servidor de mídia** vale para todas as empresas da instância. O que muda de uma empresa para outra é o plano: cada uma usa só as chamadas que ele libera.
>
> **Salvei o Servidor de mídia e uma empresa continua sem chamadas.** Confira o plano da empresa no menu **Configurações  ›  Planos**: as chamadas da equipe dependem de **Chamadas no chat interno**, e a videochamada, de **Videochamada com o cliente**.
