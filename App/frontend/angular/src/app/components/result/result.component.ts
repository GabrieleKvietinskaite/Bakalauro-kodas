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
          //const state = this.router.getCurrentNavigation().extras.state as {GameId: number, ScenarioId: number};
          //if(state === undefined){
          //    this.router.navigate(['scenarios']);
          //}
          this.gameId = 29;
          this.scenarioId = 1;
          this.getReport();
          //this.getResults(this.gameId);
          //this.getGraphs();
  }

  ngAfterViewInit(){

  }

  getGraphs(){
    this.gameService.getGraphs(this.gameId).subscribe(
      data => {
        this.graphs = data;
      }
    );
  }

  transform(graph: string){
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image + graph);
}

  getResults(gameId: number){
    let receivedPoints;
    let maxPoints;
    let categories;

    this.gameService.getResults(this.gameId).subscribe(
        results => {
          receivedPoints = results.received_points.split(';').map(Number);
          maxPoints = results.maximum_points.split(';').map(Number);
          categories = Array(maxPoints.length).fill(null).map((_, i) => (i+1).toString());
        },
        error => this.error = <any>error,
        () => this.load(receivedPoints, maxPoints, categories)
    )
  }

  getReport(){
    this.gameService.getReport(this.gameId).subscribe(
      report => {
        this.pdfSrc = window.URL.createObjectURL(report);
      }
    )
  }

  public load(receivedPoints: number[], maxPoints: number[], categories: string[]){
        this.chartOptions = {
          series: [
            {
              name: "Received points",
              data: receivedPoints,
            },
            {
              name: "Maximum available points",
              data: maxPoints
            }
          ],
          chart: {
            height: 350,
            type: "line"
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            width: 5,
            curve: "straight",
            dashArray: [8, 0]
          },
          title: {
            text: "Game statistics",
            align: "left"
          },
          legend: {
            tooltipHoverFormatter: function(val, opts) {
              return (
                val +
                " - <strong>" +
                opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] +
                "</strong>"
              );
            }
          },
          markers: {
            size: 0,
            hover: {
              sizeOffset: 6
            }
          },
          xaxis: {
            labels: {
              trim: false
            },
            categories: categories
          },
          yaxis: {
            min: -1,
            max: 4,
            tickAmount: 5
          },
          tooltip: {
            y: [
              {
                title: {
                  formatter: function(val) {
                    return val + " per question";
                  }
                }
              },
              {
                title: {
                  formatter: function(val) {
                    return val + " per question";
                  }
                }
              },
            ]
          },
          grid: {
            borderColor: "#f1f1f1"
          }
      };
  }
}
