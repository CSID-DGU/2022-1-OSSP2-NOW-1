import { Column, Entity, JoinColumn, ManyToOne, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsString, IsInt, Min } from 'class-validator';
import { TetroPool } from './tetro_pool.entity.js';

@Entity()
export class UserScore {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column({nullable: false})
    @IsString()
    name : string;

    @Column({nullable: false})
    @IsInt({message:'점수가 정수형이 아닙니다.'})
    @Min(0)
    score : number;

    @Column({ name: 'tetro_id' })   // <-
    tetro_id?: number;                // <-

    @ManyToOne(() => TetroPool)
    @JoinColumn({ name: 'tetro_id' })
    tetro_pool?: Relation<TetroPool>;

    constructor(name: string, score: number) {
        this.name = name;
        this.score = score;
    }
}