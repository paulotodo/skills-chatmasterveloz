# Trust Proxy em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-trust-proxy
- **Categoria:** Recursos
- **Menu:** Configurações › Trust Proxy em Configurações

---

🧩 O card **Trust Proxy** diz ao servidor quantas camadas de proxy existem entre quem acessa e ele — é o que faz o IP real de cada usuário aparecer certo nos registros.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Trust Proxy**.
>
> ➡️ Informe o número em **Trust proxy (hops)** e clique em **Salvar**. O valor em vigor aparece em **Aplicado em runtime**.

## O campo

🔘 **Trust proxy (hops):** quantos proxies há na frente do servidor. Nas palavras da tela: *1 = atrás de Nginx local. 2 = Cloudflare/CDN antes do Nginx. 0 = sem proxy. O valor é persistido e aplicado imediatamente, sem precisar reiniciar.*

⚠️ Valor errado tem dois sintomas: com número a menos, todo mundo aparece com o mesmo IP (o do proxy); com número a mais, o IP passa a ser o que o cliente disser que é. Conte as camadas reais da sua infraestrutura.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Todos os acessos aparecem com o mesmo IP.** O valor está baixo para a sua infraestrutura. Se há CDN antes do servidor web, é **2**.
>
> **Preciso reiniciar depois de salvar?** Não. A tela aplica na hora e mostra em **Aplicado em runtime**.
