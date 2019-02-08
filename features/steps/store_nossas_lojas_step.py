from behave import *
from hamcrest import assert_that, contains_string
from features.pages.store_nossas_lojas_page import NossaLojaStorePage

use_step_matcher("re")


@given("Eu estou na página nossas lojas")
def step_impl(context):
    context.store_nossa_loja = NossaLojaStorePage(context.driver)


@then("Eu seleciono o campo estado com valor (?P<estado>.+)")
def step_impl(context, estado):
    context.store_nossa_loja.selecionar_estado(estado)


@step("Eu valido se os resultados apresentados posssuem o valor (?P<local>.+)")
def step_impl(context, local):
    assert_that(context.store_nossa_loja.validar_local(), contains_string(local))
