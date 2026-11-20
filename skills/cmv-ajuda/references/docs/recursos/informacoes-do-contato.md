# Informações do Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/informacoes-do-contato
- **Categoria:** Recursos
- **Menu:** Chats / Tickets › Informações do Contato

---

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/23623-chats-informacoes-contato-1024x546.jpg)Ao clicar no contato do ticket, uma aba lateral é aberta com mais **informações sobre o contato**. Você pode **Editar o Contato** nessa parte lateral, assim como adicionar **Observações** sobre a conversa.

Essa seção lateral pode ser personalizada para cada conexão, através de um iframe externo que recebe os dados do ticket, tornando a experiência ainda mais exclusiva.

## Iframe Externo de Contato

Para adicionar um iframe lateral em uma conexão acesse → Conexões > editar Conexão

No campo "**Iframe Externo - Integração / Contato**" digite a URL completa de sua página que será carregada na parte lateral via iframe.

Nosso sistema envia dados do ticket **via GET** (por meio da URL), permitindo que seu iframe acesse e utilize essas informações para personalizar a experiência do usuário.

## Quais dados são enviados para o iframe de contato?

```
Segue a lista dos dados do ticket
que são enviados via GET ao seu iframe:
contactNumber = número do contato
contactName = nome do contato
contactEmail = email do contato
contactCPFCNPJ = doc do contato
contactId = ID do contato
ticketId = ID do ticket
companyId = ID da empresa
backendURL = backendURL de API
userId = ID do atendente do ticket
ticket_userName = Nome do atendente do ticket
ticket_userLevel = Perfil do atendente do ticket
ticket_connectionId = ID da conexão
ticket_UUID = UUID do ticket
user_LoggedIn = ID do usuário logado
user_LoggedName = Nome do usuário logado
user_LoggedLevel = Perfil do usuário logado
```

## Como pegar os dados GET enviados usando Javascript

```
// Função para obter os parâmetros da URL
function getURLParameter(name) {
  // Cria uma expressão regular para encontrar o parâmetro na URL
  var regex = new RegExp('[?&]' + name + '=([^&]*)');
  var results = regex.exec(window.location.href);
  // Se o parâmetro for encontrado, retorna o valor decodificado
  return results ? decodeURIComponent(results[1]) : null;
}
// Obtenção dos dados enviados via GET
const contactNumber = getURLParameter('contactNumber');
const contactName = getURLParameter('contactName');
const contactEmail = getURLParameter('contactEmail');
const contactCPFCNPJ = getURLParameter('contactCPFCNPJ');
const contactId = getURLParameter('contactId');
const ticketId = getURLParameter('ticketId');
const companyId = getURLParameter('companyId');
const backendURL = getURLParameter('backendURL');
const userId = getURLParameter('userId');
const ticket_userName = getURLParameter('ticket_userName');
const ticket_userLevel = getURLParameter('ticket_userLevel');
const ticket_connectionId = getURLParameter('ticket_connectionId');
const ticket_UUID = getURLParameter('ticket_UUID');
const user_LoggedIn = getURLParameter('user_LoggedIn');
const user_LoggedName = getURLParameter('user_LoggedName');
const user_LoggedLevel = getURLParameter('user_LoggedLevel');
// Exibe os dados no console ou usa conforme necessário
console.log("contactNumber:", contactNumber);
console.log("contactName:", contactName);
console.log("contactEmail:", contactEmail);
console.log("contactCPFCNPJ:", contactCPFCNPJ);
console.log("contactId:", contactId);
console.log("ticketId:", ticketId);
console.log("companyId:", companyId);
console.log("backendURL:", backendURL);
console.log("userId:", userId);
console.log("ticket_userName:", ticket_userName);
console.log("ticket_userLevel:", ticket_userLevel);
console.log("ticket_connectionId:", ticket_connectionId);
console.log("ticket_UUID:", ticket_UUID);
console.log("user_LoggedIn:", user_LoggedIn);
console.log("user_LoggedName:", user_LoggedName);
console.log("user_LoggedLevel:", user_LoggedLevel);
// Agora você pode usar esses dados em seu iframe.
```

## Como pegar os dados GET enviados usando PHP

```php
<?php
// Função para obter os parâmetros da URL
function getURLParameter($name) {
    // Verifica se o parâmetro está presente na URL e retorna seu valor
    return isset($_GET[$name]) ? urldecode($_GET[$name]) : null;
}
// Obtenção dos dados enviados via GET
$contactNumber = getURLParameter('contactNumber');
$contactName = getURLParameter('contactName');
$contactEmail = getURLParameter('contactEmail');
$contactCPFCNPJ = getURLParameter('contactCPFCNPJ');
$contactId = getURLParameter('contactId');
$ticketId = getURLParameter('ticketId');
$companyId = getURLParameter('companyId');
$backendURL = getURLParameter('backendURL');
$userId = getURLParameter('userId');
$ticket_userName = getURLParameter('ticket_userName');
$ticket_userLevel = getURLParameter('ticket_userLevel');
$ticket_connectionId = getURLParameter('ticket_connectionId');
$ticket_UUID = getURLParameter('ticket_UUID');
$user_LoggedIn = getURLParameter('user_LoggedIn');
$user_LoggedName = getURLParameter('user_LoggedName');
$user_LoggedLevel = getURLParameter('user_LoggedLevel');
// Exibe os dados ou os utiliza conforme necessário
echo "contactNumber: " . $contactNumber . "<br></br>";
echo "contactName: " . $contactName . "<br></br>";
echo "contactEmail: " . $contactEmail . "<br></br>";
echo "contactCPFCNPJ: " . $contactCPFCNPJ . "<br></br>";
echo "contactId: " . $contactId . "<br></br>";
echo "ticketId: " . $ticketId . "<br></br>";
echo "companyId: " . $companyId . "<br></br>";
echo "backendURL: " . $backendURL . "<br></br>";
echo "userId: " . $userId . "<br></br>";
echo "ticket_userName: " . $ticket_userName . "<br></br>";
echo "ticket_userLevel: " . $ticket_userLevel . "<br></br>";
echo "ticket_connectionId: " . $ticket_connectionId . "<br></br>";
echo "ticket_UUID: " . $ticket_UUID . "<br></br>";
echo "user_LoggedIn: " . $user_LoggedIn . "<br></br>";
echo "user_LoggedName: " . $user_LoggedName . "<br></br>";
echo "user_LoggedLevel: " . $user_LoggedLevel . "<br></br>";
// Agora você pode usar esses dados em seu iframe.
?>
```
