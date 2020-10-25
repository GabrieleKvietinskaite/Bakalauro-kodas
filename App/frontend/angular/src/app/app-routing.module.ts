import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompetenceListComponent } from './components/competence-list/competence-list.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { RoleListComponent } from './components/role-list/role-list.component';
import { ScenarioComponent } from './components/scenario/scenario.component';

const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'competences', component: CompetenceListComponent },
  { path: 'roles', component: RoleListComponent },
  { path: 'scenarios', component: ScenarioComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
