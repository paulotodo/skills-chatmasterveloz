# Importar Contatos (planilha)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/importar-contatos-planilha
- **Categoria:** Recursos
- **Menu:** Contatos › Importar Contatos (planilha)

---

Ao **importar**, você pode adicionar ou atualizar vários contatos de uma só vez.

Acesse o menu **Contatos  ›  Importar / Exportar  ›  Importar Arquivo**.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20240-contatos-importar-exportar-1024x232.jpg)

> **[ATENCAO]**
>
> #### Atenção
>
> ➡️ O procedimento de importação de planilha para **Adicionar Novos Contatos** é diferente de **Atualizar Contatos** (veja abaixo).

## Como Importar Novos Contatos

É possível **importar novos** contatos com os seguintes campos:

▫️Número, ▫️Nome, ▫️Email, ▫️CPF/CNPJ, ▫️Gênero, ▫️Estado, ▫️Cidade, ▫️Referência, ▫️Aniversário, ▫️Endereço.

#### 📌 Atenção à formatação dos campos:  
- **Número**: somente com números (sem espaço, letra ou símbolos) e no formato DDI DDD NUMERO (Ex: 551199998888)
- **Aniversário**: o dia e o mês bastam, no formato DIA/MÊS (Ex: 20/11). O ano é opcional. A planilha também aceita o formato com ano e horário (Ex: 1982-11-20T10:30), mas o horário não é guardado.

## Modelo Planilha de Importação

Baixe a planilha modelo para garantir que seu arquivo de importação esteja no formato correto.

> **[DOWNLOAD]**
>
> #### Download
>
> Planilha modelo para importar contatos.
>
> [📄 planilha_importar_contatos.xlsx](https://clihelper.chatmasterveloz.com/docs-arquivo/arq-6a9b2bdb1f4bc-planilha_importar_contatos.xlsx)

## Como Atualizar Contatos (usando planilha)

Nosso sistema permite **atualizar** contatos em massa alterando os campos ▫️Nome, ▫️Email, ▫️CPF/CNPJ, ▫️Gênero, ▫️Estado, ▫️Cidade, ▫️Referência, ▫️Aniversário, ▫️Endereço.

#### 📌 Além desses, você pode atualizar também:

▫️Carteira, ▫️Tag, ▫️Status (a situação do atendimento)

> **[ATENCAO]**
>
> #### Atenção
>
> Para atualizar contatos é preciso adicionar a coluna "**Atualizar**" na planilha de importação, colocando um número que serve como referência aos campos que serão atualizados (veja a tabela abaixo).                             
>
> | Valor do campo | Será atualizado |
> |---|---|
> | 1 | **Nome** |
> | 2 | **Nome** e **E-mail** |
> | 3 | **Carteira** (definir o ID do atendente) |
> | 4 | **Tag** (definir o ID da tag e o ID da Conexão na coluna WhatsApp) |
> | 5 | **Campos extras** como ▫️CPF/CNPJ, ▫️Gênero, ▫️Estado, ▫️Cidade, ▫️Referência, ▫️Aniversário, ▫️Endereço |

## Como aplicar Tags pela planilha

Com **Atualizar** = **4**, preencha a coluna **whatsapp** com o ID da Conexão (só números) e a coluna **tag** com o ID da tag — mais de uma, separadas por vírgula. A coluna **status** é opcional e aceita **closed**, **pending** ou **open**.

🔘 **Sem status, nada muda de situação:** quem está em **Aguardando** continua em **Aguardando**, e quem está em atendimento continua com o mesmo atendente.

🔘 **A tag vai para o atendimento** do contato, e não para o cadastro dele.

🔘 **Contato novo na planilha também recebe a tag:** ele é criado com um atendimento já **encerrado**, que leva a tag, sem cair no **Aguardando**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Importar uma lista com tags enche o Aguardando?** Não, com a coluna **status** vazia. A importação só aplica as tags e mantém cada atendimento como estava.
>
> **Onde aparece a tag que a planilha aplicou?** No atendimento do contato. Contato que ainda não tinha atendimento ganha um, já encerrado, com a tag.
