import { Column, Entity, JoinColumn, ManyToOne, OneToMany, PrimaryColumn, PrimaryGeneratedColumn } from 'typeorm';
import { Length, IsString, IsBoolean, IsInt } from 'class-validator';
import { DetailedLecture } from './detailed_lec.entity';
import { University } from './university.entity';

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
    // @JoinColumn([
    //     {name: "tetros_id", referencedColumnName:"id"}
    // ])
    univ! : University;


    @OneToMany(() => DetailedLecture, (dl) => dl.tetro, {cascade: ['remove']})
    @JoinColumn({referencedColumnName: 'tetro_id'})
    lectures? : DetailedLecture[];
}
