import {Component, OnInit, OnDestroy} from '@angular/core';
import { UtilsService } from './services/utils.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {

  constructor(public utils: UtilsService) {
  }

  ngOnInit() {
  }

  ngOnDestroy() {
  }

}
