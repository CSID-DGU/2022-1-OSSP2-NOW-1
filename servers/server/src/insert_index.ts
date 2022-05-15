import db, { initDB } from "./db/db.index.js";
import { ITetroInfo } from "./interface/tetro_pool.interface.js";
import { IUnivInfo } from "./interface/university.interface.js";
import { insert_json } from "./util/insert_json.js";

const dir = ['data', 'lectures.json'];
const univ : IUnivInfo = {name: '동국대학교'};
const tetro : ITetroInfo = {name:'컴퓨터공학과 수업', 'description':'2021년 2학기 및 2022년 1학기 컴퓨터공학과 수업 모음입니다.'};

await initDB();
await insert_json(univ, tetro, dir);