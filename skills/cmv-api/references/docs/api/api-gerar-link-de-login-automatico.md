# API Gerar Link de Login Automático

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-gerar-link-de-login-automatico
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Gerar Link de Login Automático

---

🧩 Gera **um link de login automático**, que abre o painel já logado como uma pessoa da equipe, também dentro de um iframe.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/login-automatico
```

##### Método

```
POST
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "email": "atendente@empresa.com",
    "destino": "/tickets",
    "validadeSegundos": 60,
    "status": "offline"
}
```

➡️ **“email”:** o e-mail de quem entra, como está no cadastro da pessoa no menu **Equipe**. **Obrigatório**, ou o `userId` no lugar dele.

◽ Para usar o ID, troque a linha por `"userId": 18`, com o **ID** que aparece no card da pessoa, no menu **Equipe**.

◽ A pessoa precisa ser desta empresa e estar ativa. Pessoa de outra empresa, ou inativa, faz a chamada ser recusada.

➡️ **“destino”:** a tela de chegada, um caminho do painel como `/tickets` ou `/contacts`.

◽ Sem ele, ou com um endereço de fora da plataforma, a pessoa chega à **Página inicial após o login** escolhida no cadastro dela, no menu **Equipe  ›  editar o usuário**. Sem nenhuma escolhida, chega aos **Chats**.

➡️ **“validadeSegundos”:** quantos segundos o link vale antes de ser aberto, de 10 a 300. Sem ele, o link vale 60 segundos.

➡️ **“status”:** o status com que a pessoa entra: `online`, `away` (Ausente) ou `offline`. Sem ele, a pessoa entra com o status que já tinha.

◽ Ausente e Offline não recebem atendimentos do rodízio.

➡️ A resposta traz o link no campo `url` e o horário em que ele vence em `expiraEm`. Abra o `url` na janela do navegador, ou como `src` de um iframe na página do seu sistema, antes desse horário.

◽ O link vale uma vez só. Aberto de novo, ou depois de vencer, ele mostra *"Este link de acesso venceu ou já foi usado. Peça um novo na plataforma de origem."* Peça um link novo a cada entrada.

⚠️ **O login automático precisa estar ligado** no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**, em **Ligar o login automático**. Desligado, a chamada é recusada.

⚠️ **Faça esta chamada no servidor do seu sistema, nunca no navegador.** O Token da Empresa dá acesso à empresa inteira, e no código de uma página ele fica à vista de quem abrir.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/login-automatico',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "email": "atendente@empresa.com",
    "destino": "/tickets",
    "validadeSegundos": 60,
    "status": "offline"
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/login-automatico' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"email":"atendente@empresa.com","destino":"/tickets","validadeSegundos":60,"status":"offline"}'
```
