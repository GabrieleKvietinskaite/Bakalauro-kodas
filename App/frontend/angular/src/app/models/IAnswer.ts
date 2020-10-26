export interface IAnswer {
    id: number;
    scenario_id: number;
    questionI_id: number;
    number: number;
    answer: string;
    next_question_id: number;
    weight: number;
    /*times_chosen*/ quantity: number;
}