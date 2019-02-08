from behave import *
from features.pages.store_atendimento_page import AtendimentoStorePage


use_step_matcher("re")


@given("Eu estou na página Central de Atendimento")
def step_impl(context):
    context.store_atendimento_page = AtendimentoStorePage(context.driver)


@then("Eu clico no link entrar em contato por email")
def step_impl(context):
    context.store_atendimento_page.clicar_link_contato_email()
