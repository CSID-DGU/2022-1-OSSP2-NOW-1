import {RequestHandler } from "express";
import db from "../db/db.index.js";

/**
 * 현재 존재하는 대학들을 보여준다
 * 
 * @route /api/tetro/univ 
 */
 const showAvailableUniv : RequestHandler = async (req, res, next) => {

};


/**
 * 현재 사용 가능한 테트로미노 풀을 보여준다
 * 
 * @route /api/tetro/대학이름/tetro-pool 
 */
const showAvailableTetroPool : RequestHandler = async (req, res, next) => {

};
