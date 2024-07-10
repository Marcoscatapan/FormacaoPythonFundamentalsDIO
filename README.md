# 6️⃣ Manipulando Arquivos no Sistema Bancário em Python

Nossa aplicação financeira reconhece a importância de rastrear e auditar as ações dos usuários para garantir a segurança e integridade das operações. Para melhorar essa funcionalidade, decidimos modificar o decorador de log atual, que imprime informações no console, para que ele registre essas informações em um arquivo de log. Isso não apenas facilitará a revisão e análise das operações, mas também permitirá um backup contínuo das atividades.

🎯 Objetivo

O objetivo deste projeto é implementar um decorador de log que registre detalhes específicos para cada chamada de função no sistema bancário. As informações registradas incluem data e hora atuais, nome da função, argumentos passados e valor retornado pela função, se aplicável. Esses registros serão salvos no arquivo log.txt.

🛠️ Funcionalidades

- Depósito: Permite ao cliente do banco depositar fundos em sua conta.

- Saque: Permite ao cliente do banco sacar fundos de sua conta, desde que haja saldo disponível e respeitando o limite de transações diárias.

- Extrato: Fornece ao cliente do banco um extrato de suas transações recentes, incluindo a data e a hora de cada transação.

- Nova Conta: Permite ao banco criar uma nova conta para um cliente.

- Listar Contas: Mostra todas as contas registradas no banco.

- Novo Usuário: Gera um novo usuário com informações básicas.

- Registro Detalhado: Cada operação será registrada com:

Data e hora da operação.

Nome da função executada.

Argumentos passados para a função.

Valor retornado pela função, se houver.

- Arquivo de Log log.txt:

Novos registros serão adicionados ao final do arquivo, se ele já existir.

Cada entrada de log será formatada em uma nova linha para facilitar a leitura e análise.

📚 Implementações Específicas

- Persistência de Dados: Garantir que todas as operações sejam registradas de forma persistente no arquivo log.txt.
  
- Facilidade de Revisão: Permitir uma revisão fácil e análise detalhada das operações realizadas pelos usuários do sistema bancário.

📝 Como Executar

Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório para o seu ambiente local.

Navegue até o diretório do projeto.

Execute o arquivo principal (Manipulando Arquivos no Sistema Bancário em Python.py) em seu terminal ou IDE Python.

🤝 Como Contribuir

Se deseja contribuir para este projeto, siga estas etapas:

Faça um fork do repositório.

Crie uma branch para sua nova feature (git checkout -b feature/nova-feature).

Implemente suas melhorias e novas funcionalidades utilizando funções em Python.

Commit suas mudanças (git commit -am 'Adiciona uma nova feature').

Push para a branch (git push origin feature/nova-feature).

Crie um novo Pull Request.

📋 Síntese do Projeto

Este projeto visa fortalecer a segurança e a integridade do sistema bancário Python, adicionando um decorador de log que registra todas as operações em um arquivo log.txt. Essa implementação não apenas simplifica a revisão das atividades realizadas, mas também possibilita análises mais profundas das operações dos usuários, contribuindo significativamente para a transparência e controle do sistema. Para mais detalhes sobre o projeto ou para qualquer dúvida, entre em contato conosco.
