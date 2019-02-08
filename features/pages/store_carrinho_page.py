from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CarrinhoStorePage(BasePage):
    botao_continuar = (By.ID, "proceed-checkout")

    def clicar_continuar_carrinho(self):
        self.click(self.botao_continuar)
