from APIManager import APIManager
from PathUrls import PathUrls

apiManager = APIManager()

apiManager.RequestEmpenhos()
apiManager.RequestDespesas()


apiManager.data.to_excel("dados_teste1.xlsx", index = False)