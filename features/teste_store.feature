  # Created by crazydogretro at 26/01/19
  Feature: Teste no site da Saraiva
    # Feature para efetuar testes de no site da saraiva


    Scenario Outline: Efetuar Login com sucesso
      Given Eu estou na página principal
      Then  Eu clico em Login
      Given Eu estou na página de login
      Then Eu preencho o campo email do login com valor <email>
      And Eu preeencho o campo senha do login com valor <senha>
      Then Eu clico no botão continuar do login
      And Eu valido usuario logado com valor <usuario>

      Examples: login
        | email               | senha      | usuario       |
        | email               | senha      | projeto alegre|



    Scenario Outline: Entrar em contato com atendimento por email
      Given Eu estou na página principal
      And Eu clico no link de atendimento
      Given Eu estou na página Central de Atendimento
      Then Eu clico no link entrar em contato por email
      Given Eu estou na página de ajuda
      Then Eu clico no link quero informações sobre meu pedido
      And Eu preencho o campo nome da ajuda com valor <nome>
      And Eu preencho o campo documento da ajuda com valor <documento>
      And Eu preencho o campo email da ajuda com valor <email>
      And Eu preencho o campo telefone de contato da ajuda com valor <telefone>
      And Eu preencho o campo pedido com valor <pedido>
      And Eu seleciono o campo loja por com valor <loja>
      And Eu preeencho o campo da mensagem com valor <mensagem>
      And Eu clico no botão enviar
      And Eu valido se a mensagem foi enviada atraves da confirmação <confirmacao>

      Examples: ajuda
        | nome     | pedido       | email             | telefone    | loja    | mensagem   | confirmacao                          | documento   |
        | fernando | 654564564654 | email             | telefone    | Saraiva | Lorem ipsu | Sua mensagem foi enviada com sucesso.| 03975669829 |


    Scenario Outline: Efetuar uma busca por lojas no estado de Pernambuco
      Given Eu estou na página principal
      And Eu clico no botão Nossas Lojas
      Given Eu estou na página nossas lojas
      Then Eu seleciono o campo estado com valor <estado>
      And Eu valido se os resultados apresentados posssuem o valor <local>

      Examples: lojas
        | estado     | local           |
        | pe         | Shopping Recife |


    Scenario Outline: Efetuar busca por produto
      Given Eu estou na página principal
      Then  Eu digito na barra de busca o valor <produto>
      And Eu clico no botão da lupa
      Given Eu estou na página de busca do produto
      Then Eu seleciono o produto que foi efetuado a busca <produto>
      Given Eu estou na página do produto
      And Eu valido a descrição do produto <produto>


      Examples: produto
        | produto               |
        | Watch Dogs - Xbox One |

    @wip
    Scenario Outline: Adicionar produto ao carrinho
      Given Eu estou na página principal
      Then  Eu digito na barra de busca o valor <produto>
      And Eu clico no botão da lupa
      Given Eu estou na página de busca do produto
      Then Eu seleciono o produto que foi efetuado a busca <produto>
      Given Eu estou na página do produto
      And Eu valido a descrição do produto <produto>
      And Eu clico no botão comprar
      Given Eu estou na página do carrinho
      Then Eu clico no botão continuar do cadastro
      Given Eu estou na página de login
      Then Eu preencho o campo email do login compra com valor <email>
      And Eu preeencho o campo senha do login compra com valor <senha>
      And Eu clico no botão continuar do login
      Given Eu estou na Entrega page
      And Eu valido dados da entrega nome valor <nome>
      And Eu valido dados da entrega endereço valor <endereco>
      And Eu valido dados da entrega complemento valor <complemento>
      Then Eu clico no botao continuar
      Given Eu estou na pagina de pagamento
      Then Eu seleciono a opção boleto
      And Eu clico no botão finalizar compra
      Given Eu estou na pagina de final de compra
      Then Eu valido se pedido foi efetuado com sucesso atraves da <mensagem>

      Examples: compra
        | produto                                                           | email               | senha      | endereco                    | complemento                                  | mensagem              | nome          |
        | Tom Clancy's - Ghost Recon Wildlands - Limited Edition - Xbox One | email               | senha      | Avenida Ulisses Montarroyos | Piedade Jaboatao dos Guararapes - Pernambuco | Aguardando pagamento! | Fernando cruz |

