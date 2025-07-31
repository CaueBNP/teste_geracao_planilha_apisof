from APIManager import APIManager
from PathUrls import PathUrls

#Coloque seu Token da API no parâmetro do Objeto APIManager
apiManager = APIManager("1c6f8da4-84d2-3bb0-835b-58e450026f7d")

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
