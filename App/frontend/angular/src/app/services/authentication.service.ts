import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IRegistrationDetails } from '../models/IRegistrationDetails.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private AUTH_SERVICE = "http://localhost:8000/auth";

  constructor(private httpClient: HttpClient) { }

  register(user: IRegistrationDetails) {
    let form = {"username": user.Username, "email": user.Email, "password1": user.Password, "password2": user.Password}
    return this.httpClient.post(this.AUTH_SERVICE + '/registration/', form);
  }
}
