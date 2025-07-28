from APIManager import APIManager
from PathUrls import PathUrls

apiManager = APIManager("4548610b-e673-32db-ba6f-6d68f78772f8")

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
             "codFonteRecurso", "txDescricaoFonteRecurso"
             ]
apiManager.RequestEmpenhos(filtered_columns)


filtered_columns = ["valOrcadoInicial", "valSuplementado", "valCongelado", "valDisponivel", "valReservadoLiquido"]
apiManager.RequestDespesas(filtered_columns)


apiManager.data.to_excel("dados_teste.xlsx", index = False)