type Nullable<T> = T | null;

export interface IAnswer {
    id: number;
    scenario_id: number;
    questionI_id: number;
    number: number;
    answer: string;
    next_question_id: number;
    times_chosen: number;
    p_answer: number;
    p_question_answer: number;
    is_competence_achieved: Nullable<boolean>;
}