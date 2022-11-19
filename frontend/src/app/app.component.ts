import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {ArticleApiService} from './services/article-api.service';
import {Article} from './entities/article.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  articleListSubs: Subscription;
  articleList: Article[];

  constructor(private articlesApi: ArticleApiService) {
  }

  ngOnInit() {
    this.articleListSubs = this.articlesApi
      .getArticles()
      .subscribe(res => {
          this.articleList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.articleListSubs.unsubscribe();
  }
}
