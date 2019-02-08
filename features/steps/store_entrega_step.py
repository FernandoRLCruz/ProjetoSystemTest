from behave import *
from hamcrest import assert_that, contains_string
from features.pages.store_entrega_page import EntregaStorePage

use_step_matcher("re")


@given("Eu estou na Entrega page")
def step_impl(context):
    context.store_entrega_page = EntregaStorePage(context.driver)


@step("Eu valido dados da entrega nome valor (?P<nome>.+)")
def step_impl(context, nome):
    assert_that(context.store_entrega_page.validar_nome_entrega(), contains_string(nome))


@step("Eu valido dados da entrega endereço valor (?P<endereco>.+)")
def step_impl(context, endereco):
    assert_that(context.store_entrega_page.validar_endereco_entrega(), contains_string(endereco))


@step("Eu valido dados do produto valor (?P<valor>.+)")
def step_impl(context, valor):
    assert_that(context.store_entrega_page.valor_total_entrega(), contains_string(valor))


@step("Eu valido dados da entrega complemento valor (?P<complemento>.+)")
def step_impl(context, complemento):
    assert_that(context.store_entrega_page.validar_endereco_complemento(), contains_string(complemento))


@then("Eu clico no botao continuar")
def step_impl(context):
    context.store_entrega_page.clicar_continuar_cadastro()