import express from 'express';
import { getSpecificTetroPool } from '../controller/data.controller.js';

const tetroRouter = express.Router();

tetroRouter.get('/', (req,res,next) =>{
    res.send('tetro router');
});

tetroRouter.get('/get', (req,res,next) =>{
    res.send('tetro!!!');
})
tetroRouter.get('/get/:tid', getSpecificTetroPool);

export default tetroRouter;