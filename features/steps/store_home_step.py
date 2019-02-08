from behave import *
from hamcrest import assert_that, contains_string

from features.pages.store_home_page import HomeStorePage
from features.pages.store_produto_page import ProdutoStorePage

use_step_matcher("re")


@given("Eu estou na página principal")
def step_impl(context):
    context.store_home_page = HomeStorePage(context.driver)
    context.store_home_page.navegar_pagina(context.config.userdata['url'])


@then("Eu clico em Login")
def step_impl(context):
    context.store_home_page.clicar_link_cadastro()


@step("Eu valido usuario logado com valor (?P<usuario>.+)")
def step_impl(context, usuario):
    assert_that(context.store_home_page.validar_usuario_logado(), contains_string(usuario))


@step("Eu clico no link de atendimento")
def step_impl(context):
    context.store_home_page.clicar_link_atendimento()


@step("Eu clico no botão Nossas Lojas")
def step_impl(context):
    context.store_home_page.clicar_link_nossas_lojas()


@then("Eu digito na barra de busca o valor (?P<produto>.+)")
def step_impl(context, produto):
    context.store_home_page.inserir_nome_produto(produto)

@step("Eu clico no botão da lupa")
def step_impl(context):
    context.store_home_page.clicar_lupa()


@given("Eu estou na página de busca do produto")
def step_impl(context):
    context.store_produto_page = ProdutoStorePage(context.driver)



@then("Eu seleciono o produto que foi efetuado a busca (?P<produto>.+)")
def step_impl(context, produto):
    context.store_home_page.clicar_produto_pesquisado()