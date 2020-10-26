type Nullable<T> = T | null;

export interface IQuestion {
    id: number;
    scenario_id: number;
    question: string;
    win: Nullable<boolean>;
    quantity: number;
    average: number;
}