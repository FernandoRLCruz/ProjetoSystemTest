from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AtendimentoStorePage(BasePage):
    contato_email = (By.XPATH, "(//button[contains(@class, 'contentTab__item-btn')])[1]")

    def navegar_pagina(self, url):
        self.open_url(url)

    def clicar_link_contato_email(self):
        self.press_down(self.contato_email)
        self.click(self.contato_email)

