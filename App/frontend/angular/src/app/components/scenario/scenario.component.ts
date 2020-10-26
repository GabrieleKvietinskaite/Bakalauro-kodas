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
  playerId: string;

  constructor(private scenarioService: ScenarioService,
      private gameService: GameService,
      private authenticationService: AuthenticationService,
      private router: Router,
  ) {
    this.playerId = this.authenticationService.getTokenPlayerId();
  }
  scenariosData: Observable<any>;

  ngOnInit() {
      this.loadData();
  }

  loadData() {
    this.scenarioService.getScenarios().subscribe((data: IScenario[]) =>{
      this.scenarios = data;
    })
  }
  
  openGame(scenarioId: number) {
    /*  
    var gameId;
      var service = this.gameService.createGame(this.playerId, scenarioId);

      service.subscribe(
          _gameId => {
              gameId = _gameId;
          },
          error => this.error = <any>error,
          () => {*/
              const navigationExtras: NavigationExtras = { state: { Id: scenarioId, GameId: 1 } };
              this.router.navigate(['game'], navigationExtras);/*
          }
      )*/
  }
}
