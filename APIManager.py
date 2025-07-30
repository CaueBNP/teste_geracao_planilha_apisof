import pandas as pd
import requests
from datetime import datetime
from PathUrls import PathUrls

class APIManager:
    
    _baseUrl = "https://gateway.apilib.prefeitura.sp.gov.br/sf/sof/v4/"
    
    _headers = {"Authorization": None}
    
    _standardParams = None
    
    data = pd.DataFrame()
    
    def __init__(self, token, ano = datetime.now().year, mes = datetime.now().month):
        self._headers["Authorization"] =  f"Bearer {token}"
        
                
        self._standardParams = {
          "ano": ano,
          "mes": mes,
          "codOrgao": 25,
          "codUnidade": 10,
          "codFuncao": 13,
          }


    def RequestEmpenhos(self, filtered_columns):
        pathUrl = PathUrls.empenhos.name
        print(self._headers)
        url = self._baseUrl + pathUrl
        print(url)
        
        completeParams = self._standardParams.copy()
        completeParams["anoEmpenho"] = completeParams.pop("ano")
        completeParams["mesEmpenho"] = completeParams.pop("mes")
        
        response = requests.get(url, headers = self._headers, params = completeParams)
        
        responseData = pd.DataFrame(response.json()["lstEmpenhos"])
        
        responseData["cod_cta_desp"] = responseData["codCategoria"] + responseData["codGrupo"] + responseData["codModalidade"] + responseData["codElemento"] + "00"
        responseData["Dotacao"] = responseData.assign(codProjetoAtividade_fmt = responseData["codProjetoAtividade"].astype(str).apply(lambda x: x[0] + "." + x[1:] if len(x) > 1 else x))[[
            "codOrgao",
            "codUnidade",
            "codFuncao",
            "codSubFuncao",
            "codPrograma",
            "codProjetoAtividade_fmt",
            "cod_cta_desp",
            "codFonteRecurso"
        ]].astype(str).agg(".".join, axis=1)
                        
        self.data = responseData[filtered_columns]
        
        return
    
    
    def RequestDespesas(self, filtered_columns):
        pathUrl = PathUrls.despesas.name
        url = self._baseUrl + pathUrl
        print(url)
        
        if len(self.data) > 0:
            print("passou")
            for i in range(0, len(self.data)):
                
                completeParams = self._standardParams.copy()
                completeParams["anoDotacao"] = completeParams.pop("ano")
                completeParams["mesDotacao"] = completeParams.pop("mes")
                completeParams.update({"codSubFuncao": self.data.loc[i, "codSubFuncao"], 
                                       "codProjetoAtividade": self.data.loc[i, "codProjetoAtividade"], 
                                       "codPrograma": self.data.loc[i, "codPrograma"],
                                       "codCategoria": self.data.loc[i, "codCategoria"],
                                       "codGrupo": self.data.loc[i, "codGrupo"],
                                       "codModalidade": self.data.loc[i, "codModalidade"],
                                       "codElemento": self.data.loc[i, "codElemento"],
                                       "codFonteRecurso": self.data.loc[i, "codFonteRecurso"]})
                
                response = requests.get(url, headers = self._headers, params = completeParams)
                
                responseData = pd.DataFrame(response.json()["lstDespesas"])
                responseData = responseData[filtered_columns]
                print(responseData)
                self.data.loc[i, responseData.keys()] = responseData.values
                
<<<<<<< HEAD
            self.data.drop(["codCategoria", "txDescricaoCategoriaEconomica", "codGrupo", "txDescricaoGrupoDespesa", "codModalidade", "txDescricaoModalidade", "codElemento", "txDescricaoElemento", "codFonteRecurso", "txDescricaoFonteRecurso"], axis = 1, inplace = True)
                
=======
            self.data.drop(["codCategoria", "txDescricaoCategoriaEconomica", "codGrupo", "txDescricaoGrupoDespesa", "codModalidade", "txDescricaoModalidade", "codElemento", "txDescricaoElemento", "codFonteRecurso", "txDescricaoFonteRecurso"], axis = 1)
>>>>>>> d27afc89a53b289140f8940f69ae4b4e43eeb2c4
        else:
            print("não passou")
            return
