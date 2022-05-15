import { Column, Entity, JoinColumn, ManyToOne, OneToMany, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsInt } from 'class-validator';
import { DetailedLecture } from './detailed_lec.entity.js';
import { University } from './university.entity.js';
import { ITetroInfo } from '../../interface/tetro_pool.interface.js';

/**
 * @description 파이썬 기반 스크래핑을 통해 얻은 코드를 작성된 테트로미노 더미.
 */
@Entity()
export class TetroPool implements ITetroInfo {
    /**
     * 테트로미노 풀의 id
     */
    @PrimaryGeneratedColumn()
    @IsInt()
    id!: number;

    /**
     * 테트로미노 풀의 이름
     */
    @Column()
    name: string;

    /**
     * 테트로미노 풀에 대한 설명
     */
    @Column()
    description : string;

    @ManyToOne(() => University, univ => univ.tetro_pools, {onDelete:'CASCADE', onUpdate:'CASCADE'})
    univ! : Relation<University>;


    @OneToMany(() => DetailedLecture, (dl) => dl.tetroPool)
    lectures? : Relation<DetailedLecture>[];

    constructor(name: string, description: string)
    {
        this.name = name;
        this.description = description;
    }
}
