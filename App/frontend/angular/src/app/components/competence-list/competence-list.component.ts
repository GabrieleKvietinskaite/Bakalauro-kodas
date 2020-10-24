import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
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
              private router: Router) { }

  ngOnInit(): void {
    this.userService.getCompetences().subscribe((data: any[]) =>{
      this.competences = data;
    })
  }

  saveCompetences(){
    let userCompetences = this.selected.map(x => x.id).sort((a, b) => a - b).toString();
    this.userService.saveCompetences(1, userCompetences).subscribe();
    this.router.navigate(['roles']);
  }
}
