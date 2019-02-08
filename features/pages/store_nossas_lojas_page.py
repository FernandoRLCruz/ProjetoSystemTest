from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class NossaLojaStorePage(BasePage):

    selecionar_estado_nossa_loja = (By.ID, "estados")
    local_nossa_loja = (By.XPATH, "(//b[contains(@class, 'titulo-lista')])[1]")


    def selecionar_estado(self, value):
        self.select_in_combo_by_value(self.selecionar_estado_nossa_loja, value)

    def validar_local(self):
        return self.find(self.local_nossa_loja).text
