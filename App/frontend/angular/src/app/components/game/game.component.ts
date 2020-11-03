import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { IAnswer } from 'src/app/models/ianswer';
import { IGame } from 'src/app/models/IGame.interface';
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
    private game: IGame={
        id: null,
        player_id: null,
        scenario_id: null,
        questions: "",
        received_points: "",
        maximum_points: "",
        hypothesis: ""
    };

    constructor(private questionService: QuestionService,
        private answerService: AnswerService,
        private gameService: GameService,
        //private activatedRoute: ActivatedRoute,
        private router: Router) {
            const state = this.router.getCurrentNavigation().extras.state as {Id: number, GameId: number};
            if(state === undefined){
                this.router.navigate(['scenarios']);
            }
            this.scenarioId = state.Id;
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
        let questions;
        let points;
        let maximumPoints;
        let maxPoints = this.findMaxPoints();
        let hyp;
        let h = this.calculate(answer.p_question_answer, answer.p_answer);

        this.gameService.getGame(this.gameId).subscribe(
            data => {
                console.log(data.questions);
                this.game.questions = data.questions,
                this.game.received_points = data.received_points,
                this.game.maximum_points = data.maximum_points,
                this.game.hypothesis = data.hypothesis
            },
            error => this.error = <any>error,
            () => {
                if(this.game.questions != ""){
                    questions = this.game.questions += ';' + this.question.id;
                    points = this.game.received_points += ';' + answer.weight;
                    maximumPoints = this.game.maximum_points += ';' + maxPoints;
                    hyp = this.game.hypothesis += ';' + h;
                }
                else {
                    questions =  this.question.id;
                    points = answer.weight;
                    maximumPoints = maxPoints;
                    hyp = h;
                }
                this.gameService.updateGame(this.gameId, questions, points, maximumPoints, hyp).subscribe(
                    error => this.error = <any>error
                )
                this.answers = [];
                this.loadQuestion(answer.next_question_id);
            }
        );
    }

    calculate(p_q_a: number, p_a: number){
        return Math.round((((p_q_a * p_a) / this.question.p_question) + Number.EPSILON) * 100) / 100;
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
        this.gameService.finishGame(this.gameId).subscribe(
            _ => {},
            error => this.error = <any>error,
            () => {
                const navigationExtras: NavigationExtras = { state: { GameId: this.gameId, ScenarioId: this.scenarioId } };
                this.router.navigate(['result'], navigationExtras);
            }
        )
    }
}
