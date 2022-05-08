import { Entity, JoinColumn, ManyToOne, OneToMany, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsInt } from 'class-validator';
import { DetailedLecture } from './detailed_lec.entity.js';
import { University } from './university.entity.js';

/**
 * @description 파이썬 기반 스크래핑을 통해 얻은 코드를 작성된 테트로미노 더미.
 */
@Entity()
export class TetroPool {
    /**
     * 테트로미노 풀의 id
     */
    @PrimaryGeneratedColumn()
    @IsInt()
    id!: number;

    @ManyToOne(() => University, univ => univ.tetros)
    univ! : Relation<University>;


    @OneToMany(() => DetailedLecture, (dl) => dl.tetroPool, {cascade: ['remove']})
    lectures? : Relation<DetailedLecture>[];
}
