from behave import *
from hamcrest import assert_that, contains_string
from features.pages.store_ajuda_page import AjudaStorePage

use_step_matcher("re")


@given("Eu estou na página de ajuda")
def step_impl(context):
    context.store_ajuda_page = AjudaStorePage(context.driver)


@then("Eu clico no link quero informações sobre meu pedido")
def step_impl(context):
    context.store_ajuda_page.clicar_botao_informacao_pedido()


@step("Eu preencho o campo nome da ajuda com valor (?P<nome>.+)")
def step_impl(context, nome):
    context.store_ajuda_page.inserir_nome(nome)


@step("Eu preencho o campo email da ajuda com valor (?P<email>.+)")
def step_impl(context, email):
    context.store_ajuda_page.inserir_email(email)


@step("Eu preencho o campo telefone de contato da ajuda com valor (?P<telefone>.+)")
def step_impl(context, telefone):
    context.store_ajuda_page.inserir_telefone(telefone)


@step("Eu preencho o campo pedido com valor (?P<pedido>.+)")
def step_impl(context, pedido):
    context.store_ajuda_page.inserir_numero_pedido(pedido)


@step("Eu seleciono o campo loja por com valor (?P<loja>.+)")
def step_impl(context, loja):
    context.store_ajuda_page.selecionar_loja(loja)


@step("Eu preeencho o campo da mensagem com valor (?P<mensagem>.+)")
def step_impl(context, mensagem):
    context.store_ajuda_page.inserir_mensagem(mensagem)


@step("Eu valido se a mensagem foi enviada atraves da confirmação (?P<confirmacao>.+)")
def step_impl(context, confirmacao):
    assert_that(context.store_ajuda_page.validar_mensagem(), contains_string(confirmacao))


@step("Eu preencho o campo documento da ajuda com valor (?P<documento>.+)")
def step_impl(context, documento):
    context.store_ajuda_page.inserir_documento(documento)


@step("Eu clico no botão enviar")
def step_impl(context):
    context.store_ajuda_page.clicar_enviar()
