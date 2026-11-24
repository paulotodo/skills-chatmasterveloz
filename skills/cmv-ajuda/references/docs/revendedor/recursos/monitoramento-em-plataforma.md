# Monitoramento em Plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/monitoramento-em-plataforma
- **Categoria:** Recursos
- **Menu:** Configurações › Plataforma em Configurações › Monitoramento em Plataforma

---

🧩 O grupo **Monitoramento** acompanha a instância por fora: as tags do Google na página de cadastro, os números de funcionamento do servidor para o seu Prometheus e o diagnóstico de desempenho que o suporte do servidor pede. Tudo aqui vale para a instância inteira.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Plataforma**, grupo **Monitoramento**.
>
> ➡️ Cada campo grava assim que você muda o valor. Não há botão Salvar.

## ⚡ Google Analytics

Os dois campos de **Google Analytics** colocam as suas tags do Google na **página de cadastro (Signup)** — a página pública onde alguém escolhe um plano e cria a própria empresa. É o seu funil de entrada que passa a ser medido.

➡️ No Google Analytics, copie o **ID de medição** da propriedade. No Tag Manager, copie o **ID do contêiner**.

➡️ Cole cada um no campo correspondente.

🔘 **Google Analytics Measurement ID (ex: G-XXXXXXXXXX):** o ID de medição da propriedade, que começa com `G-`. *Este ID será usado na página de cadastro (Signup)*.

🔘 **Google Tag Manager ID (ex: GTM-XXXXXXX):** o ID do contêiner do Tag Manager, que começa com `GTM-`. Mesma página, e opcional — só faz sentido se você usa o Tag Manager.

### O que entra na medição

Entra o que acontece na página de cadastro: quem chegou, de onde veio e quem terminou criando a empresa. É o caminho entre o anúncio (ou o link) e a conta nova.

⚠️ Sem o cadastro público liberado — **Registro (Inscrição) Permitida? = Sim**, na seção **Configurações Globais** do grupo **Marca e acesso** —, não há o que medir: a página que recebe a tag é justamente a de quem se cadastra sozinho.

### Medir não é converter

A plataforma faz uma coisa só: coloca a tag na página. O resto é configuração da sua conta do Google.

➡️ Com o **ID de medição**, o cadastro concluído vira evento no Analytics — e é esse evento que você importa como conversão no Google Ads, para a campanha otimizar por ele.

➡️ Com o **Tag Manager**, você dispara outras tags na mesma página sem precisar mexer na plataforma de novo: conversão de outras redes, remarketing, o que a sua operação de mídia usar.

## ⚡ Infra / Observabilidade

A seção **Infra / Observabilidade** deixa você acompanhar a saúde do servidor da sua instância por fora da plataforma. O servidor publica num endereço próprio, o `/metrics`, os números de funcionamento dele — memória, uso de processador, versão, há quanto tempo está no ar — e o **METRICS_TOKEN** é a senha que decide quem pode ler esses números.

![Painel de monitoramento estilo Grafana com CPU, memória, heap e atraso do event loop da instância](https://revendedor.chatmasterveloz.com/docs-imagem/ed-6aa329be3f673.png)

### O que você ganha

O ganho é perceber problema **antes do seu cliente**. Dois exemplos do que dá para acompanhar:

☑️ **Atraso de resposta do servidor:** existe um número que sobe quando o servidor começa a engasgar. Enquanto ele está baixo, tudo responde na hora; quando dispara, o atendente sente a tela lenta e o cliente sente a demora. Ver esse número subindo é o aviso para agir antes de o atendimento travar.

☑️ **Consumo de memória ao longo dos dias:** se a memória sobe e nunca volta, é vazamento — o serviço vai cair sozinho de madrugada. No gráfico você vê a tendência com antecedência; sem ele, descobre pela queda.

São números de máquina — não são dados de atendimento. Aqui não entra quantidade de tickets, de mensagens ou de contatos; entra a saúde de quem sustenta tudo isso.

### Passo a passo

➡️ Aqui na plataforma, na seção **Infra / Observabilidade**, preencha um token longo em **METRICS_TOKEN**.

➡️ Numa VPS sua, instale o **Prometheus** e o **Grafana**.

➡️ No Prometheus, crie um alvo para o `/metrics` da sua instância informando o mesmo token.

➡️ No Grafana, conecte o Prometheus, monte os painéis e configure os alertas.

### Como funciona na prática

O monitoramento roda **fora da plataforma, numa máquina sua** — uma VPS. Nessa máquina você instala dois programas gratuitos:

🔘 **Prometheus:** de tempos em tempos ele visita o `/metrics` da sua instância pela internet, apresenta o token e guarda os números, montando o histórico.

🔘 **Grafana:** lê o que o Prometheus guardou e transforma em gráficos na tela. É nele também que você cria os alertas — um aviso por e-mail, Telegram ou outro canal quando um número passa do limite que você definir.

### Exemplo de configuração do Prometheus

No arquivo do Prometheus, o alvo fica assim — troque `SEU_TOKEN_AQUI` pelo valor que você colocou no campo:

```
scrape_configs:
  - job_name: minha-instancia
    scheme: https
    metrics_path: /metrics
    authorization:
      type: Bearer
      credentials: SEU_TOKEN_AQUI
    static_configs:
      - targets: ['api2.chatmasterveloz.com']
```

O que cada parte faz:  
- **scheme / metrics_path:** dizem que o endereço é `https` e termina em `/metrics`.
- **authorization:** manda o token no cabeçalho, no formato **Bearer**. É o único formato aceito — token na URL não funciona.
- **targets:** o endereço da sua instância.

### O campo

🔘 **METRICS_TOKEN (Prometheus /metrics):** a senha que o Prometheus precisa apresentar para ler o `/metrics`. Com o campo preenchido, uma leitura sem o token certo é recusada com **401**.

⚠️ **Com o campo em branco, o `/metrics` só responde ao próprio servidor** — aos endereços locais `127.0.0.1` e `::1`. Um Prometheus numa VPS sua não consegue ler as métricas enquanto o **METRICS_TOKEN** estiver vazio: para monitorar de fora, **preencha o token**.

Se o servidor também tiver um **METRICS_TOKEN** definido nas variáveis de ambiente, vale o valor deste campo.

## ⚡ Diagnóstico de Desempenho

A seção **Diagnóstico de Desempenho** liga o envio de um retrato do desempenho desta instância ao suporte do servidor, de tempos em tempos. A própria tela orienta ligar só quando o suporte do servidor pedir.

➡️ Só a pedido do suporte do servidor, escolha **Habilitado** em **Diagnóstico de Desempenho** e depois o intervalo em **Intervalo do Diagnóstico**.

🔘 **Diagnóstico de Desempenho:** **Habilitado** ou **Desabilitado**. Nas palavras da tela, *"Envia ao suporte do servidor um retrato do desempenho desta instância."*

🔘 **Intervalo do Diagnóstico:** de quanto em quanto tempo o retrato é enviado — **5**, **10**, **15**, **30** ou **60 min**. O campo fica travado enquanto o **Diagnóstico de Desempenho** está em **Desabilitado**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso preencher os dois campos de Google Analytics?** Não. O **Google Analytics Measurement ID** sozinho já mede a página de cadastro. O **Google Tag Manager ID** entra quando você quer gerenciar outras tags no mesmo contêiner.
>
> **O Google Analytics mede o uso da plataforma pelas empresas que já são clientes?** Não. Os dois IDs vão para a página de cadastro. O que acontece dentro da plataforma, no dia a dia do atendimento, não passa por aqui.
>
> **O Google Analytics serve para uma empresa cliente medir o site dela?** Não. O campo é da sua instância e alcança a sua página de cadastro.
>
> **Coloquei o ID do Google Analytics e não aparece nada.** Confira se o cadastro público está liberado e se alguém de fato abriu a página. Enquanto ninguém visitar a página de cadastro, não há evento para chegar.
>
> **Preciso de acesso ao servidor da plataforma para usar o METRICS_TOKEN?** Não. O Prometheus roda numa máquina sua e alcança o endereço público da sua instância. Você só precisa da sua própria VPS.
>
> **Onde eu vejo as métricas do /metrics e configuro os avisos?** No Grafana, na sua VPS — não na plataforma. É lá que os números viram gráfico e que você define o alerta. A plataforma só publica os números e guarda o token.
>
> **Sou obrigado a usar a Infra / Observabilidade?** Não. Com o **METRICS_TOKEN** em branco, o `/metrics` só responde ao próprio servidor, e ninguém de fora lê as métricas. O token só é preciso para o Prometheus ler de fora.
>
> **O Prometheus não consegue ler as métricas.** O token dele precisa ser idêntico ao do **METRICS_TOKEN** e ir no cabeçalho **Authorization**, no formato Bearer. Confira o valor e o lugar.
>
> **Trocar o METRICS_TOKEN derruba alguma coisa?** Só a coleta, e só até você atualizar o mesmo valor no Prometheus. O atendimento e as empresas não sentem nada — este token é só do endereço de métricas.
>
> **Preciso deixar o Diagnóstico de Desempenho habilitado?** Não. A própria tela pede para ligar apenas a pedido do suporte do servidor.
