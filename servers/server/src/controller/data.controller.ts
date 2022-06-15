import { validate } from "class-validator";
import { RequestHandler } from "express";
import db from "../db/db.index.js";
import { TetroPool } from "../db/entity/tetro_pool.entity.js";
import { UserScore } from "../db/entity/user_score.entity.js";
import { ILec } from '../interface/lecture.interface.js';

/**
 *  요청된 특정 테트로미노 풀을 반환.
 * @route /api/tetro/get-tetro/:tid
 */
export const getSpecificTetroPool: RequestHandler = async (req, res, next) => {
    let params = req.params;

    const id = params['tid'] ? parseInt(params['tid']) : null;
    if (id && !isNaN(id)) // id가 존재하면서 숫자일 때
    {
        const tetroRepo = db.getRepository(TetroPool);
        try {
            const tetro_pool = await tetroRepo.findOne({
                where: { id: id }, relations: {
                    lectures: {
                        lec_times: true
                    }
                }
            });
            if (tetro_pool) { // 요청한 테트로미노 풀이 존재할 때
                const lec_list: ILec[] = []; // 강의 풀

                const lectures = tetro_pool.lectures;
                if (lectures) {
                    for (const ldata of lectures) {
                        const lec_times = ldata.lec_times; // loc에 대응
                        const loc = []

                        if (lec_times) // 각 시간대 정보 가져오기
                        {
                            for (const lec_time of lec_times) {
                                let arr = [lec_time.dow, lec_time.start, lec_time.end];
                                loc.push(arr);
                            }
                        }

                        // 강의 생성
                        const lecture: ILec =
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
                return res.status(404).json({ message: '존재하지 않는 테트로미노 풀' });
            }

        }
        catch {
            return res.status(404).json({ message: '알수 없는 오류' });
        }
    }
    else {
        return res.status(404)
            .json({ message: '부적절한 id를 지정' });
    }

};


/**
 * 경쟁 모드에서 특정 테트로미노 풀에 대한 점수 목록을 반환
 * @route /api/tetro/get-scores/:tid
 */
export const getUsersScore : RequestHandler = async (req, res, next) => {
    const tid = parseInt(req.params['tid']);
    if(isNaN(tid)) {
        return res.status(400).json({message: '잘못된 인덱스입니다.'});
    }
    const scores = await db.getRepository(UserScore)
                        .createQueryBuilder()
                        .where('tetro_id = :tid', {tid : tid})
                        .orderBy('score',"DESC")
                        .limit(10)
                        .getMany();
    const score_json = scores.map(s => {
        return {
            name : s.name,
            score : s.score
        };
    })

    return res.json(score_json);
};

/**
 * 경쟁 모드에서 특정 테트로미노 풀에 대한 점수를 기록
 * @route /api/tetro/set-score/:tid
 */
export const setUserScore : RequestHandler = async (req, res, next) => {
    const tid = parseInt(req.params['tid']);
    const tetro = await db.getRepository(TetroPool).findOneBy({id: tid});

    if(!isNaN(tid))
    {
        if(tetro == null)
        {
            return res.status(404).json({message: '존재하지 않는 테트로미노 풀'});
        }
    }
    else {
        return res.status(400).json({message: '잘못된 테트로미노 id'});
    }

    const name = req.body.name;
    const score = parseInt(req.body.score);

    const usRepo = db.getRepository(UserScore);
    const user_score = new UserScore(name, score);
    user_score.tetro_pool = tetro;

    const validation = await validate(user_score);
    if(validation.length > 0)
    {
        const message = validation.map(c => {
            return {
                property: c.property,
                constraints : c.constraints
            }
        })
        return res.status(400).json({message: message});
    }

    await usRepo.save(user_score);

    return res.status(200).json({message: '유저 등록 성공!'});
};