import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompetenceListComponent } from './components/competence-list/competence-list.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { RoleListComponent } from './components/role-list/role-list.component';

const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'competences', component: CompetenceListComponent },
  { path: 'roles', component: RoleListComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
