from modulos import integra_git, imprimi_format, ledados

nome, projeto = ledados()
num_estrelas = integra_git(nome, projeto)


if __name__ == "__main__":
    imprimi_format(num_estrelas)

