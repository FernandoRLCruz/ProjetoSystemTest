from behave import *
from features.pages.store_carrinho_page import CarrinhoStorePage

use_step_matcher("re")


@given("Eu estou na página do carrinho")
def step_impl(context):
    context.store_carrinho_page = CarrinhoStorePage(context.driver)

@then("Eu clico no botão continuar do cadastro")
def step_impl(context):
    context.store_carrinho_page.clicar_continuar_carrinho()
