from behave import *
from hamcrest import assert_that, contains_string
from features.pages.store_produto_page import ProdutoStorePage

use_step_matcher("re")


@given("Eu estou na página do produto")
def step_impl(context):
    context.store_produto_page = ProdutoStorePage(context.driver)


@step("Eu valido a descrição do produto (?P<produto>.+)")
def step_impl(context, produto):
    assert_that(context.store_produto_page.validar_mensagem(), contains_string(produto))


@step("Eu clico no botão comprar")
def step_impl(context):
    context.store_produto_page.clicar_comprar()
