# Projeto - Curso Python DIO

O presente trata-se de um projeto desenvolvido no Curso de Python da plataforma DIO, com o intuito de botar em prática os conceitos trabalhados nas aulas anteriores. Tratando-se de um software que simula um sistema bancário básico.

A princípio, o sistema foi desenvolvido considerando apenas um usuário, sem a necessidade de manter os dados da conta ou informações pessoais. Focou-se apenas no controle do saldo da conta, possibilitando o usuário a relaizar 3 operações com o sistema:
* Saque: podendo realizar 3 saques diários, de no máximo R$ 500,00 reais cada;
* Depósito
* Extrato: gera um extrato detalhado das operações que foram realizadas na conta na ordem em que forma realizadas.

O menu foi desenvolvido através de estruturas condicionais if/elif/else.

A função de saque, assim como o menu, foi montado através de estruturas condicionais para verificar se o valor do saque excede o saldo atual ou o limite, ou se o número de saques feitos no dia excedem o limite diário.

Além disso, fora implementado um mecanismo, tanto na função de saque como na de depósito, que caso o usuário informe um valor negativo, o mesmo seja transformado em um número positivo ao multiplicá-lo por -1. Evitando assim problemas decorrentes dessa possível confusão.
