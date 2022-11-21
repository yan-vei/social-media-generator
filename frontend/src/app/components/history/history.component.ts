import { Component, OnInit } from '@angular/core';
import { Article } from 'src/app/entities/article.model';
import { TextExtract } from 'src/app/entities/text-extract.model';
import { ArticleService } from 'src/app/services/article.service';
import { TextService } from 'src/app/services/text.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  public articles: Article[] = [];
  public texts: TextExtract[] = []

  constructor(private textService: TextService, private articleService: ArticleService) { }

  ngOnInit(): void {
  }

  getArticles()
  {
    this.articleService.getArticles()
      .subscribe((articles) =>
      {
        this.articles = articles;
      },
      (err) =>
      {
        console.log(err)
      }
      )
  }

  getTexts()
  {
    this.textService.getTextExtracts()
      .subscribe((texts) =>
      {
        this.texts = texts;
      },
      (err) =>
      {
        console.log(err)
      }
      )
  }

}
