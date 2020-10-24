import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { UserService } from 'src/app/services/user.service';
import { ICompetence } from '../../models/ICompetence.interface';

@Component({
  selector: 'app-competence-list',
  templateUrl: './competence-list.component.html',
  styleUrls: ['./competence-list.component.css']
})
export class CompetenceListComponent implements OnInit {

  competences: ICompetence[];
  selected: ICompetence [];

  constructor(private userService: UserService,
              private router: Router,
              private authentcationService: AuthenticationService) { }

  ngOnInit(): void {
    this.userService.getCompetences().subscribe((data: any[]) =>{
      this.competences = data;
    })
  }

  saveCompetences(){
    let userCompetences = this.selected.map(x => x.id).sort((a, b) => a - b).toString();
    let playerId = this.authentcationService.getTokenPlayerId();
    this.userService.saveCompetences(playerId, userCompetences).subscribe();
    this.router.navigate(['roles']);
  }
}
