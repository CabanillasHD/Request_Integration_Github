from modulos import integra_git, imprimi_format

nome = str(input('Digite o nome do seu GITHUB: ')).strip()
projeto = str(input('Digite o nome do seu Projeto: ')).strip()

if nome.strip() == '':
    num_estrelas = integra_git()
elif projeto.strip() == '':
    num_estrelas = integra_git()
else:
    num_estrelas = integra_git(nome, projeto)

if __name__ == "__main__":
    imprimi_format(num_estrelas)

