# Projeto: Docker Auto Updater

## Tema do Projeto

Desenvolvimento de um sistema automatizado capaz de monitorar imagens Docker com a tag **`latest`**, detectar novas versões publicadas em um registry e atualizar automaticamente os containers em execução.

---

## Objetivo do Projeto

O objetivo deste projeto é desenvolver uma solução automatizada capaz de monitorar periodicamente imagens Docker publicadas em registries de containers e identificar alterações em imagens que utilizam a tag **`latest`**.

Quando uma nova versão da imagem for detectada no registry, o sistema deverá:

- Identificar a atualização;
- Baixar a nova imagem;
- Interromper o container antigo;
- Remover o container desatualizado;
- Criar um novo container utilizando a imagem atualizada;
- Restaurar a execução da aplicação automaticamente.

---

## Conceitos Abordados

Este projeto busca explorar conceitos fundamentais relacionados a:

- Gerenciamento de containers;
- Automação de infraestrutura;
- Versionamento de imagens;
- Registries Docker;
- CI/CD (Continuous Integration / Continuous Delivery);
- Rolling Updates;
- Atualização contínua;
- Observabilidade;
- Automação operacional.

---

## Fluxo de Funcionamento

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

## Resultado Esperado

Ao final do projeto, o sistema deverá ser capaz de realizar atualizações automáticas de containers Docker sem intervenção manual, garantindo que aplicações executem sempre a versão mais recente disponível da imagem monitorada.

## Estrutura Atual do Projeto

Até o momento foi criada a estrutura base da aplicação em Python, utilizando a Docker SDK para comunicação direta com o Docker Engine.

```text
docker-auto-updater/
├── config/
│   └── config.yaml
├── logs/
├── scheduler/
│   └── scheduler.py
├── updater/
│   ├── image_checker.py
│   ├── container_manager.py
│   └── rollback.py
├── main.py
├── requirements.txt
└── venv/
```

---

# Tecnologias Escolhidas

## Python

Foi escolhido Python por possuir uma curva de desenvolvimento rápida, boa integração com Docker através da Docker SDK e facilidade para automação de processos.

## Docker SDK for Python

A biblioteca `docker` foi escolhida para atender ao requisito de utilização da API Docker, evitando a dependência exclusiva da Docker CLI.

## PyYAML

Utilizado para carregar as configurações do sistema a partir de um arquivo externo (`config.yaml`), permitindo alterar parâmetros sem modificar o código-fonte.

---

# Componentes Implementados

## config/config.yaml

Arquivo responsável pelas configurações da aplicação.

### Atualmente armazena:

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

### Motivação

Centralizar configurações em um único local para facilitar manutenção e testes.

---

## scheduler/scheduler.py

Responsável pela execução periódica das verificações.

### Função principal

* Executar continuamente o monitoramento em intervalos definidos.

### Motivação

Separar a lógica de agendamento da lógica de atualização.

---

## updater/image_checker.py

Responsável por verificar se existe uma nova versão da imagem monitorada.

### Funções implementadas

* Obter a imagem local;
* Realizar download da imagem mais recente;
* Comparar versões;
* Informar se houve atualização.

### Motivação

Manter toda a lógica de detecção de atualizações isolada em um único módulo.

---

## updater/container_manager.py

Responsável pelo gerenciamento dos containers Docker.

### Funções implementadas

* Parar containers;
* Remover containers;
* Criar novos containers;
* Configurar portas automaticamente.

### Motivação

Centralizar toda interação com a Docker API.

---

## updater/rollback.py

Módulo reservado para futuras implementações de rollback.

### Atualmente

* Registra eventos de falha durante a atualização.

### Motivação

Preparar a arquitetura para expansão futura sem alterar a estrutura principal do projeto.

---

## main.py

Arquivo principal da aplicação.

### Responsabilidades

* Carregar configurações;
* Iniciar monitoramento;
* Coordenar os módulos;
* Executar o fluxo completo de atualização.

### Fluxo implementado

1. Ler configurações;
2. Verificar atualização da imagem;
3. Detectar nova versão;
4. Parar container antigo;
5. Remover container antigo;
6. Criar novo container;
7. Registrar resultado em log.

---

# Dependências Instaladas

O projeto utiliza atualmente:

```txt
docker
PyYAML
requests
```

### Instalação

```bash
pip install -r requirements.txt
```

---

# Estado Atual do Desenvolvimento

## Concluído

* Estrutura inicial do projeto;
* Ambiente Python configurado;
* Ambiente virtual configurado;
* Configuração via YAML;
* Integração inicial com Docker SDK;
* Módulo de monitoramento;
* Módulo de gerenciamento de containers;
* Sistema de logs;
* Estrutura para rollback.

## Em Desenvolvimento

* Testes integrados;
* Comparação por digest SHA256;
* Health Check;
* Rollback funcional;
* Dockerfile;
* Docker Compose;
* Suporte a múltiplos containers.

---

# Próximos Passos

1. Executar testes locais;
2. Validar atualização automática;
3. Implementar comparação por digest;
4. Implementar Health Check;
5. Implementar rollback real;
6. Criar Dockerfile;
7. Criar docker-compose.yml;
8. Finalizar documentação;
9. Gravar vídeo demonstrativo.

