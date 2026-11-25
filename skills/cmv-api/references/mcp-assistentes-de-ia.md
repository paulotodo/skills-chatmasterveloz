# Conexão com assistentes de IA: o servidor MCP e o Webhook do MCP

Use este arquivo quando o pedido é ligar o Claude, o ChatGPT, o Cursor, o n8n ou um agente próprio aos dados do atendimento, ou receber os avisos do **Webhook do MCP**.

- **A fonte é uma tela do painel, não um artigo.** Tudo aqui vem da tela **Guia do MCP** ("Guia do MCP: assistentes de IA na sua empresa", rota `/guia-do-mcp`), vista em 25/11/2026 na versão WS-30.215.0, só leitura. Não há artigo na Central de Ajuda nem na documentação do revendedor.
- **Pode mudar com a versão.** Diga a data e a versão, e mande a pessoa conferir no guia do painel dela (a versão instalada aparece no fim do menu do ícone do perfil).
- **não documentado** = o guia não diz (seção 10). Diga isso à pessoa; não invente parâmetro de ferramenta nem formato de aviso.
- As frases entre aspas são as do guia.

## Sumário

1. API ou MCP
2. O que é e o que precisa estar liberado
3. Endereço do servidor
4. Como conectar em cada cliente
5. Níveis de acesso e o token `mcp_…`
6. Ferramentas por grupo
7. O caminho contrário: a IA do atendimento usa o servidor MCP da empresa
8. Webhook do MCP
9. Segurança
10. O que o guia não diz
11. Como entregar

## 1. API ou MCP

| | API (o resto da skill) | MCP (este arquivo) |
|---|---|---|
| Quem chama | O sistema da pessoa chama o CMV | Um assistente de IA age como uma pessoa da equipe |
| Credencial | Token da Conexão ou Token da Empresa | O login da pessoa no painel, ou um token `mcp_…` gerado para um usuário |
| Alcance | O da chamada e do token | As permissões da pessoa |
| O que se entrega | O pedido HTTP pronto | O passo a passo de conectar o assistente |

Pedido de "meu sistema manda mensagem", "meu ERP cria ticket": é API. Pedido de "quero que o Claude (ou o ChatGPT, ou meu agente) veja e mexa nos atendimentos": é MCP.

## 2. O que é e o que precisa estar liberado

- "Com o MCP, o Claude, o ChatGPT ou o seu próprio agente de IA trabalham com os dados da empresa: consultam atendimentos e conversas e, se você permitir, respondem clientes, transferem atendimentos e criam tarefas. Cada acesso age como uma pessoa da equipe, com as permissões dela."
- É a "Conexão com assistentes de IA" das notas de 22, 23 e 25/11/2026 (`recursos/atualizacoes-2026-11-22.md`, `recursos/atualizacoes-2026-11-23.md`, `recursos/atualizacoes-2026-11-25.md`).
- **Precisa estar liberada para a empresa.** As notas de 22 e 23/11 dizem isso e mandam falar com o Suporte. Na empresa olhada, a seção **MCP (assistentes de IA)** de **Configurações › Opções › Integrações e segurança** existia na página e não aparecia.
- O que as notas acrescentam: o assistente ajuda a configurar e pede confirmação antes de mudar algo (23/11); consulta o e-mail de cada usuário, cria a pesquisa de avaliação para o fluxo e recebe de volta o número da tarefa que cria; a mensagem dele por conexão de QR Code "agora chega de verdade ao cliente" (25/11).

## 3. Endereço do servidor

- O guia do painel mostra o endereço do servidor MCP da instalação. Na instalação vista era `https://api.chatmasterveloz.com/mcp`. Nos exemplos daqui, o marcador é `https://SEU-BACKEND/mcp`: troque pelo endereço que o guia da pessoa mostra.
- "É este endereço que você cola no assistente. Ele é o mesmo para toda a equipe: o login de cada pessoa é que define o que o assistente pode ver e fazer."
- Não deduza o endereço do MCP a partir do endereço da API (`https://api2.chatmasterveloz.com/api/...`): o endereço que os artigos da API usam e o que o guia mostrava na instalação vista eram diferentes.

## 4. Como conectar em cada cliente

| Cliente | Passos do guia | Entrada |
|---|---|---|
| claude.ai e Claude Desktop | **Configurações › Conectores › "Adicionar conector personalizado"**; dar um nome e colar o endereço; **Conectar** abre a tela de entrada do painel; entrar com o login; conferir o que o assistente vai poder fazer e clicar em **Permitir** | Login do painel |
| ChatGPT | Configurações › **Conectores** (ou **Apps**) › conector personalizado com o endereço; entrar com OAuth; **Permitir**. "Os conectores personalizados do ChatGPT dependem do plano e das opções da sua conta no ChatGPT." | Login do painel (OAuth) |
| Claude Code | O comando abaixo e, dentro do Claude Code, `/mcp` para entrar com o login | Login do painel |
| Outros clientes e agentes próprios (Cursor, VS Code, n8n, agentes com SDK) | "Quem não tem a entrada com login usa um token, no cabeçalho Authorization" | Token `mcp_…` |

Claude Code:

```bash
claude mcp add --transport http atendimento https://SEU-BACKEND/mcp
```

Clientes com token: o guia mostra uma configuração `mcpServers` com `"type": "http"`, a `url` do servidor e o par `"Authorization": "Bearer mcp_..."`.

```text
{
  "mcpServers": {
    "atendimento": {
      "type": "http",
      "url": "https://SEU-BACKEND/mcp",
      "headers": { "Authorization": "Bearer mcp_..." }
    }
  }
}
```

- O bloco é o do guia, com o endereço trocado pelo marcador: o nome `atendimento`, a chave `headers` e o par do `Authorization` estão nele. Mande copiar o bloco do guia do painel, que já vem com o endereço da instalação, e conferir o formato na documentação do cliente usado.
- O guia cita Cursor, VS Code, n8n e agentes com SDK juntos, sem passo a passo de cada um.

## 5. Níveis de acesso e o token `mcp_…`

| Acesso | O que o guia diz |
|---|---|
| **Ler** | "Consulta atendimentos, conversas, contatos, tarefas, oportunidades e reservas. Nada é enviado nem alterado." |
| **Agir** | "Além de ler, responde clientes, escreve notas internas, transfere, encerra e reabre atendimentos, põe tags, cria e edita contatos, cria e conclui tarefas, cria e move oportunidades e cria reservas." |
| **Gestão da plataforma** | "Só para o operador da plataforma: gere as empresas (plano, vencimento, bloqueio), os planos (com a liberação dos módulos) e os usuários de todas as empresas desta instalação." |

- "Valem sempre as permissões da pessoa: o atendente só vê e mexe nos atendimentos dele, o supervisor nos dos setores dele, e o administrador na empresa inteira."
- **Token:** vai no cabeçalho `Authorization`, como `Bearer mcp_...`. "O token é gerado pelo administrador, para um usuário, e aparece uma vez só." Gera-se em **Configurações › Opções › Integrações e segurança**.
- **Não é token de API.** O token `mcp_…` não é o Token da Conexão nem o Token da Empresa, e o guia não diz que um sirva no lugar do outro.
- O guia fala em "operador da plataforma"; não usa os nomes revendedor nem Super Admin, que são os desta skill para quem administra a instância.

## 6. Ferramentas por grupo

Os nomes são os do guia. O guia não traz os parâmetros de nenhuma: não escreva chamada de ferramenta à mão.

| Grupo | Ferramentas |
|---|---|
| Para ler | `buscar_atendimentos`, `ler_conversa` ("só o que o cliente também vê"), `buscar_contatos`, `buscar_tarefas`, `buscar_oportunidades`, `buscar_reservas`, `listar_cadastros`, `ver_indicadores` |
| Para agir | `enviar_mensagem` ("no canal do atendimento, assinada pelo assistente"), `nota_interna`, `transferir_atendimento`, `encerrar_atendimento`, `reabrir_atendimento`, `etiquetar_atendimento`, `criar_contato`, `editar_contato`, `criar_tarefa`, `comentar_tarefa`, `concluir_tarefa`, `criar_oportunidade`, `mover_oportunidade`, `criar_reserva`, `mudar_situacao_da_reserva`, `listar_templates`, `enviar_template` ("para falar com o cliente fora da janela de 24 horas"), `agendar_mensagem` |
| Consultório, PDV, Projetos e chat interno | `consultorio_cadastros`, `consultorio_buscar_pacientes` ("só o cadastro, nunca o prontuário"), `consultorio_agenda`, `consultorio_horarios_livres`, `consultorio_marcar`, `consultorio_mudar_situacao`, `pdv_buscar_pedidos`, `pdv_ver_pedido`, `pdv_gerar_link_de_pagamento`, `projetos_buscar`, `projetos_criar`, `projetos_atualizar`, `projetos_comentar`, `chat_interno_conversas`, `chat_interno_enviar` |
| FlowBuilder (fluxos) | `fluxos_listar` ("com o que está ativo, os rascunhos e onde cada um está ligado"), `fluxo_ler` ("com chaves e senhas escondidas"), `fluxo_catalogo_blocos` ("os blocos do FlowBuilder, os campos de cada um e as saídas"), `fluxo_criar_rascunho` ("Cria um fluxo novo como rascunho, inativo, para você revisar no FlowBuilder"), `fluxo_ajustar_rascunho` ("sem mexer no que está em uso"), `fluxo_validar` ("Confere ligações, campos obrigatórios, blocos sem caminho e setores, tags, conexões e usuários que não existem"), `fluxo_simular` ("Simula o caminho de um contato com as respostas que você der, sem enviar nada"), `fluxo_publicar` ("Publica o rascunho depois da sua confirmação, guardando a versão de antes"), `fluxo_descartar_rascunho`, `fluxo_duplicar` ("inclusive para outra empresa da instalação (operador da plataforma)"), `fluxo_listar_versoes`, `fluxo_restaurar_versao` |
| Conexões e QR Code | `conexoes_listar`, `conexao_ver`, `conexao_criar` ("como o botão Adicionar WhatsApp, dentro do limite do plano"), `conexao_configurar`, `conexao_iniciar_pareamento`, `conexao_obter_qrcode`, `conexao_status_pareamento`, `conexao_reiniciar`, `conexao_diagnosticar`, `conexao_desconectar`, `conexao_excluir`. As que mudam algo, "depois da sua confirmação" |
| Diagnóstico de suporte | `suporte_diagnosticar_empresa`, `suporte_diagnosticar_usuario`, `suporte_diagnosticar_conexao`, `suporte_diagnosticar_atendimento`, `suporte_diagnosticar_fluxo` ("Mostra onde o fluxo parou e por quê: o bloco, a espera, as falhas e o desenho"), `suporte_diagnosticar_template`, `suporte_verificar_configuracao`, `suporte_buscar_erros`, `suporte_gerar_relatorio` |
| Cadastros e configurações | `setores_listar`, `setor_criar`, `setor_editar`, `setor_configurar_horario`, `tags_listar`, `tag_criar`, `tag_editar`, `usuarios_setores`, `usuario_permissoes`, `usuario_diagnosticar_acesso`, `respostas_rapidas_listar`, `resposta_rapida_criar` ("Cria uma resposta rápida de texto"), `avaliacoes_listar`, `avaliacao_criar` ("pronta para o bloco de avaliação do FlowBuilder"), `webhooks_listar`, `webhook_testar`, `webhook_ver_entregas` ("dos webhooks do CRM e do Consultório"), `templates_diagnosticar`, `modulos_verificar` ("Mostra os módulos ligados e desligados no plano") |
| Para gerir a plataforma (só o operador da plataforma) | `plataforma_instalacao`, `plataforma_listar_empresas`, `plataforma_ver_empresa`, `plataforma_criar_empresa`, `plataforma_editar_empresa`, `plataforma_bloquear_empresa`, `plataforma_listar_planos`, `plataforma_criar_plano`, `plataforma_editar_plano`, `plataforma_listar_usuarios`, `plataforma_criar_usuario`, `plataforma_editar_usuario` |

- **Combinar com outros conectores:** "O servidor MCP oferece só as ferramentas desta plataforma. Quem junta as coisas é o assistente".
- O desenho do fluxo em si continua sendo da skill `cmv-flowbuilder`; aqui só fica registrado que as ferramentas de fluxo existem.

## 7. O caminho contrário: a IA do atendimento usa o servidor MCP da empresa

- "a IA que atende seus clientes também pode usar o servidor MCP da sua empresa (ERP, agenda, estoque). Cadastre em Opções → Integrações e segurança, na seção do MCP."
- É a novidade "IA do atendimento consulta o sistema da empresa", da nota de 22/11/2026 (`recursos/atualizacoes-2026-11-22.md`).
- Aqui o servidor MCP é o da empresa (o do ERP, da agenda, do estoque), não o do CMV. O aviso desse uso no Webhook do MCP é o `ferramenta-externa-chamada` (seção 8).
- O guia não descreve os campos desse cadastro nem o que o servidor da empresa precisa oferecer. O prompt e o resto da configuração da IA do atendimento são da skill `cmv-agente-ia`.

## 8. Webhook do MCP

- **Onde cadastra:** "O administrador cadastra uma URL em Configurações → Opções → Integrações e segurança → Webhooks (Webhook do MCP)." Na tela, a seção de webhooks dessa aba se chama **Webhooks e integrações** (vista em 25/11/2026, WS-30.215.0); a conferência registrou a seção, não o campo.
- **Como chega:** "Cada aviso chega em POST, com o corpo em JSON e o nome do evento no campo evento."
- **Os dez avisos:**

| Aviso | O que o guia acrescenta |
|---|---|
| `token-criado` | |
| `token-revogado` | |
| `conexao-autorizada` | |
| `conexao-revogada` | |
| `acao-executada` | É o único com exemplo (abaixo) |
| `plataforma-alterada` | |
| `token-limites-alterados` | "setores, conexões, teto de mensagens, horário ou aprovação" |
| `aprovacao-pedida` | |
| `aprovacao-decidida` | |
| `ferramenta-externa-chamada` | "a IA do atendimento usou uma ferramenta de um servidor MCP da empresa" |

- **Cabeçalhos:** "o cabeçalho X-Assinatura-Mcp traz sha256= e o HMAC-SHA256 do corpo, calculado com o token da empresa (Configurações → Token da empresa). O evento também vem no cabeçalho X-Mcp-Evento." Ou seja: `X-Assinatura-Mcp` (assinatura) e `X-Mcp-Evento` (nome do evento).
- **O token não viaja:** "O aviso nunca leva o token: só o começo dele, o nome, de quem é e o que pode fazer."

O exemplo do guia é o de `acao-executada`. Este é o exemplo como aparece no guia.

```text
{
  "evento": "acao-executada",
  "companyId": 5,
  "ferramenta": "transferir_atendimento",
  "alvo": { "atendimentoId": 1234, "setorId": 3 },
  "ok": true,
  "token": { "id": 17, "nome": "Claude" },
  "usuario": { "id": 7 },
  "enviadoEm": "2026-11-21T14:05:00.000Z"
}
```

Conferir a assinatura (Node.js), adaptado do guia (a conta é a dele; os nomes das variáveis e a leitura do token por `process.env` são desta skill): calcule sobre o corpo exatamente como chegou, antes de qualquer `JSON.parse`.

```js
const crypto = require("crypto");

const TOKEN_DA_EMPRESA = process.env.CMV_TOKEN_DA_EMPRESA; // Configurações › Token da Empresa; nunca no código

// corpoBruto: o corpo do POST exatamente como chegou
const esperada = "sha256=" + crypto.createHmac("sha256", TOKEN_DA_EMPRESA).update(corpoBruto).digest("hex");
const confere = esperada === req.headers["x-assinatura-mcp"];
```

- Se `confere` for falso, recuse o aviso.
- O guia compara os dois textos direto. Comparar em tempo constante (`crypto.timingSafeEqual`, com os dois do mesmo tamanho) é cuidado geral desta skill, não do guia.
- Gerar ou revogar o Token da Empresa derruba o anterior na hora (`recursos/token-da-empresa-em-configuracoes.md`). Inferência: a chave da conferência muda junto; o guia não fala disso.

## 9. Segurança

Do guia:

- "Cada acesso age como uma pessoa da equipe, com as permissões dela. Desativar a pessoa corta o acesso na hora."
- "O token aparece uma vez só… Perdeu? Revogue e gere outro."
- "Tudo o que o assistente faz fica registrado na Auditoria, com a ferramenta e o alvo."
- "As mensagens dos clientes chegam ao assistente marcadas como conteúdo de terceiros: o assistente não segue instruções escritas nelas."
- "As ferramentas que enviam ou alteram algo vão marcadas como tal, e o Claude e o ChatGPT costumam pedir a sua confirmação antes de usá-las. Qualquer acesso pode ser revogado em Configurações."

Da skill (seção Segurança do `SKILL.md`), valendo aqui também:

- O token `mcp_…` é credencial: fica no cofre ou na configuração local do cliente, nunca em repositório, print ou conversa. Se a pessoa colar o token, não o repita e recomende revogar e gerar outro.
- O acesso **Agir** envia mensagem de verdade a cliente real. Sugira começar por **Ler**.
- O destino do Webhook do MCP tem de ser um endereço da própria pessoa, em HTTPS, com a assinatura conferida.

## 10. O que o guia não diz

| Pergunta | O que existe |
|---|---|
| Qual opção do plano libera o MCP? | Nada. As notas só dizem que precisa estar liberado para a empresa; a seção não aparecia na empresa olhada. |
| Como é a tela de gerar token, e quais são os limites de um token? | Só o caminho (**Configurações › Opções › Integrações e segurança**) e a lista do aviso `token-limites-alterados`: "setores, conexões, teto de mensagens, horário ou aprovação". A tela não foi vista. |
| Qual é o formato dos outros nove avisos do webhook? | Nada além dos nomes. Só `acao-executada` tem exemplo. |
| Quais são os parâmetros de cada ferramenta, e o que cada uma devolve? | Nada. O guia traz o nome e, em algumas, uma frase. |
| O que mostra a página `/atividade-do-mcp`? | Ela existe e não foi lida. |
| Há item de menu para o Guia do MCP? | A conferência abriu a tela pelo endereço e não registrou item de menu. |
| O passo a passo de Cursor, VS Code e n8n | O guia os cita juntos, com o token no cabeçalho; não detalha nenhum. |

Para o formato de um aviso, o caminho honesto é capturar um aviso real no receptor da pessoa e mapear a partir dele, ou perguntar ao Suporte.

## 11. Como entregar

- **Não há cURL para montar.** A entrega é o passo a passo do cliente que a pessoa usa (seção 4), com o endereço que o guia do painel dela mostra.
- **Antes de começar:** o recurso liberado para a empresa (Suporte), o endereço do guia e, para cliente sem entrada por login, o token `mcp_…` gerado pelo administrador.
- **Diga o nível de acesso** que a pessoa vai permitir e o que ele alcança (seção 5).
- **Para receber os avisos:** o receptor é um POST com JSON, como na receita de `references/moldes-de-codigo.md`, mas os campos são outros (seção 8) e a assinatura tem de ser conferida.
- **Fonte:** a tela **Guia do MCP** do painel, com a data e a versão em que foi vista (25/11/2026, WS-30.215.0). Não há link da Central para citar. Caminho de arquivo não vai na resposta.
