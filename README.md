
# Scraping com Python utilizando Scrapy

Neste projeto percorre-se mais de 200 paginas, fazendo a extração de mais de 10.000 itens com nome, preço e links de todas as ofertas no site [Mercado Livre](https://www.mercadolivre.com.br/ofertas), utilizando a linguagem de programação Python e a biblioteca [Scrapy](https://scrapy.org/). 


## Instalação

1. Instale a biblioteca scrap com pip

```bash
  pip install scrapy
```
2. Criar o projeto:
```bash
  scrapy startproject mercadolivre
```

3. Acessar o diretório do projeto:
```bash
 cd mercadolivre
```

4. Gerando o spyder no diretório do projeto:
```bash
scrapy genspider ml mercadolivre.com
```   
    
## Explicação

No ml.py definimos um link de pesquisa como exemplo. Esse link padrão do mercado livre leva para as ofertas do dia.

A cada página de ofertas coletamos os dados como: **Produto**, **Preço** e **Link**. O código faz a coleta dos dados da página atual e a seguir vai para a próxima página até que chegue na última página de ofertas. 

Os dados poderão ser salvos nos seguintes formatos: **'json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle'**.

## Configurando o arquivo settings.py

```javascript
BOT_NAME = 'mercadolivre'

SPIDER_MODULES = ['mercadolivre.spiders']
NEWSPIDER_MODULE = 'mercadolivre.spiders'

USER_AGENT = 'MY_USER_AGENT'

ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED = True
}
```

## Exemplo

```python
import scrapy


class MlSpider(scrapy.Spider):
    name = 'ml'

    start_urls = ['https://www.mercadolivre.com.br/ofertas?page=1']

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="promotion-item max"]'):
            price = i.xpath(
                './/div[@class="andes-money-amount-combo__main-container"]//span//span[3]//text()').getall()
            title = i.xpath(
                './/p[@class="promotion-item__title"]//text()').get()
            link = i.xpath(
                './/a/@href').get()

            yield {
                'Preço': price,
                'Produto': title,
                'Link': link
            }

        next_page = response.xpath(
            '//a[contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

```

## Rodando os testes

Para rodar os testes, rode o seguinte comando, substituindo a extensão para aquelas suportadas, caso necessário.

```bash
  scrapy crawl ml -o pagination.json
```

## Funcionalidades

- Extração de dados de forma rápida e prática; 
- Exportação dos dados coletados em diversos formatos.

## Stack utilizada

**Linguagem:** Python
