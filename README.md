# Profile Craft

## 🧬 Gerador de Perfis Sintéticos para Testes e Simulações

O **Profile Craft** é uma ferramenta para geração de **perfis sintéticos (dados fictícios)** voltados para testes de sistemas, simulações de dados e validação de regras de negócio.

Permite criar perfis estruturados com dados sintéticos realistas, proporcionando maior confiabilidade e agilidade em ambientes de desenvolvimento, QA e homologação.

---

## Funcionalidades:

- ✅ Geração de perfis completos
- ✅ Distribuição por região do Brasil
- ✅ Estados organizados por região
- ✅ 50 profissões por região
- ✅ Nomes, sobrenomes e cpf (fictícios)
- ✅ Telefones e e-mails aleatórios
- ✅ Dados demográficos simulados
- ✅ Estrutura JSON pronta para integração
- ✅ Geração em volume para testes de escala

---

## Exemplos de perfis:

Perfis simples:
```json
  {
      "name": "Leonardo",
      "lastname": "Ramos",
      "second_lastname": "Coutinho",
      "email": "leonardo_coutinho@mail.io"
  }
```


Perfis completos:
```json
{
   "cpf": "776.730.881-26",
      "name": "Gabriela",
      "lastname": "Goncalves",
      "second_lastname": "Conceicao",
      "birthday": "10/09/1961",
      "uf": "MS",
      "state": "Mato Grosso do Sul",
      "city": "Campo Grande",
      "job": "Analista de RH",
      "telephone": [
          "(67)3406-8370",
          "(67)7303-1766"
      ],
      "email": [
          "ga_conceicao2@mail.io",
          "goncalves.gabriela@mail.com.br",
          "goncalves_gabriela@mail.net"
      ],
      "relationship": "Casado(a)",
      "partner": {
          "cpf": "435.078.181-16",
          "name": "Fabio",
          "lastname": "Santo",
          "second_lastname": "Pinto",
          "birthday": "10/09/1961",
          "uf": "GO",
          "state": "Goiás",
          "city": "Goiânia",
          "job": "Eletricista",
          "telephone": [
              "(62)96644-8103"
          ],
          "email": [
              "fabio_santo@mail.ia@edumail.edu",
              "santofabiopinto@mail.io",
              "pintofabio@mail.net"
          ]
      }
  }
```

Perfil com hereditário:

```json
{
      "cpf": "595.303.659-00",
      "name": "Sara",
      "lastname": "Diniz",
      "second_lastname": "Brandao",
      "birthday": "25/11/2005",
      "uf": "PR",
      "state": "Paraná",
      "city": "Curitiba",
      "job": "Vendedor(a) de lojas",
      "telephone": [
          "(41)98680-2026",
          "(41)95160-8274",
          "(41)98724-4620"
      ],
      "email": [
          "saraviera@mail.io"
      ],
      "relationship": "Casado(a)",
      "partner": {
          "cpf": "071.255.454-83",
          "name": "Ronaldo",
          "lastname": "Medeiros",
          "second_lastname": "Farias",
          "birthday": "25/11/2005",
          "uf": "PE",
          "state": "Pernambuco",
          "city": "Recife",
          "job": "Vigilante",
          "telephone": [
              "(81)97241-8385",
              "(81)94687-7781",
              "(81)94060-3024"
          ],
          "email": [
              "medeiros.ronaldo.farias@mail.net",
              "medeiros.ronaldo.farias@mail.io"
          ]
      },
      "father": {
          "cpf": "870.885.431-00",
          "name": "Orlando",
          "lastname": "Diniz",
          "second_lastname": "Leite",
          "birthday": "31/08/1974",
          "uf": "MT",
          "state": "Mato Grosso",
          "city": "Cuiabá",
          "job": "Analista financeiro",
          "telephone": [
              "(65)0886-1516"
          ],
          "email": [
              "orlando-diniz@xmail.com",
              "orla_leite36@mail.com.br",
              "diniz.orlando@mail.com"
          ]
      },
      "mother": {
          "cpf": "871.086.663-08",
          "name": "Rosilene",
          "lastname": "Brandao",
          "second_lastname": "Saraiva",
          "birthday": "27/06/1961",
          "uf": "PI",
          "state": "Piauí",
          "city": "Teresina",
          "job": "Desempregado(a)",
          "telephone": [
              "(86)97056-5513",
              "(86)4842-7850",
              "(86)7547-8433"
          ],
          "email": [
              "rosaraiva48@mail.io",
              "rosilene.brandao@mail.ia@edumail.edu",
              "saraiva_rosilene@xmail.com"
          ]
      }
  }
```
