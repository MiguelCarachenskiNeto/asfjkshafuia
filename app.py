import os
import webbrowser as wb

sites=[ {"nome":"Google","endereco":"https://www.google.com/"},
        {"nome":"Youtube","endereco":"https://www.youtube.com/?app=desktop&hl=pt"},
        {"nome":"Classroom","endereco":"https://edu.google.com/intl/ALL_br/workspace-for-education/classroom/"}]


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main() 

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()


def desligar_app():
    mostrar_subtitulo("Finalizando o app")

def opcao_invalida():
    os.system("clear")
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def listar_sites():
    os.system("clear")
    print("sites cadastrados:\n")
    for site in sites:
        nome_site = site["nome"]
        endereco = site["endereco"]
        print(f"-{nome_site} --- {endereco}")
    voltar_ao_menu_principal() 

def abrir_site():
    os.system("clear")
    nome_site=input("digite o nome do site que deseja abrir:\n")
    site_encontrado = False
    os.system("clear")
    for site in sites:
        if nome_site == site["nome"]:
            site_encontrado = True
            wb.open_new_tab("https://www.google.com/")
    if not site_encontrado:
        print("O site não foi encontrado")
    voltar_ao_menu_principal()

def cadastrar_site():
    os.system("clear")
    nome_do_site=input("digite o nome do novo site: \n")
    os.system("clear")
    endereco_do_site=input(f"digite o endereço do site {nome_do_site}\n")
    sites.append({"nome":nome_do_site,"endereco":endereco_do_site})
    print(f"\nO site {nome_do_site} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

            

def nome_app():
    print("""

░██████╗░███████╗██████╗░███████╗███╗░░██╗░█████╗░██╗░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗
██╔════╝░██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░██╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝██║███████║██║░░██║██║░░██║██████╔╝  ██║░░██║█████╗░░
██║░░╚██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██║██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
╚██████╔╝███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗
░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

░██████╗██╗████████╗███████╗░██████╗
██╔════╝██║╚══██╔══╝██╔════╝██╔════╝
╚█████╗░██║░░░██║░░░█████╗░░╚█████╗░
░╚═══██╗██║░░░██║░░░██╔══╝░░░╚═══██╗
██████╔╝██║░░░██║░░░███████╗██████╔╝
╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
""")

def exibir_opcoes():
    print("1-listar sites")
    print("2-Abrir um site")
    print("3-cadastrar um site")
    print("4-Sair do programa\n")

def escolher_opcoes():
    try:
        escolha=int(input("Escolha uma opção: "))
        print("Você selecionou a opção:",escolha,"\n")
        if escolha == 1:
            listar_sites()
        elif escolha == 2:
            abrir_site()
        elif escolha == 3:
            cadastrar_site()
        elif escolha == 4:
            print("Você escolheu sair do programa\n")
            desligar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__=="__main__":
    main()
