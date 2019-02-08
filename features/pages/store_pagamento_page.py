from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class PagamentoStorePage(BasePage):
    opcao_boleto = (By.XPATH, "//div[contains(@class, 'accord_title paymentmanager_billetpaymentmanager_billet')]")
    botao_finalizar_compra = (By.XPATH, "//button[contains(@class, 'co_bt_send_payment')]")

    def clicar_boleto(self):
        self.click(self.opcao_boleto)


    def clicar_finalizar_compra(self):
        self.click(self.botao_finalizar_compra)