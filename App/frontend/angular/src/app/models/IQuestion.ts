type Nullable<T> = T | null;

export interface IQuestion {
    id: number;
    scenario_id: number;
    question: string;
    win: Nullable<boolean>;
    times_showed: number;
    times_lost: number;
    p_question: number;
}