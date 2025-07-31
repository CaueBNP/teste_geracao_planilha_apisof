from APIManager import APIManager
from PathUrls import PathUrls

#Coloque seu Token da API no parâmetro do Objeto APIManager
apiManager = APIManager("Seu token da API")

filtered_columns = [
             "codOrgao", "txDescricaoOrgao",
             "codUnidade", "txDescricaoUnidade",
             "codFuncao", "txDescricaoFuncao",
             "codSubFuncao", "txDescricaoSubFuncao",
             "codProjetoAtividade", "txDescricaoProjetoAtividade",
             "codPrograma", "txDescricaoPrograma",
             "codCategoria", "txDescricaoCategoriaEconomica",
             "codGrupo", "txDescricaoGrupoDespesa",
             "codModalidade", "txDescricaoModalidade",
             "codElemento", "txDescricaoElemento",
             "codFonteRecurso", "txDescricaoFonteRecurso",
             "Dotacao", "cod_cta_desp"
             ]
apiManager.RequestEmpenhos(filtered_columns)


filtered_columns = ["valOrcadoInicial", "valSuplementado", "valCongelado", "valDisponivel", "valReservadoLiquido"]
apiManager.RequestDespesas(filtered_columns)


apiManager.data.to_excel("dados_teste.xlsx", index = False)
