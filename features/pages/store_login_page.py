from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class LoginStorePage(BasePage):
    button_cadastro = (By.XPATH, "//a[contains(@title, 'Cadastre-se')]")
    email = (By.ID, "email")
    senha = (By.ID, "pass")
    botao_continuar = (By.ID, "send2")
    login_email_compra = (By.ID, "login-email")
    login_password_compra = (By.ID, "login-password")



    def clicar_botao_cadastro(self):
        self.click(self.button_cadastro)

    def inserir_email(self, value):
        self.type_in(self.email, value)

    def inserir_senha(self, value):
        self.type_in(self.senha, value)

    def clicar_continuar(self):
        self.click(self.botao_continuar)

    def inserir_email_compra(self, value):
        self.type_in(self.login_email_compra, value)

    def inserir_password_compra(self, value):
        self.type_in(self.login_password_compra, value)