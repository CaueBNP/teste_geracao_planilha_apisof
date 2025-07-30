class ColumnBuilder:
    
    def __init__(self):
        return
    
    def buildCodCtaDesp(self, data):
        value = data["codCategoria"] + data["codGrupo"] + data["codModalidade"] + data["codElemento"]
        data["Dotacao"] = value
    
    def buildDotacao(self, data):
        value = data["codOrgao"] + data["codUnidade"] + data["codFuncao"] + data["codOrgao"] + data["codSubFuncao"] + data["codPrograma"] + data[""]
        data["Dotacao"] = data[""]