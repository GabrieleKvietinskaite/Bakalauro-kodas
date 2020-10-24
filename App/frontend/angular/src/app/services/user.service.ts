import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';
 
@Injectable({
  providedIn: 'root'
})
export class UserService {

  private REST_API_SERVICE = "http://localhost:8000/api";
 
  private httpOptions: any;
  private errors: any;
 
  constructor(private httpClient: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  public getCompetences(){
    return this.httpClient.get(this.REST_API_SERVICE + '/competences');
  }

  public saveCompetences(userId: number, competences: string){
    let form = {"competences": competences};

    return this.httpClient.put(this.REST_API_SERVICE + `/player/${userId}`, form, this.httpOptions);
  }

  public getRoles(){
    return this.httpClient.get(this.REST_API_SERVICE + '/roles');
  }

  public saveRoles(userId: number, roles: string){
    let form = {"roles": roles};

    return this.httpClient.put(this.REST_API_SERVICE + `/player/${userId}`, form, this.httpOptions);
  }
}