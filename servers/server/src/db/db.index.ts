import { DataSource } from 'typeorm';
import Key from '../util/key.js';
import { DetailedLecture } from './entity/detailed_lec.entity.js';
import { LecTime } from './entity/lec_time.entity.js';
import { TetroPool } from './entity/tetro_pool.entity.js';
import { University } from './entity/university.entity.js';
import { User } from './entity/user.entity.js';
import { UserScore } from './entity/user_score.entity.js';

let db: DataSource;

let entities = [User, University, TetroPool, DetailedLecture, LecTime, UserScore]

db = new DataSource({
    type: 'mysql',
    host:  Key.DB_HOST,
    username: Key.DB_USER,
    database: Key.DB_DATABASE,
    password: Key.DB_PASSWORD,
    timezone: '+09:00',
    entities: entities,
    synchronize: true,
    charset:'utf8mb4'
});

export const initDB = async () => {
    await db.initialize();
}

export default db;