import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from './services/authentication.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  token: string;


  constructor (
      private router: Router,
      private authenticationService: AuthenticationService
  ) {
      this.authenticationService.token.subscribe(x => this.token = x);
  }

  logout() {
      this.authenticationService.logout();
      this.router.navigate(['/']);
  }

  home(){
    this.router.navigate(['home'])
  }

  register(){
    this.router.navigate(['register'])
  }

  login(){
    this.router.navigate(['login'])
  }
}
