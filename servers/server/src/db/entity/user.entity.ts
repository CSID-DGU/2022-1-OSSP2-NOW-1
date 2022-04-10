import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';
import {Length, IsString, IsBoolean} from 'class-validator';

@Entity()
export class User {
    @PrimaryGeneratedColumn({ type: 'int' })
    id?: number;
    // 여기서는 지정하지 않지만, 알아서 생성된다.

    @Column()
    @IsString()
    @Length(1, 20)
    firstName: string;

    @Column()
    @IsString()
    @Length(1, 20)
    lastName: string;

    @Column()
    @IsBoolean()
    isActive: boolean;

    constructor(firstName: string, lastName: string, isActive: boolean) 
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.isActive = isActive;
    }
}