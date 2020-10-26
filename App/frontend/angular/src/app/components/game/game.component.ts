import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { IAnswer } from 'src/app/models/ianswer';
import { IQuestion } from 'src/app/models/iquestion';
import { AnswerService } from 'src/app/services/answer.service';
import { GameService } from 'src/app/services/game.service';
import { QuestionService } from 'src/app/services/question.service';

@Component({
    selector: 'app-game',
    templateUrl: './game.component.html',
    styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {
    question: IQuestion;
    answers: IAnswer[] = null;
    error: string;
    scenarioId: number;
    gameId: number;

    constructor(private questionService: QuestionService,
        private answerService: AnswerService,
        private gameService: GameService,
        //private activatedRoute: ActivatedRoute,
        private router: Router) {
            const state = this.router.getCurrentNavigation().extras.state as {Id: number, GameId: number};
            if(state === undefined){
                this.router.navigate(['scenarios']);
            }
            this.scenarioId = 1;//state.Id;
            this.gameId = state.GameId;
            this.loadQuestion(1);
        }

    ngOnInit() {
    }

    loadQuestion(questionId: number){
        this.questionService.getQuestion(this.scenarioId, questionId).subscribe((data: IQuestion) =>{
            this.question = data;
            this.loadAnswers(questionId)
        })
        /*
        this.questionService.getQuestion(this.scenarioId, questionId).subscribe(
            question => {
                this.question = question;
            },
            error => this.error = <any>error,
            () => this.loadAnswers(questionId)
        )*/
    }

    loadAnswers(questionId: number){
    this.answerService.getAnswers(this.scenarioId, questionId).subscribe((data: IAnswer[]) =>{
            this.answers = this.shuffle(data);
    })
        /*
        this.answerService.getAnswers(this.scenarioId, questionId).subscribe(
            answers => {
                this.allAnswers = answers;
            },
            error => this.error = <any>error,
            () => this.filterAnswers()
        ) */
    }

    shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
        }

        return array;
    }

    updateData(answer: IAnswer){
        /*
        this.questionService.updateQuestion(this.scenarioId, this.question.Id, answer.number).subscribe(
            error => this.error = <any>error
        )
        this.gameService.updateGame(this.gameId, this.question.Id, answer.Weight, this.findMaxPoints()).subscribe(
            error => this.error = <any>error
        )*/
        this.answers = [];
        this.loadQuestion(answer.next_question_id);
    }

    findMaxPoints(){
        var max = 0;

        this.answers.forEach(function(value){
            if(value.weight > max){
                max = value.weight;
            }
        })

        return max;
    }
    
    finishGame() {
        /*
        this.gameService.finishGame(this.gameId).subscribe(
            _ => {},
            error => this.error = <any>error,
            () => {*/
                const navigationExtras: NavigationExtras = { state: { GameId: this.gameId, ScenarioId: this.scenarioId } };
                this.router.navigate(['results'], navigationExtras);
            /*}
        )*/
    }
}
