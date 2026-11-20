# Chat Master Veloz — documentação da plataforma (Central de Ajuda)

Cópia em Markdown da Central de Ajuda, para consulta por agentes: como cada recurso funciona, passo a passo de uso e a referência da API.

- **Fonte:** <https://clihelper.chatmasterveloz.com/docs>
- **Copiado em:** 12/11/2026
- **Conteúdo:** 661 artigos (14 de Trilhas, 369 de Recursos, 273 de APIs, 5 fora do menu), 233 endpoints e 17 vídeos
- **Para atualizar:** `python3 _gerar.py` baixa o site de novo e regenera tudo, menos este arquivo.

Para CSS e JS de customização do painel (seletores, atributos `data-*`), a referência é outra: `../docs-css-chatmasterveloz/`.

## Não leia tudo: ache o artigo e leia só ele

São cerca de 4 MB em 661 arquivos, um por artigo. O caminho é: índice ou `grep` → abrir o artigo.

| Preciso de… | Onde |
|---|---|
| a lista de todos os recursos, na hierarquia do menu | `INDICE-recursos.md` |
| um endpoint da API pelo endereço ou método | `INDICE-api-endpoints.md` |
| os artigos da API por assunto (inclui webhooks e conceitos) | `INDICE-api.md` |
| por onde começar a aprender o sistema, em ordem | `INDICE-trilhas.md` |
| artigos que existem mas não estão em nenhum menu | `INDICE-outros.md` |
| os vídeos tutoriais (YouTube) | `videos.md` |
| o que mudou na plataforma, dia a dia | `recursos/atualizacoes-AAAA-MM-DD.md` |

Buscas úteis, a partir desta pasta:

```bash
grep -il 'transferir' recursos/*.md              # quais artigos falam de um assunto
grep -rn -i 'encerrar por inatividade' recursos   # a frase exata, com a linha
grep -n -i 'tickets' INDICE-api-endpoints.md      # endpoints de um recurso
grep -n -i 'quadro' INDICE-recursos.md            # onde um módulo está no menu
```

O nome do arquivo é o mesmo do endereço do artigo no site: `recursos/transferir-ticket.md` é `…/docs/transferir-ticket`.

## Como é cada artigo

Todo arquivo começa igual:

```markdown
# Título do artigo

- **Fonte:** endereço do artigo no site
- **Categoria:** Trilhas | Recursos | APIs | Fora do menu
- **Menu:** caminho no menu do site (Pai › Filho › Artigo)

---
```

Depois vem o texto do artigo, sem resumo e sem corte. Convenções:

- **Blocos de destaque** viram citação com o tipo entre colchetes: `> **[RESUMO]**`, `> **[DUVIDAS]**`, `> **[ERROS]**`, `> **[ATENCAO]**`, `> **[DICA]**`, `> **[PREREQUISITO]**`, `> **[DOWNLOAD]**`, `> **[SUPORTE]**`. Para ver só as dúvidas comuns de um assunto: `grep -A12 'DUVIDAS' recursos/conexoes.md`.
- **Caminho de menu no painel** aparece como `Configurações › Empresas`.
- **Etiquetas** aparecem entre colchetes: `[Básica]`, `[Pro]`, `[Oficial]`, `[Hub]`, `[Webchat]`, `[Todas]`. Nos artigos de API, dizem para qual tipo de conexão o endpoint vale.
- **Links entre artigos** apontam para o arquivo local (`../recursos/…md`). Links externos ficam como estão.
- **Imagens** são links para o site (`![…](https://clihelper…/docs-imagem/…)`). O conteúdo da imagem não foi transcrito.
- **Vídeos embutidos** aparecem como `[Vídeo Voomly — id …]`, sem endereço público.

## Artigos de API

Os que declaram endpoint seguem quase sempre esta ordem: descrição, `Endpoint`, `Método`, `Autenticação`, `Payload` (quando há), a explicação de cada campo, um exemplo de código (PHP, na maioria) e, logo abaixo, o mesmo pedido em `cURL`.

- O token é o da conexão: `Authorization: Bearer {seutokenaqui}`.
- `{ticketId}`, `{seutokenaqui}` e outros nomes entre chaves são para substituir.
- Vários recursos têm mais de um artigo, um por tipo de conexão (por exemplo `api-mensagem-de-texto`, `api-oficial-mensagem`, `api-webchat-mensagem-de-texto`). Confira a etiqueta e a linha **API:** antes de escolher.

## O que não está aqui

- A página inicial e as três páginas de categoria: só têm os cartões de entrada, que os índices substituem.
- A busca do site.
- O que as imagens e os vídeos mostram.
