import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { UserService } from 'src/app/services/user.service';
import { ICompetence } from '../../models/ICompetence.interface';

@Component({
  selector: 'app-competence-list',
  templateUrl: './competence-list.component.html',
  styleUrls: ['./competence-list.component.css']
})
export class CompetenceListComponent implements OnInit {

  roleId: number;
  competences: ICompetence[];
  selected: ICompetence [];

  constructor(private userService: UserService,
    private router: Router,
    private authentcationService: AuthenticationService) {
      const state = this.router.getCurrentNavigation().extras.state as {RoleId: number, Competences: ICompetence[]};
      if(state === undefined){
          this.router.navigate(['roles']);
      }
      this.roleId = state.RoleId;
      this.competences = state.Competences;
  }

  ngOnInit(): void {
    /*
    this.userService.getCompetences().subscribe((data: any[]) =>{
      this.competences = data;
    })*/
  }

  saveCompetences(){
    let userCompetences = this.selected.map(x => x.id).sort((a, b) => a - b).toString();
    let playerId = this.authentcationService.getTokenPlayerId();
    this.userService.saveCompetences(playerId, userCompetences).subscribe();
    const navigationExtras: NavigationExtras = { state: { RoleId: this.roleId } };
    this.router.navigate(['scenarios'], navigationExtras);
  }
}
