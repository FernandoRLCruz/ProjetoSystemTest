from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AjudaStorePage(BasePage):
    botao_informacao_pedido = (By.XPATH, "(//button[contains(@class, 'attendance--btn-subjects')])[1]")
    nome_ajuda = (By.ID, "formularioMeuPedido-nome")
    documento_ajuda = (By.ID, "formularioMeuPedido-documento")
    email_ajuda = (By.ID, "formularioMeuPedido-e-mail")
    telefone_ajuda = (By.ID, "formularioMeuPedido-telefone")
    numero_pedido_ajuda = (By.ID, "formularioMeuPedido-pedido")
    loja_ajuda = (By.NAME, "loja")
    mensagem_ajuda = (By.ID, "formularioMeuPedido-mensagem")
    botao_enviar_ajuda = (By.XPATH, "(//input[contains(@class, 'bt_enviar btn-primary btn-medium')])[1]")
    loja_campo_selecionar_ajuda = (By.XPATH, "(//div[contains(@class, 'chosen-container chosen-container-single chosen-container-single-nosearch')])[1]")
    loja_campo_valor_ajuda = (By.XPATH, "(//li[contains(@data-option-array-index, '1')])[1]")
    mensagem_confirmacao_ajuda = (By.XPATH, "(//h2)[1]")

    def clicar_botao_informacao_pedido(self):
        self.click(self.botao_informacao_pedido)

    def inserir_nome(self, value):
        self.type_in(self.nome_ajuda, value)

    def inserir_documento(self, value):
        self.type_in(self.documento_ajuda, value)

    def inserir_email(self, value):
        self.type_in(self.email_ajuda, value)

    def inserir_telefone(self, value):
        self.type_in(self.telefone_ajuda, value)

    def inserir_numero_pedido(self, value):
        self.type_in(self.numero_pedido_ajuda, value)

    def selecionar_loja(self):
        self.click(self.loja_campo_selecionar_ajuda)
        self.click(self.loja_campo_valor_ajuda)

    def inserir_mensagem(self, value):
        self.type_in(self.mensagem_ajuda, value)

    def clicar_enviar(self):
        self.click(self.botao_enviar_ajuda)

    def validar_mensagem(self):
        return self.find(self.mensagem_confirmacao_ajuda).text