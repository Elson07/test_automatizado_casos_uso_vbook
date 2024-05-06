class Xpath():

    BTN = {        
        'USUARIO' : '/html/body/div/div/div[3]/div[1]/div/div[2]/button', 
        'ENTRAR' : '/html/body/div/div/div[3]/div[1]/div/div[2]/div/div/form/div[4]/button',
        'GERENCIAR' : '/html/body/div/div/div[3]/div[1]/div/div[2]/div/div/a[1]',
        'CRIAR' : '/html/body/div/div/div[1]/div[2]/div[4]/a[2]',
        'CADASTRAR_SE': '//*[@id="content"]/div[1]/div/div[2]/div/div/form/a[1]',
        'ENVIAR_CADASTRO_USUARIO' : '/html/body/div/div/div[2]/form/div[2]/button',
        'CONFIRMAR_CODIGO' : '/html/body/div/div/div[2]/form/button',
        'MINHA_CONTA' : '//*[@id="conta-cabelcalho"]',
        'CANCELAR_CONTA' : '/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div/a',
        'CONFIRMAR_CANCELAR_CONTA' : '/html/body/div/div[1]/form/button'
    }

    BTN_EMAIL = {
        'AVANSAR' : '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span',
        'LOGAR' : '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span',
        'VBOOK' : '/html/body/div[7]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]',
        'PESQUISA' : '/html/body/div[7]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div[2]/form/button[4]',
        'EMAIL' : '//*[@id=":5a"]',
        'LIXEIRA' : '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/div'
    }

    ############################################################ COMCLUIDO ############################################################
    CADASTRO_USUARIO = {
        'APELIDO' : ['//*[@id="nome"]', 'APELIDO'],
        'NOME_COMPLETO' : ['//*[@id="nomeSobrenome"]', 'NOME_COMPLETO'],
        'EMAIL' : ['//*[@id="email"]', 'EMAIL'],
        'CELULAR' : ['//*[@id="telefone"]', 'CELULAR'],
        'SENHA' : ['//*[@id="senha"]', 'SENHA'],
        'CONFIRMAR_SENHA' : ['//*[@id="confSenha"]', 'SENHA']
    }


    INPUT = {
        'ENTRAR_USUARIO' : '//*[@id="exampleInputEmail1"]',
        'ENTRAR_SENHA' : '//*[@id="exampleInputPassword1"]',
        'CRIAR_TITULO' : '//*[@id="titulo"]',
        'CADASTRO_CODIGO' : ['//*[@id="c1"]', '//*[@id="c2"]', '//*[@id="c3"]', '//*[@id="c4"]', '//*[@id="c5"]', '//*[@id="c6"]'],
        'CANCELAR_CONTA' : '/html/body/div/div[1]/form/input'
    }


    INPUT_EMAIL = {
        'USUARIO' : '//*[@id="identifierId"]',
        'SENHA' : '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input',
        'PESQUISA' : '/html/body/div[7]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/input[1]'
    }

    ELEMENT_EMAIL = {
        'CODIGO' : '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]'
    }