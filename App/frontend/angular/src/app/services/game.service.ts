import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { IGame } from '../models/IGame.interface';

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
        let url = `/game/create/player/${playerId}/scenario/${scenarioId}`;
        let form = {"player_id": playerId, "scenario_id": scenarioId}

        return this.httpClient.post(this.REST_API_SERVICE + url, form);
    }

    updateGame(gameId: number, questions: string, points: string, maximumPoints: string){
        let url = `/game/${gameId}`;
        let form = {"questions": questions, "received_points": points, "maximum_points": maximumPoints};

        return this.httpClient.put(this.REST_API_SERVICE + url, form, this.httpOptions);
    }

    getGame(gameId: number){
        let url = `/game/${gameId}`;

        return this.httpClient.get<IGame>(this.REST_API_SERVICE + url);
    }
/*
    finishGame(gameId: number){
        var url = `api/game/${gameId}/finish`;

        return this.http.post(url, null, options)
            .pipe(map(response => response),
                catchError(this.handleError));
    }*/
    /*
    getResults(gameId: number){
        var url = `api/game/${gameId}/results`;

        return this.http.get<IResults>(url, options)
            .pipe(map(response => response),
                catchError(this.handleError));
    }*/
/*
    getStatistics(){
        var url = `api/statistics`;

        return this.http.get<IStatistics>(url, options)
            .pipe(map(response => response),
                catchError(this.handleError));
    }*/
}
