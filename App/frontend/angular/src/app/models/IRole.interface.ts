import { ICompetence } from './ICompetence.interface';

export interface IRole {
    [x: string]: any;
    id: number;
    role: string;
    description: string;
    competences: ICompetence[];
  }