export class Pokemon {
    constructor(init:Partial<Pokemon>) {
        Object.assign(this, init);
    }
    name!: string;
    imgUrl!: string;
    hp!: number;
    attack!: number;
    defense!: number;
    spAtk!: number;
    spDef!: number;
    speed!: number;
}