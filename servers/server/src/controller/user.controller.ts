/**
 * @document User Controller
 * 현재 프로젝트 및 mysql 데이터베이스가 typeorm을 통해 정상적으로 연결되는지 여부를 검사하기 위한 컨트롤러
 * @with user.entity.ts
 * 유저의 엔티티를 정의한 파일
 */
import { RequestHandler } from "express";
import { validate } from 'class-validator';
import db from "../db/db.index.js";
import { User } from "../db/entity/user.entity.js";
import { resolve } from "path";

/**
 * @controller getUsers
 * 현재 서버상에 저장된 유저들의 정보를 가져오는 컨트롤러 
 */
// export const getUsers: RequestHandler = async (req, res, next) => {
//     const userRepository = db.getRepository(User);
//     const users = await userRepository.find();
//     res.status(200).send({
//         user: users
//     });
// };

/**
 * @controller showUserPage
 * http POST 연산을 수행하기 위해 
 */
export const showUserPage: RequestHandler = async (req, res, next) => {
    res.sendFile(resolve('public/view/index.html'));
};

/**
 * @controller setUser 
 * 유저 설정 
 */
export const setUser: RequestHandler = async (req, res, next) => {
    const userRepo = db.getRepository(User);

    const test = await userRepo.findOneBy({id:1});
    if(test)
    {
        return res.status(200).send('이미 유저가 존재');
    }
    const user = new User("John", "Doe", true);

    const err = await validate(user);
    if (err.length > 0) {
        return res.status(400).send(err);
    }
    else {
        // await userRepository.save(user);
        res.status(200).send("유저가 생성됨!");
    }
};