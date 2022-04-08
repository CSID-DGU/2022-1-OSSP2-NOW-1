import "reflect-metadata"; //typeorm을 사용하기 위한 코드
import e from 'express';

const server = e();

/* 서버에서 사용되는 미들웨어들 */
server.use(e.urlencoded({ extended: true }));
server.use(e.static("public", { extensions: ['js'] }));

/* 라우터 */


server.use('*',)

server.listen(3000); //포트 넘버 3000