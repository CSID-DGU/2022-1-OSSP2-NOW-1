import express from 'express';
import { showAvailableTetroPool, showAvailableUniv } from '../controller/info.controller.js';

const infoRouter = express.Router();

infoRouter.get('/info/univs', showAvailableUniv);
infoRouter.get('/info/:uid/tetro-pools', showAvailableTetroPool);

export default infoRouter;