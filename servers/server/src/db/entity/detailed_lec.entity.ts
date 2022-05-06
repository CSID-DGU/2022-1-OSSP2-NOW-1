import { Column, Entity, JoinColumn, ManyToOne, OneToMany, PrimaryColumn, PrimaryGeneratedColumn } from 'typeorm';
import { IsString, IsInt } from 'class-validator';
import { TetroPool } from './tetro_pool.entity';
import { LecTime } from './lec_time.entity';

/**
 * @description 테트로미노 풀 속에 있는 강의
 */
@Entity()
export class DetailedLecture {
    /**
     * 테트로미노 풀의 id
     */
    @PrimaryColumn()
    @IsInt()
    tetro_id: number;

    /**
     * 학수강좌번호
     */
    @PrimaryColumn()
    @IsString()
    c_num: string;

    /**
     * 교과목명
     */
    @Column()
    @IsString()
    name: string;

    /**
     * 교원명
     */
    @Column()
    @IsString()
    professor: string;

    /**
     * 강의 시간대
     */
    @OneToMany(() => LecTime, lec => lec.lecture)
    lec_times?: LecTime[];

    /**
     * 비고
     */
    @Column()
    @IsString()
    note: string;

    /**
     * join 관계를 가지는 테트로미노 풀
     */
    @ManyToOne(() => TetroPool, t => t.lectures)
    @JoinColumn({ referencedColumnName: 'id' })
    tetro?: TetroPool; // 테트로 엔티티와 Many To One 관계를 가진다.

    constructor(tetro_id: number, c_num: string, name: string, professor: string, note: string) {
        this.tetro_id = tetro_id;
        this.c_num = c_num;
        this.name = name;
        this.professor = professor;
        this.note = note;
    }
}

