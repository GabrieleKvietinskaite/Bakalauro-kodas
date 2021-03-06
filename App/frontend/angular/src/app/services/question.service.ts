import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { IQuestion } from '../models/iquestion';

@Injectable({
  providedIn: 'root'
})
export class QuestionService {

  private REST_API_SERVICE = "http://localhost:8000/api";
  private httpOptions: any;

    constructor(private httpClient: HttpClient) { 
      this.httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
      };
    }

  getQuestion(scenarioId: number, questionId: number) {
      var url = `/scenario/${scenarioId}/question/${questionId}`;
      
      return this.httpClient.get<IQuestion>(this.REST_API_SERVICE + url);
  }

  private handleError(error: HttpResponse<Error>) {
      return throwError(error);
  }
}
