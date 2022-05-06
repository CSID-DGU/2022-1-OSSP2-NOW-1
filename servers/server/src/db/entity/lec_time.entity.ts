import { Column, Entity, JoinColumn, ManyToOne, PrimaryColumn, PrimaryGeneratedColumn } from 'typeorm';
import { Length, IsString, IsBoolean, IsInt, IsDecimal } from 'class-validator';
import { DetailedLecture } from './detailed_lec.entity';

@Entity()
export class LecTime {
    @PrimaryGeneratedColumn()
    @IsInt()
    id!: number;

    @Column({type: 'int'})
    @IsInt()
    dow : number;

    @Column({type:'decimal'})
    @IsDecimal()
    start : number;
    
    @Column({type:'decimal'})
    @IsDecimal()
    end : number;

    @ManyToOne(() => DetailedLecture, dl => dl.lec_times)
    @JoinColumn([
        {referencedColumnName: 'tetro_id'},
        {referencedColumnName: 'c_num'}
    ])
    lecture?: DetailedLecture;

    constructor(dow: number, start: number, end: number) {
        this.dow = dow;
        this.start = start;
        this.end = end;
    }
}