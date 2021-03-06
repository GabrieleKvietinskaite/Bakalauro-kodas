import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { IGame } from '../models/IGame.interface';
import { IGraphs } from '../models/IGraphs.interface';

@Injectable({
  providedIn: 'root'
})
@Injectable({ providedIn: 'root' })
export class GameService {
  
  private REST_API_SERVICE = "http://localhost:8000/api";
  private httpOptions: any;

  constructor(private httpClient: HttpClient) { 
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

    createGame(playerId: number, scenarioId: number) {
        let url = `/game/player/${playerId}/scenario/${scenarioId}/create`;
        let form = {"player_id": playerId, "scenario_id": scenarioId}

        return this.httpClient.post(this.REST_API_SERVICE + url, form);
    }

    updateGame(gameId: number, question: string, points: string, maximumPoints: string, competence: string){
        let url = `/game/${gameId}/update`;
        let form = {"question": question, "received_points": points, "maximum_points": maximumPoints, "competences": competence};

        return this.httpClient.put(this.REST_API_SERVICE + url, form, this.httpOptions);
    }

    getGame(gameId: number){
        let url = `/game/${gameId}`;

        return this.httpClient.get<IGame>(this.REST_API_SERVICE + url);
    }

    finishGame(gameId: number, question: string){
        let url = `/game/${gameId}/finish`;
        let form = {"question": question};

        return this.httpClient.put(this.REST_API_SERVICE + url, form, this.httpOptions);
    }
    
    getResults(gameId: number){
        var url = `/game/${gameId}`;

        return this.httpClient.get<IGame>(this.REST_API_SERVICE + url);
    }

    getGraphs(gameId: number){
      var url = `/results/game/${gameId}`;

        return this.httpClient.get<IGraphs>(this.REST_API_SERVICE + url);
    }

    getReport(gameId: number){
      var url = `/game/${gameId}/results`;

      return this.httpClient.get(this.REST_API_SERVICE + url, { responseType: 'blob' });
    }
}
