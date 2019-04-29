export class Pokemon {
    constructor(init:Partial<Pokemon>) {
        Object.assign(this, init);
    }
    no!: number;
    name!: string;
    hp!: number;
    attack!: number;
    defense!: number;
    spAtk!: number;
    spDef!: number;
    speed!: number;
}