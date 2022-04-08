import {DataSource} from 'typeorm';

const db = new DataSource({
    type: 'mysql',
    host: 'localhost',
    port: 3306,
    database: 'test',
    password: 'password',
    username: 'root',
    
})