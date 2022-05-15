import {RequestHandler } from "express";
import db from "../db/db.index.js";
import { TetroPool } from "../db/entity/tetro_pool.entity.js";
import {ILec} from '../interface/lecture.interface.js';

/**
 *  요청된 특정 테트로미노 풀을 반환.
 */
export const getSpecificTetroPool : RequestHandler = async (req, res, next) => {
    let params = req.params;

    const id = params['tid'] ? parseInt(params['tid']) : null;
    if(id && !isNaN(id)) // id가 존재하면서 숫자일 때
    {
        const tetroRepo = db.getRepository(TetroPool);
        try {

            const tetro_pool = await tetroRepo.find({where:{id:id}, relations:{
                lectures:{
                    lec_times: true
                }
            }});
            console.log(tetro_pool);
            if (tetro_pool.length > 0) { // 요청한 테트로미노 풀이 존재할 때
                const lec_list : ILec[] = []; // 강의 풀

                const lectures = tetro_pool[0].lectures;
                if (lectures)
                {
                    for(const ldata of lectures)
                    {
                        const lec_times = ldata.lec_times; // loc에 대응
                        const loc = []

                        if (lec_times) // 각 시간대 정보 가져오기
                        {
                            for (const lec_time of lec_times)
                            {
                                let arr = [lec_time.dow, lec_time.start, lec_time.end];
                                loc.push(arr);
                            }
                        }

                        // 강의 생성
                        const lecture : ILec =
                        {
                            c_num: ldata.c_num,
                            note: ldata.note,
                            name: ldata.name,
                            professor: ldata.professor,
                            loc: loc
                        };
                        // 강의 풀에 푸시
                        lec_list.push(lecture);
                    }
                }
                console.log(`데이터 전달. id = ${id}`);
                return res.status(200).json(lec_list);
            }
            else {
                return res.status(404).json({message : '존재하지 않는 대학.'});
            }

        }
        catch {
        }
    }
    else {
        return res.status(404)
        .json({message: '부적절한 id를 지정'});
    }
    
}