from connection import criar_conexao, fechar_conexao, insere_usuario, select_usuarios, del_usuarios, update_usuarios

def main():
    con = criar_conexao('localhost', 'root', '', 'escola')

    insere_usuario(con, 'Pedro Sampaio', 'pedriintrembala@gmail.com')

    # del_usuarios(con)

    # update_usuarios(con)

    select_usuarios(con)

    fechar_conexao(con)

    

if __name__ == '__main__':
    main()