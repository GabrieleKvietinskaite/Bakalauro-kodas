import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { IScenario } from 'src/app/models/IScenario.interface';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { GameService } from 'src/app/services/game.service';
import { ScenarioService } from 'src/app/services/scenario.service';

@Component({
  selector: 'app-scenario',
  templateUrl: './scenario.component.html',
  styleUrls: ['./scenario.component.css']
})
export class ScenarioComponent implements OnInit {
  scenarios: IScenario[];
  error: string;
  playerId: number;
  roleId: number;
  levelId: number;

  constructor(private scenarioService: ScenarioService,
      private gameService: GameService,
      private authenticationService: AuthenticationService,
      private router: Router
  ) {
    this.playerId = this.authenticationService.getTokenPlayerId();
    const state = this.router.getCurrentNavigation().extras.state as {RoleId: number, LevelId: number};
      if(state === undefined){
          this.router.navigate(['home']);
      }
      this.roleId = state.RoleId;
  }
  scenariosData: Observable<any>;

  ngOnInit() {
      this.loadData();
  }

  loadData() {
    let level = 0;

    if(this.levelId){
      level = this.levelId;
    }

    this.scenarioService.getScenarios(this.roleId, level).subscribe((data: IScenario[]) =>{
      this.scenarios = data;
    })
  }
  
  openGame(scenarioId: number) { 
    var gameId;
      var service = this.gameService.createGame(this.playerId, scenarioId);

      service.subscribe(
          _gameId => {
              gameId = _gameId;
          },
          error => this.error = <any>error,
          () => {
              const navigationExtras: NavigationExtras = { state: { Id: scenarioId, GameId: gameId } };
              this.router.navigate(['game'], navigationExtras);
          }
      )
  }

  no(){
    this.router.navigate(['roles']);
  }
}
