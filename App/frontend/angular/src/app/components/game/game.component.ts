import { Component, OnInit, ViewChild } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { CountdownComponent } from 'ngx-countdown/countdown.component';
import { IAnswer } from 'src/app/models/IAnswer.interface';
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
    @ViewChild('countdown', { static: false }) private counter: CountdownComponent;

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

    ngAfterViewInit() {
        this.counter.restart();
    }

    loadQuestion(questionId: number){
        this.questionService.getQuestion(this.scenarioId, questionId).subscribe((data: IQuestion) =>{
            this.question = data;
            this.loadAnswers(questionId)
        })
    }

    loadAnswers(questionId: number){
    this.answerService.getAnswers(this.scenarioId, questionId).subscribe((data: IAnswer[]) =>{
            this.answers = this.shuffle(data);
    })
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
        let maximumPoints = this.findMaxPoints();
        let hyp = this.calculate(answer.p_question_answer, answer.p_answer);

        this.answerService.updateAnswer(this.scenarioId, this.question.id, answer.number).subscribe();
        this.gameService.updateGame(this.gameId, this.question.id.toString(), answer.weight.toString(), maximumPoints.toString(), hyp.toString()).subscribe(
            _ => {},
            error => this.error = <any>error,
            () => {
                this.answers = [];
                this.loadQuestion(answer.next_question_id);
            }
        );
    }

    calculate(p_q_a: number, p_a: number){
        return Math.round((((p_q_a * p_a) / this.question.p_question) + Number.EPSILON) * 100000) / 100000;
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
        this.gameService.finishGame(this.gameId, this.question.id.toString()).subscribe(
            _ => {},
            error => this.error = <any>error,
            () => {
                const navigationExtras: NavigationExtras = { state: { GameId: this.gameId, ScenarioId: this.scenarioId } };
                this.router.navigate(['result'], navigationExtras);
            }
        )
    }

    gameOver() {
        let maxPoints = this.findMaxPoints();

        this.gameService.updateGame(this.gameId, this.question.id.toString(), '-1', maxPoints.toString(), '0').subscribe(
            _ => {},
            error => this.error = <any>error,
            () => {
                this.finishGame();
            }
        );
    }

    onTimerFinished(e:Event){
        if (e["action"] == "done"){
            this.gameOver();
        }
    }
}
