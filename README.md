# web_crawler
Projeto de web crawler para varrer um conjunto de domínios e identificar links de páginas com erros (famílias 400 e 500)

___


## Requisitos
|RF01 - Ler os endereços base a serem checados de um arquivo de configuração|
|RF02 - Controlar os endereços para não checar 2 vezes o mesmo endereço, mas registrar as diferentes origens para um mesmo endereço|
|RF03 - Identificar e registrar endereços que contenham HTTP status 4xx ou 5xx|

|RNF01 - Utilizar threads para agilizar o processo|


**Considerações**

Nesta primeira versão não trabalharei na disponibilização amigável dos dados ao usuário


## Escolhas técnicas
Utilizarei UUID v7 para ter uma ordenação temporal das execuções, caso venha surgir necessidade futura e para melhor identificar as execuções nos testes pela ordenação.


___


# Etrutura de dados
As checagens criarão os seguintes dados:

## Endereços com erros
Registro contendo todos os endereços que retornaram algum erro 4xx ou 5xx

**Atributos**

| Endereço | Erro |
| -------- | ---- |
| string   | int  |
| string   | int  |
| string   | int  |


## Links
Registro contendo os vínculos de quais endereços referenciam quais endereços, mesmo que multiplas vezes

**Atributos**

| Origem | Destino |
| ------ | ------- |
| string | string  |
| string | string  |
| string | string  |