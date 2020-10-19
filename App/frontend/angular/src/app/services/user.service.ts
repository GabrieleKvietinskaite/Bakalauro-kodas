import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { tap, shareReplay } from 'rxjs/operators';
 
@Injectable()
export class UserService {
  
  private REST_API_SERVICE = "http://localhost:8000/api";
  private AUTH_SERVICE = "http://localhost:8000/auth";
 
  private httpOptions: any;
  private errors: any;
 
  constructor(private httpClient: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }
/*
  get token(): string {
    return localStorage.getItem('token');
  }

  register(username: string, email: string, password1: string, password2: string) {
    return this.httpClient.post(
      this.AUTH_SERVICE.concat('/register/'),
      { username, email, password1, password2 }
    ).pipe(
      tap(response => this.setSession(response)),
      shareReplay(),
    );
  }
 
  // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
  public login(user) {
    this.httpClient.post(this.AUTH_SERVICE + '/login/', JSON.stringify(user), this.httpOptions).subscribe(
      data => {
        this.setSession(data);
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  public logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('expires_at');
  }
 
  // Refreshes the JWT token, to extend the time the user is logged in
  public refreshToken() {
    if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
      return this.httpClient.post(
        this.AUTH_SERVICE.concat('/refresh-token/'),
        { token: this.token }
      ).pipe(
        tap(response => this.setSession(response)),
        shareReplay(),
      ).subscribe();
    }
  }

  getExpiration() {
    const expiration = localStorage.getItem('expires_at');
    const expiresAt = JSON.parse(expiration);

    return moment(expiresAt);
  }

  isLoggedIn() {
    return moment().isBefore(this.getExpiration());
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }
 
  private setSession(authResult) {
    let token = authResult.token;
    let payload = <IJwtPayload> jwtDecode(token);
    let expiresAt = moment.unix(payload.exp);

    localStorage.setItem('token', authResult.token);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }
*/
  public getCompetences(){
    return this.httpClient.get(this.REST_API_SERVICE + '/competences');
  }

  //public saveCompetences(userId: number, competences: string): Observable<IPlayer>{
    //return this.httpClient.put<IPlayer>(this.REST_API_SERVICE + `/player/${userId}`, )
  //}

  public getRoles(){
    return this.httpClient.get(this.REST_API_SERVICE + '/roles');
  }
}