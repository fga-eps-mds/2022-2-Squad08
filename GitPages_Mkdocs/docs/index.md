---
hide:
  - navigation
  - toc
---

# 2022-2-Certifik8
---
<center>

[![Contributors](https://img.shields.io/github/contributors/fga-eps-mds/2022-2-Certifik8.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Certifik8/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/fga-eps-mds/2022-2-Certifik8.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Certifik8/issues)
[![MIT License](https://img.shields.io/github/license/fga-eps-mds/2022-2-Certifik8.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/LICENSE)

</center>

<!-- 
<br />
<div align="center">
  <a href="https://github.com/fga-eps-mds/2022-2-Certifik8">
    <img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/logo.png" width="300" height="300">
  </a>
   -->

<center>

![Certifik8](img/logo.png){width="400" height="400"}

</center>

<center>
#Certifik8
</center>

<center>
Gerador Automático de Certificados 

[Documentos](docs)
[Reportar Bug](https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/SECURITY.md)
[Recomendar Feature](https://github.com/fga-eps-mds/2022-2-Certifik8/issues)
    
</center>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a href="#Sobre-o-projeto">📝 Sobre o projeto</a>
      <ul>
        <li><a href="#Tecnologias">💻 Tecnologias</a></li>
      </ul>
    </li>
    <li><a href="#Funcionalidade">🤖 Funcionalidade</a></li>
    <li><a href="#Requisitos">❗ Requisitos</a></li>
    <li><a href="#Como-rodar">🛞 Como executar</a></li>
    <li><a href="#Devenvolvedores">👨‍💻 Desenvolvedores</a></li>
  </ol>
</details>

## 📝 Sobre o projeto
---

Certifik8 é um gerador de certificados automático criado em Python. O projeto busca facilitar a geração massiva de documentos a serem emitidos após algum evento. 

## 💻 Tecnologias
---
#### Tecnologias utilizadas neste projeto:

<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=python,html,css"/>
	</a>
</p>

## 🤖 Funcionalidade
---
O Certifik8 precisa apenas que o usuário escolha uma tabela excel .xlsx em algum de seus arquivos para em seguida escolher o local na qual a pasta com os certificados, de modelo já definido, ficarão salvos. Após essa escolha, a geração dos certificados em formato PDF acontece de forma que cada tabela escolhida possua uma pasta homônima no destino escolhido e cada pasta apresente subpastas que vão filtrar os participantes do evento de acordo com suas funções. 

<center>

![Certificado Exemplo](img/Melissa Ribeiro Araujo.png){width="600" height="600"}

</center>

## ❗ Requisitos
---
O Certifik8 só funciona em sistemas operacionais Linux. 

Testado no:
- Linux Mint 21
- Ubuntu 22.04.01


![LinuxMint](https://img.shields.io/badge/Linux_Mint-87CF3E?style=for-the-badge&logo=linux-mint&logoColor=black)

![Ubuntu](https://img.shields.io/static/v1?style=for-the-badge&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=FFFFFF&label=)



**Para conseguir executá-lo, o usuário precisa instalar:**

  - **Python3 e Pip**
```
sudo apt install python3 && sudo apt install python3-pip
```
 
  - **As bibliotecas pdfkit, BeautifulSoup e Pandas**
```
pip install pdfkit
```

```
pip install beautifulsoup4
```

```
pip install pandas
```

  - **Instalar a ferramenta wkhtmltopdf**
```
sudo apt install wkhtmltopdf
```

## 🛞 Como executar/rodar
---
### **- 👩‍🦰 Usuário**
1. **Abra seu terminal e digite o comando para instalar o Certifik8 do Pypi:**
```
pip install certifik8
```

2. **Comando para instalar as dependências não presentes no Pypi**
```
certifik8 --install
```
3. **Comando para acessar tutorial da aplicação**
```
certifik8 --h
```	
4. **As tabelas dos cursos devem seguir uma padronização, caso contrário elas não irão gerar certificados:**

* Estrutura da tabela Excel ([Exemplo](Certifik8/examples/completa.xlsx)): 

| 1 |           Nome             |       CPF      |    Função    | Frequência |     Informações    |
|---|----------------------------|----------------|--------------|------------|--------------------|
| 2 |Samuel Barbosa Alves        |729.334.326-41  |PARTICIPANTE  |100         |Nome do Curso       |
| 3 |Melissa Ribeiro Araujo      |201.544.482-30  |MONITOR       |97          |Carga Horaria       |
| 4 |Gabrielly Rodrigues Castro  |451.016.912-40  |PARTICIPANTE  |80          |Nome do Professor   |
| 5 |           ...              |      ...       |     ...      |    ...     |Nome do Departamento|
| 6 |           ...              |      ...       |     ...      |    ...     |Data Inicial        |
| 7 |           ...              |      ...       |     ...      |    ...     |Data Final          |
| 8 |           ...              |      ...       |     ...      |    ...     |Nome Decano(a)      |
|...|           ...              |      ...       |     ...      |    ...     |                    |

*Obs.: As tabelas devem possuir essas cinco colunas com os mesmos nomes e em qualquer ordem. A coluna informações deve possuir seis linhas, e seus dados devem seguir a ordem da tabela de exemplo abaixo

*Demonstração de funcionalidade.*

5. **Comando para rodar a aplicação**
```
certifik8
```

6. **Selecione as tabelas que possuem as informações do certificado:**
<center>

![Escolhe Tabela](img/escolhe_tabela.png){width="600" height="600"}

</center>


7. **Selecione a pasta onde deseja guardar os certificados:**
<center>

![Escolhe Tabela](img/escolhe_pastas.png){width="600" height="600"}

</center>

### **- 🧙🏼‍♀️ Desenvolvimento local**

1. **Clone o repositório**

```
git clone https://github.com/fga-eps-mds/2022-2-Certifik8.git
```
2. **Para instalar as dependências não advindas do Pypi, abra o repositório em seu computador e rode o comando:**
```
cd Certifik8/installer
```
```
./dependencies.sh
```

2. **Para instalar as dependências no ambiente virtual, rode o comando no diretório raiz:**
```
poetry install
```
	
3 **Para acessar tutorial da aplicação, rode o comando no diretório raiz:**
```
poetry run certifik8 --h
```	
	
4 **Para rodar a aplicação no diretório raiz:**
```
poetry run certifik8
```

## 👨‍💻 Desenvolvedores

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/PedroSampaioDias">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90795603?v=4" width="150px;"/>
                <h5 class="text-center">Pedro Sampaio</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/phmelosilva">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/88786258?v=4" width="150px;"/>
                <h5 class="text-center">Pedro Henrique</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Victor-oss">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/55855365?v=4" width="150px;"/>
                <h5 class="text-center">Victório Lazaro</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/daniel-de-sousa">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/95941136?v=4" width="150px;"/>
                <h5 class="text-center">Daniel Sousa</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Leanddro13">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86811628?v=4" width="150px;"/>
                <h5 class="text-center">Leandro Silva</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/BlimblimCFT">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/12275797?v=4" width="150px;"/>
                <h5 class="text-center">Geovane Freitas</h5>
            </a>
        </td>
</table>
</center>
