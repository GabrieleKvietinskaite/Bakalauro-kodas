import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { UserService } from 'src/app/services/user.service';
import { IRole } from '../../models/IRole.interface';

@Component({
  selector: 'app-role-list',
  templateUrl: './role-list.component.html',
  styleUrls: ['./role-list.component.css']
})
export class RoleListComponent implements OnInit {

  roles: IRole[];
  selected: IRole [];

  constructor(private userService: UserService,
              private router: Router,
              private authentcationService: AuthenticationService) { }

  ngOnInit(): void {
    this.userService.getRoles().subscribe((data: any[]) =>{
      this.roles = data;
    })
  }

  saveRoles(){
    let userRoles = this.selected.map(x => x.id).sort((a, b) => a - b).toString();
    let playerId = this.authentcationService.getTokenPlayerId();
    this.userService.saveRoles(playerId, userRoles).subscribe();
    //this.router.navigate(['menu']);
  }

}
