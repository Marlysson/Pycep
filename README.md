## Pycep

Um wrapper para a api da ViaCEP para consulta dos endereços dos ceps do Brasil.
Depois de requisitar o endereço de um cep você pode tratar o retorno como se fosse um objeto normal , inclusive já feito o cast para o valor adequado.

### Requisitos
> Temporário ( futuramente não será necessário dependências )

- requests

## Como usar

Primeiramente rode o arquivo de requisitos do projeto.

```bash
pip install -r requirements.txt
```

Com as dependências instaladas você pode começar a requisitar os endereços.

```python
>>> from pycep import Pycep as pycep
>>> endereco = pycep.get("01001-000")
>>> endereco.localidade
São Paulo
>>> endereco.ibge
3550308
>>> endereco2 = pycep.get("01001000")
>>> endereco2.localidade
São Paulo
```

### Tratando erros:

Em qualquer caso de erro é levantada a exceção ```InvalidCepException``` , seja se o cep tiver strings , não contiver 8 caracteres..

```python
try:
	endereco = pycep.get("123456789")
except InvalidCepException:
	# Processamento em caso de erro
```

### Caso para o endereço não encontrado:

```python
try:
	endereco = pycep.get("99999999")
except AddressNotFound:
	# Processamento para endereço inexistente
```