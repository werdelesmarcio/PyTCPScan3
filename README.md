
![Logo](https://i.ibb.co/S3WGFQk/Sem-t-tulo-removebg-preview.png)

[![Maintainability](https://api.codeclimate.com/v1/badges/bf596a2940ddf3183bab/maintainability)](https://codeclimate.com/github/werdelesmarcio/PyTCPScan3/maintainability) [![Build status](https://ci.appveyor.com/api/projects/status/050o62vq1v03wv4c?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/pytcpscan3) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan3&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan2) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan3&metric=bugs)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan3) ![GitHub License](https://img.shields.io/github/license/werdelesmarcio/PyTCPScan3)

# PyTCPScan (Version 3.0)
_Repositório para a aplicação PyTCPScan._

Consiste em uma aplicação voltada para principalmente para sistemas **GNU/Linux** _(embora o interpretador python3 no windows também execute a aplicação normalmente)_ e tem como finalidade, a execução de scanner de portas, onde irá verificar quais portas estão abertas dentro de um range de portas informados por argumentos e retornar **STATUS OPEN**, em caso positivo. 

Os argumentos informados consistem no endereço de host ou IP do alvo que será analisado, seguidos do range de portas inicial e final.

**OBS.: Se sua meta é de escanear apenas uma porta, pode colocar o mesmo valor para os dois ultimos parâmetros.**

O sistema está na versão 3 _(beta)_ e ainda encontra-se em fase de desenvolvimento.

## Funcionalidades
Estas são as instruções para que você tenha uma cópia do **PyTCPScan** em sua máquina para fins de desenvolvimento e teste.
Execute o download ou clone o repositório para a sua máquina e descompacte-o em um local de preferência.

- _Não é necessário instalar o PyTCPScan._
- _Para usar como executável, lembrar de dar permissão de execução (caso esteja usando uma Distribuição GNU/Linux._
- _Alterações no sistema para funcionalidade multiplataforma._

## Pré-Requisitos

Para rodar esse projeto, você vai precisar se atentar às dependências abaixo:

- Ter instalado em sua máquina o interpretador python na versão 3.xx e o pip3.
- Se estiver rodando uma distro linux, fazer o update e upgrade do sistema antes de rodar.


## Permissões (usuários GNU/Linux)

_Para dar permissão de execução._

```bash
#: > sudo chmod +x pytcpscan.py
```
    
## Execução

_Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial e a porta final. Ele irá verificar quais portas estão com o Status Open._

**GNU/Linux**
```bash
$: > ./pytcpscan [target] [init_port] [final_port]
```
**Windows**
```powershell
$: > python3 pytcpscan.py [target] [init_port] [final_port]
```

## Exemplo de Resposta
<img src="https://i.imgur.com/iI9ncVh.png">

## Autores
**Werdeles (gh05tb0y) Soares:** _Desenvolvedor_

### Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!
Usuário do github: [@werdelesmarcio](https://github.com/werdelesmarcio) 

## Licença
Este projeto está sob Licença GPL-3.0. Para mais informações, consulte a documentação de licença no link abaixo.
* [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan3?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan3?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/SoftwareLivre.png?raw=true" width =120 align="Right">
<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/PoweredByLinux.png?raw=true" width =80 align="Right">
