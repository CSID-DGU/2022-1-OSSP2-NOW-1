import { RequestHandler } from "express";
import db from "../db/db.index.js";
import { University } from "../db/entity/university.entity.js";


/**
 * 현재 존재하는 대학들을 보여준다
 * 
 * @route /api/info/univs
 */
export const showAvailableUniv: RequestHandler = async (req, res, next) => {
    const univRepo = db.getRepository(University);

    const univs = await univRepo.find({});

    const univs_json = univs.map((v) => { return { id: v.id, name: v.name }; });

    return res.json(univs_json);
};


/**
 * 현재 사용 가능한 테트로미노 풀을 보여준다
 * 
 * @route /api/info/:uid/tetro-pools
 */
export const showAvailableTetroPool: RequestHandler = async (req, res, next) => {
    const univ_id = parseInt(req.params['univ-name']);
    if (isNaN(univ_id)) {
        return res.status(400).json({ message: '잘봇된 대학 id' });
    }

    const univRepo = db.getRepository(University);
    const univs = await univRepo.findOne({ where: { id: univ_id }, relations: { tetro_pools: true } });

    if (univs) { // 대학 있다면
        const tetro_pools = univs.tetro_pools!;
        const tetro_jsons = tetro_pools.map(tetro => {
            return {
                id: tetro.id,
                name: tetro.name,
                description: tetro.description
            };
        });

        return res.json(tetro_jsons); // json으로 바꿔서 대학 목록 반환.
    }
    else { // 존재하지 않는 대학이라면
        return res.status(404).json({ message: '존재하지 않는 대학' });
    }
};
