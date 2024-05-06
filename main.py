from testAutomatizado import TesteAutomatizado
from model.usuario import Usuario
from model.livro import Livro


#user1 = TesteAutomatizado()
#user1.longin(Usuario.USUARIO['P'])
#user1.cadastroLivro(Livro.LIVRO['L0'])

cadastro_1 = TesteAutomatizado()
cadastro_1.cadastroUsuario(Usuario.USUARIO['P'])

#deletar_1 = TesteAutomatizado()
#deletar_1.deletarUsuario(Usuario.USUARIO['O']) 