export class Pokemon {
    constructor(init: Partial<Pokemon>) {
        Object.assign(this, init);
    }
    no!: number;
    name!: string;
    stats!: Status;
    evolutions!: Array<string>;
}

class Status {
    hp!: number;
    attack!: number;
    defence!: number;
    spAttack!: number;
    spDefence!: number;
    speed!: number;
}