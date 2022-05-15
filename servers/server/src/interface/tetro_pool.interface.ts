import { ILec } from "./lecture.interface";

export interface ITetroInfo {
    name : string;
    description : string;
}

export interface ITetro extends ITetroInfo {
    lectures: ILec[];
}