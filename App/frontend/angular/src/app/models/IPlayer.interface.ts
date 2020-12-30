import { ILevel } from "./ILevel.interface";
import { IRole } from "./IRole.interface";

export interface IPlayer {
    id: number;
    competences: string;
    role: IRole;
    level: ILevel;
  }