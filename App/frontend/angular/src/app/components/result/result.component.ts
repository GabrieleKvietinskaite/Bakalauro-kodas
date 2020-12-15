import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { GameService } from 'src/app/services/game.service';
import {
    ApexAxisChartSeries,
    ApexTitleSubtitle,
    ApexDataLabels,
    ApexChart,
    ChartComponent,
    ApexXAxis,
    ApexStroke,
    ApexMarkers,
    ApexYAxis,
    ApexGrid,
    ApexLegend
  } from "ng-apexcharts";
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';
import { IGraphs } from 'src/app/models/IGraphs.interface';

export type ChartOptions = {
    series: ApexAxisChartSeries;
    chart: ApexChart;
    xaxis: ApexXAxis;
    stroke: ApexStroke;
    dataLabels: ApexDataLabels;
    markers: ApexMarkers;
    tooltip: any; // ApexTooltip;
    yaxis: ApexYAxis;
    grid: ApexGrid;
    legend: ApexLegend;
    title: ApexTitleSubtitle;
};

declare var window: any;

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements AfterViewInit{
  @ViewChild("chart", {static: false}) chart: ChartComponent;
  public chartOptions: Partial<ChartOptions>;
  
  error: string;
  gameId: number;
  scenarioId: number;
  graphs: IGraphs;
  base64Image: string = 'data:image/png;base64,';
  pdfSrc;

  constructor(private gameService: GameService,
      private router: Router,
      private sanitizer: DomSanitizer) {
          
          const state = this.router.getCurrentNavigation().extras.state as {GameId: number, ScenarioId: number};
          if(state === undefined){
              this.router.navigate(['scenarios']);
          }
          this.gameId = state.GameId;
          this.scenarioId = state.ScenarioId;
          
          //this.gameId = 45;
          //this.scenarioId = 1;
          this.getReport();
          //this.getResults(this.gameId);
          //this.getGraphs();
  }

  ngAfterViewInit(){

  }

  transform(graph: string){
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image + graph);
}

  getReport(){
    this.gameService.getReport(this.gameId).subscribe(
      report => {
        this.pdfSrc = window.URL.createObjectURL(report);
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