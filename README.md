# Projeto: Docker Auto Updater

## Tema do Projeto

Desenvolvimento de um sistema automatizado capaz de monitorar imagens Docker com a tag **latest**, detectar novas versões publicadas em um registry e atualizar automaticamente os containers em execução.

---

##  Equipe

- Guilherme Manoel da Silva
- Mihael Reinaldo Araújo de Albuquerque Escobar
- Wellington Antonio da Silva

##  Disciplina
Virtualização: IFPB - 2026.1

---

# Objetivo do Projeto

O objetivo deste projeto é desenvolver uma solução automatizada capaz de monitorar periodicamente imagens Docker publicadas em registries de containers e identificar alterações em imagens que utilizam a tag **latest**.

Quando uma nova versão da imagem for detectada, o sistema deverá:

* Identificar a atualização;
* Baixar a nova imagem;
* Interromper o container antigo;
* Remover o container desatualizado;
* Criar um novo container utilizando a imagem atualizada;
* Restaurar automaticamente a execução da aplicação.

---

# Conceitos Abordados

Este projeto explora conceitos fundamentais relacionados a:

* Gerenciamento de containers;
* Docker Engine;
* Docker Registry;
* Docker API;
* Docker SDK for Python;
* Automação de infraestrutura;
* Atualização contínua;
* CI/CD;
* Observabilidade;
* Deploy automatizado;
* Versionamento de imagens;
* Containers Linux.

---

# Arquitetura da Solução

```text
                 Docker Registry
                        │
                        ▼
              Verificação Periódica
                        │
                        ▼
             Docker Auto Updater
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Verifica nova imagem          Mantém logs
        │
        ▼
 Docker Pull
        │
        ▼
 Parar Container
        │
        ▼
 Remover Container
        │
        ▼
 Criar Novo Container
        │
        ▼
 Aplicação Atualizada
```

---

# Fluxo de Funcionamento

```text
Monitoramento da Imagem
          │
          ▼
Verificação de Nova Versão
          │
          ▼
Download da Nova Imagem
          │
          ▼
Parada do Container Antigo
          │
          ▼
Remoção do Container Antigo
          │
          ▼
Criação do Novo Container
          │
          ▼
Aplicação Atualizada em Execução
```

---

# Tecnologias Utilizadas

* Python 3.12
* Docker Engine
* Docker SDK for Python
* PyYAML
* Logging
* Docker Compose
* Linux Ubuntu

---

# Estrutura Final do Projeto

```text
Projeto-Imagem-com-tag-Latest/
├── config/
│   └── config.yaml
├── logs/
│   └── updater.log
├── scheduler/
│   └── scheduler.py
├── updater/
│   ├── image_checker.py
│   ├── container_manager.py
│   └── rollback.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── .dockerignore
├── .gitignore
└── README.md
```

---

# Componentes Implementados

## config/config.yaml

Arquivo responsável pelas configurações da aplicação.

### Configurações disponíveis

* Imagem monitorada;
* Nome do container;
* Intervalo de verificação;
* Mapeamento de portas.

### Exemplo

```yaml
image: nginx:latest

container_name: nginx_app

interval: 60

ports:
  "8080": "80"
```

### Objetivo

Permitir alterações de configuração sem necessidade de modificar o código-fonte.

---

## scheduler/scheduler.py

Responsável pela execução periódica das verificações.

### Funções

* Executar verificações automaticamente;
* Respeitar o intervalo definido no arquivo de configuração;
* Manter o monitoramento contínuo.

---

## updater/image_checker.py

Responsável pela detecção de novas versões das imagens.

### Funções

* Obter ID da imagem local;
* Executar Docker Pull;
* Comparar versões da imagem;
* Identificar atualizações.

### Estratégia Utilizada

A detecção ocorre através da comparação entre o ID da imagem local e o ID retornado após o download da imagem mais recente.

---

## updater/container_manager.py

Responsável pelo gerenciamento dos containers.

### Funções

* Parar containers;
* Remover containers;
* Criar novos containers;
* Aplicar mapeamento de portas;
* Restaurar automaticamente a aplicação.

---

## updater/rollback.py

Módulo preparado para futuras implementações de rollback.

### Situação Atual

* Estrutura criada;
* Registro de falhas;
* Ponto de expansão para futuras versões.

---

## main.py

Arquivo principal do sistema.

### Responsabilidades

* Carregar configurações;
* Iniciar monitoramento;
* Coordenar os módulos;
* Executar atualizações automáticas;
* Registrar logs do processo.

---

# Sistema de Logs

O projeto registra automaticamente todas as operações realizadas.

Arquivo:

```text
logs/updater.log
```

Exemplo:

```text
Docker Auto Updater iniciado

Imagem atual: sha256:...

Verificando atualizações para nginx:latest

Nenhuma alteração detectada

Nenhuma atualização encontrada
```

Os logs permitem acompanhar todo o processo de monitoramento e atualização.

---

# Dockerfile

Foi criado um Dockerfile para permitir a execução da aplicação em containers.

Objetivos:

* Padronizar ambiente;
* Facilitar implantação;
* Simplificar execução em outros computadores.

---

# Docker Compose

Foi criado um arquivo docker-compose.yml para facilitar a execução do projeto.

Benefícios:

* Inicialização simplificada;
* Configuração centralizada;
* Persistência de logs;
* Integração com Docker Socket.

---

# Como Executar o Projeto

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

* Linux (Ubuntu recomendado);
* Docker instalado e em execução;
* Python 3.12 ou superior;
* Pip instalado;
* Acesso ao Docker Engine.

Verificar instalações:

```bash
docker --version

python3 --version

pip --version
```

---

## Método 1 — Execução Local com Python

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>

cd Projeto-Imagem-com-tag-Latest
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ativar ambiente virtual

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar aplicação

```bash
python main.py
```

O sistema iniciará o monitoramento automático da imagem configurada.

---

## Método 2 — Execução com Docker Compose

### Instalar Docker Compose (caso necessário)

Ubuntu:

```bash
sudo apt update

sudo apt install docker-compose-v2 -y
```

Verificar instalação:

```bash
docker compose version
```

### Construir e iniciar os containers

```bash
docker compose up -d --build
```

### Verificar containers em execução

```bash
docker ps
```

### Visualizar logs

```bash
tail -f logs/updater.log
```

### Encerrar execução

```bash
docker compose down
```

---

# Como Testar o Projeto

## Criar Container Monitorado

Criar um container utilizando a imagem monitorada:

```bash
docker run -d \
  --name nginx_app \
  -p 8080:80 \
  nginx:latest
```

Verificar se o container está ativo:

```bash
docker ps
```

---

## Validar Aplicação

Executar:

```bash
curl http://localhost:8080
```

Resultado esperado:

```text
Welcome to nginx!
```

---

## Validar Monitoramento

Executar o projeto:

```bash
python main.py
```

ou

```bash
docker compose up -d
```

Acompanhar logs:

```bash
tail -f logs/updater.log
```

Resultado esperado:

```text
Docker Auto Updater iniciado

Scheduler iniciado

Imagem atual: sha256:...

Verificando atualizações para nginx:latest

Nenhuma alteração detectada

Nenhuma atualização encontrada
```

O log deverá continuar sendo atualizado automaticamente conforme o intervalo configurado.

---

# Estado Final do Projeto

## Funcionalidades Implementadas

* Monitoramento periódico de imagens Docker;
* Suporte à tag latest;
* Download automático de imagens atualizadas;
* Comparação de versões através do ID da imagem;
* Integração com Docker SDK;
* Parada automática de containers;
* Remoção automática de containers;
* Criação automática de novos containers;
* Sistema de logs persistentes;
* Configuração via arquivo YAML;
* Execução local via Python;
* Execução containerizada via Docker Compose;
* Estrutura preparada para futuras implementações de rollback.

---

# Requisitos Atendidos

O projeto atende aos requisitos mínimos definidos na proposta:

- Monitoramento periódico de imagens Docker;
- Suporte à tag latest;
- Verificação de alterações da imagem;
- Download automático da nova imagem;
- Identificação de containers associados;
- Parada automática do container antigo;
- Remoção automática do container antigo;
- Criação automática de novo container;
- Restauração automática da aplicação;
- Compatibilidade com Linux e Docker.

---

# Resultados Obtidos

Durante os testes realizados foi possível validar:

* Monitoramento contínuo funcionando corretamente;
* Atualização automática da imagem monitorada;
* Gerenciamento automatizado de containers;
* Integração bem-sucedida com Docker Engine;
* Persistência de logs;
* Execução local e containerizada;
* Compatibilidade com ambiente Linux.

Todos os requisitos obrigatórios definidos no projeto foram implementados e testados com sucesso.

# Dificuldades Encontradas

Durante o desenvolvimento foram encontrados desafios relacionados a:

* Configuração do ambiente Python;
* Integração com Docker SDK;
* Gerenciamento de permissões do Docker;
* Persistência de logs;
* Execução containerizada utilizando Docker Compose.

Todos os problemas foram resolvidos durante a implementação e validação do projeto.

---

# Aprendizados Obtidos

Com este projeto foi possível compreender:

* Funcionamento da Docker API;
* Manipulação de imagens Docker;
* Gerenciamento de containers via código;
* Automação de deploy;
* Monitoramento contínuo;
* Estruturação de aplicações DevOps;
* Utilização de Docker Compose;
* Boas práticas de automação operacional.

---

# Conclusão

O projeto atingiu os objetivos propostos, implementando um sistema capaz de monitorar imagens Docker com tag latest, detectar alterações e atualizar automaticamente containers em execução.

A solução atende aos requisitos mínimos definidos na especificação e fornece uma base sólida para futuras evoluções, como rollback automático, health checks, notificações e suporte a múltiplos containers.

