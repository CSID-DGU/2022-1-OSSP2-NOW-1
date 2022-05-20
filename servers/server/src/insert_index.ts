import { exit } from "process";
import { initDB } from "./db/db.index.js";
import { ITetroInfo } from "./interface/tetro_pool.interface.js";
import { IUnivInfo } from "./interface/university.interface.js";
import { insert_json } from "./util/insert_json.js";

let target = process.env.TETRO_TARGET;
let t_id: number;

if (target) {
    t_id = parseInt(target);
}
else {
    console.error('숫자가 아님');
    exit();
}
const file = `lectures${t_id+1}.json`;

const univ: IUnivInfo = { name: '동국대학교' };

const dir = ['data', file];

const tetro1: ITetroInfo = { name: '컴공01', 'description': '2022년 1학기 학기 정보(01)' };
const tetro2: ITetroInfo = { name: '컴공02', 'description': '2022년 1학기 학기 정보(02)' };
const tetro3: ITetroInfo = { name: '컴공03', 'description': '2021년 2학기 학기 정보(03)' };
const tetro4: ITetroInfo = { name: '컴공04', 'description': '2021년 2학기 학기 정보(04)' };

const tetros = [tetro1, tetro2, tetro3, tetro4];

await initDB();

await insert_json(univ, tetros[t_id], dir);
