import express from 'express';
import { getSpecificTetroPool } from '../controller/data.controller.js';
import { showAvailableTetroPool, showAvailableUniv } from '../controller/info.controller.js';

const tetroRouter = express.Router();

tetroRouter.get('/', (req,res,next) =>{
    res.send('tetro router');
});

tetroRouter.get('/get', (req,res,next) =>{
    res.send('tetro!!!');
})
tetroRouter.get('/get/:tid', getSpecificTetroPool);

tetroRouter.get('/info/univs', showAvailableUniv);
tetroRouter.get('/info/:uid/tetro-pools', showAvailableTetroPool);

export default tetroRouter;