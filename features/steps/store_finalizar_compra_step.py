from behave import *
from hamcrest import assert_that, contains_string
from features.pages.store_finalizar_compra_page import FinalizarCompraStorePage

use_step_matcher("re")


@given("Eu estou na pagina de final de compra")
def step_impl(context):
    context.store_finalizar_compra_page = FinalizarCompraStorePage(context.driver)


@then("Eu valido se pedido foi efetuado com sucesso atraves da (?P<mensagem>.+)")
def step_impl(context, mensagem):
    assert_that(context.store_finalizar_compra_page.validar_compra(), contains_string(mensagem))
