# 2022-2-Certifik8

<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/fga-eps-mds/2022-2-Certifik8">
    <img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/logo.png" width="300" height="300">
  </a>

<h3 align="center">Certifik8</h3>

<p align="center">
   Gerador Automatico de Certificados 
    <br />
    <a href="docs">Documentos</a>
    -
    <a href="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/SECURITY.md#pol%C3%ADtica-de-seguran%C3%A7a">Reportar Bug</a>
    -
    <a href="https://github.com/fga-eps-mds/2022-2-Certifik8/issues">Recomendar Feature</a>
  </p>
</div>
<!-- TABLE OF CONTENTS -->

<details>
  <summary>Conteúdo</summary>
  <ol>
    <li><a href="#-especificações-técnicas">📝 Especificações Técnicas</a></li>
    <li><a href="#-funcionamento">⚙️ Funcionamento</a></li>
    <li><a href="#-como-utilizar">💻 Como Utilizar</a>
    <li><a href="#-métricas">📈 Métricas</a>
  </ol>
</details>
<br>

## 📝 Especificações Técnicas

#### Linguagem:
<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=python"/>
	</a>
    <br>
    Versão: 3.10
</p>

#### Bibliotecas para Executar as Funcionalidades:

<ul>
    <li>Pandas: 1.5.2</li>
    <li>Setuptools: 65.6.3</li>
    <li>Pillow: 9.3.0</li>
    <li>PyPDF2: 2.11.1</li>
    <li>Pdfkit: 1.0.0</li>
    <li>Beautifulsoup4: 4.11.1</li>
    <li>Openpyxl: 3.0.10</li>
    <li>Tqdm: 4.64.1</li>
</ul>

<br>

#### Biblioteca para Criação do Ambiente Virtual e Gestão de Pacotes:
<ul>
  <li>Poetry: 1.3.2</li>
</ul>

<br>

#### Bibliotecas para Cobrimento de Testes
<ul>
  <li>Pytest: 7.2.1</li>
  <li>Coverage: 7.1.0</li>
</ul>

<br>

#### Diagrama de Arquivos
<a href="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/docs_tecnica/docs/Diagrama%20de%20Arquivos.png">
		<img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/docs_tecnica/docs/Diagrama%20de%20Arquivos.png"/>
	</a>

#### Onde se está dispovível para Utilização:

- Linux Mint 21
- Ubuntu 22.04.01

<div align="center">

![LinuxMint](https://img.shields.io/badge/Linux_Mint-87CF3E?style=for-the-badge&logo=linux-mint&logoColor=black) 
![Ubuntu](https://img.shields.io/static/v1?style=for-the-badge&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=FFFFFF&label=)

</div>

<br>

## ⚙️ Funcionamento
O funcionamento do Certifik8 segue as seguintes etapas:
<ol>
    <li>Escolha de um ou mais arquivos .xlsx</li>
    <li>Escolha da Pasta de destino final dos certificados</li>
    <li>Geração dos Certificados separadas em subpastas de acordo com a função no evento</li>
</ol>

<br>

## 💻 Como Utilizar

1. **Clone o repositório**

```
git clone https://github.com/fga-eps-mds/2022-2-Certifik8.git
```

2. **Para instalar as dependências no ambiente virtual, rode os comandos:**
```
poetry install
```
	
3 **Comando para acessar tutorial da aplicação**
```
poetry run certifik8 --h
```	
	
4 **Comando para rodar a aplicação**
```
poetry run certifik8
```
5 **Comando para rodar os Testes**
```
pytest --cov-config=.coveragerc --cov=Certifik8
```

<br>

## 📈 Métricas
Para gerenciamento das métricas de manutenrabilidade e de cobertura de testes, se esta utiliando o Code Climate.
<div align="center">

[![Maintainability](https://api.codeclimate.com/v1/badges/e00e7a4c51d3c657319d/maintainability)](https://codeclimate.com/github/fga-eps-mds/2022-2-Certifik8/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e00e7a4c51d3c657319d/test_coverage)](https://codeclimate.com/github/fga-eps-mds/2022-2-Certifik8/test_coverage)

</div>