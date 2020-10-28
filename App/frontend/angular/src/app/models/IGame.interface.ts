export interface IGame {
    id: number;
    player_id: number;
    scenario_id: number;
    questions: string;
    received_points: string;
    maximum_points: string;
    hypothesis: string;
}