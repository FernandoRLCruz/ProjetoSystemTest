from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class FinalizarCompraStorePage(BasePage):
    mensagem_compra = (By.XPATH, "(//h1)[1]")

    def validar_compra(self):
        return self.find(self.mensagem_compra).text