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

## ✅ Resultado Esperado

Ao final do projeto, o sistema deverá ser capaz de realizar atualizações automáticas de containers Docker sem intervenção manual, garantindo que aplicações executem sempre a versão mais recente disponível da imagem monitorada.
