# Endpoints da API (35)

Uma linha por artigo que declara um endpoint, em ordem de endereço. Os artigos da categoria APIs que não estão aqui são conceituais (webhooks, autenticação, exemplos).

| Método | Endpoint | Artigo |
|---|---|---|
| DELETE | `https://api2.chatmasterveloz.com/api/announcements` | [API Deletar Aviso](api/api-admin-deletar-aviso.md) |
| POST | `https://api2.chatmasterveloz.com/api/announcements` | [API Criar Aviso](api/api-admin-criar-aviso.md) |
| PUT | `https://api2.chatmasterveloz.com/api/announcements` | [API Atualizar Aviso](api/api-admin-atualizar-aviso.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/announcements/media-upload` | [API Remover Mídia do Aviso](api/api-admin-remover-midia-do-aviso.md) |
| POST | `https://api2.chatmasterveloz.com/api/announcements/media-upload` | [API Anexar Mídia ao Aviso](api/api-admin-anexar-midia-ao-aviso.md) |
| GET | `https://api2.chatmasterveloz.com/api/announcements/show?id={avisoId}` | [API Obter um Aviso](api/api-admin-obter-um-aviso.md) |
| PUT | `https://api2.chatmasterveloz.com/api/announcements/toggle-status` | [API Ativar ou Desativar Aviso](api/api-admin-ativar-ou-desativar-aviso.md) |
| GET | `https://api2.chatmasterveloz.com/api/announcements?searchParam={searchParam}&pageNumber={pageNumber}` | [API Listar Avisos](api/api-admin-listar-avisos.md) |
| POST | `https://api2.chatmasterveloz.com/api/application/restart` | [API Reiniciar Conexões como Super Admin](api/api-admin-reiniciar-conexoes-como-super-admin.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies` | [API Obter uma Empresa (completa)](api/api-admin-obter-uma-empresa-completa.md) |
| POST | `https://api2.chatmasterveloz.com/api/companies/add` | [API Criar Empresa](api/api-admin-criar-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/all` | [API Listar Empresas](api/api-admin-listar-empresas.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/count` | [API Contar Empresas](api/api-admin-contar-empresas.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/{companyId}` | [API Obter uma Empresa](api/api-admin-obter-uma-empresa.md) |
| PUT | `https://api2.chatmasterveloz.com/api/companies/{companyId}` | [API Atualizar o Cadastro de uma Empresa](api/api-admin-atualizar-o-cadastro-de-uma-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/{companyId}/api-token` | [API Conferir o Token da Empresa](api/api-admin-conferir-o-token-da-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/companies/{companyId}/api-token` | [API Criar Token da Empresa](api/api-admin-criar-token-da-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/companies/{companyId}/block` | [API Bloquear Empresa](api/api-admin-bloquear-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/companies/{companyId}/unblock` | [API Desbloquear Empresa](api/api-admin-desbloquear-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/companies/{companyId}/whatsapps` | [API Criar Conexão em uma Empresa](api/api-admin-criar-conexao-em-uma-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/flowbuilder` | [API Criar Fluxo em uma Empresa](api/api-admin-criar-fluxo-em-uma-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/invoices/listar` | [API Obter Faturas](api/api-admin-obter-faturas.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/recuperar` | [API Recuperar Mensagens](api/api-admin-recuperar-mensagens.md) |
| GET | `https://api2.chatmasterveloz.com/api/plans` | [API Listar Planos](api/api-admin-listar-planos.md) |
| POST | `https://api2.chatmasterveloz.com/api/plans` | [API Criar Plano](api/api-admin-criar-plano.md) |
| GET | `https://api2.chatmasterveloz.com/api/plans/{planId}` | [API Obter um Plano](api/api-admin-obter-um-plano.md) |
| PUT | `https://api2.chatmasterveloz.com/api/plans/{planId}` | [API Atualizar Plano](api/api-admin-atualizar-plano.md) |
| POST | `https://api2.chatmasterveloz.com/api/queues` | [API Criar Setor em uma Empresa](api/api-admin-criar-setor-em-uma-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/quick-messages` | [API Criar Resposta Rápida em uma Empresa](api/api-admin-criar-resposta-rapida-em-uma-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/quick-messages?companyId={companyId}&queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}` | [API Listar Respostas Rápidas de uma Empresa](api/api-admin-listar-respostas-rapidas-de-uma-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/settings/media-upload?ref=login` | [API Trocar Imagens da Plataforma](api/api-admin-trocar-imagens-da-plataforma.md) |
| POST | `https://api2.chatmasterveloz.com/api/subscription/manualpaid` | [API Pagar Fatura](api/api-admin-pagar-fatura.md) |
| POST | `https://api2.chatmasterveloz.com/api/tags` | [API Criar Tag em uma Empresa](api/api-admin-criar-tag-em-uma-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/users` | [API Criar Usuário em uma Empresa](api/api-admin-criar-usuario-em-uma-empresa.md) |
| PUT | `https://api2.chatmasterveloz.com/api/users/{userId}` | [API Atualizar Usuário de uma Empresa](api/api-admin-atualizar-usuario-de-uma-empresa.md) |
