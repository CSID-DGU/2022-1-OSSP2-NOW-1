import express from 'express';
import {getUsers, setUser, showUserPage} from '../controller/user.controller.js';


const userRouter = express.Router();

userRouter.get('/', (req,res,next) =>{
    res.send("Hello!!!");
});
userRouter.get('/get-users', getUsers);
userRouter.get('/set-user', showUserPage);
userRouter.post('/set-user', setUser);

export default userRouter;