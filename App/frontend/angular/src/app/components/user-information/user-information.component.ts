import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { ICompetence } from 'src/app/models/ICompetence.interface';
import { IPlayer } from 'src/app/models/IPlayer.interface';
import { IRole } from 'src/app/models/IRole.interface';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-user-information',
  templateUrl: './user-information.component.html',
  styleUrls: ['./user-information.component.css']
})
export class UserInformationComponent implements OnInit {
  user: IPlayer;
  error: string;
  playerId: number;
  username: string;
  roleInfo: IRole;
  competencesInfo: ICompetence[] = [];
  competences: ICompetence[];
  state;

  constructor(private userService: UserService,
    private authenticationService: AuthenticationService,
    private router: Router) {
      this.playerId = this.authenticationService.getTokenPlayerId();
      this.username = this.authenticationService.getTokenPlayerUsername();  
      this.state = this.router.getCurrentNavigation().extras.state as {Role: IRole, Competences: ICompetence[]};
     }

  ngOnInit() {
    this.getUserData();
  }

  getUserData() {
    this.userService.getUser(this.playerId).subscribe((data: IPlayer) =>{
      this.user = data;
    },
      error => this.error = <any>error,
      () => {
        if(this.state === undefined){
          this.userService.getCompetences().subscribe((data: ICompetence[]) =>{
            this.competences = data;
          },
          error => this.error = <any>error,
          () => {
            this.roleInfo = this.user.role;
            let temp = this.user.competences.split(',');
            let c = 1;
            temp.forEach(competence => { 
              this.competencesInfo.push(this.competences.find(x => x.id === +competence));
            });
          });
        }
        else{
          this.roleInfo = this.state.Role;
          this.competencesInfo = this.state.Competences;
        }
      }
    );
  }



  chooseRole(){
    this.router.navigate(['roles']);
  }

  chooseScenario(){
    const navigationExtras: NavigationExtras = { state: { RoleId: this.user.role.id, LevelId: this.user.level.id } };
    this.router.navigate(['scenarios'], navigationExtras);
  }
}
