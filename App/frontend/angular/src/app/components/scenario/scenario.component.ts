import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IScenario } from 'src/app/models/IScenario.interface';
import { ScenarioService } from 'src/app/services/scenario.service';

@Component({
  selector: 'app-scenario',
  templateUrl: './scenario.component.html',
  styleUrls: ['./scenario.component.css']
})
export class ScenarioComponent implements OnInit {
  scenarios: IScenario[];
  error: string;
  token: string;

  constructor(private scenarioService: ScenarioService,
      //private gameService: GameService,
      //private authenticationService: AuthenticationService,
      //private router: Router,
  ) {
      //this.authenticationService.token.subscribe(x => this.token = x);
  }
  scenariosData: Observable<any>;

  ngOnInit() {
      this.loadData();
  }

  loadData() {
    this.scenarioService.getScenarios().subscribe((data: IScenario[]) =>{
      this.scenarios = data;
      console.log(this.scenarios[0].title)
    })
  }
  /*
  openGame(scenarioId: number) {
      var gameId;
      var service = this.gameService.createGame(this.authenticationService.getTokenId(this.token), scenarioId);

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
  }*/
}
