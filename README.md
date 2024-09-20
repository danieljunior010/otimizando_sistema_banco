# Otimizando Sistema Bancário

# Sistema Bancário em Python

Este é um sistema bancário simples implementado em Python, que permite realizar operações básicas como saque, depósito e exibição de extrato. Além disso, ele oferece funcionalidades para criar novos usuários e contas correntes, gerenciando as informações através de listas.

## Funcionalidades

O sistema oferece as seguintes operações:

- **Depósito**: Permite ao usuário realizar um depósito em sua conta.
- **Saque**: Permite ao usuário realizar saques, respeitando o limite diário de valor e o número máximo de saques permitidos.
- **Extrato**: Exibe o extrato da conta, mostrando as movimentações (depósitos e saques) e o saldo atual.
- **Criar Usuário**: Permite o cadastro de novos usuários. Cada usuário é identificado pelo CPF, e não é permitido cadastrar dois usuários com o mesmo CPF.
- **Criar Conta Corrente**: Permite a criação de contas correntes vinculadas a um usuário existente, utilizando o CPF para identificar o usuário.
- **Listar Contas**: Exibe todas as contas criadas no sistema, juntamente com suas respectivas agências e titulares.

## Estrutura de Dados

- **Usuários**: Um usuário é composto pelos seguintes dados:
  - `Nome`: Nome completo do usuário.
  - `Data de Nascimento`: Data de nascimento no formato `dd-mm-aaaa`.
  - `CPF`: Número do CPF (somente os dígitos).
  - `Endereço`: Endereço no formato `logradouro, número, bairro, cidade/sigla estado`.

- **Contas Correntes**: Cada conta corrente possui:
  - `Agência`: Fixa em "0001".
  - `Número da Conta`: Um número sequencial que começa em 1.
  - `Usuário`: O usuário titular da conta, identificado pelo CPF.

## Requisitos

- Python 3.6 ou superior.

## Como Executar

1. Clone este repositório ou baixe o arquivo `sistema_bancario.py`.
2. Execute o arquivo Python em seu terminal:
   ```bash
   python sistema_bancario.py

3. Interaja com o menu so Sistema
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[l] Listar Contas
[q] Sair

## Exemplo de uso
# Criar usuário

Ao escolher a opção "U" no menu, você deverá fornecer as seguintes informações:
- `Nome`: João Silva
- `Data de nascimento (dd-mm-aaaa)`: 15-08-1985
- `CPF (apenas números)`: 12345678901
- `Endereço (logradouro, número, bairro, cidade/sigla estado)`: Rua A, 100, Centro, São Paulo/SP
- Usuário criado com sucesso!
