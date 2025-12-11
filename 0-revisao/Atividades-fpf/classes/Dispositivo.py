


class Dispositivo:
    total_ativos = 0
    
    def __init__(self, id_serie: str, localizacao: str) -> None:
        self.id_serie = id_serie
        self.localizacao = localizacao
        self.rede_padrao = "Rede Doméstica V.2"
        self.status = "Desconectado"
        Dispositivo.total_ativos += 1
    
    def conexao(self):
        status = self.status="Conectado"
        ssid = self.rede_padrao
        dispositivos  = Dispositivo.total_ativos
        descricao_conexao = f"Status: {status} | Rede: {ssid}  | Nº dispositivos: {dispositivos} "
        return descricao_conexao



        