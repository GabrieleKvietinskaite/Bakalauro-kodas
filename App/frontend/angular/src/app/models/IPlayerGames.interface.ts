import { IScenario } from "./IScenario.interface";

export interface IPlayerGames {
    id: number;
    scenario: IScenario;
    finished_at: string;
  }