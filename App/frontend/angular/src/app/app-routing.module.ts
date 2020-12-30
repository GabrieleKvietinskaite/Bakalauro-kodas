import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompetenceListComponent } from './components/competence-list/competence-list.component';
import { GameComponent } from './components/game/game.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { ResultComponent } from './components/result/result.component';
import { RoleListComponent } from './components/role-list/role-list.component';
import { ScenarioComponent } from './components/scenario/scenario.component';
import { UserInformationComponent } from './components/user-information/user-information.component';
import { AuthGuard } from './guards/auth.guard';

const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'home', component: UserInformationComponent, canActivate: [AuthGuard] },
  { path: 'competences', component: CompetenceListComponent, canActivate: [AuthGuard] },
  { path: 'roles', component: RoleListComponent, canActivate: [AuthGuard] },
  { path: 'scenarios', component: ScenarioComponent, canActivate: [AuthGuard] },
  { path: 'game', component:GameComponent, canActivate: [AuthGuard] },
  { path: 'result', component:ResultComponent, canActivate: [AuthGuard] }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
