import random


class CpfCreator:
    """
        Script que gera cpfs para uso em teste de sistemas
        !!! Importante esses cpfs são FICTICIOS servindo apenas para testes!!!
    """

    uf_code: int = 0

    def return_new_cpf(self, uf: int) -> str:
        self.uf_code = uf
        return self.create_new_cpf()

    def create_new_cpf(self):
        """
            Cria um novo cpf

            Steps:
                - Cria a sequencia basica do cpf
                - Adiciona o codigo da uf no fim da sequencia basica
                - Gera o primeiro codigo verificador
                - Adiciona o codifo verificador ao fim da sequencia anterior
                - Gera o segundo codigo verificador
                - Adiciona o segundo codigo verificador ao fim da sequencia anterior
                - Formata o cpf

            Return:
                - Retorna o cpf já formatado
        """
        try:
            # sequencia base com 8 digitos aleatorios
            base: str = self.create_sequence_base()
            # sequnecia base + o digito da uf
            sequence: str = base + str(self.uf_code)

            # retorna o primeiro digito verificador
            first: str = self.validate_character(sequence, 9)
            # sequencia + primeiro digito verificador
            text: str = sequence + first
            # retorna o segundo digito verificador
            second: str = self.validate_character(text, 10)

            return self.return_cpf_formated(sequence, first, second)

        except TypeError:
            print("Valor invalido!\n")

    @staticmethod
    def return_cpf_formated(sequence, first, second):
        cpf: str = f"{sequence[:3]}.{sequence[3:6]}.{sequence[6:9]}-{first}{second}"
        return cpf

    def create_sequence_base(self) -> str:
        """ Cria a sequencia base do cpf """
        value: str = ''

        for _ in range(8):
            number = self.get_random_number()
            value += number
        return str(value)

    @staticmethod
    def get_random_number() -> str:
        value = str(random.randint(0, 9))
        return value

    @staticmethod
    def validate_character(value, index) -> str:
        """ Cria o digito de verificação """
        m: int = index + 1
        total: int = 0

        for item in value:
            total += int(item) * m
            m -= 1

        result: int = total % 11
        if result > 2:
            result = 11 - result

        else:
            result = 0

        return str(result)
