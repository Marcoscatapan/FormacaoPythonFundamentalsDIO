# 4️⃣Inserindo Decoradores, Geradores e Iteradores no Sistema Bancário

Neste projeto, vamos atualizar a implementação do sistema bancário para incluir decoradores, geradores e iteradores, proporcionando um sistema mais robusto e eficiente.

🎯 Objetivo

O objetivo deste projeto é utilizar a Programação Orientada a Objetos (POO) para criar um sistema bancário estruturado, integrando decoradores, geradores e iteradores para funcionalidades avançadas.

🛠️ Funcionalidades

- Depósito: Permite ao cliente do banco depositar fundos em sua conta.
 
- Saque: Permite ao cliente do banco sacar fundos de sua conta, desde que haja saldo disponível.

- Extrato: Fornece ao cliente do banco um extrato de suas transações recentes.

- Nova Conta: Permite ao banco criar uma nova conta para um cliente.

- Listar Contas: Mostra todas as contas registradas no banco.

- Novo Usuário: Gera um novo usuário com informações básicas.

📚 Implementações Específicas

- Decorador de Log:

Implementação de um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc).
Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

- Gerador de Relatórios:

Criação de um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas.
Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).
Iterador Personalizado:

- Iterador:
  
Implementação de um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).

📝 Como Executar 

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone este repositório para o seu ambiente local.

3. Navegue até o diretório do projeto.

4. Execute o arquivo principal (Implementando gerador iterador e decorador no sistema bancário.py) em seu terminal ou IDE Python.

🤝 Como Contribuir 

Se deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma branch para sua nova feature (git checkout -b feature/nova-feature).

3. Implemente suas melhorias e novas funcionalidades utilizando funções em Python.

4. Commit suas mudanças (git commit -am 'Adiciona uma nova feature').

5. Push para a branch (git push origin feature/nova-feature).

6. Crie um novo Pull Request.

📋 Síntese do Projeto

Este projeto visa a otimização do sistema bancário em Python, adicionando um decorador de log, um gerador de relatório e um iterador personalizado. Se precisar de mais detalhes sobre as etapas do projeto ou tiver alguma dúvida, sinta-se à vontade para entrar em contato.
