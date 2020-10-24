import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { IRegistrationDetails } from '../models/IRegistrationDetails.interface';
// @ts-ignore  
import jwt_decode from "jwt-decode";

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private AUTH_SERVICE = "http://localhost:8000/auth";
  private tokenSubject: BehaviorSubject<string>;
  public token: Observable<string>;

  constructor(private httpClient: HttpClient,) { 
    this.tokenSubject = new BehaviorSubject<string>(JSON.parse(localStorage.getItem('Token')));
    this.token = this.tokenSubject.asObservable();
  }

  register(user: IRegistrationDetails) {
    let form = {"username": user.Username, "email": user.Email, "password1": user.Password, "password2": user.Password}
    return this.httpClient.post(this.AUTH_SERVICE + '/registration/', form);
  }

  login(username: string, password: string) {
    return this.httpClient.post<any>(this.AUTH_SERVICE + '/token/', { username, password })
    .pipe(map(jwtToken => {
        if(jwtToken) {
          jwtToken = jwtToken.token;
          localStorage.setItem('Token', JSON.stringify(jwtToken));
          this.tokenSubject.next(JSON.stringify(jwtToken));
        }
        
        return jwtToken;
    }))
  }

  public get tokenValue(): string {
    return this.tokenSubject.value;
  }

  logout() {
    localStorage.removeItem('Token');
    this.tokenSubject.next(null);
  }

  getTokenExpirationDate(token: string): Date {
      const decoded = jwt_decode(token);

      if(decoded.exp === undefined) return null;

      const date = new Date(0);
      date.setUTCSeconds(decoded.exp);
      return date;
  }

  isTokenExpired(token?: string): boolean {
    if(!token) token = this.tokenValue;
    if(!token) return true;

    const date = this.getTokenExpirationDate(token);
    if(date === undefined) return false;

    const currentDate = new Date();
    return !(date.valueOf() > currentDate.valueOf());
  }

  getTokenPlayerId(token: string) {
    return jwt_decode(token).user_id;
  }
}
