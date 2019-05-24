export class Pokemon {
    constructor(init: Partial<Pokemon>) {
        Object.assign(this, init);
    }
    no!: number;
    name!: string;
    stats!: Status;
    evolutions!: Array<string>;
    abilities!: Array<string>;
    types!: Array<string>;

    getImgUri():string{
        const no = ("000" + this.no).slice(-3);
        return `/assets/pokemon/${no}.jpg`;
    }
}

class Status {
    hp!: number;
    attack!: number;
    defence!: number;
    spAttack!: number;
    spDefence!: number;
    speed!: number;
}