# API Criar Plano

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-plano
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Planos › API Criar Plano

---

🧩 Cria **um plano** na instalação, com os mesmos campos do cadastro pela tela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/plans
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
    "name": "Profissional",
    "users": 10,
    "connections": 3,
    "connectionLimits": {
        "whatsappMeta": 1
    },
    "queues": 10,
    "value": 199.90,
    "useWhatsapp": true,
    "useFacebook": false,
    "useInstagram": false,
    "useCampaigns": true,
    "useSchedules": true,
    "useInternalChat": false,
    "useExternalApi": true,
    "useKanban": true,
    "usePixel": false,
    "usePerfex": false,
    "useRD": false,
    "useCV": false,
    "useIXC": false,
    "useAI": true,
    "useCHAMA": false,
    "useTYPE": false,
    "useZAIA": false,
    "useGPT": true,
    "useGPTA": false,
    "useAnswerFromIA": false,
    "useHS": false,
    "useNNN": false,
    "useHUB": false,
    "useCRM": true,
    "useFLOW": true,
    "useBTN": false,
    "useCALL": false,
    "useVOIP": false,
    "useVIDEOCALL": false,
    "useVoiceBilling": false,
    "useDIFY": false,
    "usePUSH": false,
    "useWABAOWN": false,
    "useWABAAINI": false,
    "useProducts": true,
    "useServices": false,
    "useWEBCHAT": false,
    "useCHATEXTERNO": false,
    "useTELEGRAMAINI": false,
    "useINSTAGRAMAINI": false,
    "useTIKTOKAINI": false,
    "useFACEBOOKAINI": false,
    "useFACEBOOKPORTAL": false,
    "useINSTAGRAMPORTAL": false,
    "useInstagramAuto": false,
    "useEMAIL": false,
    "useRCS": false,
    "useAIPROVIDERS": false,
    "useCRMCOPILOT": false,
    "useMobileDocker": false,
    "useQuadro": true,
    "useInternal": false
}
```

➡️ **“name”:** nome do plano, com pelo menos 2 caracteres e único.

➡️ **“users”:** quantos usuários a empresa pode ter.

➡️ **“connections”:** quantas conexões a empresa pode ter, no total.

➡️ **“queues”:** quantos Setores a empresa pode ter.

➡️ **“value”:** valor do plano.

➡️ **“connectionLimits”:** teto por grupo de canal — `whatsapp`, `whatsappMeta`, `hub`, `telegramInc` e os demais. Grupo que você não informar herda o limite geral de `connections`.

➡️ **Os módulos do plano** são os campos que começam com `use`, cada um `true` ou `false`. Cada um corresponde a uma opção da tela de Planos:

◽ `useWhatsapp`, `useFacebook`, `useInstagram`, `useCampaigns`, `useSchedules`, `useInternalChat`, `useExternalApi`, `useKanban`, `usePixel`, `usePerfex`, `useRD`, `useCV`, `useIXC`, `useAI`, `useCHAMA`, `useTYPE`, `useZAIA`, `useGPT`, `useGPTA`, `useAnswerFromIA`, `useHS`, `useNNN`, `useHUB`, `useCRM`, `useFLOW`, `useBTN`, `useCALL`, `useVOIP`, `useVIDEOCALL`, `useVoiceBilling`, `useDIFY`, `usePUSH`, `useWABAOWN`, `useWABAAINI`, `useProducts`, `useServices`, `useWEBCHAT`, `useCHATEXTERNO`, `useTELEGRAMAINI`, `useINSTAGRAMAINI`, `useTIKTOKAINI`, `useFACEBOOKAINI`, `useFACEBOOKPORTAL`, `useINSTAGRAMPORTAL`, `useInstagramAuto`, `useEMAIL`, `useRCS`, `useAIPROVIDERS`, `useCRMCOPILOT`, `useMobileDocker`, `useQuadro`, `useInternal`.

⚠️ **A lista de módulos cresce.** Quando a plataforma ganha um recurso novo, ele aparece aqui sem aviso — para ver a lista de hoje, consulte um plano que já existe e olhe os campos `use` da resposta.

◽ Nem todo módulo do plano tem campo na tela: o `useProducts`, por exemplo, está no plano e não aparece lá.

◽ A chamada passa pela mesma conferência da tela: módulo que a tela de Planos recusa também é recusado aqui.

◽ São obrigatórios o `name`, o `users`, o `connections`, o `queues` e o `value`. Os números não podem ser negativos.

⚠️ **O exemplo acima traz tudo o que a criação aceita, para você escolher** — não é obrigatório enviar inteiro. Módulo que você não mandar nasce desligado.

◽ Nome repetido é recusado.

◽ Campo que não é do plano volta na resposta, em `camposIgnorados`.

⚠️ **Não existe limite por empresa por cima do plano.** Para dar mais a um cliente, o caminho é trocar o plano dele, e não abrir uma exceção.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/plans',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "name": "Profissional",
    "users": 10,
    "connections": 3,
    "connectionLimits": {
        "whatsappMeta": 1
    },
    "queues": 10,
    "value": 199.90,
    "useWhatsapp": true,
    "useFacebook": false,
    "useInstagram": false,
    "useCampaigns": true,
    "useSchedules": true,
    "useInternalChat": false,
    "useExternalApi": true,
    "useKanban": true,
    "usePixel": false,
    "usePerfex": false,
    "useRD": false,
    "useCV": false,
    "useIXC": false,
    "useAI": true,
    "useCHAMA": false,
    "useTYPE": false,
    "useZAIA": false,
    "useGPT": true,
    "useGPTA": false,
    "useAnswerFromIA": false,
    "useHS": false,
    "useNNN": false,
    "useHUB": false,
    "useCRM": true,
    "useFLOW": true,
    "useBTN": false,
    "useCALL": false,
    "useVOIP": false,
    "useVIDEOCALL": false,
    "useVoiceBilling": false,
    "useDIFY": false,
    "usePUSH": false,
    "useWABAOWN": false,
    "useWABAAINI": false,
    "useProducts": true,
    "useServices": false,
    "useWEBCHAT": false,
    "useCHATEXTERNO": false,
    "useTELEGRAMAINI": false,
    "useINSTAGRAMAINI": false,
    "useTIKTOKAINI": false,
    "useFACEBOOKAINI": false,
    "useFACEBOOKPORTAL": false,
    "useINSTAGRAMPORTAL": false,
    "useInstagramAuto": false,
    "useEMAIL": false,
    "useRCS": false,
    "useAIPROVIDERS": false,
    "useCRMCOPILOT": false,
    "useMobileDocker": false,
    "useQuadro": true,
    "useInternal": false
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/plans' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Profissional","users":10,"connections":3,"connectionLimits":{"whatsappMeta":1},"queues":10,"value":199.9,"useWhatsapp":true,"useFacebook":false,"useInstagram":false,"useCampaigns":true,"useSchedules":true,"useInternalChat":false,"useExternalApi":true,"useKanban":true,"usePixel":false,"usePerfex":false,"useRD":false,"useCV":false,"useIXC":false,"useAI":true,"useCHAMA":false,"useTYPE":false,"useZAIA":false,"useGPT":true,"useGPTA":false,"useAnswerFromIA":false,"useHS":false,"useNNN":false,"useHUB":false,"useCRM":true,"useFLOW":true,"useBTN":false,"useCALL":false,"useVOIP":false,"useVIDEOCALL":false,"useVoiceBilling":false,"useDIFY":false,"usePUSH":false,"useWABAOWN":false,"useWABAAINI":false,"useProducts":true,"useServices":false,"useWEBCHAT":false,"useCHATEXTERNO":false,"useTELEGRAMAINI":false,"useINSTAGRAMAINI":false,"useTIKTOKAINI":false,"useFACEBOOKAINI":false,"useFACEBOOKPORTAL":false,"useINSTAGRAMPORTAL":false,"useInstagramAuto":false,"useEMAIL":false,"useRCS":false,"useAIPROVIDERS":false,"useCRMCOPILOT":false,"useMobileDocker":false,"useQuadro":true,"useInternal":false}'
```
