import express from 'express';
import { showAvailableTetroPool, showAvailableUniv } from '../controller/info.controller.js';

const infoRouter = express.Router();

infoRouter.get('/univs', showAvailableUniv);
infoRouter.get('/:uid/tetro-pools', showAvailableTetroPool);

export default infoRouter;