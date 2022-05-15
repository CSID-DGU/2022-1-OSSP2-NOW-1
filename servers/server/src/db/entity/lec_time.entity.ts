import { Column, Entity, JoinColumn, ManyToOne, PrimaryGeneratedColumn, Relation } from 'typeorm';
import { IsInt, IsDecimal } from 'class-validator';
import { DetailedLecture } from './detailed_lec.entity.js';

@Entity()
export class LecTime {
    @PrimaryGeneratedColumn()
    @IsInt()
    id!: number;

    @Column({type: 'int'})
    @IsInt()
    dow! : number;

    @Column({type:'decimal', precision: 5, scale: 2, default: 0})
    @IsDecimal()
    start! : number;
    
    @Column({type:'decimal', precision: 5, scale: 2, default: 0})
    @IsDecimal()
    end! : number;

    @ManyToOne(() => DetailedLecture, dl => dl.lec_times, {onDelete:'CASCADE', onUpdate:'CASCADE'})
    lecture?: Relation<DetailedLecture>;

    constructor(dow: number, start: number, end: number) {
        this.dow = dow;
        this.start = start;
        this.end = end;
    }
}