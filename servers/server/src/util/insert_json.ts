// import "reflect-metadata"; //typeorm을 사용하기 위한 코드
// import { initDB } from "./db/db.index.js";
import { readFile } from 'fs/promises';
import { resolve } from "path";
import db from '../db/db.index.js';
import { DetailedLecture } from '../db/entity/detailed_lec.entity.js';
import { LecTime } from '../db/entity/lec_time.entity.js';
import { TetroPool } from '../db/entity/tetro_pool.entity.js';
import { University } from '../db/entity/university.entity.js';
import { ILec } from '../interface/lecture.interface.js';
import { ITetroInfo } from '../interface/tetro_pool.interface.js';
import { IUnivInfo } from '../interface/university.interface.js';

// university
// tetro_pool
// detailed_lec
// lec_time



/**
 * 테트로미노 풀 정보
 */



export const insert_json = async (univInfo: IUnivInfo, tetroInfo: ITetroInfo, json_path: string[]) => {
    let data_path = resolve(...json_path);
    // let data_path = resolve('data', 'lectures.json');


    let buffer = await readFile(data_path, { encoding: 'utf8' });
    let str = buffer.toString();
    let json = JSON.parse(str);
    console.log(json);

    let univ = new University(univInfo.name);

    let values: ILec[] = (Object.values(json) as ILec[][]).reduce((prev, cur) => prev.concat(cur), []); // 배열 붙이기

    console.log(values)

    let lecs: DetailedLecture[] = [];
    const tetro_pool = new TetroPool(tetroInfo.name, tetroInfo.description);
    // const tetro_pool = new TetroPool('컴퓨터공학과 모음', '2021년 2학기 및 2022년 1학기 컴퓨터공학과 수업 모음입니다.');

    const univRepo = await db.getRepository(University);
    const tetroRepo = await db.getRepository(TetroPool);
    const lectureRepo = await db.getRepository(DetailedLecture);
    const lectRepo = await db.getRepository(LecTime);

    for (let v of values) {
        const lecture = new DetailedLecture(v.c_num, v.name, v.professor, v.note);
        const lec_times: LecTime[] = [];

        for (let l_t of v.loc) {
            let lec_time = new LecTime(l_t[0], l_t[1], l_t[2])
            // lec_time.lecture = lecture;
            lec_times.push(lec_time);
        }

        await lectRepo.save(lec_times); // 데이터베이스에 삽입.
        lecture.lec_times = lec_times; // 관계 연결
        // lecture.tetroPool = tetro_pool; 
        lecs.push(lecture);
    } // 데이터 삽입
    await lectureRepo.save(lecs); // 데이터베이스 내에 강의들 삽입

    tetro_pool.lectures = lecs; // 테트로미노 풀 데이터베이스에 삽입

    // 이전에 저장된 놈이 있는지 검사.
    const before_univ = await univRepo.findOne({ where: { name: univ.name } });
    console.log(before_univ?.id, before_univ?.name);
    //이미 저장된 놈이 있다면
    if (before_univ) {
        // before_univ은 join 조건을 따로 안줬기 때문에 tetro_pools가 항상 없음!
        tetro_pool.univ = before_univ;
        await tetroRepo.save(tetro_pool); // 테트로 풀 삽입함!
    }
    else {
        await tetroRepo.save(tetro_pool);
        univ.tetro_pools = [tetro_pool];
        await univRepo.save(univ);
    }

    // tetro_pool.univ = univ;
    console.log("success!");

}