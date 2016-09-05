# Semantic Template Tests

## Como desenvolver?

Siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```bash
git clone https://github.com/rg3915/semantic-template.git
cd semantic-template
python -m venv .venv
source .venv/bin/activate # Linux
pip install -r requirements.txt
python contrib/env_gen.py
var=`python contrib/secret_gen.py`
printf '\nSECRET_KEY='$var >> .env
python manage.py test
```