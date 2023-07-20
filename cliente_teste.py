from unittest import main, TestCase
from entidades.cliente import Cliente
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ClienteTeste(TestCase):
    def setUp(self) -> None:
        super().setUp()
        hoje = datetime.today()
        ontem = hoje + timedelta(-1)
        self.ontem = ontem
        self.cliente = Cliente(
            nome_completo="teste da silva",
            data_criacao=ontem.strftime("%d/%m/%Y"),
            data_nascimento="10/10/2000",
            email="teste@gmail.com"
        )
    
    def testar_regra_cupom_10(self):
        cupom_gerado = self.cliente.gerar_cupom_desconto()
        self.assertEqual(cupom_gerado, "TESTE10", "Erro na regra para gerar 10% de desconto")

    def testar_regra_cupom_20(self):
        ano_retrassado = self.ontem - relativedelta(years=2)
        self.cliente.data_criacao = ano_retrassado.strftime("%d/%m/%Y")
        cupom_gerado = self.cliente.gerar_cupom_desconto()
        self.assertEqual(cupom_gerado, "TESTE20", "Erro na regra para gerar 20% de desconto")
    
    def testar_regra_cupom_30(self):
        ano_retrassado = self.ontem - relativedelta(years=3)
        self.cliente.data_criacao = ano_retrassado.strftime("%d/%m/%Y")
        cupom_gerado = self.cliente.gerar_cupom_desconto()
        self.assertEqual(cupom_gerado, "TESTE30", "Erro na regra para gerar 30% de desconto")


if __name__ == "__main__":
    main()