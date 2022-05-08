import { Column, Entity, OneToMany, PrimaryColumn, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsString, IsInt } from 'class-validator';
import { TetroPool } from './tetro_pool.entity.js';

/**
 * @description
 */
@Entity()
export class University {
    /**
     * 학교 id. 자동으로 생성.
     */
    @PrimaryGeneratedColumn()
    @IsInt()
    id!: number;

    /**
     * 학교의 이름
     */
    @Column()
    @IsString()
    name: string;

    /**
     * 학교의 id를 기반으로 테트로미노가 생성될 수 있다.
     */
    @OneToMany(() => TetroPool, t => t.univ)
    tetros? : Relation<TetroPool>[];

    constructor(name: string)
    {
        this.name = name;
    }

}

