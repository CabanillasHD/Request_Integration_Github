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
        print(f'Esse projeto tem um total de: {estrelas} estrelas' if estrelas > 1 else
              f'Esse projeto tem um total de: {estrelas} estrela')
        print('=*' * 20)


def ledados():
    git = str(input('Digite o nome do seu GITHUB: ')).strip()
    if git.strip() == '':
        git = 'CabanillasHD'
        proj = 'PythonBeginner'
        print(f'Você não preencheu o nome do Github, com isso usaremos o {git} e o projeto {proj}, '
              'como padrão')
        return git, proj
    else:
        gitpreenchido = git
        proj = str(input('Digite o nome do seu Projeto: ')).strip()
        if proj.strip() == '':
            proj = str('PythonBeginner')
            print(f'Nome de projeto inválido, o git usado será o {git} e projeto {proj} será usado como padrão')
            return gitpreenchido, proj
        else:
            return git, proj
