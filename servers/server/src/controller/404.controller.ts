import { RequestHandler } from "express";

/**
 * @controller NotFound
 * 제공된 경로가 존재하지 않는 경우 사용되는 컨트롤러 
 */
export const NotFound : RequestHandler = (req, res, next) => {
    res.status(404).send("존재하지 않는 페이지입니다.");
}