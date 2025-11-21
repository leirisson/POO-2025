

export class Pessoa {
    private  name: string
    constructor(name: string) {
        this.name = name
    }

    getName() {
        return this.name
    }

    setNome(name:string){
        this.name = name
    }
}