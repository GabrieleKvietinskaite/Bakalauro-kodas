import { AfterViewInit, Component } from '@angular/core';
import { GameService } from 'src/app/services/game.service';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';
import { IGraphs } from 'src/app/models/IGraphs.interface';

declare var window: any;

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements AfterViewInit{
  
  error: string;
  gameId: number;
  scenarioId: number;
  graphs: IGraphs;
  base64Image: string = 'data:image/png;base64,';
  pdfSrc;
  loading = true;
  check;

  constructor(private gameService: GameService,
      private router: Router,
      private sanitizer: DomSanitizer) {
          
          const state = this.router.getCurrentNavigation().extras.state as {GameId: number, ScenarioId: number};
          if(state === undefined){
              this.router.navigate(['scenarios']);
          }
          this.gameId = state.GameId;
          this.scenarioId = state.ScenarioId;
          this.getReport();
  }

  ngAfterViewInit(){

  }

  transform(graph: string){
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image + graph);
}

  getReport(){
    this.gameService.getReport(this.gameId).subscribe(
      report => { 
        this.check = report;  
        this.loading = false;
        if(report){
          this.pdfSrc = window.URL.createObjectURL(report);
        }
        else{
          setTimeout(() => {
            this.router.navigate(['home']);
          }, 5000);
        }
      }
    )
  }

  download(){
    const link = document.createElement('a');
    link.setAttribute('target', '_blank');
    link.setAttribute('href', this.pdfSrc);
    link.setAttribute('download', `${this.gameId}report.pdf`);
    document.body.appendChild(link);
    link.click();
    link.remove();
  }
}