# Execução de Código JS

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-execucao-de-codigo-js
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Execução de Código JS

---

🧩 O bloco **Execução de Código JS** roda um trecho de JavaScript no meio do fluxo. Serve para tratar um dado antes de usá-lo, como limpar um CPF ou pegar o DDD do telefone, e para chamar uma API escrevendo a chamada à mão.

O que o código devolve no `return` pode ser guardado por um bloco **Variável** logo depois. Para chamar uma API sem escrever código, use o bloco **HTTP Request**.

**🏷️ Categoria: Dados - Integração**

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Execução de Código JS**.
>
> ➡️ Escreva o código, use **Testar Código** e clique em **Adicionar**.
>
> ➡️ Para guardar o resultado, ligue um bloco **Variável** logo depois.

## Como configurar o bloco Execução de Código JS

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Execução de Código JS**

🔘 **Tipo:** **MENU** ou **REQUISIÇÃO**. Para chamar um link externo, como nos exemplos abaixo, use **REQUISIÇÃO**, que processa o código na hora.

🔘 **Webhook (JS Script):** o código JavaScript. O valor do `return` é o resultado do bloco.

🔘 **Testar Código:** executa o código num ambiente de teste. A janela mostra as variáveis que encontrou no código e pede um **Payload de Teste (JSON)** com valores para elas.

🔲 Para finalizar, clique em **Adicionar**.

Os trechos entre `{{...}}` são substituídos pelos dados do atendimento quando o fluxo roda, e as variáveis do fluxo entram como `%nome_da_variavel%`. A variável do fluxo é trocada pelo valor dentro do próprio código, antes de ele rodar.

## Como guardar o resultado numa variável

Ligue um bloco **Variável** logo depois da **Execução de Código JS**: ela grava o que o código devolveu no `return`.

Devolva no `return` um texto ou um número. Um objeto devolvido direto, como `return { nome: 'Ana' }`, aparece como *[object Object]* quando a variável é usada numa mensagem. Para guardar um JSON inteiro, devolva o JSON como texto, com `return JSON.stringify(dados);`.

Para usar um campo de um JSON guardado numa variável, escreva o campo depois de um ponto, direto na mensagem: `%dados.nome%`, e um campo dentro de outro, `%dados.cidade.nome%`. Dentro de um segundo bloco **Execução de Código JS**, o `JSON.parse` também lê a variável e devolve só o campo:

```
const d = JSON.parse('%dados%');
return d.nome;
```

O mesmo `JSON.parse` lê a resposta de um **HTTP Request** guardada em **Variável Única**, como `JSON.parse('%httpResponse%')`.

## Exemplo: chamar uma API da própria plataforma

```
// definir
let endpoint = "https://{{backendURL}}/api/url";
let method = "POST";
let payload = {
  "number": "{{number}}",
  "contactId": "{{contact_id}}",
  "name": "{{name}}",
  "firstName": "{{firstName}}",
  "ticketId": "{{ticket_id}}",
  "protocol": "{{protocol}}",
  "queueId": "{{queue}}",
  "userName": "{{user}}",
  "connectionName": "{{connection}}",
  "companyName": "{{name_company}}",
  "backendURL": "{{backendURL}}",
  "token": "{{connection_token}}",
  "dataHora": "{{data_hora}}"
  // apague ou insira outros payloads desejados aqui
};
let authorization = "{{connection_token}}";
// estrutura
try {
    const response = await axios({
      url: endpoint,
      method: method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authorization
      },
      data: payload,
      maxBodyLength: Infinity
    });
    return JSON.stringify(response.data, null, 2);
} catch (error) {
    return "Algo deu errado: " + error.message;
}
```

O código monta o endereço com `{{backendURL}}`, envia os dados do atendimento e devolve a resposta como texto:  
- `{{number}}` — telefone do contato
- `{{contact_id}}` e `{{ticket_id}}` — identificadores do contato e do atendimento
- `{{name}}` e `{{firstName}}` — nome completo e primeiro nome do contato
- `{{protocol}}` — protocolo do atendimento
- `{{connection_token}}` — token da conexão, usado na autorização

## Exemplo: chamar uma API ou URL externa

```
// definir
let endpoint = "https://enderecoExterno";
let method = "POST";
let payload = {
  "number": "{{number}}",
  "contactId": "{{contact_id}}",
  "name": "{{name}}",
  "firstName": "{{firstName}}",
  "ticketId": "{{ticket_id}}",
  "protocol": "{{protocol}}",
  "queueId": "{{queue}}",
  "userName": "{{user}}",
  "connectionName": "{{connection}}",
  "companyName": "{{name_company}}",
  "backendURL": "{{backendURL}}",
  "token": "{{connection_token}}",
  "dataHora": "{{data_hora}}"
  // apague ou insira outros payloads desejados aqui
};
// estrutura
try {
    const response = await axios({
      url: endpoint,
      method: method,
      headers: {
        'Content-Type': 'application/json'
      },
      data: payload,
      maxBodyLength: Infinity
    });
    return JSON.stringify(response.data, null, 2);
} catch (error) {
    return "Algo deu errado: " + error.message;
}
```

Igual ao anterior, mas o endereço é o do seu sistema e a chamada vai sem o token da plataforma.

## Exemplos de tratamento de dados

### Guardar um texto

```
let dados = "Meu nome é João";
return dados;
```

### Pegar o DDD do contato

```
let meuNumero = "{{number}}";
const ddd = parseInt(meuNumero.substring(2, 4), 10);
return ddd;
```

### Limpar e validar um CPF

```
function tratarEValidarCPF(valor) {
    let cpf = String(valor).replace(/\D/g, '');
    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
        return "CPF inválido!";
    }
    function validarDigito(base) {
        let soma = 0;
        let peso = base.length + 1;
        for (let i = 0; i < base.length; i++) {
            soma += parseInt(base[i]) * peso--;
        }
        let resto = soma % 11;
        return resto < 2 ? 0 : 11 - resto;
    }
    const digito1 = validarDigito(cpf.substring(0, 9));
    const digito2 = validarDigito(cpf.substring(0, 10));
    if (digito1 !== parseInt(cpf[9]) || digito2 !== parseInt(cpf[10])) {
        return "CPF inválido!";
    }
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
}
return tratarEValidarCPF("%cpf_tratar%");
```

O exemplo do CPF lê a variável `%cpf_tratar%`, guardada antes por um bloco **Variável**, e devolve o CPF formatado ou *CPF inválido!*.

### Formatar um CNPJ

```
function tratarCNPJ(mensagem) {
    let cnpj = String(mensagem).replace(/\D/g, '');
    if (cnpj.length !== 14) {
        return "CNPJ inválido! Certifique-se de que digitou corretamente.";
    }
    return cnpj.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");
}
return tratarCNPJ("%resposta_cnpj_lead%");
```

### Tirar as marcações HTML de um texto

```
function removeHTML(htmlString) {
    return String(htmlString).replace(/<[^>]*>/g, '');
}
return removeHTML("<p>Olá, <b>flowbuilders</b>!</p>");
```

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a linguagem aceita pelo bloco Execução de Código JS?** JavaScript.
>
> **Como guardo o resultado do bloco Execução de Código JS?** Com um bloco **Variável** logo depois. A **Variável** grava o que o código devolveu no `return`.
>
> **Posso usar uma variável do fluxo dentro do código da Execução de Código JS?** Pode. Escreva `%nome_da_variavel%` no código, como em `JSON.parse('%dados%')`: a variável é trocada pelo valor antes de o código rodar.
>
> **Posso chamar um endpoint da própria plataforma no bloco Execução de Código JS?** Pode, inclusive usando os dados do atendimento entre `{{...}}` e as variáveis do fluxo entre `%...%`.
>
> **Prefiro não escrever código. Como chamo uma API?** Use o bloco **HTTP Request**, que monta a chamada pelos campos da janela.

> **[ERROS]**
>
> #### Erros Comuns
>
> **[object Object] no texto:** a mensagem mostra *[object Object]* no lugar do resultado. O código devolveu um objeto no `return`. **Solução:** devolva só o valor que vai usar, como `return dados.nome`, ou o JSON como texto, com `return JSON.stringify(dados);`.
