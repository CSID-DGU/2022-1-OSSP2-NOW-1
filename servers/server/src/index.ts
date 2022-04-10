import "reflect-metadata"; //typeorm을 사용하기 위한 코드
import e from 'express';
import { NotFound } from "./controller/404.controller.js";
import userRouter from "./router/user.router.js";
import { initDB } from "./db/db.index.js";

const server = e();


/* 서버에서 사용되는 미들웨어들 */
server.use(e.urlencoded({ extended: true }));
server.use(e.static("public", { extensions: ['js'] }));

/* 라우터 */

server.use('/user', userRouter);
server.use('*', NotFound);

try {
    await initDB(); // 데이터베이스 연결 상태 확인
    server.listen(3000); // 포트 넘버 3000
} catch (e) {
    console.log(e);
}