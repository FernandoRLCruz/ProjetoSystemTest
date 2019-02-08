from behave import *


from features.pages.store_pagamento_page import PagamentoStorePage

use_step_matcher("re")


@given("Eu estou na pagina de pagamento")
def step_impl(context):
    context.store_pagamento_page = PagamentoStorePage(context.driver)


@then("Eu seleciono a opção boleto")
def step_impl(context):
    context.store_pagamento_page.clicar_boleto()


@step("Eu clico no botão finalizar compra")
def step_impl(context):
    context.store_pagamento_page.clicar_finalizar_compra()