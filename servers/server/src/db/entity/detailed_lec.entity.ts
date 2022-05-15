import { Column, Entity, JoinColumn, ManyToOne, OneToMany, PrimaryColumn, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsString, IsInt } from 'class-validator';
import { TetroPool } from './tetro_pool.entity.js';
import { LecTime } from './lec_time.entity.js';
import { ILecBase } from '../../interface/lecture.interface.js';

/**
 * @description 테트로미노 풀 속에 있는 강의
 */
@Entity()
export class DetailedLecture implements ILecBase {
    /**
     * 테트로미노 풀의 id
     */
    @PrimaryGeneratedColumn()
    @IsInt()
    tetro_id! : number;

    /**
     * 학수강좌번호
     */
    @Column()
    @IsString()
    c_num!: string;

    /**
     * 교과목명
     */
    @Column()
    @IsString()
    name!: string;

    /**
     * 교원명
     */
    @Column()
    @IsString()
    professor!: string;

    /**
     * 강의 시간대
     */
    @OneToMany(() => LecTime, lec => lec.lecture)
    lec_times?: Relation<LecTime>[];

    /**
     * 비고
     */
    @Column()
    @IsString()
    note!: string;

    /**
     * join 관계를 가지는 테트로미노 풀
     */
    @ManyToOne(() => TetroPool, t => t.lectures, {onDelete:'CASCADE', onUpdate:'CASCADE'})
    tetroPool?: Relation<TetroPool>; // 테트로 엔티티와 Many To One 관계를 가진다.

    constructor(c_num: string, name: string, professor: string, note: string) {
        this.c_num = c_num;
        this.name = name;
        this.professor = professor;
        this.note = note;
    }
}

