from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomeStorePage(BasePage):
    login = (By.XPATH, "//li[contains(@class, 'my-account login-btn')]")
    usuario_logado = (By.XPATH, "//span[contains(@class, 'ellipsis-text')]")
    atendimento = (By.XPATH, "(//a[contains(text(), 'Atendimento')])[2]")
    nossas_lojas = (By.XPATH, "(//a[contains(@href, '/nossas-lojas')])[2]")
    pesquisa = (By.ID, "q")
    lupa = (By.XPATH, "//div[contains(@class, 'chaordic-search-button full-width-button')]")
    produto_pesquisado = (By.XPATH, "//a[contains(@class, 'nm-product-img-link details')]")


    def navegar_pagina(self, url):
        self.open_url(url)

    def clicar_link_cadastro(self):
        self.click(self.login)

    def validar_usuario_logado(self):
        return self.find(self.usuario_logado).text

    def clicar_link_atendimento(self):
        self.click(self.atendimento)

    def clicar_link_nossas_lojas(self):
        self.press_down(self.nossas_lojas)
        self.click(self.nossas_lojas)

    def inserir_nome_produto(self, produto):
        self.type_in(self.pesquisa, produto)
        self.press_enter(self.pesquisa)

    def clicar_lupa(self):
        self.click(self.lupa)

    def clicar_produto_pesquisado(self):
        self.click(self.produto_pesquisado)
