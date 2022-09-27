import requests
import json


def integra_git(nome_git='CabanillasHD', nome_projeto='PythonBeginner'):
    r = requests.get(f'https://api.github.com/repos/{nome_git}/{nome_projeto}')
    if r.status_code == 200:
        dic = r.json()
        return dic['stargazers_count']


def imprimi_format(num):
    try:
        estrelas = int(num)
    except:
        print('Ops: Algo deu errado')
    else:
        print('=*' * 20)
        print(f'Esse projeto tem um total de {estrelas} estrelas' if estrelas > 1 else
              f'Esse projeto tem um total de {estrelas} estrela')
        print('=*' * 20)

