import express from 'express';
import { getSpecificTetroPool, getUsersScore, setUserScore } from '../controller/data.controller.js';

const tetroRouter = express.Router();

tetroRouter.get('/', (req,res,next) =>{
    res.send('tetro router');
});

tetroRouter.get('/get', (req,res,next) =>{
    res.send('tetro!!!');
})
tetroRouter.get('/get-tetro/:tid', getSpecificTetroPool);
tetroRouter.get('/get-scores/:tid', getUsersScore);
tetroRouter.post('/set-score/:tid', setUserScore);

export default tetroRouter;