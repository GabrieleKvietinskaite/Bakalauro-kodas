import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';

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
/*
    createGame(userId: number, scenarioId: number) {
        var url = `api/game`;
        var game: IGame = {
            GameId: null,
            UserId: userId,
            ScenarioId: scenarioId,
            Questions: null,
            ReceivedPoints: null,
            MaxPoints: null,
            StartedAt: null,
            FinishedAt: null
        };

        return this.http.post(url, game, options)
            .pipe(map(response => response),
                catchError(this.handleError));
    }*/
/*
    updateGame(gameId: number, questionId: number, receivedPoints: number, maxPoints: number){
        var url = `api/game/${gameId}/edit`;

        return this.http.post(url, {questionId, receivedPoints, maxPoints}, options)
            .pipe(map(response => response),
                catchError(this.handleError));
    }*/
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

    private handleError(error: HttpResponse<Error>) {
        return throwError(error);
    }
}
