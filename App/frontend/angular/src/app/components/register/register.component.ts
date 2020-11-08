import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { MustMatch } from 'src/app/helpers/MustMatchValidator';
import { IRegistrationDetails } from 'src/app/models/IRegistrationDetails.interface';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  loading = false;
  submitted = false;
  //returnUrl: string;
  error = '';

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private authenticationService: AuthenticationService
  ) {
      //if(this.authenticationService.tokenValue) {
      //    this.router.navigate(['/']);
      //}
  }

  ngOnInit() {
      this.registerForm = this.formBuilder.group({
          username: ['', [ Validators.required, Validators.minLength(2), Validators.maxLength(20) ]],
          email: ['', [ Validators.required, Validators.email ]],
          password: ['', [ Validators.required, Validators.minLength(6), Validators.maxLength(16) ]],
          confirmPassword: ['', Validators.required]
      },
      {
          validator: MustMatch('password', 'confirmPassword')
      });

      // get return url from route parameters or default to '/'
      //this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  // convenience getter for easy access to form fields
  get f() {
      return this.registerForm.controls;
  }

  onSubmit() {
      this.submitted = true;

      if(this.registerForm.invalid) {
        return;
      }

      this.loading = true;

      const user: IRegistrationDetails = {
        username: this.f.username.value,
        email: this.f.email.value,
        password: this.f.password.value,
      }

      this.authenticationService.register(user)
        .pipe(first())
        .subscribe(
            data => {
                //this.router.navigate([this.returnUrl]);
            },
            error => {
                this.error = error;
                this.loading = false;
            }
        );
  }
}