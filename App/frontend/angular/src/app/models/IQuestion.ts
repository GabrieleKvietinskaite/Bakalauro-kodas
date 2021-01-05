import { ICompetence } from "./ICompetence.interface";

type Nullable<T> = T | null;

export interface IQuestion {
    id: number;
    scenario_id: number;
    question: string;
    competence: ICompetence
    win: Nullable<boolean>;
    times_showed: number;
    times_lost: number;
    p_question: number;
    time: number;
}