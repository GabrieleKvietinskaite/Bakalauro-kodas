import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { IScenario } from '../models/IScenario.interface';

@Injectable({
  providedIn: 'root'
})
export class ScenarioService {

  private REST_API_SERVICE = "http://localhost:8000/api";
  private httpOptions: any;

    constructor(private httpClient: HttpClient) { 
      this.httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
      };
    }

    getScenarios() {
      return this.httpClient.get(this.REST_API_SERVICE + '/scenario');
    }

    private handleError(error: HttpResponse<Error>) {
        return throwError(error);
    }
}