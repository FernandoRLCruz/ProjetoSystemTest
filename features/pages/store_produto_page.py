from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProdutoStorePage(BasePage):


    titulo_produto = (By.XPATH, "(//h1)[2]")
    botao_comprar = (By.XPATH, "//button[contains(@data-button, 'add-to-cart')]")

    def validar_mensagem(self):
        return self.find(self.titulo_produto).text

    def clicar_comprar(self):
        self.click(self.botao_comprar)