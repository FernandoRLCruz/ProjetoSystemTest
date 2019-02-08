import time

from behave import *
from features.pages.store_login_page import LoginStorePage

use_step_matcher("re")


@given("Eu estou na página de login")
def step_impl(context):
    context.store_login_page = LoginStorePage(context.driver)


@then("Eu clico no botão efetuar cadastro")
def step_impl(context):
    context.store_login_page.clicar_botao_cadastro()


@step("Eu preeencho o campo senha do login compra com valor (?P<senha>.+)")
def step_impl(context, senha):
    context.store_login_page.inserir_password_compra(senha)


@step("Eu preencho o campo email do login compra com valor (?P<email>.+)")
def step_impl(context, email):
    context.store_login_page.inserir_email_compra(email)

@step("Eu preeencho o campo senha do login com valor (?P<senha>.+)")
def step_impl(context, senha):
    context.store_login_page.inserir_senha(senha)


@step("Eu preencho o campo email do login com valor (?P<email>.+)")
def step_impl(context, email):
    context.store_login_page.inserir_email(email)


@then("Eu clico no botão continuar do login")
def step_impl(context):
    context.store_login_page.clicar_continuar()



