# Access Token Meta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/access-token-meta
- **Categoria:** Recursos
- **Menu:** Integrações › Access Token Meta

---

🔑 O **Access Token da Meta** (Facebook) é uma **credencial de autenticação** usada para permitir que aplicações ou sistemas se comuniquem com a Meta de forma segura e autorizada.

Em nosso sistema, utilizaremos o Access Token da Meta para chamar a API de Eventos da Meta (API de Conversão), com o objetivo de **registrar eventos de conversão no pixel**.

## Como conseguir o Access Token da Meta

1️⃣ Em seu **Gerenciador de Anúncios** da Meta, acesse o menu → Gerenciador de Eventos

2️⃣ Na **Conta de Anúncio** desejada, acesse o menu → Fontes de Dados

3️⃣ Selecione o nome de um de seus **dados (pixel)** (se necessário vá antes em "+ Conectar dados"). Dica: abaixo do nome você pode pegar o número de Identificação (ID) do seu pixel.

4️⃣ Siga para a aba **Configurações**

5️⃣ Em **Configurar Integração direta**, selecione a opção "Configurar com a Dataset Quality API" e gerar seu Access Token.

Guarde seu token para utilizar no Pixel Meta dentro de nossa plataforma!

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/22139-access-token-meta-1024x536.jpg)

## Como configurar um Pixel da Meta em nosso sistema

O Pixel da Meta em nosso sistema pode ser configurado em uma Tag ou em um bloco do FlowBuilder Nativo.

**➡️ Access Token:** seu token da Meta.

**➡️ Pixel ID:** o ID (identificador) do seu pixel.

**➡️ Nome do Evento:** deve ser digitado exatamente igual a documentação da Meta: **Leads**, **CompleteRegistration**, **AddToWishlist**, **AddToCart**, **Purchase**, por exemplo. (documentação completa em [https://developers.facebook.com/docs/meta-pixel/reference](https://developers.facebook.com/docs/meta-pixel/reference))

**➡️ Custom Data:** json das propriedades do evento. Consulte a documentação para saber os campos opcionais e obrigatórios.

No evento Purchase é obrigatório "currency" e "value". Veja um exemplo:

```json
{
    "value": 115.00,
    "currency": "BRL"
}
```

**➡️ Source:** indica o local que o evento está sendo enviando. Webiste, server, crm ou nesse caso poderia colocar o nome da nossa plataforma Chat Master Veloz.
