
enum Status  {
    Pendente = "pendente",
    Vencida = "Vencida"
}

export type TTarefa = {
    titulo: string
    descricao: string
    dataVencimento: Date
    status?: Status
}

