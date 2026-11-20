# Asaas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-asaas
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Asaas

---

🧩 O bloco **Asaas** liga o fluxo ao gateway de pagamentos Asaas. Com o CPF ou o CNPJ do cliente, ele consulta se há cobrança pendente e envia a fatura pronta para pagamento.

**🏷️ Categoria: Financeiro - Integração**

☑️ **Autoatendimento:** emissão de segunda via de boleto sem ninguém da equipe, a qualquer hora.

☑️ **Menos inadimplência:** facilita a vida de quem quer pagar, com o link na hora.

☑️ **Agilidade:** o fluxo informa quantas faturas estão abertas e já foca na cobrança prioritária.

![Flowbuilder - bloco Asaas](https://clihelper.chatmasterveloz.com/docs-imagem/14344-bloco-asaas-1.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Gere a chave de API no Asaas, em **Perfil**, depois **Integrações** e **Chaves de API**.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Asaas**.
>
> ➡️ Cole o token e clique em **Adicionar**.
>
> ➡️ Antes do bloco, use uma **Pergunta** para pedir o CPF ou CNPJ, só números. Depois dele, ligue as saídas **Sucesso** e **Erro**.

## Como configurar o bloco Asaas

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Asaas**

![Formulário do bloco Asaas](https://clihelper.chatmasterveloz.com/docs-imagem/14344-bloco-asaas-formulario.jpg)

A janela **Adicionar bloco: Asaas** tem um campo:

🔘 **Token de Integração Asaas:** a chave de API gerada no Asaas.

🔲 Para finalizar, clique em **Adicionar**.

## Como conseguir o token no Asaas

No site do **Asaas**, abra **Perfil**, depois **Integrações** e **Chaves de API**. Clique em **Gerar Chave de API**, dê um nome à chave e copie o valor gerado.

## Como o bloco Asaas funciona na prática

O bloco usa o CPF ou CNPJ, só com números, informado pelo cliente. Peça esse dado num bloco **Pergunta** antes do Asaas e avise o cliente para digitar só números; se quiser validar, use um bloco **Execução de Código JS**.

No desenho, o bloco tem duas saídas:

🟢 **Sucesso:** o Asaas encontrou o cliente e processou a busca.

🔴 **Erro:** houve falha na API do Asaas, o serviço caiu ou o documento é inválido.

No **Sucesso**, o fluxo informa se o cliente tem ou não faturas em aberto, indica o total de faturas e envia o link de pagamento da mais recente. Para pagar as mais antigas, o cliente quita a mais recente primeiro ou é transferido para uma pessoa.

📌 Depois de cada saída, um bloco **Intervalo** de alguns segundos ajuda o cliente a ler antes da próxima mensagem.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente digitou o CPF com pontos. O bloco Asaas funciona?** Não. A API do Asaas costuma recusar o documento com pontos e traços. Peça só números e, se precisar, limpe o dado com um bloco **Execução de Código JS**.
>
> **Posso escolher qual fatura o bloco Asaas envia?** Não. O bloco envia sempre a mais recente. Para negociar faturas antigas, leve o cliente a um Setor com o bloco **Setor**.
>
> **Quais formas de pagamento o link do Asaas aceita?** O link abre a fatura padrão do Asaas, com PIX, boleto ou cartão, conforme configurado no painel do Asaas.
>
> **Perdi o token do Asaas. E agora?** O token aparece só uma vez, na criação. Exclua a chave antiga no Asaas, gere outra e cole o novo token no bloco.

> **[ERROS]**
>
> #### Erros Comuns
>
> **CPF com pontos na Pergunta:** o cliente digita com traços e o bloco não encontra nada. **Solução:** avise para digitar só números ou trate o dado antes do Asaas.
>
> **Achar que todas as faturas vão aparecer:** o cliente tem cinco boletos atrasados, o fluxo avisa que são cinco e envia só o link do último. **Solução:** combine com a equipe como tratar as faturas antigas.
>
> **Saída Erro sem ligação:** com o Asaas fora do ar, o cliente fica parado no fluxo. **Solução:** ligue a saída **Erro** a uma mensagem ou a um Setor.
