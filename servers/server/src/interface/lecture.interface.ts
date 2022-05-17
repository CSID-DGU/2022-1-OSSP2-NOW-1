export interface ILecBase {
    c_num: string,
    note: string,
    name: string,
    professor: string,
}
export interface ILec extends ILecBase {
    loc: number[][]
}

