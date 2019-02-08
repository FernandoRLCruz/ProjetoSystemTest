from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class EntregaStorePage(BasePage):
    botao_continuar = (By.XPATH, "(//button[contains(text(), 'Continuar')])[2]")
    nome_entrega = (By.XPATH, "(//p[contains(@class, 'sa_name')])[1]")
    endereco_entrega = (By.XPATH, "(//p[contains(@class, 'sa_adress')])[1]")
    complemento_entrega = (By.XPATH, "(//p[contains(@class, 'sa_adress_2')])[1]")
    valor_total_entrega = (By.XPATH, "(//p[contains(@class, 'total_final')]/*)[1]")

    def clicar_continuar_cadastro(self):
        self.press_down(self.botao_continuar)
        self.click(self.botao_continuar)

    def validar_nome_entrega(self):
        return self.find(self.nome_entrega).text

    def validar_endereco_entrega(self):
        return self.find(self.endereco_entrega).text

    def validar_endereco_complemento(self):
        return self.find(self.complemento_entrega).text

    def valor_total_entrega(self):
        return self.find(self.valor_total_entrega).text