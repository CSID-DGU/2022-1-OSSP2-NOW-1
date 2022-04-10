import { DataSource } from 'typeorm';
import Key from '../key.js';
import { User } from './entity/user.entity.js';

let db: DataSource;

db = new DataSource({
    type: 'mysql',
    host:  Key.DB_HOST,
    username: Key.DB_USER,
    database: Key.DB_DATABASE,
    password: Key.DB_PASSWORD,
    timezone: '+09:00',
    entities: [User],
    synchronize: true
});

export const initDB = async () => {
    await db.initialize();
}

export default db;